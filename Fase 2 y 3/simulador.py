import random 
from tkinter import * 
import psycopg2



con = psycopg2.connect(

            host="localhost",

            database="Farmacia_Roja",

            user="postgres",

            password="pokopo"

)

cur = con.cursor()


#Simulacion 
def simulacion():
	
	loop = int(cant.get()) 
	while loop != 0:
		num_productos = random.randint(1,5)
		cliente_ran = random.choice(cliente)
		empleado_ran = random.choice(empleado)
		venta = 'VN' + (mes.get()) + (year.get())
		hora = str(random.randint(00,24))
		minuto = str(random.randint(00,59))
		segundo = str(random.randint(00,59))
		time = hora + ":" + minuto + ":" + segundo
		mess=mes.get()
		realmes=' '

		if mess =='jan':
			realmes='01'

		elif mess =='feb':
			realmes='02'

		elif mess=='mar':
			realmes='03'

		elif mess=='apr':
			realmes='04'

		elif mess=='may':
			realmes='05'

		elif mess=='jun':
			realmes='06'

		elif mess=='jul':
			realmes='07'

		elif mess=='aug':
			realmes='08'

		elif mess=='sep':
			realmes='09'

		elif mess=='oct':
			realmes='10'

		elif mess=='nov':
			realmes='11' 

		elif mess=='dec':
			realmes='12'

		numf = loop 
		stnumf = str(numf)

		facura = '20'+(year.get())+'_'+realmes+'_'+stnumf

		realdate = '20'+(year.get())+'-'+realmes+'-'+(dia.get())


		while num_productos != 0:
			precio  = random.randint(10,500)
			producto_ran= random.choice(producto)


			cur.execute('INSERT INTO public."Ventas Especificas"(codigo_vn, hora, "numero de factura ", dinero_generado, codigo_ep, codigo_cl, codigo_mc, precio, date) VALUES (%s, %s, %s, 15, %s, %s, %s, %s, %s);',(venta,time, factura,15,empleado_ran,cliente_ran,producto_ran,precio,realdate))
			con.commit()

			num_productos = num_productos - 1

		loop = loop - 1

	



#Creacion de Raiz
root  = Tk() 


root.title("Proyecto Bases de Datos")



#Creacion del Frame

leFrame=Frame()


#Empaquetacion del Frame

leFrame.pack()

#Propiedades del Frame


leFrame.config(width="700", height="500")
leFrame.config(bg="red3")
leFrame.config(relief="sunken")




# Labels, entries y boton
label1= Label(leFrame, text="INGRESE LA CANTIDAD DE TRANSACCIONES", font = (40))
label1.place(x=100,y=100)

cant = StringVar()
entry1= Entry(leFrame, textvariable=cant)
entry1.place(x=100,y=130)

label2= Label(leFrame, text="INGRESE EL MES", font = (40))
label2.place(x=100,y=200)

mes= StringVar() 
entry2= Entry(leFrame,textvariable=mes)
entry2.place(x=100,y=230)

label3= Label(leFrame, text="INGRESE EL DIA", font = (40))
label3.place(x=100,y=280)

dia= StringVar()
entry3= Entry(leFrame,textvariable=dia)
entry3.place(x=100,y=310)

label4= Label(leFrame, text="INGRESE EL AÑO", font = (40))
label4.place(x=100,y=360)

year= StringVar() 
entry4= Entry(leFrame,textvariable=year)
entry4.place(x=100,y=390)

boton1= Button(leFrame, text="SIMULAR", command = simulacion)
boton1.place(x=600,y=200)



#Prework
cliente =['cl01','cl02','cl03','cl04','cl05','cl06', 'cl07', 'cl08', 'cl09', 'cl10', 'cl11', 'cl12', 'cl13', 'cl014', 'cl15', 'cl16', 'cl17', 'cl18', 'cl19', 'cl20', 'cl21', 'cl22', 'cl23', 'cl24', 'cl25']
producto =['mc01','mc02','mc03','mc04','mc05','mc06','mc07','mc08','mc09','mc10','mc11','mc12','mc13','mc14','mc15','mc16','mc17','mc18','mc019','mc020']
empleado =['ep01', 'ep02', 'ep03', 'ep04', 'ep05']






res_cliente = random.choice(cliente)
res_producto = random.choice(producto)
res_empleado = random.choice(empleado)









#End del Frame
root.mainloop()
cur.close()

con.close()
