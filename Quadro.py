from tkinter import *
from math import *
import matplotlib.pyplot as plt #Y=....
import numpy as np #[min,max]

x1=0
x2=0
D=-1
graf=False

def quadro():
    global D,graf
    a = txt1.get()
    b = txt2.get()
    c = txt3.get()
    D = float(b)**2-4*float(a)*float(c)
    if D > 0:
        x1 = (-1*float(b) + sqrt(float(D))) / (2*float(a))
        x2  =(-1*float(b) - sqrt(float(D))) / (2*float(a))
        Answer.configure(text = f"x1 = {round(x1,2)} x2 = {round(x2,2)}")
        graf=True
    elif D == 0:
        x1 = (-1*float(b)+sqrt(float(D)))/(2*float(a))
        Answer.configure(text = f"x = {x1}")
        graf=True
    else:
        Answer.configure(text = "Нет корней")
        graf=False
    return graf,D

def grafik():
    graf,D=quadro()
    if graf==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x1=np.arange(x0-10, x0+10, 0.5) #min max step [min,max]
        y1=a_*x1*x1+b_*x1*c_
        fig=plt.figure()
        plt.plot(x0, y0, x1, y1, "r-d")
        plt.title("Квадратное уравнение")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"Нет возможности построить график"
    vastus.configure(text=f"D={D}\n{t}\n{text}")
t=0

def veel():
    global t
    if t==0:
        win.geometry(str(win.winfo_width())+"x"+str(win.winfo_height()+200))
        btn_veel.config(text="Уменьшить окно")
        t=1
    else:
        win.geometry(str(win.winfo_width())+"x"+str(win.winfo_height()-200))
        btn_veel.config(text="Увеличить окно")
        t=0

def kala():
    x1 = np.arange(0, 9.5, 0.5)#min max step
    y1=(2/27)*x1*x1-3
    x2 = np.arange(-10, 0.5, 0.5)#min max step
    y2=0.04*x2*x2-3
    x3 = np.arange(-9, -2.5, 0.5)#min max step
    y3=(2/9)*(x3+6)**2+1
    x4 = np.arange(-3, 9.5, 0.5)#min max step
    y4=(-1/12)*(x4-3)**2+6
    x5 = np.arange(5, 9, 0.5)#min max step
    y5=(1/9)*(x5-5)**2+2
    x6 = np.arange(5, 8.5, 0.5)#min max step
    y6=(1/8)*(x6-7)**2+1.5
    x7 = np.arange(-13, -8.5, 0.5)#min max step
    y7=(-0.75)*(x7+11)**2+6
    x8 = np.arange(-15, -12.5, 0.5)#min max step
    y8=(-0.5)*(x8+13)**2+3
    x9 = np.arange(-15, -10, 0.5)#min max step
    y9=[1]*len(x9)
    x10 = np.arange(3, 4, 0.5)#min max step
    y10=[3]*len(x10)
    fig = plt.figure()
    plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('Кит')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def ochki():
    x1= np.arange(-9,-0.5, 0.5)
    y1=(-1/16)*(x1+5)**2+2
    x2= np.arange(1, 9.5, 0.5)
    y2=(-1/16)*(x2-5)**2+2
    x3= np.arange(-9, -0.5, 0.5)
    y3=(1/4)*(x3+5)**2-3
    x4= np.arange(1, 9.5, 0.5)
    y4=(1/4)*(x4-5)**2-3
    x5= np.arange(-9, -5.5, 0.5)
    y5=-(x5+7)**2+5
    x6= np.arange(6, 9.5, 0.5)
    y6=-(x6-7)**2+5
    x7= np.arange(-1, 1.5, 0.5)
    y7=-(0.5)*x7**2+1.5
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title("Очки")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def zont():
    x1=np.arange(-12, 12.5, 0.5)
    y1=(-1/18)*x1**2+12
    x2=np.arange(-4, 4.5, 0.5)
    y2=(-1/8)*x2**2+6
    x3=np.arange(-12, -3.5, 0.5)
    y3=(-1/8)*(x3+8)**2+6
    x4=np.arange(4, 12.5, 0.5)
    y4=(-1/8)*(x4-8)**2+6
    x5=np.arange(-4, -0.3, 0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4, 0.2, 0.5)
    y6=1.5*(x6+3)**2-10
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title("Зонт")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def baboch():
    x1 = np.arange(-9, -0.5, 0.5)
    y1 = -(1/8)*(x1+9)**2+8
    x2 = np.arange(1, 9.5, 0.5)
    y2 = -(1/8)*(x2-9)**2+8
    x3 = np.arange(-9, -7.5, 0.5)
    y3 = 7*(x3+8)**2+1
    x4 = np.arange(8, 9.5, 0.5)
    y4 = 7*(x4-8)**2+1
    x5 = np.arange(-8, -0.5, 0.5)
    y5 = 1/49*(x5+1)**2
    x6 = np.arange(1, 8.5, 0.5)
    y6=1/49*(x6-1)**2
    x7 = np.arange(-8, -0.5, 0.5)
    y7 = -4/49*(x7+1)**2
    x8 = np.arange(1, 8.5, 0.5)
    y8 = -4/49*(x8-1)**2
    x9 = np.arange(-8, -1.5, 0.5)
    y9 = 1/3*(x9+5)**2-7
    x10 = np.arange(2, 8.5, 0.5)
    y10 = 1/3*(x10-5)**2-7
    x11 = np.arange(-2, -0.5, 0.5)
    y11 = -2*(x11+1)**2-2
    x12 = np.arange(1, 2.5, 0.5)
    y12 = -2*(x12-1)**2-2
    x13 = np.arange(-1, 1.5, 0.5)
    y13 = -4*x13**2+2
    x14 = np.arange(-1, 1.5, 0.5)
    y14 = 4*x14**2-6
    x15 = np.arange(-2, 0.5, 0.5)
    y15 = -1.5*x15+2
    x16 = np.arange(0, 2.5, 0.5)
    y16 = 1.5*x16+2
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16)
    plt.title('Бабочка')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def figura():
    global var
    valik=var.get()
    if valik==1:
        kala()
    elif valik==2:
        ochki()
    elif valik==3:
        zont()
    else:
        baboch()

