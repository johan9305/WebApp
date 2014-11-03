
import Dealing
import yate
from mako.template import Template
temp = Template(filename="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\templ.html")
print(yate.start_response())
print(temp.render())

