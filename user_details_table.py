import sys
import mysql.connector as ms

mycon= ms.connect(host="localhost", user="root", password="Arsh@2005")

if mycon.is_connected()==False:
    sys.stderr.write("Connection failed!")
else:
    print("Connection Successful!")
    
mycur=mycon.cursor()

mycur.execute("create database details")
mycur.execute("use details")

mycur.execute("create table if not exists user_details(sl_no int primary key, Name varchar(200) not null, DOB date, email varchar(200), place_of_residence varchar(200), Gender varchar(20), username varchar(200), password varchar(200) )")
mycon.commit()

mycur.execute("""insert into user_details values(1,"John", "2004-01-10", "John123@gmail.com", "Shivajinagar, Bangalore", "Male", "John123", "john@678")""")
mycon.commit()



mycon.close()





