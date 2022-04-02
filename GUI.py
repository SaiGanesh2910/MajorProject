import os
import tkinter as tk



HEIGHT = 800
WIDTH = 1500



# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3







root = tk.Tk()
def open_shoulder_press():
    os.system('python c:/Users/chaitanya/PycharmProjects/MajorProject_dev/venv/share/shoulder_press.py')
def open_lateral_raise():
    os.system('python c:/Users/chaitanya/PycharmProjects/MajorProject_dev/venv/share/single_lateral_raise.py')

def open_bicep_curl():
    os.system('python c:/Users/chaitanya/PycharmProjects/MajorProject_dev/venv/share/main.py')
    #os.system('c:/Windows/system32/notepad.exe')
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=15)
frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

button = tk.Button(frame, text="Bicep_Curls", font=40,command=open_bicep_curl)
button.place(relx=0.03, relheight=0.25, relwidth=0.2)
button = tk.Button(frame, text="Shoulder_Press", font=40,command=open_shoulder_press)
button.place(relx=0.03,rely=0.3, relheight=0.25, relwidth=0.2)
button = tk.Button(frame, text="Single_lateral_raises", font=40,command=open_lateral_raise)
button.place(relx=0.03,rely=0.6, relheight=0.25, relwidth=0.2)




root.mainloop()
