__author__ = 'Joan'


import cgi
import cgitb
import MySQLdb

db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")

cur = db.cursor()
cgitb.enable()
get_data = cgi.FieldStorage()
id =  1234
"""get_data['which'].value"""

def get(id):
    cur.execute('select * from Drone where Id = "%d"'  %(id))
    result =cur.fetchall()

    return  result
list =[]
lista = get(id)
for a in lista :
    list.append(a[1])
    list.append(a[2])
    list.append(a[3])
    list.append(a[4])
    list.append(a[5])
    list.append(a[6])
    list.append(a[7])

print(list)