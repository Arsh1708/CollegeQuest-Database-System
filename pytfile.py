import sys
import mysql.connector as ms
import webbrowser as wb
import time

#----------------------------------------------------------
def NITK():
     f1=open("NITK.txt","r")
     data=f1.read()#string


     x=data.partition("COURSES OFFERED:")#breaks data into: heading, courses offered heading, rest
     z=x[2]#takes the rest data
     y=z.partition("AWARDS AND RECOGNITIONS:")#breaks into courses offered data, awards heading,rest
     courses=y[0]

     a=y[2].partition("RATINGS:")
     awards=a[0]


     b=a[2].partition("PEOPLES REVIEW:")
     ratings=b[0]

     c=b[2].partition("LOCATION:")
     review=c[0]


     d=c[2].partition("EXTRA CURRICULAR ACTIVITIES:")
     location=d[0]
     activities=d[2]
     while True:
          x=int(input("""What would you like to find out:
.Courses offered: Type 1
.Awards and recognitions:Type 2
.Ratings: Type 3
.People's Review:Type 4
.Location: Type 5
.Extra-Curricular Activities: Type 6
.Exit:Type 7
"""))
          if x==1:
               print(courses)
          elif x==2:
               print(awards)
          elif x==3:
               print(ratings)
          elif x==4:
               print(review)
          elif x==5:
               print(location)
          elif x==6:
               print(activities)
          else:
               print("""Hope this was helpful!
                     Thank you for searching!
                     """)
               break
def IEM_KOLKATA():
     f1=open("IEM_KOLKATA.txt","r")
     data=f1.read()#string


     x=data.partition("COURSES OFFERED:")#breaks data into: heading, courses offered heading, rest
     z=x[2]#takes the rest data
     y=z.partition("AWARDS AND RECOGNITIONS:")#breaks into courses offered data, awards heading,rest
     courses=y[0]

     a=y[2].partition("RATINGS:")
     awards=a[0]


     b=a[2].partition("PEOPLES REVIEW:")
     ratings=b[0]

     c=b[2].partition("LOCATION:")
     review=c[0]


     d=c[2].partition("EXTRA CURRICULAR ACTIVITIES:")
     location=d[0]
     activities=d[2]
     while True:
          x=int(input("""What would you like to find out:
.Courses offered: Type 1
.Awards and recognitions:Type 2
.Ratings: Type 3
.People's Review:Type 4
.Location: Type 5
.Extra-Curricular Activities: Type 6
.Exit:Type 7
"""))
          if x==1:
               print(courses)
          elif x==2:
               print(awards)
          elif x==3:
               print(ratings)
          elif x==4:
               print(review)
          elif x==5:
               print(location)
          elif x==6:
               print(activities)
          else:
               print("""Hope this was helpful!
                     Thank you for searching!
                     """)
               break
     
 

def IIITB():
     f1=open("IIITB.txt","r")
     data=f1.read()#string


     x=data.partition("COURSES OFFERED:")#breaks data into: heading, courses offered heading, rest
     z=x[2]#takes the rest data
     y=z.partition("AWARDS AND RECOGNITIONS:")#breaks into courses offered data, awards heading,rest
     courses=y[0]

     a=y[2].partition("RATINGS:")
     awards=a[0]


     b=a[2].partition("PEOPLES REVIEW:")
     ratings=b[0]

     c=b[2].partition("LOCATION:")
     review=c[0]


     d=c[2].partition("EXTRA CURRICULAR ACTIVITIES:")
     location=d[0]
     activities=d[2]
     while True:
          x=int(input("""What would you like to find out:
.Courses offered: Type 1
.Awards and recognitions:Type 2
.Ratings: Type 3
.People's Review:Type 4
.Location: Type 5
.Extra-Curricular Activities: Type 6
.Exit:Type 7
"""))
          if x==1:
               print(courses)
          elif x==2:
               print(awards)
          elif x==3:
               print(ratings)
          elif x==4:
               print(review)
          elif x==5:
               print(location)
          elif x==6:
               print(activities)
          else:
               print("""Hope this was helpful!
                     Thank you for searching!
                     """)
               break
