import numpy as np
import mysql.connector
import random


def pull():
    connection = mysql.connector.connect(
        host="localhost",
        user="Greg",
        password="contpass01",
        database="AIRY"
    )
    cursor = connection.cursor()

    for i in np.arange(0, 25, 0.1):
        for j in np.arange(0, 25, 0.1):
            for k in range(10):
                query = "INSERT INTO COORD (X, Y, TYPE) VALUES (%s, %s, %s)"
                values = (i, j, 0)
                cursor.execute(query, values)
                connection.commit()
    connection.close()


def change(x, y):
    connection = mysql.connector.connect(
        host="localhost",
        user="Greg",
        password="contpass01",
        database="AIRY"
    )
    cursor = connection.cursor()
    sql = "UPDATE coord SET TYPE = %s WHERE X BETWEEN %s AND %s AND Y BETWEEN %s AND %s"
    values = (1, x - 1, x + 1, y - 1, y + 1)
    cursor.execute(sql, values)
    connection.commit()
    connection.close()


def add(x, y):
    connection = mysql.connector.connect(
        host="localhost",
        user="Greg",
        password="contpass01",
        database="AIRY"
    )
    cursor = connection.cursor()
    sql = "UPDATE coord SET TYPE = %s WHERE X = %s AND Y = %s"
    values = (1, x, y)
    cursor.execute(sql, values)
    connection.commit()

    for i in range(30000):
        query = "INSERT INTO COORD (X, Y, TYPE) VALUES (%s, %s, %s)"
        values = (x, y, 1)
        cursor.execute(query, values)
        connection.commit()
    connection.close()


def per_number(x, y):
    connection = mysql.connector.connect(
        host="localhost",
        user="Greg",
        password="contpass01",
        database="AIRY"
    )
    cursor = connection.cursor()
    for i in range(10000):
        for j in range(2):
            x_non = random.uniform(0, 25)
            x_non = round(x_non, 3)
            y_non = random.uniform(0, 25)
            y_non = round(y_non, 3)
            while x_non == x or y_non == y:
                x_non = random.uniform(0, 25)
                x_non = round(x_non, 3)
                y_non = random.uniform(0, 25)
                y_non = round(y_non, 3)
            query = "INSERT INTO COORD (X, Y, TYPE) VALUES (%s, %s, %s)"
            values = (x_non, y_non, 0)
            cursor.execute(query, values)
            connection.commit()
        query = "INSERT INTO COORD (X, Y, TYPE) VALUES (%s, %s, %s)"
        values = (x, y, 1)
        cursor.execute(query, values)
        connection.commit()
    connection.close()


# change(1.2, 10.6)
# pull()
per_number(10.27, 0.28)
