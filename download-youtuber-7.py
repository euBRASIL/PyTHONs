from tkinter import *
from tkinter.ttk import Progressbar
from threading import Thread
from pytube import YouTube
import os
import requests
from PIL import ImageTk, Image
import io
import time

# creating tkinter object
root = Tk()
# setting dimensions for the GUI application
root.geometry('1200x600')
# application cannot be resized
root.resizable(0, 0)
# setting background color to the application
root.configure(bg='yellow')
# setting title of the application
root.title("euBRASIL | Youtube Downloader")

# placeholder to enter link of the youtube video to be downloaded
link = StringVar()

# function to update progress bar
def progress(stream, chunk, bytes_remaining):
    progress_bar['value'] = int(((stream.filesize - bytes_remaining) / stream.filesize) * 100)

# function to update download speed
def update_speed(stream, chunk, remaining):
    speed = stream.get_speed()  # Get download speed in bytes per second
    speed_label.config(text=f'Velocidade de Download: {speed // 1000} KB/s')  # Display speed in KB/s

# function to download video
def Downloader():
    try:
        start_time = time.time()  # Start time
        # url of the video
        url = YouTube(str(link.get()), on_progress_callback=progress)
        video = url.streams.first()
        
        # Format video information
        video_info = f'<i>Título:</i> {url.title}\n<i>Autor:</i> {url.author}\n<i>Duração:</i> {url.length} segundos\n<i>Resolução:</i> {video.resolution}\n<i>Formato:</i> {video.mime_type}'
        Label(root, text=video_info, font='arial 11', bg='yellow', wraplength=500, justify=LEFT).place(x=10, y=200)

        # Download video thumbnail
        thumbnail_url = url.thumbnail_url
        response = requests.get(thumbnail_url)
        thumbnail_data = response.content
        thumbnail_image = ImageTk.PhotoImage(Image.open(io.BytesIO(thumbnail_data)))
        thumbnail_label = Label(root, image=thumbnail_image, bg='yellow')
        thumbnail_label.image = thumbnail_image  # mantendo uma referência para a imagem
        thumbnail_label.place(x=548, y=80)

        # function to download video in a separate thread
        def download_video():
            video.download()
            # update GUI after download is complete
            end_time = time.time()  # End time
            elapsed_time = end_time - start_time
            root.after(0, lambda: Label(root, text=f'Download efetuado com êxito. Tempo decorrido: {elapsed_time:.2f} segundos', font='arial 11 bold', bg='blue', fg='white').place(x=10, y=330))

        # start download in a separate thread
        Thread(target=download_video).start()
    except Exception as e:
        # Display error message if download fails
        Label(root, text=f'Erro ao baixar vídeo: {e}', font='arial 11 bold', bg='red', fg='white').place(x=10, y=330)

# labels and entry widget
Label(root, text='\nQual é o Video Youtube ?', font='arial 20 bold', bg='yellow').pack()
Label(root, text='Insira o seu Link :', font='arial 15 bold', bg='yellow').place(x=30, y=100)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=130, height=30)

# Download button
Button(root, text='*** Download ***', font='arial 15 bold', bg='black', fg='white', padx=2, command=Downloader).place(x=284, y=160)

# Label to display download speed
speed_label = Label(root, text='', font='arial 11 bold', bg='yellow')
speed_label.place(x=10, y=400)

# Counter for processing actions
counter_label = Label(root, text='Tempo de processamento: 0 segundos', font='arial 11 bold', bg='yellow')
counter_label.place(x=10, y=10)

# Progress bar
progress_bar = Progressbar(root, orient=HORIZONTAL, length=1180, mode='determinate')
progress_bar.place(x=10, y=570)

# Function to update counter label
def update_counter():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        counter_label.config(text=f'Tempo de processamento: {elapsed_time:.2f} segundos')
        time.sleep(1)

# Start counter in a separate thread
Thread(target=update_counter).start()

# Running infinite loop of the tkinter object until the user exits the application
root.mainloop()
