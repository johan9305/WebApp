import yate
import cgi
import cgitb
import Dealing
from mako.template import Template 

cgitb.enable()
get_data = cgi.FieldStorage()
person_name = get_data['wich'].value

datos = Dealing.get_from_file("..\\data\\"+person_name+'.txt')
mytemplate =  Template(filename = "..templates\\show.txt")
print(yate.start_response())
print(mytemplate.render(name = datos.name , ad = datos.adress , DOB = datos.DOB ))
