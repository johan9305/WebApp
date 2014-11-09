__author__ = 'Joan'

from mako.template import Template
import MySQLdb
import yate

db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")
clients =[]
cur = db.cursor()
cur.execute('Select * from Product')
table = cur.fetchall()
for a in table:
    clients.append(a[3])

print(yate.start_response())
mytemplate = Template(filename ="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\list_products.html",enable_loop="True")
print(mytemplate.render(clients = clients))
