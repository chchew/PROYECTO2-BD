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
miFrame.config(width="700", height="300")
miFrame.config(bg="white")
miFrame.config(relief="sunken")
leFrame.config(width="700", height="300")
leFrame.config(bg="red3")
leFrame.config(relief="sunken")

def ingresar_fecha():
    #fecha para el query
    FechaActual = str(year.get())+"-"+str(month.get())+"-"+str(day.get())
    print(FechaActual)
    

#Comienzo de la estructura
#titulo
labelT = Label(miFrame, text="Simular Dia", fg= "red", font="Times")
labelT.place(x=255, y=10)
#Botones de fecha
labelYear= Label(leFrame, text="Año", fg="white", bg="red3")
labelYear.place(x=20, y=20)
year = Spinbox(leFrame, from_=0, to=1000000, width=10)
year.place(x=20, y=50)

labelMonth= Label(leFrame, text="Mes", fg="white", bg="red3")
labelMonth.place(x=20, y=80)
month = Spinbox(leFrame, from_=0, to=12, width=10)
month.place(x=20, y=110)

labelDay= Label(leFrame, text="Dia", fg="white", bg="red3")
labelDay.place(x=20, y=140)
day = Spinbox(leFrame, from_=0, to=31, width=10)
day.place(x=20, y=170)

fechaBoton = Button(leFrame, text="FECHA A SIMULAR", command=ingresar_fecha)
fechaBoton.place(x=20, y=200)

root.mainloop()
cur.close()
con.close()  
