from tkinter import *
from math import *

DISC=0
Disc1=0
Disc2=0

def quadro():
    """
    """
    DISC= Ans1.get()
    DISC=b ** 2 - 4 * a * c
    if DISC >= 0:
        x1= (-b + math.sqrt(Disc)) / (2 *a ) 
        x2= (-b - math.sqrt(Disc)) / (2 * a)
        Disc1=Ans2.get()
        Disc2=Ans2.get()
        Disc1 = print(f"x1= {x1}")
        Disc2 = print(f"x2= {x2}")
    elif DISC == 0:
        x1 = -b / (2 * a)
        Disc1 = print(f"x1= {x1}") 
    else:
        Ndisc = print("Нет корней")

win=Tk()
win.title("Квадратное уравнение")
win.geometry("800x500")

name=Label(win,text="Решение квадратного уравнения",height=2,width=40,font="Arial 20",fg="green",bg="lightblue",relief="solid")
name.place(x=80,y=2)

txt1=Entry(win,width=5,font="Arial 20",fg="green",bg="lightblue",relief="solid",justify=CENTER)
txt1.place(x=1,y=150)

lbl1=Label(win,text="x**2+",width=5,font="Arial 20",fg="green",bg="lightblue",relief="solid")
lbl1.place(x=90,y=149)

txt2=Entry(win,width=5,font="Arial 20",fg="green",bg="lightblue",relief="solid",justify=CENTER)
txt2.place(x=190,y=150)

lbl2=Label(win,text="x+",width=5,font="Arial 20",fg="green",bg="lightblue",relief="solid")
lbl2.place(x=280,y=149)

txt3=Entry(win,width=5,font="Arial 20",fg="green",bg="lightblue",relief="solid",justify=CENTER)
txt3.place(x=380,y=150)

lbl3=Label(win,text="=0",width=5,font="Arial 20",fg="green",bg="lightblue",relief="solid")
lbl3.place(x=470,y=149)

But=Button(win,text="Решить",height=2,width=10,font="Arial 20",bg="Green",fg="Black",relief=RAISED)
But.place(x=570,y=125)
But.bind("<Return>",quadro)

Answer=Label(win,text="",height=4,width=25,font="Arial 20",fg="Black",bg="Yellow",relief="solid")
Answer.place(x=180,y=280)

Ans1=Label(win,text=DISC,height=1,width=5,font="Arial 20",fg="Black",bg="Yellow",relief="solid")
Ans1.place(x=200,y=300)

Ans2=Label(win,text=Disc1,height=1,width=5,font="Arial 20",fg="Black",bg="Yellow",relief="solid")
Ans2.place(x=200,y=350)

Ans3=Label(win,text=Disc2,height=1,width=5,font="Arial 20",fg="Black",bg="Yellow",relief="solid")
Ans3.place(x=200,y=400)


win.mainloop()
