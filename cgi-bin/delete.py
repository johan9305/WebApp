
__author__ = 'Joan'
import Dealing
import cgi
import cgitb
import yate
from mako.template import Template
cgitb.enable()

get_data = cgi.FieldStorage()
name = get_data['which'].value

Dealing.Remove("C:\\Users\\Joan\\Desktop\\WebApp\\data\\"+str(name)+".txt" )
Dealing.replace(str(name))




tem = Template(filename="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\client_deleted.html")
print(yate.start_response())
print(tem.render())



