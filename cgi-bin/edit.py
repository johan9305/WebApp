# /usr/bin/env python
__author__ = 'Joan'
from mako.template import Template
import Dealing
import cgi
import cgitb
import yate
import MySQLdb
cgitb.enable()
get_data = cgi.FieldStorage()
person = get_data['which'].value
db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")
cur = db.cursor()
def get(name) :
    cur.execute('select * from Client where Nombre = "%s"'  %(name))
    result =cur.fetchall()

    return  result
list =[]
lista = get(person)
for a in lista :
    list.append(a[1])
    list.append(a[2])
    list.append(a[3])

Address = list.pop()
DOB = list.pop()
Name = list.pop()



def update(file,name,dob,ad):
    cur.execute('update Clientset Nombre = "%s" , FechaNacimiento ="%s" , Direccion = "%s"where  Nombre = "%s" '%(name,dob,ad , file) )
    db.commit()



mytemplate = Template(filename="C:\\Users\\Joan\Desktop\\WebApp\\templates\\edit.html")

print(yate.start_response())
print(mytemplate.render(name = Name , address = Address ,dob = DOB , b = Name ))

