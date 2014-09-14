__author__ = 'Joan'



from mako.template import Template
import Dealing

clients = Dealing.get_client_list(file="C:\\Users\\Joan\\Desktop\\WebApp\\data")


mytemplate = Template(filename ="..\\templates\\list.html",enable_loop="True")
print(mytemplate.render(clients = clients))
