__author__ = 'Joan'



from mako.template import Template
import yate
import MySQLdb

db =MySQLdb.connect(host = 'localhost',
                    user = 'matter_app',
                    passwd = 'm@tt3r',
                    db = 'matter')


clients =[]
cur = db.cursor()
cur.execute('Select * from Client')
table = cur.fetchall()
for a in table:
    clients.append(a[1])

print(yate.start_response())
mytemplate = Template(filename ="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\list_edit.html",enable_loop="True")
print(mytemplate.render(clients = clients))
