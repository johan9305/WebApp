import yate
import cgi
import cgitb
import Dealing
from mako.template import Template 

cgitb.enable()
get_data = cgi.FieldStorage()
person_name = get_data['wich'].value

datos = Dealing.get_from_file("C:\\Users\\Joan\\Desktop\\web\\data\\"+person_name+'.txt')
mytemplate =  Template(filename = "C:\\Users\\Joan\\Desktop\\web\\templates\\show.txt")
print(yate.start_response())
print(mytemplate.render(name = datos.name , ad = datos.adress , DOB = datos.DOB ))
