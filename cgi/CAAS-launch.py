#!/usr/bin/python36

import  cgi
import subprocess as sp

print("content-type: text/html")
print("")

form = cgi.FieldStorage()
cname = form.getvalue('cname')
imgname = form.getvalue('imgname')
port=65001
p_op=sp.getoutput("sudo netstat -tnlp | awk '{ print $4}'")
while(1):
	if str(port) in p_op:
		port=port-1
	else:
                break
print(port)
#print(cname , imgname)

docker_launch_output = sp.getstatusoutput("sudo docker run -dit --name  {c} -p {port}:4200 {i}".format(c=cname,port=port,i=imgname))
print(docker_launch_output)
if docker_launch_output[0]  == 0:
	print("container named {c} launched ..".format(c=cname))
	print("<a href='docker-manage.py?p={}'>click here to manage Container</a>".format(port))
else:
	
	print("container named {c} failed ..".format(c=cname))






