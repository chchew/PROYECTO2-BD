from tkinter import * 
import psycopg2

con = psycopg2.connect(

            host="localhost",
            database="Farmacia_Roja",
            user="postgres",
            password="pokopo"
)
cur = con.cursor()
root  = Tk() 
root.title("Proyecto Bases de Datos")

#Creacion del Frame
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

#Comienzo de la estructura
#titulo

labelT = Label(miFrame, text="Simular Dia", fg= "red", font="Times")
labelT.place(x=555, y=10)



 

root.mainloop()
cur.close()
con.close()  
