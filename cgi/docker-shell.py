#!/usr/bin/python36
import subprocess as sp

print("content-type: text/html")
print("")

import cgi
form=cgi.FieldStorage()
cname=form.getvalue('x')
op=sp.getstatusoutput("docker inspect -f '{{ .NetworkSettings.IPAddress }}' %s" %cname)
print (op)
print("<a href='{}:4200'> open shell </a>".format(op[1]))
