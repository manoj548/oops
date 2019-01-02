import psycopg2 as pg2
a = int(input("Enter id:"))
b = input("Enter name:")
c = input("Enter location:")
con = pg2.connect(dbname = "mydb", host="localhost",password = "Manu123@123",
                  port="5432",user="postgres")
print("connection is established:",con)
cursor = con.cursor()
cursor.execute("""insert into emp values(%s,%s,%s)""")
cursor.execute("select * from emp")
data = cursor.fetchall()
con.commit()
print(data)
con.close()