def CIT():
     f1=open("CIT.txt","r")
     data=f1.read()#string


     x=data.partition("COURSES OFFERED:")#breaks data into: heading, courses offered heading, rest
     z=x[2]#takes the rest data
     y=z.partition("AWARDS AND RECOGNITIONS:")#breaks into courses offered data, awards heading,rest
     courses=y[0]

     a=y[2].partition("RATINGS:")
     awards=a[0]


     b=a[2].partition("PEOPLES REVIEW:")
     ratings=b[0]

     c=b[2].partition("LOCATION:")
     review=c[0]


     d=c[2].partition("EXTRA CURRICULAR ACTIVITIES:")
     location=d[0]
     activities=d[2]
     while True:
          x=int(input("""What would you like to find out:
.Courses offered: Type 1
.Awards and recognitions:Type 2
.Ratings: Type 3
.People's Review:Type 4
.Location: Type 5
.Extra-Curricular Activities: Type 6
.Exit:Type 7
"""))
          if x==1:
               print(courses)
          elif x==2:
               print(awards)
          elif x==3:
               print(ratings)
          elif x==4:
               print(review)
          elif x==5:
               print(location)
          elif x==6:
               print(activities)
          else:
               print("""Hope this was helpful!
                     Thank you for searching!
                     """)
               break
      
      

def VIT():
     f1=open("VIT.txt","r")
     data=f1.read()#string


     x=data.partition("COURSES OFFERED:")#breaks data into: heading, courses offered heading, rest
     z=x[2]#takes the rest data
     y=z.partition("AWARDS AND RECOGNITIONS:")#breaks into courses offered data, awards heading,rest
     courses=y[0]

     a=y[2].partition("RATINGS:")
     awards=a[0]


     b=a[2].partition("PEOPLES REVIEW:")
     ratings=b[0]

     c=b[2].partition("LOCATION:")
     review=c[0]


     d=c[2].partition("EXTRA CURRICULAR ACTIVITIES:")
     location=d[0]
     activities=d[2]
     while True:
          x=int(input("""What would you like to find out:
.Courses offered: Type 1
.Awards and recognitions:Type 2
.Ratings: Type 3
.People's Review:Type 4
.Location: Type 5
.Extra-Curricular Activities: Type 6
.Exit:Type 7
"""))
          if x==1:
               print(courses)
          elif x==2:
               print(awards)
          elif x==3:
               print(ratings)
          elif x==4:
               print(review)
          elif x==5:
               print(location)
          elif x==6:
               print(activities)
          else:
               print("""Hope this was helpful!
                     Thank you for searching!
                     """)
               break

def Ramaiah():
     f1=open("Ramaiah.txt","r")
     data=f1.read()#string


     x=data.partition("COURSES OFFERED:")#breaks data into: heading, courses offered heading, rest
     z=x[2]#takes the rest data
     y=z.partition("AWARDS AND RECOGNITIONS:")#breaks into courses offered data, awards heading,rest
     courses=y[0]

     a=y[2].partition("RATINGS:")
     awards=a[0]


     b=a[2].partition("PEOPLES REVIEW:")
     ratings=b[0]

     c=b[2].partition("LOCATION:")
     review=c[0]


     d=c[2].partition("EXTRA CURRICULAR ACTIVITIES:")
     location=d[0]
     activities=d[2]
     while True:
          x=int(input("""What would you like to find out:
.Courses offered: Type 1
.Awards and recognitions:Type 2
.Ratings: Type 3
.People's Review:Type 4
.Location: Type 5
.Extra-Curricular Activities: Type 6
.Exit:Type 7
"""))
          if x==1:
               print(courses)
          elif x==2:
               print(awards)
          elif x==3:
               print(ratings)
          elif x==4:
               print(review)
          elif x==5:
               print(location)
          elif x==6:
               print(activities)
          else:
               print("""Hope this was helpful!
                     Thank you for searching!
                     """)
               break
def NETAJI_SUBHAS_INSTITUTE_OF_TECHNOLOGY():
     f1=open("NETAJI_SUBHAS_INSTITUTE_OF_TECHNOLOGY.txt","r")
     data=f1.read()#string


     x=data.partition("COURSES OFFERED:")#breaks data into: heading, courses offered heading, rest
     z=x[2]#takes the rest data
     y=z.partition("AWARDS AND RECOGNITIONS:")#breaks into courses offered data, awards heading,rest
     courses=y[0]

     a=y[2].partition("RATINGS:")
     awards=a[0]


     b=a[2].partition("PEOPLES REVIEW:")
     ratings=b[0]

     c=b[2].partition("LOCATION:")
     review=c[0]


     d=c[2].partition("EXTRA CURRICULAR ACTIVITIES:")
     location=d[0]
     activities=d[2]
     while True:
          x=int(input("""What would you like to find out:
.Courses offered: Type 1
.Awards and recognitions:Type 2
.Ratings: Type 3
.People's Review:Type 4
.Location: Type 5
.Extra-Curricular Activities: Type 6
.Exit:Type 7
"""))
          if x==1:
               print(courses)
          elif x==2:
               print(awards)
          elif x==3:
               print(ratings)
          elif x==4:
               print(review)
          elif x==5:
               print(location)
          elif x==6:
               print(activities)
          else:
               print("""Hope this was helpful!
                     Thank you for searching!
                     """)
               break

