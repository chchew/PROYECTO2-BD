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
miFrame.config(width="1250", height="500")
miFrame.config(bg="white")
miFrame.config(relief="sunken")
leFrame.config(width="1250", height="500")
leFrame.config(bg="red3")
leFrame.config(relief="sunken")

#Creacion de otras ventanas
def Insertar_informacion():
    call(["python", "Insertar_Informacion.py"])
    
#titulo
Label0= Label(miFrame, text="FARMACIA ROJA", fg = "red", font = "Times")
Label0.place(x=555, y=10)

#boton para ir a la ventana insertar
VInsertar=Button(miFrame, text="INSERTAR INFORMACIÓN", command=Insertar_informacion)
VInsertar.pack()
VInsertar.place(x=100,y= 410)



root.mainloop()
