
import Dealing
import cgi
import cgitb
import yate
import MySQLdb
from mako.template import Template
cgitb.enable()

get_data = cgi.FieldStorage()
name = get_data['name'].value
address = get_data['ad'].value
DOB = get_data['DOB'].value

db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")

cur = db.cursor()

def create(name , DOB , AD):
    cur.execute("Insert into Client (Id , Nombre , FechaNacimiento,Direccion) VALUES ( NULL ,'%s','%s','%s')" %(name,DOB,AD))
    db.commit()


create(name,DOB,address)

tem = Template(filename="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\Lista_clientes.html")
print(yate.start_response())
print(tem.render(Name = name , Address = address , DOBs = DOB))



