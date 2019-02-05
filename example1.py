import sqlite3
name="lavanya"
branch="cse"
rollno="548"
con=sqlite3.connect("mydb.sqlite")
cur=con.cursor()
cur.execute("create table if not exists mydata(name text,rollno integer,branch text)")
name=raw_input("enter the name")
branch=raw_input("enter the branch")
rollno=raw_input("enter the rollno")
cur.execute("insert into mydata values(?,?,?)",(name,rollno,branch))
con.commit()
cur.execute("SELECT * from mydata")
for row in cur.fetchall():
	print(row)
cur.close()
con.close()
