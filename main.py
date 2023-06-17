import mysql.connector as c
con = c.connect(host = "localhost", user = "root", password = "password@123")
cur = con.cursor()

cur.execute("use password_manager")
#password creator
import random
password = ""
def paswrd():     #password generator
    lim = 0
    pswrd = ""
    while lim ==0:
        n1 = random.randint(1,17)
        n2 = random.randint(1,17)
        n3 = random.randint(1,17)
        sum = n1+n2+n3
        if (sum) == 12:
            for i in range(n1):
                p1 = random.randint(1,26)
                cur.execute(f"select uchar from upalpha where uid = {p1}")
                l = cur.fetchone()
                for i in l:
                    #print(i)
                    pswrd+=i
            for i in range(n2):
                p2 = random.randint(1,26)
                cur.execute(f"select lchar from loalpha where lid = {p2}")
                l = cur.fetchone()
                for i in l:
                    #print(i)
                    pswrd+=i
            for i in range(n3):
                p3 = random.randint(1,10)
                cur.execute(f"select calpha from chalpha where cid = {p3}")
                l = cur.fetchone()
                for i in l:
                    #print(i)
                    pswrd+=i

            lim = 1

    return (pswrd)


def passt(a, p,u): #password storage
    try:
        cur.execute(f"insert pswrd_store(pswrd_adres,pswrd_usr,pswrd) values('{a}','{u}','{p}');")
        con.commit()

    except :
        print("error")



def pasdis():  #password display
    cur.execute("select * from pswrd_store")
    l = cur.fetchall()
    print("The details about your password/s are:")
    print(" ")
    for i in range(len(l)):
        print(l[i][0],"  ",l[i][1],"  ",l[i][2]," ",l[i][3])




if __name__ == "__main__":
    lim = 0
    while lim==0:
        inp = input("enter 'p' for password generation and 'd' to get details of your password or 'e' to simply exit ")
        if inp=="p":
            addres = input("enter the password address")
            usr = input("enter username/mail id/phone_number")
            p = paswrd()
            print("your generated password is ",p)
            passt(addres,p,usr)
            lim=1
        elif inp=="d":
            pasdis()
            lim = 1
        elif inp=="e":
            lim=1
        else:
            print("sorry I can't help you with that")







