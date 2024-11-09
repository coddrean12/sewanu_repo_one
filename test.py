#!C:\Users\HODEWU\Documents\Web_backend\Python\mysql_env\Scripts\python.exe
print("Content-Type: text/html\n\n")

import mysql.connector, cgi, jsonify
from mysql.connector import Error

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="contact_dunis"
    )

    cursor = con.cursor()

    cursor.execute("SELECT * FROM  WHERE 1")
    result = cursor.fetchall()
    if result: 
        # print(jsonify([x for x in result]))
         print(f"<h1>recipes:{[x for x in result]} </h1>")

except Error as e:
    print(f"<h1>Error: {e}</h1>")

except Exception as e:
    print(f"<h1>Error: {e}</h1>")

finally:
    if con.is_connected():
        cursor.close()
        con.close()