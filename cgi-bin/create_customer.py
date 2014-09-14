import Dealing
import yate
from mako.template import Template
temp = Template(filename="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\templ.html")
print(yate.start_response())
print(yate.start_form("cgi-bin\save.py"))
print(temp.render())
print(yate.end_form("selects"))
