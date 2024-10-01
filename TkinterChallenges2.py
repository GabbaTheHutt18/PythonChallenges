from tkinter import *

def ComfirmChoice():
    choice = PhotoImage(file = entry_box.get() + ".gif")
    photobox.image = choice
    photobox["image"] = choice
    photobox.update()

window = Tk()
window.title("Tkinter Challenges")
window.geometry("450x100")
entry_box = Entry(text = 0)
entry_box.place(x = 10, y = 10)
Button = Button(text = "Confirm Choice", command=ComfirmChoice)
Button.place(x = 10, y = 30)
photo = PhotoImage(file = "")
photobox = Label(window, image = photo)
photobox.place(x = 10, y = 70)
window.mainloop()