def REVA():
     f1=open("REVA.txt","r")
     data=f1.read()#string


     x=data.partition("COURSES OFFERED:")#breaks data into: heading, courses offered heading, rest
     z=x[2]#takes the rest data
     y=z.partition("AWARDS AND RECOGNITIONS:")#breaks into courses offered data, awards heading,rest
     courses=y[0]

     a=y[2].partition("RATINGS:")
     awards=a[0]


     b=a[2].partition("PEOPLES REVIEW:")
     ratings=b[0]

     c=b[2].partition("LOCATION:")
     review=c[0]


     d=c[2].partition("EXTRA CURRICULAR ACTIVITIES:")
     location=d[0]
     activities=d[2]
     while True:
          x=int(input("""What would you like to find out:
.Courses offered: Type 1
.Awards and recognitions:Type 2
.Ratings: Type 3
.People's Review:Type 4
.Location: Type 5
.Extra-Curricular Activities: Type 6
.Exit:Type 7"""))
          if x==1:
               print(courses)
          elif x==2:
               print(awards)
          elif x==3:
               print(ratings)
          elif x==4:
               print(review)
          elif x==5:
               print(location)
          elif x==6:
               print(activities)
          else:
               print("""Hope this was helpful!
                     Thank you for searching!
                     """)
               break
def NIT_TIRCHEE():
     f1=open("NIT_TIRCHEE.txt","r")
     data=f1.read()#string


     x=data.partition("COURSES OFFERED:")#breaks data into: heading, courses offered heading, rest
     z=x[2]#takes the rest data
     y=z.partition("AWARDS AND RECOGNITIONS:")#breaks into courses offered data, awards heading,rest
     courses=y[0]

     a=y[2].partition("RATINGS:")
     awards=a[0]


     b=a[2].partition("PEOPLES REVIEW:")
     ratings=b[0]

     c=b[2].partition("LOCATION:")
     review=c[0]


     d=c[2].partition("EXTRA CURRICULAR ACTIVITIES:")
     location=d[0]
     activities=d[2]
     while True:
          x=int(input("""What would you like to find out:
.Courses offered: Type 1
.Awards and recognitions:Type 2
.Ratings: Type 3
.People's Review:Type 4
.Location: Type 5
.Extra-Curricular Activities: Type 6
.Exit:Type 7"""))
          if x==1:
               print(courses)
          elif x==2:
               print(awards)
          elif x==3:
               print(ratings)
          elif x==4:
               print(review)
          elif x==5:
               print(location)
          elif x==6:
               print(activities)
          else:
               print("""Hope this was helpful!
                     Thank you for searching!
                     """)
               break
def NIT_WARANGAL():
     f1=open("NIT_WARANGAL.txt","r")
     data=f1.read()#string


     x=data.partition("COURSES OFFERED:")#breaks data into: heading, courses offered heading, rest
     z=x[2]#takes the rest data
     y=z.partition("AWARDS AND RECOGNITIONS:")#breaks into courses offered data, awards heading,rest
     courses=y[0]

     a=y[2].partition("RATINGS:")
     awards=a[0]


     b=a[2].partition("PEOPLES REVIEW:")
     ratings=b[0]

     c=b[2].partition("LOCATION:")
     review=c[0]


     d=c[2].partition("EXTRA CURRICULAR ACTIVITIES:")
     location=d[0]
     activities=d[2]
     while True:
          x=int(input("""What would you like to find out:
.Courses offered: Type 1
.Awards and recognitions:Type 2
.Ratings: Type 3
.People's Review:Type 4
.Location: Type 5
.Extra-Curricular Activities: Type 6
.Exit:Type 7"""))
          if x==1:
               print(courses)
          elif x==2:
               print(awards)
          elif x==3:
               print(ratings)
          elif x==4:
               print(review)
          elif x==5:
               print(location)
          elif x==6:
               print(activities)
          else:
               print("""Hope this was helpful!
                     Thank you for searching!
                     """)
               break
