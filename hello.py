from tkinter import *
from PIL import ImageTk,Image

root=Tk()

myimage1=ImageTk.PhotoImage(Image.open("Screenshot_4.png"))
myimage2=ImageTk.PhotoImage(Image.open("Screenshot_5.png"))
myimage3=ImageTk.PhotoImage(Image.open("Screenshot_6.png"))


header=Label(root,text="Image slider")
header.grid(row=0,column=1)

myimages=[myimage1,myimage2,myimage3]

imagelabel=Label(image=myimage1)

imagelabel.grid(row=0,column=0)

def forward(number):

    if number==3:
        number=0

    global imagelabel

    imagelabel.grid_forget()
    imagelabel=Label(image=myimages[number])
    imagelabel.grid(row=0,column=0)
    fbutton=Button(root,text=">",command=lambda :forward(number+1),padx=20,pady=20)
    fbutton.grid(row=1,column=1)

def backward(number):

    if number==-4:
        number=-1
    global imagelabel

    imagelabel.grid_forget()
    imagelabel=Label(image=myimages[number+3])
    imagelabel.grid(row=0,column=0)
    bbutton=Button(root,text="<",command=lambda :backward(number-1),pady=20,padx=20)
    bbutton.grid(row=1,column=0)

    

fbutton=Button(root,text=">",command=lambda :forward(1),padx=20,pady=20)
fbutton.grid(row=1,column=1)
bbutton=Button(root,text="<",command=lambda: backward(-1),padx=20,pady=20)
bbutton.grid(row=1,column=0)

root.mainloop()