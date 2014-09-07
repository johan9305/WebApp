__author__ = 'Joan'


import yate
from mako.template import Template
import Dealing
clients = Dealing.get_client_list(file = "C:\\Users\\Joan\Desktop\\web\\data\\Clients.txt")

print(yate.start_response())
mytemplate = Template(filename = "C:\\Users\\Joan\\Desktop\\web\\templates\\list.html",enable_loop="True")
print(mytemplate.render(clients = clients))
