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
    print("6 insert marks")
    print("7 view all marks")
    print("8 view individual marks")
    print("9 subjectwise marks")
    print("10 exit")

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
        print("insert marks")
        adm = input("enter the admno:") 
        sql = 'SELECT `id` FROM `students` WHERE `admno` = '+adm
        mycursor.execute(sql)
        result = mycursor.fetchall()
        id = 0
        for i in result:
            id = str(i[0])
        print("studentid is: ",id)

        physicsmark = input("enter the marks:")
        chemistrymark = input("enter the marks:") 
        mathsmarkmark = input("enter the marks:")   
        sql = "INSERT INTO `marks`(`studentid`, `physicsmark`, `chemistrymark`, `mathsmark`) VALUES (%s,%s,%s,%s)"
        data = (id,physicsmark,chemistrymark,mathsmarkmark)
        mycursor.execute(sql , data)
        mydb.commit()
        print("marks are inserted")

    elif(choice==7):
        print("view all marks")
        sql= "SELECT s.`name`, s.`rollnumber`, s.`admno`, s.`college`, m.`physicsmark`, m.`chemistrymark`, m.`mathsmark` FROM `students` s join marks m on s.id = m.studentid"
        mycursor.execute(sql)
        result =  mycursor.fetchall()
        for i in result:
            print(i)

    elif(choice==8):
        print("view individual marks")
        adm = input('enter the admnumber : ')
        sql = 'SELECT `id` FROM `students` WHERE `admno`=' +adm
        mycursor.execute(sql)
        result = mycursor.fetchall()
        id = 0
        for i in result:
            id = str(i[0])
        print('id of the student : ', id)
        sql = 'SELECT * FROM `marks` WHERE `id`='+id
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)

    elif(choice==9):
        print('Display subject wise mark')
        adm = input('Enter the admi number ')
        sub = input('enter the subject you need to display (physicsmark,chemistrymark,mathsmarks) : ')
        sql = 'SELECT `id` FROM `students` WHERE `admno`=' +adm
        mycursor.execute(sql)
        result = mycursor.fetchall()
        id = 0
        for i in result:
            id = str(i[0])
        print('Id of the student : ', id)
        if(sub == 'physicsmark'):
            sql = 'SELECT `physicsmark` FROM `marks` WHERE `studentid`='+id
            
        elif(sub == 'chemistry_mark'):
            sql = 'SELECT `chemistrymark` FROM `marks` WHERE `studentid`='+id
           
        else:
            sql = 'SELECT `mathsmark` FROM `marks` WHERE `studentid`='+id
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print('mark of the student is ',result[0])


    elif(choice==10):
        break
    