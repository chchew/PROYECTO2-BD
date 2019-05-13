from tkinter import *
import psycopg2

con = psycopg2.connect(
            host="localhost",
            database="Farmacia Roja",
            user="postgres",
            password="pokopo"
)
cur = con.cursor()

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

#titulo
Label0= Label(miFrame, text="Insertar informacion", fg = "red", font = "Times")
Label0.place(x=555, y=10)

#producto
label1= Label(leFrame, text="PRODUCTOS", font = (40), fg="white", bg="red3")
label1.place(x=100,y=10)

def consultar_productos():
    cur.execute('SELECT * FROM "producto"')
    rows = cur.fetchall()
    cur.execute('SELECT count(nombre) FROM "producto" ')
    rows_2 = cur.fetchall()
    for r in rows_2:
        fin = int(r[0])
    print(fin)
    labelP = Label(miFrame, text="Codigo \nmedicina:", fg="red3")
    labelP.place(x=90,y=60)
    labelP = Label(miFrame, text="Nombre:", fg="red3")
    labelP.place(x=190,y=60)
    labelP = Label(miFrame, text="cantidad:", fg="red3")
    labelP.place(x=290,y=60)
    labelP = Label(miFrame, text="farmaceutica:", fg="red3")
    labelP.place(x=390,y=60)

    n = 0
    x = 0
    while n < fin:
        labelP = Label(miFrame, text=rows[0+n], fg="red3")
        labelP.place(x=90,y=100+x)
        n = n + 1
        x = x + 30

def insertar_producto():
    cur.execute('INSERT INTO "producto"( codifo_mc, nombre, cantidad_por_unidad, farmaceutica) VALUES ((%s), (%s), (%s), (%s));',(cdmc.get(),nombreP.get(),cantidadP.get(),farmaceutica.get(),))
    rows_3 = cur.fetchall()
    labelt = Label(leFrame, text="Ingresado Correctamente", fg="white", bg="white")
    labelt.place(x=150,y=250)

cdmc = Entry(leFrame)
cdmc.place(x=115,y=60)
labelt9= Label(leFrame, text="Codigo \nmedicina:", fg="white", bg="red3")
labelt9.place(x=30,y=60)

nombreP= Entry(leFrame)
nombreP.place(x=115,y=110)
labelt10= Label(leFrame, text="Nombre:", fg="white", bg="red3")
labelt10.place(x=30,y=110)

cantidadP= Entry(leFrame)
cantidadP.place(x=115,y=160)
labelt11= Label(leFrame, text="cantidad:", fg="white", bg="red3")
labelt11.place(x=30,y=160)

farmaceutica= Entry(leFrame)
farmaceutica.place(x=115,y=210)
labelt12= Label(leFrame, text="farmaceutica:", fg="white", bg="red3")
labelt12.place(x=30,y=210)

boton5=Button(miFrame, text="CONSULTAR EMPLEADOS", command=consultar_productos)
boton5.place(x=90,y= 440)
boton5=Button(miFrame, text="INGRESAR EMPLEADOS", command=insertar_producto)
boton5.place(x=100,y= 400)


#empleados
label1= Label(leFrame, text="Empleados", font = (40), fg="white", bg="red3")
label1.place(x=313,y=10)

def consultar_empleados():
    cur.execute('SELECT * FROM "empleados"')
    rows = cur.fetchall()
    cur.execute('SELECT count(nombre) FROM "empleados" ')
    rows_2 = cur.fetchall()
    for r in rows_2:
        fin = int(r[0])
    print(fin)
    labelP = Label(miFrame, text="Codigo \nempledos:", fg="red3")
    labelP.place(x=90,y=60)
    labelP = Label(miFrame, text="Nombre:", fg="red3")
    labelP.place(x=190,y=60)
    labelP = Label(miFrame, text="salario:", fg="red3")
    labelP.place(x=290,y=60)

    n = 0
    x = 0
    while n < fin:
        labelP = Label(miFrame, text=rows[0+n], fg="red3")
        labelP.place(x=90,y=100+x)
        n = n + 1
        x = x + 30

cdme = Entry(leFrame)
cdme.place(x=390,y=60)
labelt9= Label(leFrame, text="Codigo \nempleados:", fg="white", bg="red3")
labelt9.place(x=313,y=60)

nombreP= Entry(leFrame)
nombreP.place(x=390,y=110)
labelt10= Label(leFrame, text="Nombre:", fg="white", bg="red3")
labelt10.place(x=313,y=110)

salarioP= Entry(leFrame)
salarioP.place(x=390,y=160)
labelt11= Label(leFrame, text="salario:", fg="white", bg="red3")
labelt11.place(x=313,y=160)

boton5=Button(miFrame, text="CONSULTAR EMPLEADOS", command=consultar_empleados)
boton5.place(x=313,y= 440)
boton5=Button(miFrame, text="INGRESAR EMPLEADOS")
boton5.place(x=313,y= 400)

#clientes
label1= Label(leFrame, text="Clientes", font = (40), fg="white", bg="red3")
label1.place(x=553,y=10)

def consultar_empleados():
    cur.execute('SELECT * FROM "cliente"')
    rows = cur.fetchall()
    cur.execute('SELECT count(nombre) FROM "cliente" ')
    rows_2 = cur.fetchall()
    for r in rows_2:
        fin = int(r[0])
    print(fin)
    labelP = Label(miFrame, text="Codigo \ncliente:", fg="red3")
    labelP.place(x=90,y=60)
    labelP = Label(miFrame, text="Nombre:", fg="red3")
    labelP.place(x=190,y=60)
    labelP = Label(miFrame, text="Dirrección:", fg="red3")
    labelP.place(x=290,y=60)

    n = 0
    x = 0
    while n < fin:
        labelP = Label(miFrame, text=rows[0+n], fg="red3")
        labelP.place(x=90,y=100+x)
        n = n + 1
        x = x + 30

cdme = Entry(leFrame)
cdme.place(x=640,y=60)
labelt9= Label(leFrame, text="Codigo \ncliente:", fg="white", bg="red3")
labelt9.place(x=563,y=60)

nombreP= Entry(leFrame)
nombreP.place(x=640,y=110)
labelt10= Label(leFrame, text="Nombre:", fg="white", bg="red3")
labelt10.place(x=553,y=110)

salarioP= Entry(leFrame)
salarioP.place(x=640,y=160)
labelt11= Label(leFrame, text="Dirrección:", fg="white", bg="red3")
labelt11.place(x=553,y=160)

boton5=Button(miFrame, text="CONSULTAR CLIENTES", command=consultar_empleados)
boton5.place(x=553,y= 440)
boton5=Button(miFrame, text="INGRESAR CLIENTE")
boton5.place(x=553,y= 400)






root.mainloop()
cur.close()
con.close()
