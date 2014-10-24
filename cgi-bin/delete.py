
__author__ = 'Joan'
import Dealing
import cgi
import cgitb
import MySQLdb
import yate
from mako.template import Template
cgitb.enable()

get_data = cgi.FieldStorage()
name = get_data['which'].value

db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")
cur = db.cursor()
def eliminate(name):
    cur.execute('delete  from Client where Nombre = "%s" '%(name))
    db.commit()
eliminate(name)

tem = Template(filename="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\client_deleted.html")
print(yate.start_response())
print(tem.render())



