import pyautogui
import keyboard
import cv2
import numpy as np

fps = 15
tamanho_tela = tuple(pyautogui.size())
print(tamanho_tela)

codec = cv2.VideoWriter_fourcc(*"XVID")
video = cv2.VideoWriter("video.avi", codec, fps, tamanho_tela)

while True:
	frame = pyautogui.screenshot()
	frame = np.array(frame)

	frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

	video.write(frame)

	if keyboard.is_pressed("esc"):
		break

video.release()
cv2.destroyAllWindows()