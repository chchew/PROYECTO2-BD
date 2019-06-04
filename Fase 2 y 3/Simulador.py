import random
from tkinter import messagebox
from tkinter import *
import psycopg2



con = psycopg2.connect(
            host="localhost",
            database="Farmacia_Azul",
            user="postgres",
            password="admin"
)
cur = con.cursor()

#Creacion de Raiz
root  = Tk()
root.title("Simulación")

#Creacion del Frame
leFrame=Frame()
leFrame.pack()

#Propiedades del Frame
leFrame.config(width="700", height="500")
leFrame.config(bg="red3")
leFrame.config(relief="sunken")

def simular():
    MES = mes.get()
    DIA = dia.get()
    AÑO = año.get()
    CANT = cantidad.get()
    NN = nn.get()
    entradas = int(CANT)

    mesSTR = ''
    ##codigoVN
    if int(MES) == 1:
        mesSTR = 'ene'
    elif int(MES) == 2:
        mesSTR = 'feb'
    elif int(MES) == 3:
        mesSTR = 'mar'
    elif int(MES) == 4:
        mesSTR = 'abr'
    elif int(MES) == 5:
        mesSTR = 'may'
    elif int(MES) == 6:
        mesSTR = 'jun'
    elif int(MES) == 7:
        mesSTR = 'jul'
    elif int(MES) == 8:
        mesSTR = 'ago'
    elif int(MES) == 9:
        mesSTR = 'sep'
    elif int(MES) == 10:
        mesSTR = 'oct'
    elif int(MES) == 11:
        mesSTR = 'nov'
    elif int(MES) == 12:
        mesSTR = 'dic'
    else:
        alertaMES =  messagebox.askokcancel("CUIDADO","Ese mes no existe")
    añoVN = AÑO.strip('20')
    codigoVN = "VN"+mesSTR+añoVN

    ##hora
    hora = ["1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00"]

    #empleados
    empleados = []
    cur.execute('select codigo_ep from "empleados"')
    rows_em = cur.fetchall()
    for r in rows_em:
        r = str(r)
        r = r.strip("'(")
        r = r.strip("'                                              ',)")
        empleados.append(r)

    #cliente
    cliente = []
    cur.execute('select codigo_cl from "cliente"')
    rows_cl = cur.fetchall()
    for r in rows_cl:
        r = str(r)
        r = r.strip("'(")
        r = r.strip("'                                              ',)")
        cliente.append(r)
    CLIENTE = random.choice(cliente)

    #medicina
    medicina = []
    cur.execute('select codifo_mc from "producto"')
    rows_mc = cur.fetchall()
    for r in rows_mc:
        r = str(r)
        r = r.strip("'(")
        r = r.strip("'                                              ',)")
        medicina.append(r)

    #fecha
    date = AÑO+"-"+MES+"-"+DIA
    origen = 'farmacia_roja'


    i = 0
    e = 1
    while i < entradas:
        if e == 1:
            NNN = int(NN)
            NN = str(NNN)
            numeroFactura = AÑO+"_"+MES+"_"+NN
            horan = random.choice(hora)
            generado = 15
            EMPLEADO = random.choice(empleados)
            CLIENTE = random.choice(cliente)
            MEDICINA = random.choice(medicina)
            cur.execute('select "precio_individual" from "producto" where "codifo_mc"  = %s', (MEDICINA,))
            rows_pr = cur.fetchall()
            for r in rows_pr:
                r = str(r)
                r = r.strip("(")
                precio = r.strip(",)")
            cur.execute('INSERT INTO public."Ventas Especificas"(codigo_vn, hora, "numero de facturas", dinero_generado, codigo_ep, codigo_cl, codigo_mc, precio, date, origen)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'\
                        ,(codigoVN, horan, numeroFactura, generado, EMPLEADO, CLIENTE, MEDICINA, precio, date, origen))
            con.commit()
            e += 1
            i = i + 1

        elif e == 2:
            NNN = int(NN)
            NNN +=  1
            NN = str(NNN)
            numeroFactura = AÑO+"_"+MES+"_"+NN
            horan = random.choice(hora)
            generado = 15
            EMPLEADO = random.choice(empleados)
            CLIENTE = random.choice(cliente)
            MEDICINA = random.choice(medicina)
            cur.execute('select "precio_individual" from "producto" where "codifo_mc"  = %s', (MEDICINA,))
            rows_pr = cur.fetchall()
            for r in rows_pr:
                r = str(r)
                r = r.strip("(")
                precio = r.strip(",)")
            cur.execute('INSERT INTO public."Ventas Especificas"(codigo_vn, hora, "numero de facturas", dinero_generado, codigo_ep, codigo_cl, codigo_mc, precio, date, origen)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'\
                        ,(codigoVN, horan, numeroFactura, generado, EMPLEADO, CLIENTE, MEDICINA, precio, date, origen))
            con.commit()
            if e == 2:
                MEDICINA = random.choice(medicina)
                cur.execute('select "precio_individual" from "producto" where "codifo_mc"  = %s', (MEDICINA,))
                rows_pr = cur.fetchall()
                for r in rows_pr:
                    r = str(r)
                    r = r.strip("(")
                    precio = r.strip(",)")
                cur.execute('INSERT INTO public."Ventas Especificas"(codigo_vn, hora, "numero de facturas", dinero_generado, codigo_ep, codigo_cl, codigo_mc, precio, date, origen)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'\
                        ,(codigoVN, horan, numeroFactura, generado, EMPLEADO, CLIENTE, MEDICINA, precio, date, origen))
                con.commit()
                e += 1
                i = i + 1

        elif e == 3:
            NNN = int(NN)
            NNN +=  1
            NN = str(NNN)
            numeroFactura = AÑO+"_"+MES+"_"+NN
            horan = random.choice(hora)
            generado = 15
            EMPLEADO = random.choice(empleados)
            CLIENTE = random.choice(cliente)
            MEDICINA = random.choice(medicina)
            cur.execute('select "precio_individual" from "producto" where "codifo_mc"  = %s', (MEDICINA,))
            rows_pr = cur.fetchall()
            for r in rows_pr:
                r = str(r)
                r = r.strip("(")
                precio = r.strip(",)")
            cur.execute('INSERT INTO public."Ventas Especificas"(codigo_vn, hora, "numero de facturas", dinero_generado, codigo_ep, codigo_cl, codigo_mc, precio, date, origen)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'\
                        ,(codigoVN, horan, numeroFactura, generado, EMPLEADO, CLIENTE, MEDICINA, precio, date, origen))
            con.commit()
            if e ==3:
                MEDICINA = random.choice(medicina)
                cur.execute('select "precio_individual" from "producto" where "codifo_mc"  = %s', (MEDICINA,))
                rows_pr = cur.fetchall()
                for r in rows_pr:
                    r = str(r)
                    r = r.strip("(")
                    precio = r.strip(",)")
                cur.execute('INSERT INTO public."Ventas Especificas"(codigo_vn, hora, "numero de facturas", dinero_generado, codigo_ep, codigo_cl, codigo_mc, precio, date)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'\
                        ,(codigoVN, horan, numeroFactura, generado, EMPLEADO, CLIENTE, MEDICINA, precio, date, origen))
                con.commit()
                e = 3
                if e == 3:
                    MEDICINA = random.choice(medicina)
                    cur.execute('select "precio_individual" from "producto" where "codifo_mc"  = %s', (MEDICINA,))
                    rows_pr = cur.fetchall()
                    for r in rows_pr:
                        r = str(r)
                        r = r.strip("(")
                        precio = r.strip(",)")
                    cur.execute('INSERT INTO public."Ventas Especificas"(codigo_vn, hora, "numero de facturas", dinero_generado, codigo_ep, codigo_cl, codigo_mc, precio, date, origen)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'\
                            ,(codigoVN, horan, numeroFactura, generado, EMPLEADO, CLIENTE, MEDICINA, precio, date, origen))
                    con.commit()

                    NNN = int(NN)
                    NNN +=  1
                    NN = str(NNN)
                    e = 1
                    i = i + 1
    print("HECHO")


