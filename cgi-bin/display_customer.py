
import yate
import cgi
import cgitb
import MySQLdb
import Dealing
from mako.template import Template 

db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")

cur = db.cursor()
cgitb.enable()
get_data = cgi.FieldStorage()
person_name = get_data['which'].value

def get(name) :
    cur.execute('select * from Client where Nombre = "%s"'  %(name))
    result =cur.fetchall()

    return  result
list =[]
lista = get(person_name)
for a in lista :
    list.append(a[1])
    list.append(a[2])
    list.append(a[3])

address = list.pop()
DOB = list.pop()
Name = list.pop()


mytemplate =  Template(filename = "C:\\Users\\Joan\\Desktop\\WebApp\\templates\\show.html")
print(yate.start_response())
print(mytemplate.render(name = Name , ad = address , DOB = DOB ))
