
def admin_registration_function():  # creating function

    admin_reg_file = open("Admin_Registration.txt", "a") # creating file in append mode to store variables values in it
    name = str(input("Enter Your Name :")) # creating variable to store values
    ID = str(input("enter your ID :"))
    password = str(input("Enter Your Password: "))
    password_con = str(input("Enter Your Password Again: "))

    if len(password) <= 7:  # insuring that the number is more or equal to 8
        print("password must be at least 8 characters!")
    elif password_con != password: # if both inputs passwords do not match
        print("Password does not match! check again")

    else:
        print(
            "\nregistration successful! \tHere is the detail you entered : \nName:\t" + name + "\nID:\t" + ID +
            "\npassword:\t" + password) 

    admin_reg_file.write("\n" + ID + "\t" + name + "\t" + password)  # writing details in the file
    admin_reg_file.close()  # closing the file
    
#admin_registration_function() 

def admin_login():
    file = open('Admin_Registration.txt', 'r')  # reading the file
    print("Enter your detail to log in:")
    ID = str(input("enter your ID:"))
    password = str(input("Enter your password"))
    lines = file.readline()  # reading line from file to check
    for lines in file:
        lines = lines.split()  # splitting the stringes/integers in the file

    if ID != lines[0] or password != lines[2]: # verificating the input data with the first and third elements on the file
        print("ID or password is wrong! check again")
        
    else:
        print("Login Successful")

#admin_login()

def center_location():
    center_location_list = ["KL", "Johor", "Selangor"] #creating a list to store multiple elemnts 
    return center_location_list  # returning the list so it can be used on other functions

def sport_list():
    sport_list = ["Swimming", "Badminton", "Football", "Archery", "Gymnastics", "Volleyball", "Basketball", "Cricket",
                  "Tennis", "Table Tennis"] # creating a list to store mutiple elemnts
    return sport_list  # returning the list so it can be used on other functions


def student_registration_function():
    student_file = open("Student_File.txt", "a")
    student_info = open("Student_Info.txt", "a")
    ID = str(input("Enter ID :"))
    name = str(input("Enter your name :"))
    for location in center_location():  #looping in the center location function to get the sport center list
        location = center_location()
        print(location)
        c_location = str(input("Enter the center location you want to enroll in form the list: "))
        break
    for list in sport_list():  # looping in sport list function to get the sport list 
        list = sport_list()
        print(list)  # printing the list so the user can view it
        Sport = str(input("Enter the sport you want to enroll in from the list:"))
        break # stopping the loop 
    phone = int(input("Enter Your Phone Number: "))
    address = str(input("Enter Your Address: "))
    DOB = input("Enter your Date of Birth DD/MM/YY:")
    password = str(input("enter your password"))
    password_con = str(input("enter your password again"))

    if len(password) <= 7:
        print("password must be at least 8 characters!")
    elif password_con != password:
        print("Password does not match! check again")

    else:
        print("\nregistration successful!")
        student_file.write('\n' + ID + "\t" + password)
        student_file.close()
        student_info.write(
            ID + "\t" + name + "\t" + c_location + "\t" + Sport + "\t" + str(phone) + "\t" + address + "\t" + str(
                DOB) + "\n")


# student_registration_function()


def student_login():
    print("Enter your detail to log in:")
    file = open("Student_File.txt", "r") # reading the text Student File 
    ID = str(input("enter your ID:"))
    password = str(input("Enter your password"))
    lines = file.readline() # reading line in the file
    for lines in file:
        lines = lines.split() # splitting the line to make it  possible to check each integer or string on the line

    if ID != lines[0] or password != lines[1]:  # if not equal to the line 0  (ID) and line [1] (password) which located in the file
        print("ID or password is wrong!")

    else:
        print("Login Succsessful")
        file.close()


# student_login()

def coach_function():
    Coach_file = open("coaches_info.txt", "a")
    coach_ID = input("Enter Coach ID: ")
    coach_name = input("Enter Coach Name: ")
    coach_DJ = input("Enter Coach Date Joined DD/MM/YY: ")
    coach_TD = input("Enter Coach Date Terminated DD/MM/YY: ")
    coach_HR = int(input("Enter Coach Hourly rate: "))
    coach_phone = int(input("Enter Coach Phone Number: "))
    coach_address = input("Enter Coach Address: ")
    sport_CC = input("Enter Sport Center Code: ")
    for location in center_location():
        location = center_location()
        print(location)
        sport_CL = (input("Enter Sport Center location from the list: "))
        break
    sport_code = input("Enter Sport Code: ")
    for sport in sport_list():
        sport = sport_list()
        print(sport)
        sport_name = str(input("Enter Sport form the list: "))
        break
    coach_rating = int(input("Enter Coach Rating: "))
    Coach_file.write("\n"+coach_ID + "\t" + coach_name + "\t" + str(coach_DJ) + "\t" + str(coach_TD) + "\t" + str(coach_HR) +
                     "\t" + str(coach_phone) + "\t" + coach_address + "\t" + str(sport_CC) + "\t" + sport_CL +
                     "\t" + str(sport_code) + "\t" + sport_name + "\t" + str(coach_rating) + "\n")


