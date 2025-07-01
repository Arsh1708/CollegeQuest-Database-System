#admin
import sys
import mysql.connector as ms

mycon= ms.connect(host="localhost", user="root", password="dpsbn")

if mycon.is_connected()==False:
    sys.stderr.write("Connection failed!")
else:
    print("Connection Successful!")
    
mycur=mycon.cursor()

mycur.execute("use details")

mycur.execute("create table if not exists Admin(sl_no int primary key, Name varchar(200) not null, DOB date, email varchar(200), place_of_residence varchar(200), Gender varchar(20), username varchar(200), password varchar(200) )")
mycon.commit()

mycur.execute("""insert into Admin values(1, "Arsh", "2005-07-08", "jain.aj.arsh@gmail.com", "Bangalore", "Male", "Arsh123", "dpsbn")""")
mycon.commit()

mycur.execute("""insert into Admin values(2, "Ritam", "2005-05-18", "ritamdutta2005@gmail.com", "Bangalore", "Male", "Ritam123", "dpsbn")""")
mycon.commit()

mycur.execute("""insert into Admin values(3, "Zuhaib", "2005-11-01", "waneezuhaib@gmail.com", "Bangalore", "Male", "Zuhaib123", "dpsbn")""")
mycon.commit()
              
mycon.close()
