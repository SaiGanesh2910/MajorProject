import tkinter as tk
import os
from tkinter import *

HEIGHT = 550
WIDTH = 1000


def new_window():
    finalstr = str(entry1.get()) + "," + str(entry2.get()) + "," + str(entry3.get()) + "," + check
    print(finalstr)
    text_file = open("d:/IVth_year/2nd_Sem/Major_Project/Major_Project_dev/userFile.txt", "w")
    # write string to file
    text_file.write(finalstr)
    # close file
    text_file.close()
    os.system("python d:/IVth_year/2nd_Sem/Major_Project/Major_Project_dev/GUI.py")
    ws.destroy()



ws = tk.Tk()
ws.title("User Info")
var = IntVar()
canvas = tk.Canvas(ws, height=HEIGHT, width=WIDTH)
canvas.pack()
background_image = tk.PhotoImage(file='Startbg.png',height=HEIGHT,width=WIDTH)
background_label = tk.Label(ws, image=background_image)
background_label.place(relwidth=1, relheight=1)

tk.Label(ws, text="User Info",font=15).place(relx=0.4, rely=0.1)
name = tk.Label(ws, text="Name",font=10).place(relx=0.30, rely=0.20)
age = tk.Label(ws, text="Age",font=10).place(relx=0.30, rely=0.30)
weight = tk.Label(ws, text="Weight",font=10).place(relx=0.30, rely=0.40)
problems = tk.Label(ws, text="Problems",font=10).place(relx=0.30, rely=0.50)
sbmitbtn = tk.Button(ws, text="Submit", bg="green",font=15,command=lambda: new_window()).place(relx=0.5, rely=0.8)
entry1 = tk.Entry(ws)
entry1.place(relx=0.50, rely=0.20)
entry2 = tk.Entry(ws)
entry2.place(relx=0.50, rely=0.30)
entry3 = tk.Entry(ws)
entry3.place(relx=0.50, rely=0.40)


def sel():
    global check
    check = str(var.get())


R1 = Radiobutton(ws, text="Wrist", variable=var, value=1, command=sel).place(relx=0.50, rely=0.5)
R2 = Radiobutton(ws, text="Shoulder", variable=var, value=2, command=sel).place(relx=0.60, rely=0.5)
R3 = Radiobutton(ws, text="Elbow", variable=var, value=3, command=sel).place(relx=0.70, rely=0.5)
R4 = Radiobutton(ws, text="None", variable=var, value=4, command=sel).place(relx=0.80, rely=0.5)
sel()
ws.mainloop()
