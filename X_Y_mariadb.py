# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:33:26 2022

@author: grego
"""

import mysql.connector


def database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="Greg",
        password="contpass01",
        database="AIRY"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM DATA WHERE ID = 0")
    myresult = mycursor.fetchall()

    list_one = myresult[0]
    x = list_one[1]
    y = list_one[2]
    signal = list_one[3]
    m = [x, y, signal]
    return m
