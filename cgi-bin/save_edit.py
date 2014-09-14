import Dealing 
import cgi
import cgitb
import yate
from mako.template import Template
cgitb.enable()

get_data = cgi.FieldStorage()
name = get_data['name'].value
address = get_data['ad'].value
DOB = get_data['DOB'].value
file =get_data['file'].value

new_client = Dealing.Client(name ,DOB,address )

def rm(name):
    with open("../data/Clients.txt" ,"r+") as piru:
        list = piru.readline()
        cl = list.strip().split(',')
        cl.remove(name)


if file == name :
    Dealing.empty("C:\\Users\\Joan\\Desktop\\WebApp\\data\\" + name + ".txt")
    new_client.save_in_file( "C:\\Users\\Joan\\Desktop\\WebApp\\data\\" +name+".txt")
elif file != name:
    Dealing.Remove("C:\\Users\\Joan\\Desktop\\WebApp\\data\\" +file+".txt")
    new_client.save_in_file( "C:\\Users\\Joan\\Desktop\\WebApp\\data\\" +name+".txt")
    rm(file)
    new_client.put_in_list



tem = Template(filename="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\Lista_clientes.html")
print(yate.start_response())
print(tem.render(Name = name , Address = address , DOBs = DOB))



