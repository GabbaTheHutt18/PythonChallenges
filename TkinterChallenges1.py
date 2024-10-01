from tkinter import *
import csv


def ReadButtonPressed():
     People.delete(0, END)
     file = open("People.csv", "r")
     ReadFile = file.readlines()
     for i in range (0, len(ReadFile)):
          People.insert(i, ReadFile[i])
     file.close()

def WriteButtonPressed():
     name = nameEntry.get()
     age = ageEntry.get()
     if age.isdigit() and "," not in age and "," not in name:
          file = open("People.csv", "a")
          file.write(name + "," + age + "\n")
          file.close()

     nameEntry.delete(0,END)
     ageEntry.delete(0,END)

file = open("People.csv","w")
file.close()
window = Tk()
window.title("Tkinter Challenges")
window.geometry("450x100")
nameLabel = Label(text = "name")
nameLabel.place(x = 10, y = 10)
ageLabel = Label(text = "age")
ageLabel.place(x = 10, y = 40)
nameEntry = Entry(text = 0)
nameEntry.place(x = 50, y = 10)
ageEntry = Entry(text = 1)
ageEntry.place(x = 50, y = 40)
People = Listbox()
People.place(x = 200, y = 10)
WriteButton = Button(text="Add to file", command = WriteButtonPressed)
WriteButton.place(x = 50, y = 100)
ReadButton = Button(text="Read file", command = ReadButtonPressed)
ReadButton.place(x = 115, y = 100)
window.mainloop()