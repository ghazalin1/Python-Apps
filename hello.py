from tkinter import *
import os
os.system('clear')



root = Tk()
root.title('GhazaliCode.com - Learn to code')
root.iconbitmap('C:/Users/CZ 3/Desktop/PythonApps/dsc.ico')
#on websites it's called favicon , on programs or real life it's called icon
root.geometry("400x600")

#everything is wdidget, to create a widget we create any type of variable
#we create label   we use pack on the screen, we just want to pack


def hello():
 hello_label = Label(root, text="Hello " + myTextbox.get())
 hello_label.pack()

def hello2():
 hello2_label = Label(root, text="Hello Again " + myTextbox2.get())
 hello2_label.pack()

myLabel = Label(root, text="Enter your first name: \n")
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root, text="Submit ", command=hello)
myButton.pack()


myTextbox2 = Entry(root, width=30)
myTextbox2.pack()

myButton2 = Button(root, text="Submit Again ", command=hello2)
myButton2.pack()




root.mainloop()  
#thats how interface generally works

