from tkinter import *
from PIL import ImageTk, Image
import os

root=Tk()
root.title('The PhotoViewer')

#root.iconbitmap('justicon.ico') #can't set --may be beacause of ubuntu..


os.system("ls *.png>>out.txt")
f=open("out.txt")
os.system("rm out.txt")
imgnamelist=f.read().split()





firstimg=imgnamelist[0]

myimg= ImageTk.PhotoImage(Image.open(firstimg))


# converting myimg to a label wdiget and then displaying that label widget


mylabel = Label(image=myimg)
mylabel.grid(row=0,column=0,columnspan= 3)


i=1


def right():
	
	global i
	i=(i+1)%len(imgnamelist)

	imgviewing()



def left():

	global i
	i=(i-1)%len(imgnamelist)

	
	imgviewing()

def imgviewing():
	global myimgnew
	global i
	global mylabel

	mylabel.grid_forget()

	myimgnew= ImageTk.PhotoImage(Image.open(imgnamelist[i]))
	mylabel = Label(image= myimgnew)
	mylabel.grid(row=0,column=0,columnspan= 3)

	#mylabel.grid_forget()


rightbutton=Button(root, text=">>", command= right)
rightbutton.grid(row=1,column=2)

leftbutton=Button(root, text="<<", command= left)
leftbutton.grid(row=1,column=1)


#buttonQuit=Button(root, text="Quit",command=root.quit)
#buttonQuit.pack()



root.mainloop()
