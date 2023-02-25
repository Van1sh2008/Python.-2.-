from tkinter import *
import random
window = Tk()
window.geometry('500x500')
window.title("Добро пожаловать")
def clicked():
    canvas.delete("all")
    typegeometry=random.randint(1,3)
    if typegeometry == 1:
        canvas.create_rectangle(100,100,300,300,fill="white",outline="blue")
    elif typegeometry == 2:
        canvas.create_oval([100,100],[300,300],fill="pink")
    else:
        canvas.create_polygon([200,100],[300,300],[100,300],fill="gray", outline="yellow")
btn = Button(window, text="Click", command = clicked, bg='orange', fg='white')
btn.place(x=1, y=1)
canvas = Canvas(window,width=400,height=400,bg="gray",cursor="pencil")
canvas.pack()
window.mainloop()
