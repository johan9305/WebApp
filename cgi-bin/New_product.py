__author__ = 'Joan'
from mako.template import Template

import yate

print(yate.start_response())
mytemplate = Template(filename ="C:\\Users\\Joan\\Desktop\\WebApp\\templates\\NewProduct.html")
print(mytemplate.render())