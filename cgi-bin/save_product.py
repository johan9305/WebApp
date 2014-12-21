
import Dealing
import cgi
import cgitb
import yate
import MySQLdb
from mako.template import Template
cgitb.enable()

get_data = cgi.FieldStorage()
name = get_data['name'].value
description = get_data['ad'].value
weight = get_data['weight'].value
db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")

cur = db.cursor()

def create(des , na ,w):
    cur.execute("Insert into Product (Id , Description , Name ,Weight) VALUES ( 'NULL' ,'%s','%s','%s')" %(des,na,w))
    db.commit()


create(description,name ,weight)

tem = Template(filename="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\Lista_clientes.html")
print(yate.start_response())
print(tem.render(Name = name , DOBs = description, w = weight))



