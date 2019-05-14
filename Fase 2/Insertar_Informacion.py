from tkinter import *
from tkinter import messagebox
import psycopg2

con = psycopg2.connect(
            host="localhost",
            database="Farmacia_Roja",
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

año = []
añoactual = []
n = []
añoactual= 2019
n = 0
def año():
    global año
    global añoactual 
    global n 
    if añoactual == 2019:
        n = n + 1
        año = añoactual + n
        Saño = str(año)
        labelaño = Label(leFrame, text=Saño, fg="white", bg="red3")
        labelaño.place(x=1005,y=150)

def negative_año():
    global año
    global añoactual
    global n 
    if añoactual == 2019:
        n = n - 1
        año = añoactual + n
        Saño = str(año)
        labelaño = Label(leFrame, text=Saño, fg="white", bg="red3")
        labelaño.place(x=1005,y=150)

mes = []
mesactual = []
nmes = []
mesactual= 0
nmes= 0
def mes():
    global mes
    global mesactual 
    global nmes 
    if mesactual == 0:
        nmes = nmes + 1
        if 0 < nmes < 13:
            mes = mesactual + nmes
            Smes = str(mes)
            labelmes = Label(leFrame, text=Smes, fg="white", bg="red3")
            labelmes.place(x=1070,y=150)

def negative_mes():
    global mes
    global mesactual 
    global nmes 
    if mesactual == 0:
        nmes = nmes - 1
        if 0 < nmes < 13:
            mes = mesactual + nmes
            Smes = str(mes)
            labelmes = Label(leFrame, text=Smes, fg="white", bg="red3")
            labelmes.place(x=1070,y=150)

dia = []
diaactual = []
ndia = []
diaactual= 0
ndia= 0
def dia():
    global dia
    global diaactual 
    global ndia 
    if diaactual == 0:
        ndia = ndia + 1
        if 0 < ndia < 32:
            dia = diaactual + ndia
            Sdia = str(dia)
            labeldia = Label(leFrame, text=Sdia, fg="white", bg="red3")
            labeldia.place(x=1135,y=150)

def negative_dia():
    global dia
    global diaactual 
    global ndia 
    if diaactual == 0:
        ndia = ndia - 1
        if 0 < ndia < 32:
            dia = diaactual + ndia
            Sdia = str(dia)
            labeldia = Label(leFrame, text=Sdia, fg="white", bg="red3")
            labeldia.place(x=1135,y=150)

hora = []
horaActual = []
nhora = []
horaActual= 0
nhora= 0
def hora():
    global hora
    global horaActual 
    global nhora 
    if horaActual == 0:
        nhora = nhora + 1
        if -1 < nhora < 24:
            hora = horaActual + nhora
            Shora = str(hora)
            labelhora = Label(leFrame, text=Shora+":00", fg="white", bg="red3")
            labelhora.place(x=1005,y=250)

def negative_hora():
    global hora
    global horaActual 
    global nhora 
    if horaActual == 0:
        nhora = nhora - 1
        if -1 < nhora < 24:
            hora = horaActual + nhora
            Shora = str(hora)
            labelhora = Label(leFrame, text=Shora+":00", fg="white", bg="red3")
            labelhora.place(x=1005,y=250)



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
   alertaP =  messagebox.askokcancel("Cuidado", "Esta seguro de mandar esta información")
   if alertaP == True:
       print("producto")

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

boton5=Button(miFrame, text="CONSULTAR PRODUCTO", command=consultar_productos)
boton5.place(x=90,y= 440)
boton5=Button(miFrame, text="INGRESAR PRODUCTO", command=insertar_producto)
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

def insertar_empleado():
   alertaE =  messagebox.askokcancel("Cuidado", "Esta seguro de mandar esta información")
   if alertaE == True:
       print("empleado")

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

boton5=Button(miFrame, text="CONSULTAR EMPLEADO", command=consultar_empleados)
boton5.place(x=313,y= 440)
boton5=Button(miFrame, text="INGRESAR EMPLEADO", command=insertar_empleado)
boton5.place(x=313,y= 400)

#clientes
label1= Label(leFrame, text="Clientes", font = (40), fg="white", bg="red3")
label1.place(x=553,y=10)

def consultar_cliente():
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

def insertar_cliente():
   alertaC =  messagebox.askokcancel("Cuidado", "Esta seguro de mandar esta información")
   if alertaC == True:
       print("cliente")

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

boton5=Button(miFrame, text="CONSULTAR CLIENTES", command=consultar_cliente)
boton5.place(x=553,y= 440)
boton5=Button(miFrame, text="INGRESAR CLIENTE", command=insertar_cliente)
boton5.place(x=553,y= 400)

#Ventas especificas
label1= Label(leFrame, text="VENTAS ESPECIFICAS", font = (40), fg="white", bg="red3")
label1.place(x=800,y=10)

def consultar_ventas():
    global año
    global mes
    global dia
    global hora
    alerta = messagebox.askokcancel("Cuidado", "Esta seguro que desea ingresar esta fecha y hora? \nRecuerda no dejarlo en blanco")
    if alerta == True: 
        fechaactual = str(año)+"-"+str(mes)+"-"+str(dia)
        horacorrecta = str(hora)+":00"
        cur.execute('SELECT * FROM "Ventas Especificas" WHERE "date" = (%s) ',(fechaactual,))
        rows = cur.fetchall()
        cur.execute('SELECT count(codigo_vn) FROM "Ventas Especificas" WHERE "date" = (%s) ',(fechaactual,))
        rows_2 = cur.fetchall()
        for r in rows_2:
            fin = int(r[0])
        print(fin)
        labelP = Label(miFrame, text="Codigo \nventa:", fg="red3")
        labelP.place(x=90,y=60)
        labelP = Label(miFrame, text="hora:", fg="red3")
        labelP.place(x=190,y=60)
        labelP = Label(miFrame, text="N. factura:", fg="red3")
        labelP.place(x=290,y=60)
        labelP = Label(miFrame, text="Dinero G:", fg="red3")
        labelP.place(x=390,y=60)
        labelP = Label(miFrame, text="C. Empleado:", fg="red3")
        labelP.place(x=490,y=60)
        labelP = Label(miFrame, text="C. Cliente:", fg="red3")
        labelP.place(x=590,y=60)
        labelP = Label(miFrame, text="C. Medicina:", fg="red3")
        labelP.place(x=690,y=60)
        labelP = Label(miFrame, text="Precio:", fg="red3")
        labelP.place(x=790,y=60)
        labelP = Label(miFrame, text="Fecha:", fg="red3")
        labelP.place(x=890,y=60)

        n = 0
        x = 0
        while n < fin:
            labelP = Label(miFrame, text=rows[0+n], fg="red3")
            labelP.place(x=90,y=100+x)
            n = n + 1
            x = x + 30

def insertar_ventas():
   alertaV =  messagebox.askokcancel("Cuidado", "Esta seguro de mandar esta información")
   if alertaV == True:
       print("ventas")

cdme = Entry(leFrame)
cdme.place(x=870,y=60)
labelt9= Label(leFrame, text="Codigo \nventa:", fg="white", bg="red3")
labelt9.place(x=800,y=60)

nombreP= Entry(leFrame)
nombreP.place(x=870,y=110)
labelt10= Label(leFrame, text="numero de \nfactura:", fg="white", bg="red3")
labelt10.place(x=800,y=110)

salarioP= Entry(leFrame)
salarioP.place(x=870,y=160)
labelt11= Label(leFrame, text="Cogio \nempleado:", fg="white", bg="red3")
labelt11.place(x=800,y=160)

salarioP= Entry(leFrame)
salarioP.place(x=870,y=210)
labelt11= Label(leFrame, text="Cogio \nmedicina:", fg="white", bg="red3")
labelt11.place(x=800,y=210)

salarioP= Entry(leFrame)
salarioP.place(x=870,y=260)
labelt11= Label(leFrame, text="Cogio \ncliente:", fg="white", bg="red3")
labelt11.place(x=800,y=260)

salarioP= Entry(leFrame)
salarioP.place(x=1060,y=60)
labelt11= Label(leFrame, text="Precio:", fg="white", bg="red3")
labelt11.place(x=1005,y=60)


#año
Baño=Button(leFrame, text="+", command=año)
Baño.place(x=1005,y= 110)
Bañom=Button(leFrame, text="-", command=negative_año)
Bañom.place(x=1030,y= 110)
l1= Label(leFrame, text="--", fg="white", bg="red3")
l1.place(x=1050,y=110)
#mes 
Bmes=Button(leFrame, text="+", command=mes)
Bmes.place(x=1070,y= 110)
Bmesm=Button(leFrame, text="-", command=negative_mes)
Bmesm.place(x=1095,y= 110)
l1= Label(leFrame, text="--", fg="white", bg="red3")
l1.place(x=1115,y=110)
#dia
Bmes=Button(leFrame, text="+", command=dia)
Bmes.place(x=1135,y= 110)
Bmesm=Button(leFrame, text="-", command=negative_dia)
Bmesm.place(x=1160,y= 110)
l1= Label(leFrame, text="--", fg="white", bg="red3")
#hora
Bmes=Button(leFrame, text="+", command=hora)
Bmes.place(x=1005,y= 210)
Bmesm=Button(leFrame, text="-", command=negative_hora)
Bmesm.place(x=1030,y= 210)
l1= Label(leFrame, text="--", fg="white", bg="red3")

boton5=Button(miFrame, text="HISTORIAL DE VENTAS", command=consultar_ventas)
boton5.place(x=800,y= 440)
boton5=Button(miFrame, text="HISTORIAL DE VENTAS\nPOR MES")
boton5.place(x=950,y= 445)
boton5=Button(miFrame, text="INGRESAR VENTAS", command=insertar_ventas)
boton5.place(x=800,y= 400)
boton5=Button(miFrame, text="HISTORIAL DE VENTAS\nPOR AÑO")
boton5.place(x=950,y= 395)





root.mainloop()
cur.close()
con.close()
