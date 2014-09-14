__author__ = 'Joan'
from mako.template import Template
import Dealing
import cgi
import cgitb
import yate
cgitb.enable()
get_data = cgi.FieldStorage()
person = get_data['which'].value
data = Dealing.get_from_file("C:\\Users\\Joan\\Desktop\\WebApp\\data\\" + person + ".txt")
Name = data.name
Address = data.adress
Dob = data.DOB



mytemplate = Template(filename="C:\\Users\\Joan\Desktop\\WebApp\\templates\\edit.html")

print(yate.start_response())
print(mytemplate.render(name = Name , address = Address ,dob = Dob))

Dealing.empty("C:\\Users\\Joan\\Desktop\\WebApp\\data\\" + person + ".txt")
