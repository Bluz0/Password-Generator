from tkinter import *
import string
from random import *

def generate_password():

    password_min_lenght = 6
    password_max_lenght = 12

    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint(password_min_lenght,password_max_lenght)))
    input_password.delete(0,END)
    input_password.insert(0,password)
    



window = Tk()
window.title("Password Generator")
window.geometry("720x480")
window.config(background="#2d2d30")

#frame

frame = Frame(window,bg="#2d2d30")


#image
width = 300
height = 300
image = PhotoImage(file="images/lock.png").subsample(3) #zoom
canvas = Canvas(frame, width=width,height=height,bg="#2d2d30",bd=0,highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.grid(row=0,column=0,sticky=W)

right_frame = Frame(frame, bg="#2d2d30")


title = Label(right_frame,text="Password", font=("Helvetica",20),bg="#2d2d30",fg="white")
title.pack()


input_password = Entry(right_frame, font=("Helvetica",20),bg="#2d2d30",fg="white")
input_password.pack()

generator_button = Button(right_frame, text="Generator", font=("Helvetica",20),bg="#2d2d30",fg="white",command=generate_password)
generator_button.pack(pady=10)


right_frame.grid(row=0,column=1,sticky=W)

frame.pack(expand=True)

#menu

menu_bar = Menu(window)

file_menu = Menu(menu_bar,tearoff=0)

file_menu.add_command(label="New",command=generate_password)
file_menu.add_command(label="Quit",command=window.quit)
menu_bar.add_cascade(label="File",menu=file_menu)

window.config(menu=menu_bar)

window.mainloop()
