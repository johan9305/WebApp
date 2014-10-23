
import yate
import cgi
import cgitb
import Dealing
from mako.template import Template 

cgitb.enable()
get_data = cgi.FieldStorage()
person_name = get_data['which'].value

datos = Dealing.get_from_file("C:\\Users\\Joan\\Desktop\\WebApp\\data\\"+person_name+'.txt')
mytemplate =  Template(filename = "C:\\Users\\Joan\\Desktop\\WebApp\\templates\\show.html")
print(yate.start_response())
print(mytemplate.render(name = datos.name , ad = datos.adress , DOB = datos.DOB ))
