
import Dealing
import cgi
import cgitb
import yate
from mako.template import Template
import MySQLdb
cgitb.enable()

get_data = cgi.FieldStorage()
name = get_data['name'].value
address = get_data['ad'].value
DOB = get_data['DOB'].value
file =get_data['file'].value
db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")
clients =[]
cur = db.cursor()
def update(file,name,dob,ad):
    cur.execute('update Client set Nombre = "%s" , FechaNacimiento ="%s" , Direccion = "%s"where  Nombre = "%s" '%(name,dob,ad , file) )
    db.commit()



update(file,name,DOB,address)


tem = Template(filename="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\Lista_clientes.html")
print(yate.start_response())
print(tem.render(Name = name , Address = address , DOBs = DOB))



