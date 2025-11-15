#!/usr/bin/env python3
# scalar_steps_bip39_pt.py
# Gera 12 palavras BIP39 (pt) por cada um dos 256 passos da multiplicação escalar (double-and-add)
# - Faz download automático da wordlist PT (se possível)
# - Salva as 256 mnemonics em mnemonics_256_steps.txt
# Requisitos: Python 3.8+ (sem libs externas)

import hashlib
import os
import sys
import urllib.request
from typing import List, Optional

# -------------------------
# SECP256K1 params
# -------------------------
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
A = 0
B = 7
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# -------------------------
# ECC util
# -------------------------
def modinv(a: int, m: int) -> int:
    if a == 0:
        raise ZeroDivisionError("inverse of 0")
    lm, hm = 1, 0
    low, high = a % m, m
    while low > 1:
        r = high // low
        nm, new = hm - lm * r, high - low * r
        lm, low, hm, high = nm, new, lm, low
    return lm % m

class Point:
    __slots__ = ("x", "y")
    def __init__(self, x: Optional[int], y: Optional[int]):
        self.x = x
        self.y = y
    def is_infinite(self):
        return self.x is None and self.y is None
    def __repr__(self):
        if self.is_infinite():
            return "<INF>"
        return f"Point(x={hex(self.x)}, y={hex(self.y)})"

INFINITY = Point(None, None)

def point_add(p: Point, q: Point) -> Point:
    if p.is_infinite():
        return q
    if q.is_infinite():
        return p
    if p.x == q.x and (p.y != q.y or p.y == 0):
        return INFINITY
    if p.x == q.x:
        lam = (3 * p.x * p.x + A) * modinv(2 * p.y, P) % P
    else:
        lam = (q.y - p.y) * modinv(q.x - p.x, P) % P
    xr = (lam * lam - p.x - q.x) % P
    yr = (lam * (p.x - xr) - p.y) % P
    return Point(xr, yr)

# -------------------------
# BIP39 entropy -> mnemonic (128-bit -> 12 words)
# -------------------------
def bytes_to_bits(b: bytes) -> str:
    return ''.join(f"{byte:08b}" for byte in b)

def entropy_to_mnemonic(entropy_bytes: bytes, wordlist: List[str]) -> str:
    ENT = len(entropy_bytes) * 8
    if ENT not in (128, 160, 192, 224, 256):
        raise ValueError("Entropy length must be 128/160/192/224/256 bits")
    checksum_len = ENT // 32
    hash_digest = hashlib.sha256(entropy_bytes).digest()
    ent_bits = bytes_to_bits(entropy_bytes)
    hash_bits = bytes_to_bits(hash_digest)
    full_bits = ent_bits + hash_bits[:checksum_len]
    words = []
    for i in range(0, len(full_bits), 11):
        idx = int(full_bits[i:i+11], 2)
        words.append(wordlist[idx])
    return ' '.join(words)

# -------------------------
# Normalização do ponto
# -------------------------
def normalize_point_bytes(pt: Point) -> bytes:
    if pt.is_infinite():
        return b'\x00' * 64
    return pt.x.to_bytes(32, "big") + pt.y.to_bytes(32, "big")

# -------------------------
# Pipeline dos 256 passos
# -------------------------
def step_states_to_mnemonics(k: int, wordlist: List[str]) -> List[str]:
    k = k % N
    bits = [(k >> i) & 1 for i in range(255, -1, -1)]  # MSB -> LSB
    result = INFINITY
    addend = Point(Gx, Gy)
    mnems = []
    for step_index, bit in enumerate(bits):
        # dobro
        result = point_add(result, result)
        # add se bit == 1
        if bit == 1:
            result = point_add(result, addend)
        # estado determinístico
        st = normalize_point_bytes(result) + step_index.to_bytes(2,"big") + bytes([bit])
        digest = hashlib.sha256(st).digest()
        entropy128 = digest[:16]
        mnemonic = entropy_to_mnemonic(entropy128, wordlist)
        mnems.append(mnemonic)
    return mnems

# -------------------------
# Carregar wordlist PT (download se necessário)
# -------------------------
RAW_URLS = [
    "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/portuguese.txt",
    "https://raw.githubusercontent.com/trezor/python-mnemonic/master/mnemonic/wordlist/portuguese.txt"
]

def fetch_wordlist_try(urls=RAW_URLS) -> List[str]:
    last_err = None
    for url in urls:
        try:
            with urllib.request.urlopen(url, timeout=10) as r:
                text = r.read().decode("utf-8")
            words = [w.strip() for w in text.splitlines() if w.strip()]
            if len(words) == 2048:
                return words
            # se o arquivo tiver números de linha (raríssimo), tentamos limpar "NNN word"
            cleaned = []
            for line in words:
                parts = line.split()
                if len(parts) == 1:
                    cleaned.append(parts[0])
                else:
                    # assume "num palavra"
                    cleaned.append(parts[-1])
            if len(cleaned) == 2048:
                return cleaned
            last_err = f"arquivo em {url} retornou {len(words)} linhas"
        except Exception as e:
            last_err = str(e)
    raise RuntimeError(f"Não foi possível obter wordlist PT: {last_err}")

# -------------------------
# Main: gera e salva
# -------------------------
def main():
    print("Iniciando: obtendo wordlist BIP39 (pt)...")
    try:
        wl = fetch_wordlist_try()
        print("Wordlist obtida (2048 palavras).")
    except Exception as e:
        print("ERRO ao obter wordlist automaticamente:", e)
        print("Saindo. Baixe manualmente o arquivo 'portuguese.txt' e coloque no mesmo diretório.")
        sys.exit(1)

    # Exemplo: derive k de uma seed fixa (determinística para demo)
    k = int.from_bytes(hashlib.sha256(b"exemplo_scalar_k_2025").digest(), "big") % N
    print("k (hex):", hex(k))

    print("Executando pipeline dos 256 passos (pode levar alguns segundos)...")
    mnems = step_states_to_mnemonics(k, wl)

    out_file = "mnemonics_256_steps.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        for i, m in enumerate(mnems):
            f.write(f"step_{i:03d}: {m}\n")
    print(f"Salvo {len(mnems)} mnemonics em '{out_file}'.")
    print("\nPrimeiras 8 mnemonics (mostrando 8/256):\n")
    for i in range(min(8, len(mnems))):
        print(f"step_{i:03d}: {mnems[i]}\n")

if __name__ == "__main__":
    main()