# coach_function()


def sport_function():
    Sport_file = open("sport_info.txt","a")

    sport_C = str(input("Enter Sport Code: "))
    sport_N = str(input("Enter Sport Name: "))
    print("sport information has  been added successfully!")
    Sport_file.write("\n" + sport_C + "\t" + sport_N)
    Sport_file.close()


# sport_function()


def sport_schedule():
    swimming_file = open("Swimming_schedule.txt", "a")
    badminton_file = open("badminton_schedule.txt", "a")
    football_file = open("football_schedule.txt", "a")
    archery_file = open("archery_schedule.txt", "a")
    gymnastics_file = open("gymnastics_schedule.txt", "a")
    volleyball_file = open("volleyball_schedule.txt", "a")
    basketball_file = open("basketball_schedule.txt", "a")
    cricket_file = open("cricket_schedule.txt", "a")
    tennis_file = open("tennis_schedule.txt", "a")
    table_tennis_file = open("Table_Tennis_schedule.txt", "a")
    for sport in sport_list():
        sport = sport_list()
        print(sport)
        opt = input("Enter sport to add schedule to: ")
        if opt == "Swimming": # verifying with the user input
            day = input("Enter Day")
            time = input("Enter Time")
            swimming_file.write("\n" + day + "\t" + time)
            swimming_file.close()
            print("Schedule Add done")
            break
        elif opt == "Badminton":
            day = input("Enter Day")
            time = input("Enter Time")
            badminton_file.write("\n" + day + "\t" + time)
            badminton_file.close()
            print("Schedule Add done")
            break
        elif opt == "Football":
            day = input("Enter Day")
            time = input("Enter Time")
            football_file.write("\n" + day + "\t" + time)
            football_file.close()
            print("Schedule Add done")
            break
        elif opt == "Archery":
            day = input("Enter Day")
            time = input("Enter Time")
            archery_file.write("\n" + day + "\t" + time)
            archery_file.close()
            print("Schedule Add done")
            break
        elif opt == "gymnastics":
            day = input("Enter Day")
            time = input("Enter Time")
            gymnastics_file.write("\n" + day + "\t" + time)
            gymnastics_file.close()
            print("Schedule Add done")
            break
        elif opt == "Volleyball":
            day = input("Enter Day")
            time = input("Enter Time")
            volleyball_file.write("\n" + day + "\t" + time)
            volleyball_file.close()
            print("Schedule Add done")
            break
        elif opt == "Basketball":
            day = input("Enter Day")
            time = input("Enter Time")
            basketball_file.write("\n" + day + "\t" + time)
            basketball_file.close()
            print("Schedule Add done")
            break
        elif opt == "Cricket":
            day = input("Enter Day")
            time = input("Enter Time")
            cricket_file.write("\n" + day + "\t" + time)
            cricket_file.close()
            print("Schedule Add done")
            break
        elif opt == "Tennis":
            day = input("Enter Day")
            time = input("Enter Time")
            tennis_file.write("\n" + day + "\t" + time)
            tennis_file.close()
            print("Schedule Add done")
            break
        elif opt == "Table Tennis":
            day = input("Enter Day")
            time = input("Enter Time")
            table_tennis_file.write("\n" + day + "\t" + time)
            table_tennis_file.close()
            print("Schedule Add done")
            break

#sport_schedule()


def coach_record_display():
    coach_file = open("coaches_info.txt", "r") #reading the file 
    print(coach_file.read()) # printing the file
    coach_file.close()


# coach_record_display()

def sport_record_display():
    sport_file = open("sport_info.txt", "r")
    print(sport_file.read())
    sport_file.close()


# sport_record_display()

def registered_students_display():
    student_file = open("Student_Info.txt", "r")
    print("ID: \tName: \tLocation: \tSport: \tPhone Number: \tAddress: \tDate of Birth:")
    print(student_file.read())
    student_file.close()

# registered_students_display()



def search_coach_ID():
    ID_file = open("coaches_info.txt", "r") 
    search_ID = input("Enter coach ID to search in file:") # requsting an input to check and search in the file
    for line in ID_file: #using a for-loop to iterate through the lines of a file
        if (line.startswith(search_ID)): #reading only the first data on the lines on file
            print(line)


