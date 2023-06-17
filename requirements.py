import mysql.connector as c
import string

con = c.connect(host = "localhost", user = "root", password = "_enter_password_here_")
cur = con.cursor()
cur.execute("create database password_manager")       #database creation
cur.execute("use password_manager")                   #useing database

#character table
cur.execute("create table chalpha (cid int primary key, calpha);")   #creating table
cur.execute("insert chalpha values(1,'!');")          #values insert
cur.execute("insert chalpha values(2,'@');")
cur.execute("insert chalpha values(3,'#');")
cur.execute("insert chalpha values(4,'$');")
cur.execute("insert chalpha values(5,'%');")
cur.execute("insert chalpha values(6,'^');")
cur.execute("insert chalpha values(7,'&');")
cur.execute("insert chalpha values(8,'*');")
cur.execute("insert chalpha values(9,'(');")
cur.execute("insert chalpha values(10,')');")

#lower character table
cur.execute("create table loalpha (lid int primary key, lchar);")         #creating table
a = (string.ascii_lowercase)
for i in range(26):
    cur.execute(f"insert loalpha values({i+1},'{a[i]}');")            #inserting values

#upper character table
cur.execute("create table upalpha (uid int primary key, ulpha);")  #creating table
b = (string.ascii_uppercase)
for j in range(26):
    cur.execute(f"insert upalpha values({j+1},'{b[j]}');")           #inserting values


#creating table to store password
cur.execute("create table pswrd_store (sr_no int primary key auto_increment,pswrd_adres varchar(100) not null unique, pswrd_usr varchar(50) not null, pswrd varchar(16) not null unique, timestamp datetime default current_timestamp););")

