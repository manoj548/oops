import psycopg2 as pg2
con = pg2.connect(dbname = "mydb", host="localhost",password = "Manu123@123",
                  port="5432",user="postgres")
print("connection is established:",con)
cursor = con.cursor()
cursor.execute("select * from emp")
data = cursor.fetchall()
print(data)
con.close()