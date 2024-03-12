# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:33:26 2022

@author: grego
"""

import mysql.connector


def database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="greg",
        password="contpass01",
        database="airy"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM DATA WHERE ID = 1")
    myresult = mycursor.fetchall()

    list_one = myresult[0]
    x = list_one[1]
    y = list_one[2]
    signal = list_one[3]
    stop = list_one[4]
    m = [x, y, signal]
    return m