#Ingresar cantidad
labelf= Label(leFrame, text="INGRESE EL NUMERO DE FACTRUA", fg="white", bg="red3")
labelf.place(x=90,y=10)
nn = Spinbox(leFrame, from_=0, to=1000)
nn.place(x=90,y=40)

label1= Label(leFrame, text="INGRESE LA CANTIDAD DE TRANSACCIONES", fg="white", bg="red3")
label1.place(x=90,y=100)
cantidad= Spinbox(leFrame, from_=0, to=1000)
cantidad.place(x=90,y=130)

labelM= Label(leFrame, text="INGRESE EL MES", fg="white", bg="red3")
labelM.place(x=90,y=200)
mes = Spinbox(leFrame, from_=0, to=12)
mes.place(x=90,y=230)

labelD= Label(leFrame, text="INGRESE EL DIA", fg="white", bg="red3")
labelD.place(x=90,y=280)
dia= Spinbox(leFrame, from_=0, to=31)
dia.place(x=90,y=310)

labelA= Label(leFrame, text="INGRESE EL AÑO", fg="white", bg="red3")
labelA.place(x=90,y=360)
año= Spinbox(leFrame, from_=0, to=1000000)
año.place(x=90,y=390)

boton1= Button(leFrame, text="SIMULAR", command=simular)
boton1.place(x=100,y=450)


#End del Frame
root.mainloop()
cur.close()

con.close()
