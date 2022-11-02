from unittest import result
import mysql.connector

mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'studentdb')
mycursor = mydb.cursor()

while True:
    print("select an option from menu")
    print("1 add student")
    print("2 view all student")
    print("3 search a student")
    print("4 update the student")
    print("5 delete a student")
    print("6 exit")

    choice = int(input("Enter an option: "))
    if(choice==1):
        print("student enter selected")
        name = input("enter the name")
        rollnumber = input("enter the rollno")
        admno = input("enter the admno")
        college = input("enter the college name")
        sql = 'INSERT INTO `students`(`name`, `rollnumber`, `admno`, `college`) VALUES (%s,%s,%s,%s)'
        data = (name,rollnumber,admno,college)
        mycursor.execute(sql , data)
        mydb.commit()

    elif(choice==2):
        print("view student selected")

        sql = 'SELECT * FROM `students`'
        mycursor.execute(sql)
        result =  mycursor.fetchall()
        for i in result:
            print(i)

    elif(choice==3):
        print("search student selected")

        adm = input("enter the admission number: ")
        sql = 'SELECT `id`, `name`, `rollnumber`, `admno`, `college` FROM `students` WHERE admno = '+adm
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)

    elif(choice==4):
        print("update student selected")
        
        admno = input("enter the admno")
        name = input("enter the name to be updated")
        rollnumber = input("enter the rollno to be updated")
        college = input("enter the college name to be updted")
        sql = "UPDATE `students` SET `name`='"+name+"',`rollnumber`='"+rollnumber+"',`college`='"+college+"' WHERE `admno` ="+admno
        mycursor.execute(sql)
        mydb.commit()
        print("updated succusfully")
        

    elif(choice==5):
        print("delete student selected")
        adm = input("enter the admission number: ")
        sql = 'DELETE FROM `students` WHERE admno = '+adm
        mycursor.execute(sql)
        mydb.commit()
        print("data deleted successfully")



    elif(choice==6):
        break