from tkinter import * 
import psycopg2

con = psycopg2.connect(

            host="localhost",

            database="Farmacia_Roja",

            user="postgres",

            password="pokopo"

)

cur = con.cursor()

#Creacion de Raiz
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

#Labels de Titulos 
Label0= Label(miFrame, text="FARMACIA ROJA: Consultas Rápidas",font=(42))
Label0.place(x=555, y=10)

label1= Label(leFrame, text="EMPLEADOS", font = (40))
label1.place(x=100,y=10)

label2= Label(leFrame, text="CLIENTES", font = (40))
label2.place(x=400,y=10)

label3= Label(leFrame, text="PRODUCTO", font = (40))
label3.place(x=700,y=10)

label4= Label(leFrame, text="VENTAS", font = (40))
label4.place(x=1000,y=10)

#Label y entry de informacion por categoria

#Funciones de los botones


def mejor_vendedor():
	root.mainloop()
	cur.close()
	con.close()  

def mejor_pagado():
	cur.execute('SELECT nombre , salario FROM "empleados" ORDER BY salario DESC LIMIT 10')
	rows = cur.fetchall()
	rows

def mejor_cliente():
	root.mainloop()
	cur.close()
	con.close()  

def mas_frecuente():
	cur.execute('SELECT nombre,COUNT(nombre) AS visitas FROM "clientes" ORDER BY visitas DESC LIMIT 10')
	rows=cur.fetchall()
	rows

def mas_abundante():
	cur.execute('SELECT nombre,cantidad_por_unidad FROM "productos" ORDER BY cantidad_por_unidad DESC LIMIT 10')
	rows=cur.fetchall()
	rows

def mas_caro():
	cur.execute('SELECT nombre,precio FROM "productos" ORDER BY precio DESC LIMIT 10 ' )
	rows=cur.fetchall()
	rows

def mayor_ventas():
	cur.execute('SELECT "numero de factura", dinero_generado, date FROM "Ventas Especificasd" ORDER BY dinero_generado DESC LIMIT 10 ')
	rows=cur.fetchall()
	rows

def listado_empleados():
	cur.execute('SELECT nombre FROM "empleados" ORDER BY nombre')
	rows=cur.fetchall()
	rows 




#Buttons 

boton1=Button(leFrame, text="Mejor vendedor", command=mejor_vendedor)
boton1.place(x=100,y= 110)

boton2=Button(leFrame, text="Mejor cliente", command=mejor_cliente)
boton2.place(x=400,y= 110)

boton3=Button(leFrame, text="Mas abundante", command=mas_abundante)
boton3.place(x=700,y= 110)

boton4=Button(leFrame, text="Numero de ventas", command=mayor_venta)
boton4.place(x=1000,y= 110)

boton5=Button(leFrame, text="Mejor pagado", command=mejor_pagado)
boton5.place(x=100,y= 210)

boton6=Button(leFrame, text="Mas frecuente", command=mas_frecuente)
boton6.place(x=400,y= 210)

boton7=Button(leFrame, text="Mas caro", command= mas_caro)
boton7.place(x=700,y= 210)

boton8=Button(leFrame, text="To be continue" )
boton8.place(x=1000,y= 210)

boton9=Button(leFrame, text="Listado de Empleados", command=listado_empleados)
boton9.place(x=100,y= 310)

 

root.mainloop()
cur.close()
con.close()  
