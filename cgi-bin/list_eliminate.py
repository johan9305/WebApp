from mako.template import Template
import Dealing
import yate

clients = Dealing.get_client_list(file="C:\\Users\\Joan\\Desktop\\WebApp\\data\\Clients.txt")

print(yate.start_response())
mytemplate = Template(filename ="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\list_delete.html",enable_loop="True")
print(mytemplate.render(clients = clients))

