def main():
    print("Welcome to the UMS choose Following to proceed: ")
    choice= int(input("Choose your authority:\t\n1. Admin\n2. Faculty\n3. Exit\n"))
    while choice != 3:
        if choice == 1:          
            admin()
        elif choice == 2:
            faculty()
        choice = int(input("Choose your authority:\t\n1. Admin\n2. Student\n3. Exit\n"))
    print("\nThanks For Visiting")
    
    
def admin():
    choice_admin= int(input("Welcome Admin \n1. Add Faculty\n2. View Faculty\n3. Add Student\n4. View Student\n5. Search Faculty\n6. Search Student\n7. Visualise Attendance\n8. Delete Student/Faculty\n9. Back\n"))
    while choice_admin != 9:        
        if choice_admin == 1:
            print("1")            
        elif choice_admin == 2:
            print("2")
        elif choice_admin == 3:
            print("3")
        elif choice_admin == 4:
            print("4")
        elif choice_admin == 5:
            print("5")
        elif choice_admin == 6:
            print("6")
        elif choice_admin == 7:
            print("7")
        elif choice_admin == 8:
            delete_member()
        choice_admin = int(input("Welcome Admin \n1. Add Faculty\n2. View Faculty\n3. Add Student\n4. View Student\n5. Search Faculty\n6. Search Student\n7. Visualise Attendance\n8. Delete Student/Faculty\n9. Back\n"))    

        
def faculty():
    choice_faculty= int(input("Welcome Faculty \n1. View Students\n2. Search Student\n3. Mark Attendance\n4. View Attendance\n5. Visualise Attendance\n6. Back\n"))
    while choice_faculty != 6:       
        if choice_faculty == 1:
            print("1")
        elif choice_faculty == 2:
            print("2")
        elif choice_faculty == 3:
            print("3")
        elif choice_faculty == 4:
            print("4")
        elif choice_faculty == 5:
            print("5")
        choice_faculty = int(input("Welcome Faculty \n1. View Students\n2. Search Student\n3. Mark Attendance\n4. View Attendance\n5. Visualise Attendance\n6. Back\n"))    

def delete_member():
    choice_delete= int(input("Delete :\n1. Delete Student record\n2. Delete Faculty Record \n3. Back\n"))
    while choice_delete != 3:       
        if choice_delete == 1:
            print("1")
        elif choice_delete == 2:
            print("2")
        
        choice_delete = int(input("Delete :\n1. Delete Student record\n2. Delete Faculty Record \n3. Back\n"))
    
if __init__ == 'main':
    main()
