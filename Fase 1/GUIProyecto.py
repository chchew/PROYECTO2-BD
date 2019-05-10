from tkinter import * 
import psycopg2 

#Creacion de Raiz
root  = Tk() 


root.title("Proyecto Bases de Datos")
root.iconbitmap("logo.ico")


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
leFrame.config(bg="gray")
leFrame.config(relief="sunken")

#Labels de Titulos
Label0= Label(miFrame, text="FARMACIA ROJA",font=(42))
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

text1= Entry(leFrame)
text1.place(x=100,y=60)
labelt1= Label(leFrame, text="CodEP:")
labelt1.place(x=50,y=60)

text2= Entry(leFrame)
text2.place(x=100,y=110)
labelt2= Label(leFrame, text="Nombre:")
labelt2.place(x=50,y=110)

text3= Entry(leFrame)
text3.place(x=100,y=160)
labelt3= Label(leFrame, text="Salario:")
labelt3.place(x=50,y=160)

text4= Entry(leFrame)
text4.place(x=100,y=210)
labelt4= Label(leFrame, text="NDV:")
labelt4.place(x=50,y=210)



text5= Entry(leFrame)
text5.place(x=400,y=60)
labelt5= Label(leFrame, text="CodCL:")
labelt5.place(x=350,y=60)

text6= Entry(leFrame)
text6.place(x=400,y=110)
labelt6= Label(leFrame, text="Nombre:")
labelt6.place(x=350,y=110)

text7= Entry(leFrame)
text7.place(x=400,y=160)
labelt7= Label(leFrame, text="Gasto:")
labelt7.place(x=350,y=160)

text8= Entry(leFrame)
text8.place(x=400,y=210)
labelt8= Label(leFrame, text="Direccion:")
labelt8.place(x=350,y=210)



text9= Entry(leFrame)
text9.place(x=700,y=60)
labelt9= Label(leFrame, text="CodMC:")
labelt9.place(x=650,y=60)

text10= Entry(leFrame)
text10.place(x=700,y=110)
labelt10= Label(leFrame, text="Nombre:")
labelt10.place(x=650,y=110)

text11= Entry(leFrame)
text11.place(x=700,y=160)
labelt11= Label(leFrame, text="Precio:")
labelt11.place(x=650,y=160)

text12= Entry(leFrame)
text12.place(x=700,y=210)
labelt12= Label(leFrame, text="Cantidad:")
labelt12.place(x=650,y=210)

text13= Entry(leFrame)
text13.place(x=700,y=260)
labelt13= Label(leFrame, text="Farm:")
labelt13.place(x=650,y=260)



text14= Entry(leFrame)
text14.place(x=1000,y=60)
labelt14= Label(leFrame, text="CodVN:")
labelt14.place(x=950,y=60)

text15= Entry(leFrame)
text15.place(x=1000,y=110)
labelt15= Label(leFrame, text="CodEP:")
labelt15.place(x=950,y=110)

text16= Entry(leFrame)
text16.place(x=1000,y=160)
labelt16= Label(leFrame, text="CodCL:")
labelt16.place(x=950,y=160)

text17= Entry(leFrame)
text17.place(x=1000,y=210)
labelt17= Label(leFrame, text="CodMC:")
labelt17.place(x=950,y=210)

text18= Entry(leFrame)
text18.place(x=1000,y=260) 
labelt18= Label(leFrame, text="Fecha:")
labelt18.place(x=950,y=260)

text19= Entry(leFrame)
text19.place(x=1000,y=310)
labelt19= Label(leFrame, text="NumFac:")
labelt19.place(x=950,y=310)

text20= Entry(leFrame)
text20.place(x=1000,y=360)
labelt20= Label(leFrame, text="Hora:")
labelt20.place(x=950,y=360)



#Buttons 

boton1=Button(leFrame, text="INGRESAR")
boton1.place(x=100,y= 410)

boton2=Button(leFrame, text="INGRESAR" )
boton2.place(x=400,y= 410)

boton3=Button(leFrame, text="INGRESAR")
boton3.place(x=700,y= 410)

boton4=Button(leFrame, text="INGRESAR" )
boton4.place(x=1000,y= 410)

boton5=Button(miFrame, text="CONSULTAR EMPLEADOS", )
boton5.place(x=100,y= 410)

boton6=Button(miFrame, text="CONSULTAR CLIENTES" )
boton6.place(x=400,y= 410)

boton7=Button(miFrame, text="CONSULTAR PRODUCTOS")
boton7.place(x=700,y= 410)

boton8=Button(miFrame, text="CONSULTAR VENTAS" )
boton8.place(x=1000,y= 410)





#Funciones de los botones









 

root.mainloop()  
