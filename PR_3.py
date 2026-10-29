print("Welcome to the Student Data Organizer!")
students_list=[{
    "id"     : "18",
    "name"   : "Jhanvi",
    "age"    : "19",
    "grade"  : "A+",
    "dob"    : "14-12-2007",
    "subject": {"Maths,English"}
}, 
{ 
    "id"      : "14",
    "name"    : "Khushi",
    "age"     : "19",
    "grade"   : "B+",
    "dob"     : "18-11-2007",
    "subject" : {"Science,Commerce"}
}]

while(True):

    print("\n_______________")
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = int(input("Enter your chocie: "))

    match(choice):
        case 1:
            print("\n---- Add Student ----")
            student = {
                         "id"     : input("Student ID: "),
                         "name"   : input("Name: "),
                         "age"    : int(input("Age: ")),
                         "grade"  : input("Grade: "),
                         "dob"    : (input("Date of Birth: ")),
                         "subject": set(input("Subjects (comma-separated): ").split(",")),
                     }
            
            students_list.append(student)

            print("\nStudent Added Successfully!")

        case 2:
            print("\n---- Display All Students ----\n")
            for student in students_list:
                    print("Student ID:", student["id"])
                    print("Date of Birth:", student["dob"])
                    print("Name:", student["name"])
                    print("Age:", student["age"])
                    print("Grade:", student["grade"])
                    print("Subjects:", student["subject"])
                    print()

        case 3:
            print("\n---- Update Information ----")

            rollno = (input("\nEnter student id:"))

            for student in students_list:
                if(rollno == student["id"]):
                    print("\nEnter your choice to update:")
                    print("1. Update id")
                    print("2. Update name")
                    print("3. Update age")
                    print("4. Update grade")
                    print("5. Update dob")
                    print("6. Update subjects")

                    update = int(input("Enter your choice for update:"))

                    if(update == 1):
                        student["id"] = int(input("Enter ID: "))
                    
                    elif(update == 2):
                        student["name"] = input("Enter new name: ")
 
                    elif(update == 3):
                        student["age"] = int(input("Enter new age: "))
 
                    elif(update == 4):
                        student["grade"] = input("Enter new grade: ")
 
                    elif(update == 5):
                        student["dob"] = input("Enter new dob: ")
 
                    elif(update == 6):
                        student["subjects"] = set(input("Enter new subjects: ").split(","))
 
                    else:
                        print("Choice invalid")
                    print("\nInformation Updated Succesfully!")
                    break
            else:
                print("\nInvalid Id")
             
        case 4:
            print("\n---- Delete Student Record ----")
            rollno = input("\nEnter student id:")
            
            for student in students_list:
                if(rollno == student["id"]):
                    students_list.remove(student)
                    print("\nStudent record deleted successfully!")
                    break
            else:
                            print("\nInvalid Id")

        case 5:
            print("\n---- Display Subjects Offered ----")
            subjects = set()
            for student in students_list:
                    subjects.update(student["subject"])
                    
            for subject in subjects:
                print(subject)
                           

        case 6:
            print("Exiting the program. Goodbye!\n")
            break

        case _:
            print("Please enter valid choice")