def IIITD():
     f1=open("IIITD.txt","r")
     data=f1.read()#string


     x=data.partition("COURSES OFFERED:")#breaks data into: heading, courses offered heading, rest
     z=x[2]#takes the rest data
     y=z.partition("AWARDS AND RECOGNITIONS:")#breaks into courses offered data, awards heading,rest
     courses=y[0]

     a=y[2].partition("RATINGS:")
     awards=a[0]


     b=a[2].partition("PEOPLES REVIEW:")
     ratings=b[0]

     c=b[2].partition("LOCATION:")
     review=c[0]


     d=c[2].partition("EXTRA CURRICULAR ACTIVITIES:")
     location=d[0]
     activities=d[2]
     while True:
          x=int(input("""What would you like to find out:
.Courses offered: Type 1
.Awards and recognitions:Type 2
.Ratings: Type 3
.People's Review:Type 4
.Location: Type 5
.Extra-Curricular Activities: Type 6
.Exit:Type 7"""))
          if x==1:
               print(courses)
          elif x==2:
               print(awards)
          elif x==3:
               print(ratings)
          elif x==4:
               print(review)
          elif x==5:
               print(location)
          elif x==6:
               print(activities)
          else:
               print("""Hope this was helpful!
                     Thank you for searching!
                     """)
               break
def NIT_KURUKSHETRA():
     f1=open("NIT_KURUKSHETRA.txt","r")
     data=f1.read()#string


     x=data.partition("COURSES OFFERED:")#breaks data into: heading, courses offered heading, rest
     z=x[2]#takes the rest data
     y=z.partition("AWARDS AND RECOGNITIONS:")#breaks into courses offered data, awards heading,rest
     courses=y[0]

     a=y[2].partition("RATINGS:")
     awards=a[0]


     b=a[2].partition("PEOPLES REVIEW:")
     ratings=b[0]

     c=b[2].partition("LOCATION:")
     review=c[0]


     d=c[2].partition("EXTRA CURRICULAR ACTIVITIES:")
     location=d[0]
     activities=d[2]
     while True:
          x=int(input("""What would you like to find out:
.Courses offered: Type 1
.Awards and recognitions:Type 2
.Ratings: Type 3
.People's Review:Type 4
.Location: Type 5
.Extra-Curricular Activities: Type 6
.Exit:Type 7"""))
          if x==1:
               print(courses)
          elif x==2:
               print(awards)
          elif x==3:
               print(ratings)
          elif x==4:
               print(review)
          elif x==5:
               print(location)
          elif x==6:
               print(activities)
          else:
               print("""Hope this was helpful!
                     Thank you for searching!
                     """)
               break

     
 

     
#--------------------------------------------------------------------------------
#user
def user():
     global b
     g="TRY"
     while g=="TRY":
          b=int(input("""Sign in:Type1
     Register:Type2
     """))
          if b==1:
               
               
               x=input("Enter username")
               y=input("Enter password")
           
               mycon= ms.connect(host="localhost", user="root", password="dpsbn")

               """if mycon.is_connected()==False:
                    sys.stderr.write("Connection failed!")
               else:
                    print("Connection Successful!")"""
               mycur=mycon.cursor()
               mycur.execute("use details")
               
               mycur.execute("select password,username from user_details;")
               data1=mycur.fetchall()
               for q in data1:
                    h,i=q
                    
              
               
                    if x==str(i) and y==str(h):
                         mycur.execute("select Name from user_details where username='{}' and password='{}';".format(x,y))
                         data2=mycur.fetchone()
                         print("Welcome",data2[0])
                         flag3=1
                         break
                         
                    else:
                         flag3=0
          
                         
               if flag3==1:
                    
                    break
               else:
                    g="TRY"
                    
               
          
               
                    
               
               
          if b==2:
               global sl_no,name,dob,email,place_of_residence,gender,username,password
               mycon= ms.connect(host="localhost", user="root", password="dpsbn")
               mycur=mycon.cursor()
               mycur.execute("use details")
               mycur.execute("select count(*) from user_details;")
               data6=mycur.fetchone()
               sl_no=data6[0]+1
               email=input("Enter email address:")
               while email.endswith("@gmail.com")!=True:
                    print("Wrong email!")
                    email=input("Enter email address:")
                    
               
               name=input("Enter name:")
               dob=input("Enter date of birth in form yyyy-mm-dd:")
               
               while dob[4]!="-" or dob[7]!="-" or (1<=int(dob[5]+dob[6])<=12)==False or (1<=int(dob[8]+dob[9])<=31)==False:
                    print("Invalid date entered!")
                    dob=input("Enter date of birth in form yyyy-mm-dd:")
                    
              
               place_of_residence=input("Enter place of residence:")
               gender=input("""Enter Male or Female or Rather not say:""")
               while gender not in ["Male","Female","Rather not say"]:
                    print("Invalid entry!")
                    gender=input("""Enter Male or Female:""")
                    
               username=input("Enter username:")
               
               print("""Password should have at least 1 number and 1 symbol
                     minimum 8 characters""")
               
               
              
               while True:
                    flag4=0
                    flag5=0
                    flag6=0
                    password=input("Enter your password:")
                    d=list(password)
                    if len(password)>=8:
                         flag6=1
                    for i in d:
                         if i in ["1","2","3","4","5","6","7","8","9","0"]:
                              flag4=1
                         elif i in ["!","@","#","$","%","^","&","*","?"]:
                              flag5=1
                         
                    
                    if flag4==0 or flag5==0 or flag6==0:
                         print("Invalid password!")
                         continue
                    else:
                         print("Password accepted")
                         break
               break
                    
