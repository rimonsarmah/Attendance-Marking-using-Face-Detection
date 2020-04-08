import os
import pyttsx3
import sqlite3
import getpass
import face_recognition
import cv2
from prettytable import PrettyTable
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import attendance as atd
speak = pyttsx3.init()
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()
#cursor.execute('CREATE TABLE LOGIN_TABLE(u_id varchar(30), pass varchar(20), u_type varchar(20));')
#cursor.execute('INSERT INTO LOGIN_TABLE VALUES("admin","abcd","admin");')
#conn.commit()

speak.say("This is a system developed by Rimon, Shailesh, Vinay and Rick.")
speak.runAndWait()
login = -1
while login!=1:
    speak.say("Enter your username.")
    speak.runAndWait()
    username = input('Enter username: ')
    speak.say("Enter your password.")
    speak.runAndWait()
    print('Enter password: ')
    password = getpass.getpass()
    cursor.execute('SELECT * FROM LOGIN_TABLE WHERE u_id=?;',(username,))
    for x in cursor:
        global pass_valid
        pass_valid = x[1]
        global user_type
        user_type = x[2]
    if pass_valid == password:
        login = 1
    else:
        speak.say("I'm afraid! You have entered a wrong password. Please try again.")
        speak.runAndWait()
if user_type == 'admin':
    speak.say("Hello Admin! Welcome to Attendance Marking System Using Face Detection. Hope you'll find it interesting.")
    speak.runAndWait()
    while login == 1:
        speak.runAndWait()
        print("""


        |======================================================| 
        |==========Welcome To Attendance Marking System========|
        |======================================================|
         ------------------------------------------------------
                             Welcome Admin!

                    Enter 1 : To Add New Student
                    Enter 2 : To Add New Faculty
                    Enter 3 : To View List of Faculty
                    Enter 4 : To View List of Students
                    Enter 5 : To Search Student
                    Enter 6 : To Search Faculty
                    Enter 7 : To Delete Student
                    Enter 8 : To Delete Faculty
                    Enter 9 : To Change Password
                    Enter 10 : To Logout
                    """)
        speak.say("Choose one from the given option.")
        speak.runAndWait()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            print('Add New Student')
            s_section = input("Enter student's section: ")
            s_name = input('Enter student name: ')
            s_fname = input("Enter Father's name: ")
            s_mname = input("Enter Mother's name: ")
            s_email = input("Enter email id: ")
            s_phone = input("Enter student's phone no: ")
            s_pphone = input("Enter parent's phone no: ")
            s_address = input("Enter address: ")
            #cursor.execute("CREATE TABLE STUDENT(s_id integer PRIMARY KEY AUTOINCREMENT,s_section varchar(20), s_name varchar(30),s_fname varchar(30),s_mname varchar(30),s_email varchar(30),s_phone varchar(20),s_pphone varchar(30),s_address varchar(30));")
            cursor.execute("INSERT INTO STUDENT(s_section,s_name,s_fname,s_mname,s_email,s_phone,s_pphone,s_address) VALUES(?,?,?,?,?,?,?,?);",(s_section,s_name,s_fname,s_mname,s_email,s_phone,s_pphone,s_address))
            conn.commit()
            print('Added to STUDENT Table')
            print('Data Successfully Entered')
            speak.say("Data for new student is sucessfully added.")
            speak.runAndWait()
            speak.say("Press any key to continue.")
            speak.runAndWait()
            dummy = input('Press any key to continue...........')
           
        elif choice == 2:
            print('Add New Faculty')
            f_name = input('Enter Faculty name: ')
            f_subject = input("Enter subject: ")
            f_email = input("Enter email id: ")
            f_phone = input("Enter phone no: ")
            f_address = input("Enter address: ")
            f_pw = 'abcd'
            ac_type = 'faculty'
            #cursor.execute("CREATE TABLE FACULTY_DATA(f_id integer PRIMARY KEY AUTOINCREMENT,f_name varchar(30), f_subject varchar(30),f_email varchar(30),f_phone varchar(30),f_address varchar(30),f_pass varchar(30));")
            cursor.execute("INSERT INTO FACULTY_DATA(f_name,f_subject,f_email,f_phone,f_address,f_pass) VALUES(?,?,?,?,?,?);",(f_name,f_subject,f_email,f_phone,f_address,f_pw))
            conn.commit()
            cursor.execute("INSERT INTO LOGIN_TABLE VALUES(?,?,?);",(f_email,f_pw,ac_type));
            conn.commit()
            print('Data Successfully Entered')
            speak.say("Data of new faculty is added sucessfully.")
            speak.runAndWait()
            speak.say("Press any key to continue.")
            speak.runAndWait()
            dummy = input('Press any key to continue...........')
            
        elif choice == 3:
            print('List of Faculties: ')
            x = PrettyTable()
            cursor.execute("SELECT * from FACULTY_DATA")
            x.field_names = ["ID", "Name", "Subject", "Email", "Phone", "Address", "Password"]
            for row in cursor:
                x.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6]]);
            print(x)
            speak.say("Press any key to continue.")
            speak.runAndWait()
            dummy = input('Press any key to continue...........')
            
        elif choice == 4:
            print('List of Students: ')
            x = PrettyTable()
            cursor.execute("SELECT * from STUDENT")
            x.field_names = ["ID", "Section", "Name", "Father's Name", "Mother's Name", "Email", "Phone No", "Parent's Phone", "Address"]
            for row in cursor:
                x.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]]);
            print(x)
            speak.say("Press any key to continue.")
            speak.runAndWait()
            dummy = input('Press any key to continue...........')
           
        elif choice == 5:
            print("Search Student")
            print("1)Search by ID")
            print("2)Search by Name:")
            choice = int(input('Enter 1 or 2......'))
            if choice == 1:
                key = input('Enter ID: ')
                speak.say("please enter you identification.")
                speak.runAndWait()
                x = PrettyTable()
                cursor.execute("SELECT * from STUDENT_DATA WHERE s_id = ?;", key)
                x.field_names = ["ID", "Section", "Name", "Father's Name", "Mother's Name", "Email", "Phone No", "Parent's Phone", "Address"]
                for row in cursor:
                    x.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]]);
                print(x)
                dummy = input('Press any key to continue...........')
                speak.say("Press any key to continue.")
                speak.runAndWait()
            if choice == 2:
                key = input('Enter Name: ')
                key = key+'%'
                x = PrettyTable()
                cursor.execute("SELECT * from STUDENT_DATA WHERE s_name LIKE ?;", (key,))
                x.field_names = ["ID", "Section", "Name", "Father's Name", "Mother's Name", "Email", "Phone No", "Parent's Phone", "Address"]
                for row in cursor:
                    x.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]]);
                print(x)
                speak.say("Press any key to continue.")
                speak.runAndWait()
                dummy = input('Press any key to continue...........')
                
        elif choice == 6:
            print("Search Faculty")
            key = input('Enter Name: ')
            x = PrettyTable()
            cursor.execute("SELECT * from FACULTY_DATA where f_name LIKE ?;", key)
            x.field_names = ["ID", "Name", "Subject", "Email", "Phone", "Address", "Password"]
            for row in cursor:
                x.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6]]);
            print(x)
            dummy = input('Press any key to continue...........')
            speak.say("Press any key to continue.")
            speak.runAndWait()
        elif choice == 7:
            print('Delete Student: ')
            key = input('Enter ID: ')
            cursor.execute("DELETE from STUDENT WHERE s_id = ?;", (key,))
            conn.commit()
            print('Success')
            speak.say("Student data is successfully deleted.")
            speak.runAndWait()
            speak.say("Press any key to continue.")
            speak.runAndWait()
            dummy = input('Press any key to continue...........')
            
        elif choice == 8:
            print('Delete Faculty: ')
            key = input('Enter email ID: ')
            cursor.execute("DELETE from FACULTY_DATA WHERE f_email = ?;", (key,))
            print('Deleted from FACULTY_DATA')
            conn.commit()
            cursor.execute("DELETE from LOGIN_TABLE WHERE u_id = ?;", (key,))
            print('Deleted from LOGIN_TABLE')
            conn.commit()
            speak.say("Faculty data is successfully deleted.")
            speak.runAndWait()
            speak.say("Press any key to continuue.")
            speak.runAndWait()
            dummy = input('Press any key to continue...........')
           
        elif choice == 9:
            success = -1
            while success!=1:
                print('Enter password: ')
                speak.say("Give password or leave.")
                speak.runAndWait()
                password = getpass.getpass()
                cursor.execute('SELECT * FROM LOGIN_TABLE WHERE u_id=?;',(username,))
                for x in cursor:
                    pass_val = x[1]
                    if pass_val == password:
                        newp = input('Please enter new password: ')
                        speak.say("Please enter new password.")
                        speak.runAndWait()
                        cursor.execute("UPDATE LOGIN_TABLE set pass=? where u_id=?;",(newp,username))
                        conn.commit()
                        success = 1
                        print('Password Changed')
                        speak.say("Password changed successfully.")
                        speak.runAndWait()
                        login = 0
                    else:
                        print("I'm afraid! You have entered a wrong password. Please try again.")
                        speak.say("I'm afraid! You have entered a wrong password. Please try again.")
                        speak.runAndWait()
        elif choice == 10:
            login = 0
            speak.say("You are successfully logged out.")
            speak.runAndWait()
            print('You are successfully logged out')
            
        
