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
speak = pyttsx3.init()
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#cursor.execute('CREATE TABLE LOGIN_TABLE(u_id varchar(30), pass varchar(20), u_type varchar(20));')
#cursor.execute('INSERT INTO LOGIN_TABLE VALUES("admin","abcd","admin");')
#conn.commit()
speak.say("This is a system developed by Rimon, Shailesh, Vinay and Rick.")
speak.runAndWait()
login = -1
while login!=1:
    username = input('Enter username: ')
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

                    Enter 1 : To View List of Faculty
                    Enter 2 : To View List of Students
                    Enter 3 : To Add New Student
                    Enter 4 : To Add New Faculty
                    Enter 5 : To Change Password
                    Enter 6 : To Logout
                    """)
        speak.say("Choose an option please.")
        speak.runAndWait()
        choice = int(input('Enter your choice: '))