#------------------------------------------------------------
#admin
def admin():
     while True:
          x=input("Enter username")
          y=input("Enter password")
          mycon= ms.connect(host="localhost", user="root", password="dpsbn")
          mycur=mycon.cursor()
          mycur.execute("use details")
          mycur.execute("select username, password from Admin;")
          data=mycur.fetchall()
          for i in data:
               h,j=i
               if h==x and j==y:
                    print("Welcome sir!")
                    break
               else:
                    continue
          break
          
#-------------------------------------------------------------               
#display in screen
          
print("Welcome to CAREER CAMPS!")
#User or Admin
a=int(input("""User:Type 1
Admin:Type 2:
"""))
if a not in [1,2]:
     while a!=1 or a!=2:
          sys.stderr.write("Error no such mode\n")
          a=int(input("""User:Type 1
Admin:Type 2:
"""))
          if a==1:
                user()
                break
          elif a==2:
               admin()
elif a==1:
     user()
     if b==2:
          mycon= ms.connect(host="localhost", user="root", password="dpsbn")
          mycur=mycon.cursor()
          mycur.execute("use details;")

          mycur.execute("insert into user_details values('{}','{}','{}','{}','{}','{}','{}','{}')".format(sl_no,name,dob,email,place_of_residence,gender,username,password))
          mycon.commit()
     
elif a==2:
     admin()
