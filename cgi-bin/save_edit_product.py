
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
Stock = get_data['stock'].value
file =get_data['file'].value
weight = get_data['weight'].value
db = MySQLdb.connect(host= 'localhost',
                     user="matter_app",
                      passwd="m@tt3r",
                      db="matter")
clients =[]
cur = db.cursor()
def update(nam,De,na,we):
    cur.execute('update Product set Description = "%s" ,  Name = "%s" , Weight = "%s"where  Name  = "%s"   '%(De,na , we, nam) )
    db.commit()


update(file,address,Stock,name,weight)


tem = Template(filename="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\Lista_product.html")
print(yate.start_response())
print(tem.render(Name = name , Address = Stock  , D = address, w = weight))