win=Tk()
win.title("Квадратное уравнение")
win.geometry("900x570")
f1=Frame(win,width=900,height=500)
f1.pack(side=TOP)
f2=Frame(win,width=900,height=500)
f2.pack(side=BOTTOM)

name=Label(f1,text="Решение квадратного уравнения",height=2,width=40,font="Arial 20",fg="green",bg="lightblue",relief="solid")
name.place(x=80,y=2)

txt1=Entry(f1,width=5,font="Arial 20",fg="green",bg="lightblue",relief="solid",justify=CENTER)
txt1.place(x=1,y=150)
txt2=Entry(f1,width=5,font="Arial 20",fg="green",bg="lightblue",relief="solid",justify=CENTER)
txt2.place(x=190,y=150)
txt3=Entry(f1,width=5,font="Arial 20",fg="green",bg="lightblue",relief="solid",justify=CENTER)
txt3.place(x=380,y=150)

lbl1=Label(f1,text="x**2+",width=5,font="Arial 20",fg="green",bg="lightblue",relief="solid")
lbl1.place(x=90,y=149)
lbl2=Label(f1,text="x+",width=5,font="Arial 20",fg="green",bg="lightblue",relief="solid")
lbl2.place(x=280,y=149)
lbl3=Label(f1,text="=0",width=5,font="Arial 20",fg="green",bg="lightblue",relief="solid")
lbl3.place(x=470,y=149)

But1=Button(f1,text="Решить",height=2,width=10,font="Arial 20",bg="Green",fg="Black",relief="solid",command=quadro)
But1.place(x=570,y=125)
but2=Button(f1,text="График",height=2,width=10,font="Arial 20",bg="Green",fg="Black",relief="solid",command=grafik)
but2.place(x=730,y=125)

btn_veel=Button(f2,text="Увеличить окно",font="Calibri 26",bg="green",command=veel)
btn_veel.pack(side=TOP)
var=IntVar()

r1=Radiobutton(f2,text="Кит",variable=var,value=1, font="Calibri 26",command=figura)#command=kala
r2=Radiobutton(f2,text="Очки",variable=var,value=2, font="Calibri 26",command=figura)
r3=Radiobutton(f2,text="Зонт",variable=var,value=3, font="Calibri 26",command=figura)
r4=Radiobutton(f2,text="Бабочк0",variable=var,value=4, font="Calibri 26",command=figura)
r1.pack()
r2.pack()
r3.pack()
r4.pack()

Answer=Label(f1,text="",height=4,width=25,font="Arial 20",fg="Black",bg="Yellow",relief="solid")
Answer.place(x=180,y=280)


win.mainloop()
