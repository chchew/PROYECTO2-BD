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


cdmc = Entry(leFrame)
cdmc.place(x=93,y=60)
labelt9= Label(leFrame, text="Codigo \nmedicina:", fg="white", bg="red3")
labelt9.place(x=30,y=60)

nombreP= Entry(leFrame)
nombreP.place(x=90,y=110)
labelt10= Label(leFrame, text="Nombre:", fg="white", bg="red3")
labelt10.place(x=30,y=110)

cantidadP= Entry(leFrame)
cantidadP.place(x=90,y=160)
labelt11= Label(leFrame, text="cantidad:", fg="white", bg="red3")
labelt11.place(x=30,y=160)

farmaceutica= Entry(leFrame)
farmaceutica.place(x=115,y=210)
labelt12= Label(leFrame, text="farmaceutica:", fg="white", bg="red3")
labelt12.place(x=30,y=210)

boton5=Button(miFrame, text="CONSULTAR EMPLEADOS", command=consultar_productos)
boton5.place(x=90,y= 440)
boton5=Button(miFrame, text="INGRESAR EMPLEADOS")
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
cdme.place(x=360,y=60)
labelt9= Label(leFrame, text="Codigo \nempleados:", fg="white", bg="red3")
labelt9.place(x=313,y=60)

nombreP= Entry(leFrame)
nombreP.place(x=360,y=110)
labelt10= Label(leFrame, text="Nombre:", fg="white", bg="red3")
labelt10.place(x=313,y=110)

cantidadP= Entry(leFrame)
cantidadP.place(x=360,y=160)
labelt11= Label(leFrame, text="salario:", fg="white", bg="red3")
labelt11.place(x=313,y=160)

boton5=Button(miFrame, text="CONSULTAR EMPLEADOS", command=consultar_empleados)
boton5.place(x=313,y= 440)
boton5=Button(miFrame, text="INGRESAR EMPLEADOS")
boton5.place(x=313,y= 400)

#cliente
label1= Label(leFrame, text="Cliente", font = (40), fg="white", bg="red3")
label1.place(x=523,y=10)

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
    labelP = Label(miFrame, text="dirreccion:", fg="red3")
    labelP.place(x=290,y=60)

    n = 0
    x = 0
    while n < fin:
        labelP = Label(miFrame, text=rows[0+n], fg="red3")
        labelP.place(x=90,y=100+x)
        n = n + 1
        x = x + 30


cdme = Entry(leFrame)
cdme.place(x=360,y=60)
labelt9= Label(leFrame, text="Codigo \cliente:", fg="white", bg="red3")
labelt9.place(x=313,y=60)

nombreP= Entry(leFrame)
nombreP.place(x=360,y=110)
labelt10= Label(leFrame, text="Nombre:", fg="white", bg="red3")
labelt10.place(x=313,y=110)

cantidadP= Entry(leFrame)
cantidadP.place(x=360,y=160)
labelt11= Label(leFrame, text="dirreccion:", fg="white", bg="red3")
labelt11.place(x=313,y=160)

boton5=Button(miFrame, text="CONSULTAR EMPLEADOS", command=consultar_empleados)
boton5.place(x=313,y= 440)
boton5=Button(miFrame, text="INGRESAR EMPLEADOS")
boton5.place(x=313,y= 400)

#ventas especificas
label1= Label(leFrame, text="PRODUCTOS", font = (40), fg="white", bg="red3")
label1.place(x=739,y=10)

def consultar_productos():
    cur.execute('SELECT * FROM "Ventas Especificas"')
    rows = cur.fetchall()
    cur.execute('SELECT count(nombre) FROM "Ventas Especificas" ')
    rows_2 = cur.fetchall()
    for r in rows_2:
        fin = int(r[0])
    print(fin)
    labelP = Label(miFrame, text="Codigo \nvn:", fg="red3")
    labelP.place(x=90,y=60)
    labelP = Label(miFrame, text="Hora:", fg="red3")
    labelP.place(x=190,y=60)
    labelP = Label(miFrame, text="NumeroFactura:", fg="red3")
    labelP.place(x=290,y=60)
    labelP = Label(miFrame, text="DineroGenerado:", fg="red3")
    labelP.place(x=390,y=60)
    labelP = Label(miFrame, text="codigoep:", fg="red3")
    labelP.place(x=390,y=60)
    labelP = Label(miFrame, text="codigomc:", fg="red3")
    labelP.place(x=390,y=60)
    labelP = Label(miFrame, text="precio:", fg="red3")
    labelP.place(x=390,y=60)
    labelP = Label(miFrame, text="date:", fg="red3")
    labelP.place(x=390,y=60)

    n = 0
    x = 0
    while n < fin:
        labelP = Label(miFrame, text=rows[0+n], fg="red3")
        labelP.place(x=90,y=100+x)
        n = n + 1
        x = x + 30


cdmc = Entry(leFrame)
cdmc.place(x=93,y=60)
labelt9= Label(leFrame, text="Codigo \nvn:", fg="white", bg="red3")
labelt9.place(x=30,y=60)

nombreP= Entry(leFrame)
nombreP.place(x=90,y=110)
labelt10= Label(leFrame, text="Hora:", fg="white", bg="red3")
labelt10.place(x=30,y=110)

cantidadP= Entry(leFrame)
cantidadP.place(x=90,y=160)
labelt11= Label(leFrame, text="NumeroFactura:", fg="white", bg="red3")
labelt11.place(x=30,y=160)

farmaceutica= Entry(leFrame)
farmaceutica.place(x=115,y=210)
labelt12= Label(leFrame, text="DineroGenerado:", fg="white", bg="red3")
labelt12.place(x=30,y=210)

farmaceutica= Entry(leFrame)
farmaceutica.place(x=115,y=210)
labelt12= Label(leFrame, text="codigoep:", fg="white", bg="red3")
labelt12.place(x=30,y=210)

farmaceutica= Entry(leFrame)
farmaceutica.place(x=115,y=210)
labelt12= Label(leFrame, text="codigomc:", fg="white", bg="red3")
labelt12.place(x=30,y=210)

farmaceutica= Entry(leFrame)
farmaceutica.place(x=115,y=210)
labelt12= Label(leFrame, text="precio:", fg="white", bg="red3")
labelt12.place(x=30,y=210)

farmaceutica= Entry(leFrame)
farmaceutica.place(x=115,y=210)
labelt12= Label(leFrame, text="date:", fg="white", bg="red3")
labelt12.place(x=30,y=210)

boton5=Button(miFrame, text="CONSULTAR EMPLEADOS", command=consultar_productos)
boton5.place(x=90,y= 440)
boton5=Button(miFrame, text="INGRESAR EMPLEADOS")
boton5.place(x=100,y= 400)



root.mainloop()
cur.close()
con.close()
