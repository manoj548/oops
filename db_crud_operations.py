import psycopg2 as pg2
try:
    con = pg2.connect(dbname = "mydb", host="localhost",password = "Manu123@123",
                  port="5432",user="postgres")
    print("connection is established:",con)
    cursor = con.cursor()
    #sql = "insert into emp values(102,'manoj','bangalore');"
    cursor.execute("""insert into emp values(102,'manoj','bangalore')""")
    print("data inserted sucessfully")
    cursor.execute("select * from emp")
    data = cursor.fetchall()
    con.commit()
    print(data)

except:
    print("connection failed")
else:
    print("connection established sucessfully")

finally:

    con.close()