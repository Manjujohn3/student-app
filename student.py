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
    elif(choice==2):
        print("view student")
    elif(choice==3):
        print("search a student")
    elif(choice==4):
        print("update the student")
    elif(choice==5):
        print("delete a student")
    elif(choice):
        break