# search_coach_ID()


def search_coach_rating():
    search_rating = input("Enter Coach rating to search in file:")
    coach_file = open("Coaches_info.txt", "r")
    check = coach_file.readlines() # Reading the lines in the file
    for line in check: #using a for-loop to iterate through the lines of a file
        lines = line.split() # Splitting the lines in the file 
        if search_rating in lines[11]: #Checking if the input word are on the file specifily in the 11th elemets of the line
            print(line)

#search_coach_rating()



def search_sport_id():
    sport_ID_file = open("sport_info.txt", "r")
    search = input("Enter sport ID to search in file: ")
    for line in sport_ID_file: 
        if (line.startswith(search)):
            print(line)


# search_sport_id()

def search_student_id():
    student_file = open("Student_Info.txt", "r")
    search = input("Enter Student ID to search in file:")
    for line in student_file:
        if (line.startswith(search)):
            print(line)


# search_student_id()

def student_feedback():
    feedback = open("feedback_file.txt","a")
    rating = int(input("How was coach the coach performance 1.very poor(1)\t2.poor(2)\t3.Good(3)\t4.Very Good(4)\t5.Excellent(5)"))
    student_feedback = input("Write Coach feedback: ")
    if rating ==1: #making a condtion to check if the given input is equle to first condition or not
        feedback.write("\nvery poor (1)""\tFeedback:""\t"+student_feedback)
        print("Thank you for your feedback")
    elif rating == 2: # if first confition is False this condtion will be checked.if  this condition is True the given command line will be executed, and the rest of conditions will be skipped.
        feedback.write("\npoor (2)""\tFeedback:\t"+student_feedback)
        print("Thank you for your feedback:"+student_feedback)
    elif rating == 3:
        feedback.write("\nrating: Good (3)\tFeedback:\t"+student_feedback)
        print("Thank you for your feedback")
    elif rating == 4:
        feedback.write("\n Very Good (4)""\tFeedback:\t"+student_feedback)
        print("Thank you for your feedback")
    elif rating == 5:
        feedback.write("\n Excellent (5)""\tFeedback:\t"+student_feedback)
        print("Thank you for your feedback")
#student_feedback()



def admin_function():
    
    opt = int(input("1. To login\n2. To register\n3. To exit")) # making multiple choices for user to choose from
    if opt == 1:
        def admin_login(): #calling the admin function and verifying user login and password.
            
            file = open('Admin_Registration.txt', 'r')
            print("Enter your detail to log in:")
            ID = str(input("enter your ID:"))
            password = str(input("Enter your password"))
            lines = file.readline()
            for lines in file:
                lines = lines.split()
            if ID != lines[0] or password != lines[2]:
                print("ID or password is wrong! check again")
                admin_login()

            else:
                print("Login Successful")
                opt = int(input("Enter 1 to add records|enter 2  To display records |enter 3 To search record "))
                if opt == 1:
                    opt = int(input("1.Add records of coach\n2.add record of sport\n3.add record of sport schedule"))
                    if opt == 1:
                        coach_function() # calling coach function 
                    elif opt == 2:
                        sport_function() # calling sport function 
                    elif opt == 3:
                        sport_schedule() # calling sport scedule function
                elif opt == 2:
                    opt = int(input("1.to view record of coaches\n2.to view record of sports\n3.to view record of "
                                    "registered students")) # making another multiple choices for user to choose from
                                   
                    if opt == 1:
                        coach_record_display() #calling the coach record functoin 
                    elif opt == 2:
                        sport_record_display()  #calling the record display  functoin
                    elif opt == 3:
                        registered_students_display() #calling the students record display function
                elif opt == 3:
                
                    opt = int(input("1.to search coach by coach ID\n2.to search coach by rating\n3.to search sport by "
                                    "sport "
                                    "ID\n4.to search student by student ID"))
                    if opt == 1:
                        search_coach_ID()
                    elif opt == 2:
                        search_coach_rating()
                    elif opt == 3:
                        search_sport_id()
                    elif opt == 4:
                        search_student_id()

        admin_login()
    elif opt == 2:
        admin_registration_function()

    elif opt == 3:
        exit(print("Good bye!")) #terminating  the program

    else:
        print("Wrong choice!Choose from the stated choices")
        admin_function()#calling the admin function again


#admin_function()




