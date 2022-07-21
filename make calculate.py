from tkinter import *


root = Tk()
root.geometry("425x280")
root.title("Calculater")
root.configure(background="black")

a=StringVar()

def show1(c):
    a.set(a.get()+c)

def show2():
    b=a.get()
    a.set(eval(b))

def clr():
    a.set("")

e1=Entry(root,font="Arial  30",bg="white",fg="black",justify=RIGHT,textvariable=a)
e1.place(x=0,y=0,width=425,height=50)



b1=Button(root,text="7",font="Arial 20",width=6,bg="grey",fg="black",command=lambda :show1("7"))
b1.place(x=3,y=50)

b2=Button(root,text="8",font="Arial 20",width=6,bg="grey",fg="black",command=lambda :show1("8"))
b2.place(x=110,y=50)

b3=Button(root,text="9",font="Arial 20",width=5,bg="grey",fg="black",command=lambda :show1("9"))
b3.place(x=216,y=50)

b4=Button(root,text="+",font="Arial 20",width=7,bg="grey",fg="black",command=lambda :show1("+"))
b4.place(x=307,y=50)

b5=Button(root,text="6",font="Arial 20",width=6,bg="grey",fg="black",command=lambda :show1("6"))
b5.place(x=3,y=107)

b6=Button(root,text="5",font="Arial 20",width=6,bg="grey",fg="black",command=lambda :show1("5"))
b6.place(x=110,y=107)

b7=Button(root,text="4",font="Arial 20",width=5,bg="grey",fg="black",command=lambda :show1("4"))
b7.place(x=216,y=107)

b8=Button(root,text="-",font="Arial 20",width=7,bg="grey",fg="black",command=lambda :show1("-"))
b8.place(x=307,y=107)

b9=Button(root,text="3",font="Arial 20",width=6,bg="grey",fg="black",command=lambda :show1("3"))
b9.place(x=3,y=164)

b10=Button(root,text="2",font="Arial 20",width=6,bg="grey",fg="black",command=lambda :show1("2"))
b10.place(x=110,y=164)

b11=Button(root,text="1",font="Arial 20",width=5,bg="grey",fg="black",command=lambda :show1("1"))
b11.place(x=216,y=164)

b12=Button(root,text="*",font="Arial 20",width=7,bg="grey",fg="black",command=lambda :show1("*"))
b12.place(x=307,y=164)

b12=Button(root,text="0",font="Arial 20",width=6,bg="grey",fg="black",command=lambda :show1("0"))
b12.place(x=3,y=221)

b13=Button(root,text="C",font="Arial 20",width=6,bg="grey",fg="black",command=clr)
b13.place(x=110,y=221)

b14=Button(root,text="=",font="Arial 20",width=5,bg="grey",fg="black",command=show2)
b14.place(x=217,y=221)

b15=Button(root,text="/",font="Arial 20",width=7,bg="grey",fg="black",command=lambda :show1("/"))
b15.place(x=308,y=221)

root.mainloop()