#-------------------------------------------------------------------------------------------------------
#College search etc
if a==1:
     while True:
          x=input("""What would you like to do:
     Make a personalized account[used to keep a track on all exams you have registered to ]:Enter a
     Browse colleges:Enter b
     Predict college based on exams given:Enter c
     Browse exams:Enter d
     View personalized account:Enter e
     Edit personalized account:Enter g
     Exit:Enter f
     """)
          if x=="a":
               a=input("Enter name!")

               aa=a.replace(" ","_")
               
                    
               x=int(input("Enter number of records you want to enter: "))
               for i in range(x):
                    b=input("Enter name of exam: ")
                    c=input("Enter the website link: ")
                    d=input("Enter the date of the exam: ")
                    e=input("Enter password(used in that website):")
                    while True:
                         f=input("Enter if applied or not for that college:(YES OR NO) ")
                         if f in ["YES","NO","No","Yes","yes","no"]:
                              break
                    g=input("Enter other details (like extra subjects in that exam etc): ")
                    mycon= ms.connect(host="localhost", user="root", password="dpsbn")
                    mycur=mycon.cursor()
                    mycur.execute("use details")
                    mycur.execute("create table if not exists {}(Exam varchar(200),Website varchar(200),Date_of_Exam date,Password varchar(200),Applied varchar(200),Other_details varchar(200))".format(aa,))
                    mycon.commit()
                    mycur.execute("insert into {} values('{}','{}','{}','{}','{}','{}')".format(aa,b,c,d,e,f,g))
                    mycon.commit()
                    mycon.close()
                    print("Thank you!")
                         
               #now find that using the exams they chose, find colleges available using that
          #-------------------------------------------------------------------------------------
          if x=="b":
               while True:
                    p=int(input("""What would you like to search:
          .Colleges: Enter 1
          .College website: Enter 2
          .Exit: Enter 3
          """))
                    if p==1:
                         while True:
                              q=input("""Which college would you like to explore(Type college name as given):
               .NITK
               .IIITB(Bangalore)
               .VIT(Vellore)
               .Ramaiah Institute of technology(Type only Ramaiah)
               .REVA
               .NIT WARANGAL
               .NIT KURUKSHETRA
               .IIITD (Delhi)
               .NIT TIRCHEE
               .COORG INSTITUTE OF TECHNOLOGY(CIT)
               .NETAJI SUBHAS UNIVERSITY OF TECHNOLOGY
               .IEM KOLKATA
               .EXIT
               """)
                              if q=="NITK":
                                   NITK()
                              if q=="IIITB":
                                   IIITB()
                              if q=="VIT":
                                   VIT()
                              if q=="Ramaiah":
                                   Ramaiah()
                              if q=="REVA":
                                   REVA()
                              if q=="NIT TIRCHEE":
                                   NIT_TIRCHEE()
                              if q=="IIITD":
                                   IIITD()
                              if q=="NIT WARANGAL":
                                   NIT_WARANGAL()
                              if q=="NIT KURUKSHETRA":
                                   NIT_KURUKSHETRA()
                              if q=="CIT":
                                   CIT()
                              if q=="NETAJI SUBHAS UNIVERSITY OF TECHNOLOGY":
                                   NETAJI_SUBHAS_UNIVERSITY_OF_TECHNOLOGY()
                              if q=="IEM KOLKATA":
                                   IEM_KOLKATA()
                              
                              if q=="EXIT":
                                   break
                    if p==2:
                         while True:
                              r=input("""Which college website do you want to go to:(Type the name)
          .NITK
          .IIITB(Bangalore)
          .VIT
          .Ramaiah
          .REVA
          .NIT WARANGAL
          .NIT KURUKSHETRA
          .IIITD (Delhi)
          .NIT TIRCHEE
          .COORG INSTITUTE OF TECHNOLOGY(CIT)
          .NETAJI SUBHAS UNIVERSITY OF TECHNOLOGY
          .IEM KOLKATA
          .EXIT
          """)
                              if r=="NITK":
                                   
                                   url="https://www.nitk.ac.in/"
                                   wb.open(url)
                              if r=="Ramaiah":
                                   url="https://www.msrit.edu/"
                                   wb.open(url)
                              if r=="VIT":
                                   url="https://vit.ac.in/"
                                   wb.open(url)
                              if r=="IIITB":
                                   url="https://www.iiitb.ac.in/"
                                   wb.open(url)
                              if r=="REVA":
                                   url="https://www.reva.edu.in/"
                                   wb.open(url)
                              if r=="IEM KOLKATA":
                                   url="https://iem.edu.in/"
                                   wb.open(url)
                              if r=="NETAJI SUBHAS UNIVERSITY OF TECHNOLOGY":
                                   url="http://www.nsut.ac.in/en/home"
                                   wb.open(url)
                              if r=="CIT":
                                   url="https://www.citcoorg.edu.in/"
                                   wb.open(url)
                              if r=="NIT TIRCHEE":
                                   url="https://www.nitt.edu/"
                                   wb.open(url)
                              if r=="IIITD ":
                                   url="https://www.iiitd.ac.in/"
                                   wb.open(url)
                              if r=="NIT KURUKSHETRA":
                                   url="https://nitkkr.ac.in/"
                                   wb.open(url)
                              if r=="NIT WARANGAL":
                                   url="https://www.nitw.ac.in/"
                                   wb.open(url)
                              
                              if r=="EXIT":
                                   print("""Hope it was useful!
                                         Thank you for using Career Camps""")
                                   break
                              



                         
                    if p==3:
                         print("Hope Career Camps was helpful and you had a delightful experience!")

                         break
          if x=="c":
               print("You can see your predicted colleges based on your marks:")
               time.sleep(2)
               url="https://www.shiksha.com/college-predictor"
               wb.open(url)
          if x=="d":
               while True:
                    x=int(input("""Select the exam(Enter number):
1)JEE
2)NEET
3)KCET
4)COMEDK UGET
5)VITEE
6)SITEEE
7)SRMJEEE
8)BITSAT
9)MET
10)AP EAMCET
11)KIITEE
12)MHTCET
13)WBJEE
14)EXIT
"""))
                    if x==1:
                         print("""Colleges:
NIT TRICHEE
NIT SURATHKAL
NIT WARANGAL
NIT KURUKSHETRA
NIT RAIPUR
IIIT BANGALORE
IIIT HYDERABAD
IIIT PUNE
IIIT MANIPUR
IIIT SURAT
SRM Institute of Science and Technology, Chennai
Delhi Technological University
IEM Kolkata
REVA University
Dr. Ambedkar Institute of Technology, Bangalore""")
                         z=input("Would you like to visit the site[YES or NO]")
                         if z=="YES":
                              url="https://jeemain.nta.nic.in/"
                              wb.open(url)
                         else:
                              continue
                    if x==4:
                         print("""Colleges:
Dayananda Sagar College of Engineering
RV College of Engineering
Ramaiah Institute of Technology
BMS College of Engineering
REVA University
Dr. Ambedkar Institute of Technology, Bangalore
Bangalore Institute of Technology
Nitte Meenakshi Institute of Technology
CMR University
Christ University""")
                         z=input("Would you like to visit the site[YES or NO]")
                         if z=="YES":
                              url="https://www.comedk.org/index.html"
                              wb.open(url)
                         else:
                              continue

                    if x==3:
                         print("""Colleges:
Dayananda Sagar College of Engineering
RV College of Engineering
Ramaiah Institute of Technology
BMS College of Engineering
REVA University
Dr. Ambedkar Institute of Technology, Bangalore
Bangalore Institute of Technology
Nitte Meenakshi Institute of Technology
CMR University
PES University""")
                         z=input("Would you like to visit the site[YES or NO]")
                         if z=="YES":
                              url="https://cetonline.karnataka.gov.in/kea/"
                              wb.open(url)
                         else:
                              continue

                    if x==7:
                         print("""Colleges:
SRM Institute of Science and Technology, Chennai (jee also)
SRM Institute of Science and Technology, Ramapuram Campus
SRM University AP, Amaravati
SRM University, Delhi-NCR, Sonepat (jee also)
SRM Institute of Science and Technology, NCR Campus, Ghaziabad
SRM University, Sikkim
""")
                         z=input("Would you like to visit the site[YES or NO]")
                         if z=="YES":
                              url="https://www.srmist.edu.in/"
                              wb.open(url)
                         else:
                              continue

                    if x==5:
                         print("""Colleges:
VIT, Vellore
VIT, Chennai campus (jee also)
VIT University, Bhopal
VIT-AP University, Amaravati (jee also)
""")
                         z=input("Would you like to visit the site[YES or NO]")
                         if z=="YES":
                              url="https://vit.ac.in/"
                              wb.open(url)
                         else:
                              continue
                    if x==8:
                         print("""Colleges:
BITS Pilani – Hyderabad campus, Hyderabad
Birla Institute of Technology and Science, Pilani
BITS Pilani, Goa Campus
Swami Rama Himalayan University, Dehradun (jee also)
""")
                         z=input("Would you like to visit the site[YES or NO]")
                         if z=="YES":
                              url="https://www.bitsadmission.com/"
                              wb.open(url)
                         else:
                              continue
                    if x==10:
                         print("""Collegese:
Andhra University College of Engineering, Visakhapatnam
Gayatri Vidya Parishad College of Engineering, Visakhapatnam
RVR and JC College of Engineering, Guntur
Sri Venkateswara University College of Engineering, Tirupati
Koneru Lakshmaiah Education Foundation, Guntur (jee also)
Aditya Engineering College, Surampalem
Sree Vidyanikethan Engineering College, Tirupati
Jawaharlal Nehru Technological University College of Engineering, Kakinada
Velagapudi Ramakrishna Siddhartha Engineering College, Vijayawada
GMR Institute of Technology, Rajam
""")
                         z=input("Would you like to visit the site[YES or NO]")
                         if z=="YES":
                              url="https://cets.apsche.ap.gov.in/APSCHEHome.aspx"
                              wb.open(url)
                         else:
                              continue
                    if x==13:
                         print("""Colleges:
Jadavpur University, Kolkata
Heritage Institute of Technology, Kolkata (jee also)
Techno India University, Kolkata (jee also)
Haldia Institute of Technology, Haldia (jee also)
Techno Main, Salt lake (jee also)
Kalyani Government Engineering College, Nadia
Dr. BC Roy Engineering College, Durgapur (jee also)
Institute of Engineering and Management, Kolkata (jee also)
Aliah University, Kolkata
Adamas University
""")
                         z=input("Would you like to visit the site[YES or NO]")
                         if z=="YES":
                              url="https://wbjeeb.nic.in/WBJEEBBoardCMS/Page/Page?PageId=1&LangId=P"
                              wb.open(url)
                         else:
                              continue

                    if x==12:
                         print("""Colleges:
College of Engineering, Pune
Veermata Jijabai Technological Institute, Mumbai (jee also)
Bharati Vidyapeeth Deemed University College of Engineering, Pune (jee also)
Vishwakarma Institute of Technology, Pune (jee also)
Institute of Chemical Technology, Mumbai (jee also)
Symbiosis Institute of Technology, Pune (jee also)
KJ Somaiya College of Engineering, Mumbai (jee also)
Dr. DY Patil Institute of Technology, Pune (jee also)
AISSMS College of Engineering, Pune (jee also)
MIT WPU Faculty of Engineering, Pune (jee also)
""")
                         z=input("Would you like to visit the site[YES or NO]")
                         if z=="YES":
                              url="https://cetcell.mahacet.org/"
                              wb.open(url)
                         else:
                              continue

                    if x==9:
                         print("""Colleges:
Manipal Institute of Technology, Manipal
Mainpal University, Jaipur (jee also)
Manipal Academy of Higher education, Manipal
Sikkim Manipal Institute of Technology, Majitar, East Sikkim (jee also)
""")
                         z=input("Would you like to visit the site[YES or NO]")
                         if z=="YES":
                              url="https://manipal.edu/mu/admission/indian-students/online-entrance-exam-overview.html"
                              wb.open(url)
                         else:
                              continue

                    if x==11:
                         print("""Colleges:
Kalinga Institute of Industrial Technology, Bhubaneswar
""")
                         z=input("Would you like to visit the site[YES or NO]")
                         if z=="YES":
                              url="https://kiitee.kiit.ac.in/"
                              wb.open(url)
                         else:
                              continue

                    if x==14:
                         print("Thank you for using career camps!")
                         break

          if x=="f":
               print("Thank you for chosing Career Camps!")
               break
          if x=="e":
               a=input("Enter name with which you had made the account: ")
               aa=a.replace(" ","_")
               print("Here is your data!")
               mycon= ms.connect(host="localhost", user="root", password="dpsbn")
               mycur=mycon.cursor()
               mycur.execute("use details")
               mycur.execute("select * from {}".format(a,))
               data=mycur.fetchall()
               for i in data:
                    print(data)
          if x=="g":
               a=input("Enter name with which you had made the account: ")
               aa=a.replace(" ","_")
               x=int(input("Enter how many collegese do you want to enter: "))
               for i in range(x):
                    b=input("Enter name of exam: ")
                    c=input("Enter the website link: ")
                    d=input("Enter the date of the exam: ")
                    e=input("Enter password(used in that website):")
                    while True:
                         f=input("Enter if applied or not for that college:(YES OR NO) ")
                         if f in ["YES","NO","No","Yes","yes","no"]:
                              break
                    g=input("Enter other details (like extra subjects in that exam etc): ")
                    mycon= ms.connect(host="localhost", user="root", password="dpsbn")
                    mycur=mycon.cursor()
                    mycur.execute("use details")
                    mycur.execute("create table if not exists {}(Exam varchar(200),Website varchar(200),Date_of_Exam date,Password varchar(200),Applied varchar(200),Other_details varchar(200))".format(aa,))
                    mycon.commit()
                    mycur.execute("insert into {} values('{}','{}','{}','{}','{}','{}')".format(aa,b,c,d,e,f,g))
                    mycon.commit()
                    mycon.close()
                    print("Thank you!")
               

#--------------------------------------------------------------------------------------------
#admin controls
if a==2:
    while True:
        x=int(input("""What would you like to update:
        1)Update name,dob,email,place_of_residence,gender,username,password of user
        2)Delete a record of a user
        """))
        if x==1:
            mycon=ms.connect(host="localhost",passwd="dpsbn",user="root",database="details",auth_plugin='mysql_native_password')
            mycur=mycon.cursor()
            a=input("Enter which column you want to change:")
            b=input("Enter what do you want to change it as:")
            c=input("Enter username:")
            mycur.execute("update user_details set '{}' as '{}' where username=='{}'".format(a,b,c))
            mycon.commit()
            print("Update has been done!")
        if x==2:
            mycon=ms.connect(host="localhost",passwd="dpsbn",user="root",database="details",auth_plugin='mysql_native_password')
            mycur=mycon.cursor()
            a=input("Enter username of person whose account has to be deleted!")
            mycur.execute("delete from user_details where username='{}'".format(a,))
            mycon.commit()
            print("Update has been done!")
        if x==3:
             print("Thank you for using Career Camps!")
             break


                              
                               
                    
                         
                    
                    
              
               
          

          
     
     
          
     


     
               



           

     



           



          
     


          
                        
               
                    
               
          
          
          