elif user_type == 'faculty':
    speak.say("Hello Faculty! Welcome to Attendance Marking System Using Face Detection. Hope you'll find it interesting.")
    speak.runAndWait()
    while login == 1:
        cursor.execute("SELECT * from FACULTY_DATA where f_email=?;",(username,))
        for row in cursor:
            fac_name = row[1]

        print("""


            |======================================================| 
            |==========Welcome To Attendance Marking System========|
            |======================================================|
             ------------------------------------------------------
                                 Welcome Faculty!

                        Enter 1 : To View List of Students
                        Enter 2 : To Search Student
                        Enter 3 : To Mark Attendance
                        Enter 4 : To View Attendance
                        Enter 5 : To Visualize Attendance
                        Enter 6 : To Change Password
                        Enter 7 : To Logout
                        """)
        
        speak.say("Choose from following options .")
        speak.runAndWait()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            section = input('Enter the section: ')
            print('List of Students: ')
            x = PrettyTable()
            cursor.execute("SELECT * from STUDENT where s_section = ?",(section,))
            x.field_names = ["ID", "Section", "Name", "Father's Name", "Mother's Name", "Email", "Phone No", "Parent's Phone", "Address"]
            for row in cursor:
                x.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]]);
            print(x)
            speak.say("Press any key to continue.")
            speak.runAndWait()
            dummy = input('Press any key to continue...........')
           
        elif choice == 2:
            print("Search Student")
            print("1)Search by ID")
            print("2)Search by Name:")
            choice = int(input('Enter 1 or 2......'))
            if choice == 1:
                key = input('Enter ID: ')
                speak.say("Enter identification.")
                speak.runAndWait()
                x = PrettyTable()
                cursor.execute("SELECT * from STUDENT WHERE s_id = ?;", key)
                x.field_names = ["ID", "Section", "Name", "Father's Name", "Mother's Name", "Email", "Phone No", "Parent's Phone", "Address"]
                for row in cursor:
                    x.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]]);
                print(x)
                dummy = input('Press any key to continue...........')
                speak.say("Press any key to continue.")
                speak.runAndWait()
            if choice == 2:
                key = input('Enter Name: ')
                key = key+'%'
                x = PrettyTable()
                cursor.execute("SELECT * from STUDENT WHERE s_name LIKE ?;", (key,))
                x.field_names = ["ID", "Section", "Name", "Father's Name", "Mother's Name", "Email", "Phone No", "Parent's Phone", "Address"]
                for row in cursor:
                    x.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]]);
                print(x)
                
                speak.say("Press any key to continue.")
                speak.runAndWait()
                dummy = input('Press any key to continue...........')
        elif choice == 3:
            section = input('Enter Section: ')
            today = input('Enter date in DD-MM-YYYY format: ')
            slot = input('Enter time slot: ')
            fac_subject = input('Enter subject')
            atd.attend()
            s_present = atd.names
            print('Name of present Students: ',s_present)
            #cursor.execute("CREATE TABLE attendance(section varchar(10),s_name varchar(20),date varchar(20), time varchar(20), subject varchar(20), marked_by varchar(40), remark varchar(20));")
            cursor.execute("SELECT * from STUDENT where s_section=?;",(section,))
            s_all = []
            for row in cursor:
                s_all.append(row[2])
            print('Name of all students: ', s_all)
            for i in range(len(s_all)):
                if s_all[i] in s_present:
                    rem = 'Present'
                    cursor.execute("INSERT INTO attendance VALUES(?,?,?,?,?,?,?);",(section,s_all[i],today,slot,fac_subject,fac_name,rem))
                    conn.commit()
                else:
                    rem = 'Absent'
                    cursor.execute("INSERT INTO attendance VALUES(?,?,?,?,?,?,?);",(section,s_all[i],today,slot,fac_subject,fac_name,rem))
                    conn.commit()
            dummy = input('Press any key to continue...........')
        elif choice == 4:
            cursor.execute("SELECT * FROM attendance;")
            x = PrettyTable()
            x.field_names = ["Section", "Student Name", "Date", "Time", "Subject", "Marked by", "Remark"]
            for row in cursor:
                x.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6]]);
            print(x)
            speak.say("Press any key to continue.")
            speak.runAndWait()
            dummy = input('Press any key to continue...........')
        elif choice == 5:
            print('Visualize Attendance')
            print('1)Attendance of a particular student.')
            print('2)Attendance of a particular section.')
            choice = int(input('Enter your choice..'))
            if choice == 1:
                print('Enter details:')
                countp = 0
                total = 0
                vis_student_name = input('Enter student name: ')
                vis_student_sec = input('Enter student section: ')
                cursor.execute("SELECT * FROM attendance where s_name = ? AND section = ?;",(vis_student_name,vis_student_sec))
                for row in cursor:
                    if row[6] == 'Present':
                        countp += 1
                    total +=1
                absent = total - countp
                att_perc = (countp/total)*100
                print('Attendance percentage : ' + str(att_perc))
                labels = ['Present','Absent']
                vals = [countp,absent]
                colors = ['green','red']
                patches, texts = plt.pie(vals, colors=colors, shadow=True, startangle=90)
                plt.legend(patches, labels, loc="best")
                plt.axis('equal')
                plt.tight_layout()
                plt.show()
                speak.say("Press any key to continue.")
                speak.runAndWait()
                dummy = input('Press any key to continue...........')
            elif choice == 2:
                countp = 0
                total = 0
                print('Enter details:')
                vis_student_sec = input('Enter section: ')
                cursor.execute("SELECT * FROM attendance where section = ?;",(vis_student_sec,))
                for row in cursor:
                    if row[6] == 'Present':
                        countp += 1
                    total +=1
                absent = total - countp
                att_perc = (countp/total)*100
                print('Attendance percentage : ' + str(att_perc))
                labels = ['Present','Absent']
                vals = [countp,absent]
                colors = ['green','red']
                patches, texts = plt.pie(vals, colors=colors, shadow=True, startangle=90)
                plt.legend(patches, labels, loc="best")
                plt.axis('equal')
                plt.tight_layout()
                plt.show()
                speak.say("Press any key to continue.")
                speak.runAndWait()
        elif choice == 6:
            success = -1
            while success!=1:
                print('Enter password: ')
                password = getpass.getpass()
                cursor.execute('SELECT * FROM LOGIN_TABLE WHERE u_id=?;',(username,))
                for x in cursor:
                    pass_val = x[1]
                    if pass_val == password:
                        newp = input('Please enter new password: ')
                        cursor.execute("UPDATE LOGIN_TABLE set pass=? where u_id=?;",(newp,username))
                        conn.commit()
                        cursor.execute("UPDATE FACULTY_DATA set f_pass=? where f_email=?;",(newp,username))
                        conn.commit()
                        success = 1
                        login = 0
                    else:
                        print("I'm afraid! You have entered a wrong password. Please try again.")
        elif choice == 7:
            login = 0
            print('You are successfully logged out')
