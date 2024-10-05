from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
from pathlib import Path
from pytube import YouTube
import os
import sys
import yt_dlp





def resource_path(relative_path):
#  
    try:
      
       base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

window = Tk()
window.title("STEM")
window.geometry('736x414')
window.resizable(False, False)
window.config(bg="black")

# Ajusta la ruta del ícono
icon_path = resource_path("img/icons.ico")
window.iconbitmap(icon_path)

# CODIGO PARA COLOCAR EL FONDO
image_path = resource_path("img/image.jpg")
image3 = Image.open(image_path)
img3 = ImageTk.PhotoImage(image3)
img = tkinter.Label(window, image=img3)
img.place(relwidth=1, relheight=1, anchor="nw")


Label(window, text=' DESCARGAR VIDEOS DE PLATAFORMAS SOCIALES',font=("Courier", 13, "bold"),
      bg="#282928", fg="#ff00ff").place(x=100, y=30)
Label(window, text='INGRESE LA URL QUE DESEA DESCARGAR', font='arial 10  ',
      bg="#282928", fg="#5dade2").place(x=140, y=130)
Label(window, text='NOTA: Las URL sociales deben de ser de la "PUBLICACION ORIGIAL"', font='arial 10  ',
      bg="#282928", fg="#5dade2").place(x=90, y=250)


# BARRA DE ENTRADA DE LINK
link = StringVar()
linkenter = Entry(window, textvariable=link, width=50, font=("Courier", 9, "bold"),fg= '#0000FF').place(x=95, y=200)



#funcion de limpiar barra
def clear():
    link.set("")





#Descarga videos de cualquier plataforma social youtube,facebook,instagram,pinterest,tiktok
def download(cookies_file='cookies.txt'):
    url = str(link.get())
    path = Path.home() / "Downloads" / "Video_STEM"

    path.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        'format': 'best',
        'outtmpl': str(path / '%(title)s.%(ext)s'),
        'cookies': cookies_file,
        'noplaylist': True,
        'quiet': True,
    }

    def get_title(d):
        global video_title
        if d['status'] == 'finished':
            info_dict = d.get('info_dict', {})
            video_title = info_dict.get('title', 'Desconocido')

    ydl_opts['progress_hooks'] = [get_title]
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        try:
            ydl.download([url])
            link.set("")
            messagebox.showinfo("Video descargado",
                                f'Título del video: {video_title}')
        except:
            messagebox.showinfo("ERROR FOUND",
                                'Problema Encontrado Intente de nuevo o verifique la url')



#Descarga todos los audios de cualquier plataforma social
def audio(cookies_file='cookies.txt'):



    url = str(link.get())
    path = Path.home() / "Downloads" / "Audio_STEM"

    path.mkdir(parents=True, exist_ok=True)

    def get_title(d):
        global video_title
        if d['status'] == 'finished':
            info_dict = d.get('info_dict', {})
            video_title = info_dict.get('title', 'Desconocido')

    
    ydl_opts = {
        'format': 'bestaudio/best',  
        'outtmpl': str(path / '%(title)s.%(ext)s'),  
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  
            'preferredcodec': 'mp3',  
            'preferredquality': '192',  
        }],
        'cookies': cookies_file,
        'noplaylist': True,
        'quiet': True,
        'progress_hooks': [get_title],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            
            messagebox.showinfo("ERROR FOUND",
                                'Problema Encontrado Intente de nuevo o verifique la url')
            
        except Exception as e:
            link.set("")
            messagebox.showinfo("Audio descargado",
                                f'Título del Audio: {video_title}')


Button(window, text='VIDEO DOWNLOAD', font='arial 13 bold italic',command=download, bg="#282928", fg="#ff00ff").place(x=50, y=300)
Button(window, text='AUDIO DOWNLOAD', font='arial 13 bold italic',command=audio, bg="#282928", fg="#5dade2").place(x=300, y=300)
Button(window, text='BORRAR'         , font='arial 13 bold italic',command=clear, bg="#282928", fg="#Fff").place(x=405, y=195)



window.mainloop()
