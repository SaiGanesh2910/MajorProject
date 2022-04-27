import os
import tkinter as tk
import time

from tkinter import *
from tkinter import messagebox
from PIL import Image


time1=0.0


HEIGHT = 800
WIDTH = 1500



# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3







root = tk.Tk()
def open_shoulder_press():
    start_time1 = time.time()
    os.system('python c:/Users/chaitanya/PycharmProjects/MajorProject_dev/venv/share/shoulder_press.py')
    global time1
    time1 = time.time()-start_time1
    print(time1)
def open_lateral_raise():
    start_time2 = time.time()
    os.system('python c:/Users/chaitanya/PycharmProjects/MajorProject_dev/venv/share/single_lateral_raise.py')
    global time2
    time2 = time.time() - start_time2

def open_bicep_curl():
    start_time3 = time.time()
    os.system('python c:/Users/chaitanya/PycharmProjects/MajorProject_dev/venv/share/main.py')
    global time3
    time3 = time.time() - start_time3
    #os.system('c:/Windows/system32/notepad.exe')
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bd=15)
frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


button = tk.Button(frame, text="Bicep_Curls",bg='light green', font=40,command=open_bicep_curl)
button.place(relx=0.03, relheight=0.25, relwidth=0.2)
button = tk.Button(frame, text="Shoulder_Press",bg='light green', font=40,command=open_shoulder_press)
button.place(relx=0.03,rely=0.3, relheight=0.25, relwidth=0.2)
button = tk.Button(frame, text="Single_lateral_raises", bg='light green',font=40,command=open_lateral_raise)
button.place(relx=0.03,rely=0.6, relheight=0.25, relwidth=0.2)




file="bicep-curl2.gif"
info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None


"""def showtime1():
    messagebox.showinfo("showinfo",str(time1))"""

def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = frame.after(50,lambda :animation(count))

def stop_animation():
    gif_label.destroy()
    frame.after_cancel(anim)

gif_label = tk.Label(frame,image='')

gif_label.pack()

button = tk.Button(frame,text="Show_sample",command=lambda :animation(count))
button.place(relx=0.8,rely=0.03, relheight=0.15, relwidth=0.08)
#button.pack(side= RIGHT)
"""button = tk.Button(frame,text="Time",command= lambda :showtime1())
button.place(relx=0.7,rely=0.03, relheight=0.15, relwidth=0.08)"""

button = tk.Button(frame,text="stop",command=stop_animation)
button.place(relx=0.9, rely=0.03,relheight=0.15, relwidth=0.06)

#button.pack(side=RIGHT)

#second exercise gif
file2 = "sp2.gif"

info2 = Image.open(file2)

frames2 = info2.n_frames
# gives total number of frames that gif contains
#print(frames2)

# creating list of PhotoImage objects for each frames
im2 = [tk.PhotoImage(file=file2,format=f"gif -index {i}") for i in range(frames2)]

count2 = 0
anim2 = None
def animation2(count2):
    global anim2
    im22 = im2[count2]

    gif_label2.configure(image=im22)
    count2 += 1
    if count2 == frames2:
        count2 = 0
    anim2 = frame.after(50,lambda :animation2(count2))

def stop_animation2():
    gif_label2.destroy()
    frame.after_cancel(anim2)

gif_label2 = tk.Label(frame,image="")
gif_label2.config(bg='light blue')
gif_label2.pack()

button = tk.Button(frame,text="Show_sample2",command=lambda :animation2(count2))
button.place(relx=0.8,rely=0.3, relheight=0.15, relwidth=0.08)
button = tk.Button(frame,text="stop",command=stop_animation2)
button.place(relx=0.9, rely=0.3,relheight=0.15, relwidth=0.06)
#third exercise
file3="sl.gif"

info3 = Image.open(file3)

frames3 = info3.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im3 = [tk.PhotoImage(file=file3,format=f"gif -index {i}") for i in range(frames3)]

count3 = 0
anim3 = None
def animation3(count3):
    global anim3
    im23 = im3[count3]

    gif_label3.configure(image=im23)
    count3 += 1
    if count3 == frames3:
        count3 = 0
    anim3 = frame.after(50,lambda :animation3(count3))

def stop_animation3():
    gif_label3.destroy()
    frame.after_cancel(anim3)

gif_label3 = tk.Label(frame,image="")
gif_label3.pack()

button = tk.Button(frame,text="Show_sample",command=lambda :animation3(count3))
button.place(relx=0.8,rely=0.6, relheight=0.15, relwidth=0.08)
button = tk.Button(frame,text="stop",command=stop_animation3)
button.place(relx=0.9, rely=0.6,relheight=0.15, relwidth=0.06)


root.mainloop()
