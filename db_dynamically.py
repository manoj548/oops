import psycopg2 as pg2
con = pg2.connect(dbname = "mydb", host="localhost",password = "Manu123@123",
                  port="5432",user="postgres")
#print("connection is established:",con)
cursor = con.cursor()
a = [int(input("Enter id:"))]
b = [input("Enter name:")]
c = [input("Enter location:")]
d = []
for i in enumerate(a):
    for j in enumerate(b):
        for k in enumerate(c):
           if i[0]==j[0]==k[0]:
               d.append((i[1],j[1],k[1]))
print(d)
cursor.executemany("insert into emp(id,name,loc) values(%s%s%s)",d)
cursor.execute("""select * from emp""")
data = cursor.fetchall()
con.commit()
cursor.close()
#print(data)
con.close()

