from tkinter import *
from subprocess import call

#creacion de raiz
root = Tk()
root.title("Proyecto Bases de datos")
#Creacion del frame
miFrame=Frame()
leFrame=Frame()
#Empaquetacion del Frame
miFrame.pack()
leFrame.pack()
#Propiedades del Frame
miFrame.config(width="1000", height="300")
miFrame.config(bg="white")
miFrame.config(relief="sunken")
leFrame.config(width="1000", height="300")
leFrame.config(bg="red3")
leFrame.config(relief="sunken")

#Creacion de otras ventanas
def Insertar_informacion():
    call(["python", "Insertar_Informacion.py"])

def Simular_ventas():
    call(["python", "simulador.py"])
    
#titulo
Label0= Label(miFrame, text="FARMACIA ROJA", fg = "red", font = "Times")
Label0.place(x=450, y=10)

#boton para ir a la ventana insertar
L1= Label(miFrame, text="1.", fg = "red", bg="white", font = "Symbol")
L1.place(x=100, y=40)
VInsertar=Button(miFrame, text="INSERTAR INFORMACIÓN", command=Insertar_informacion)
VInsertar.pack()
VInsertar.place(x=150,y= 40)

#simular ventas 
L2= Label(miFrame, text="2.", fg = "red", bg="white" ,font = "Symbol")
L2.place(x=100, y=140)
consulta=Button(miFrame, text="SIMULADOR DE VENTAS", command=Simular_ventas)
consulta.pack()
consulta.place(x=150,y= 140)

#boton para ir ayuda
L2= Label(miFrame, text="3.", fg = "red", bg="white" ,font = "Symbol")
L2.place(x=100, y=240)
ayuda = Button(miFrame, text="Ayuda")
ayuda.pack()
ayuda.place(x=150, y=240)

root.mainloop()
