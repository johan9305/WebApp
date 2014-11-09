
__author__ = 'Joan'
from mako.template import Template
import MySQLdb
import yate

db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")
na = []

cur = db.cursor()
cur.execute('Select * from Product')
result = cur.fetchall()

for a in result:
    na.append(a)



    

print(yate.start_response())
mytemplate = Template(filename ="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\table.html",enable_loop="True")
print(mytemplate.render(lista = na))
