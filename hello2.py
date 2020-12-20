from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('GhazaliCode.com - Learn to code')
root.iconbitmap('dsc.ico')
#on websites it's called favicon , on programs or real life it's called icon
# no need to mention destination folder if it's occuring in same folder
root.geometry("400x600")

my_img = ImageTk.PhotoImage(Image.open("DSC_0372.jpg"))
my_Label = Label(image=my_img)
my_Label.pack()

#exit button

button_quit = Button(root, text ="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()  
#thats how interface generally works

