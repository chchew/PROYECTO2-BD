create table CLIENTES 
as 
select * 
from dblink('host=localhost
				user=postgres
				password=pokopo
				dbname=Farmacia_Roja',
				'select *
				from "cliente"') as  linktable (
													codigo_cl character(50),
													nombre character(50),
													dirreccion character(50))