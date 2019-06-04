import psycopg2

con = psycopg2.connect(
            host="localhost",
            database="Farmacia_Roja",
            user="postgres",
            password="pokopo"
)
cur = con.cursor()





cur.close()

con.close()
