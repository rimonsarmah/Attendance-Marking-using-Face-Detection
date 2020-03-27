import os
import sqlite3
import getpass
import face_recognition
import cv2
from prettytable import PrettyTable
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#cursor.execute('CREATE TABLE LOGIN_TABLE(u_id varchar(30), pass varchar(20), u_type varchar(20));')
#cursor.execute('INSERT INTO LOGIN_TABLE VALUES("admin","abcd","admin");')
#conn.commit()
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
        print("I'm afraid! You have entered a wrong password. Please try again.")
