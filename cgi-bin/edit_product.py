__author__ = 'Joan'

import yate
import cgi
import cgitb
import MySQLdb
import Dealing
from mako.template import Template
cgitb.enable()
get_data = cgi.FieldStorage()
person = get_data['which'].value
db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")

cur = db.cursor()
def get(name) :
    cur.execute('select * from Product where Name = "%s"'  %(name))
    result =cur.fetchall()

    return  result
list =[]
lista = get(person)
for a in lista :
    list.append(a[1])
    list.append(a[2])
    list.append(a[3])
    list.append(a[4])

we = list.pop()
na = list.pop()
l = list.pop()
dec = list.pop()



def update(nam,De,loc,na,we):
    cur.execute('update Clientset Description = "%s" , Location ="%s" , Name = "%s" , Weight = "%s"where  Name  = "%s" '%(nam,De,loc,na , we) )
    db.commit()



mytemplate = Template(filename="C:\\Users\\Joan\Desktop\\WebApp\\templates\\edit_product.html")

print(yate.start_response())
print(mytemplate.render(name = na , d = dec , l=l, we = we , b =na ))