def student_function():
    opt = int(input(
        "1.To view details of sport and sport schedule\n2.if new student register to access other details\n3.To login"
        "\n4.Exit"))
    if opt == 1:
        opt = int(input("1.view sport details\n2.view sport schedule"))
        if opt == 1:
            sport_record_display()
        
        elif opt == 2:
            print("1.Swimming 2.Badminton 3.Football 4.Archery 5.Gymnastics 6.Volleyball 7.Basketball 8.Cricket 9.Tennis 10.Table Tennis")
            opt = int(input("Choose which sport you want to view schedule of: "))
            if opt == 1:
                swimming_file = open("Swimming_schedule.txt", "r")
                print(swimming_file.read())
            elif opt ==2:
                badminton_file = open("badminton_schedule.txt", "r")
                print()
                print(badminton_file.read())
            elif opt ==3:
                football_file = open("football_schedule.txt", "r")
                print(football_file.read())
            elif opt == 4:
                archery_file = open("archery_schedule.txt", "r")
                print(archery_file.read())
            elif opt == 5:
                gymnastics_file = open("gymnastics_schedule.txt", "r")
                print(gymnastics_file.read())
            elif opt == 6:
                volleyball_file = open("volleyball_schedule.txt", "r")
                print(volleyball_file.read())
            elif opt == 7:
                basketball_file = open("basketball_schedule.txt", "r")
                print(basketball_file.read())
            elif opt == 8:
                cricket_file = open("cricket_schedule.txt", "r")
                print(cricket_file.read())
            elif opt == 9:
                tennis_file = open("tennis_schedule.txt", "r")
                print(tennis_file.read())
            elif opt ==10:
                table_tennis_file = open("Table_Tennis_schedule.txt", "r")
                print(table_tennis_file.read())

    elif opt == 2:
        student_registration_function()

    elif opt == 3:
            def student_login():#calling the student login function and verifying student login and password.
                print("Enter your detail to log in:")
                file = open("Student_File.txt", "r")
                ID = str(input("enter your ID:"))
                password = str(input("Enter your password"))
                lines = file.readline()
                for lines in file:
                    lines = lines.split()

                if ID != lines[0] or password != lines[
                    1]:  # if not equal to the line 0 (ID) and line [1] (password) in the file
                    print("ID or password is wrong!")
                    student_login()

                else:
                    print("Login Succsessful")
                    file.close()
                    opt = int(input("\n1.To view detail of Coach \n2.student record \n3.Sport schedule\n4.provide "
                                    "feedback and star to coach \n5Exit"))
                    if opt == 1:
                        coach_record_display()
                    elif opt ==2 :
                        registered_students_display()
                    elif opt == 3:
                        print(
                            "1.Swimming 2.Badminton 3.Football 4.Archery 5.Gymnastics 6.Volleyball 7.Basketball 8.Cricket 9.Tennis 10.Table Tennis")
                        opt = int(input("Choose your sport schedule to view: "))
                        if opt == 1:
                            swimming_file = open("Swimming_schedule.txt", "r")
                            print(swimming_file.read())
                        elif opt == 2:
                            badminton_file = open("badminton_schedule.txt", "r")
                            print(badminton_file.read())
                        elif opt == 3:
                            football_file = open("football_schedule.txt", "r")
                            print(football_file.read())
                        elif opt == 4:
                            archery_file = open("archery_schedule.txt", "r")
                            print(archery_file.read())
                        elif opt == 5:
                            gymnastics_file = open("gymnastics_schedule.txt", "r")
                            print(gymnastics_file.read())
                        elif opt == 6:
                            volleyball_file = open("volleyball_schedule.txt", "r")
                            print(volleyball_file.read())
                        elif opt == 7:
                            basketball_file = open("basketball_schedule.txt", "r")
                            print(basketball_file.read())
                        elif opt == 8:
                            cricket_file = open("cricket_schedule.txt", "r")
                            print(cricket_file.read())
                        elif opt == 9:
                            tennis_file = open("tennis_schedule.txt", "r")
                            print(tennis_file.read())
                        elif opt == 10:
                            table_tennis_file = open("Table_Tennis_schedule.txt", "r")
                            print(table_tennis_file.read())
                    elif opt == 4:
                        student_feedback()
                    elif opt == 5:
                        exit(print("Good Bye!\tSee you Again!"))
                    else:
                        print("wrong Choice")
                        student_login()

            student_login()

    elif opt == 4:
        exit(print("Good bye"))

    else:
        print("Wrong choice!Choose from the stated choices")
        student_function()
        

#student_function()

def main_menu():
    print("*****Welcome to Real Champions Sport Academy System (RCSAS)*****")
    opt = int(input("For Admin User Enter 1 | For Student User Enter 2 |  To exit Enter 3"))
    if opt == 1:
        admin_function()
    elif opt == 2:
        student_function()
    elif opt == 3:
        exit(print("Good Bye!"))
    else:
        print("Wrong choice! Select from the mentioned choices only")
        main_menu()

main_menu()
