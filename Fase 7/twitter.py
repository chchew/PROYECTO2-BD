import tweepy
import psycopg2
import random

con = psycopg2.connect(
            host="localhost",
            database="farmacia_amarilla",
            user="postgres",
            password="olakease"
)
cur = con.cursor()

oferta = []
cur.execute('select cliente.nombre from "cliente" join "ventasespecificas" on ventasespecificas.codigo_cl = cliente.codigo_cl where ventasespecificas.precio >500')
rows_cl = cur.fetchall()
for r in rows_cl:
    r = str(r)
    r = r.strip("'(")
    r = r.strip("'                                              ',)")
    oferta.append(r)
OFERTA = random.choice(oferta)

#Contraseñas para acceder a la cuenta
consumer_key = 'PJIMWe4c17gIilkMTEDa9D63m'

consumer_secret = '0xOP80bDb5Kq7kCn62W5hoTIOo7AXP2T7fP6g8ZljCxCtXAmoQ'

access_token = '1135283448317403136-UquM3xdY9y5d5c1yeYgK3gpuN40NiA'

access_token_secret = 'OoSO8gA3hLz7oND30F5st7m1lefZJMFJjNjeTwSap5S9V'


#Acceso a la cuenta de desarrollador
def OAuth():

	try:

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

		auth.set_access_token(access_token, access_token_secret)

		return auth

	except Exception as e:

		return None


oauth = OAuth()
api = tweepy.API(oauth)

#Listado de ofertas
oferta1= 'HOLA @'+OFERTA+' HOY TIENES 2X1 CON TU TARJETA CLUB BI !!!! '

oferta2='50% DE DESCUENTO EN minoxidil PARA TI @'+OFERTA+' TODO EL MES'

oferta3='@'+OFERTA+' YA TENEMOS viagra DISPONIBLE EN TODAS NUESTRAS TIENDAS !'

oferta4='@'+OFERTA+'!  DILE ADIOS A ESOS MALESTARES, 20% DESCUENTO HASTA EL 10 DE JULIO EN TODA LA TIENDA'

oferta5='3X1 EN LO QUE QUIERAS @'+OFERTA+' HASTA ACABAR EXISTENCIAS'

#Ecoje un oferta al azar
RANDOM = [oferta1,oferta2,oferta3,oferta4,oferta5]
oferton = random.choice(RANDOM)

#Publica la oferta
api.update_status(oferton) 

#Cierra la conexion con postgres
cur.close()

con.close()