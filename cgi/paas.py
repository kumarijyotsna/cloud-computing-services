#!/usr/bin/python36
import subprocess as sp
print("content-type: text/html")
print("")

import cgi
form = cgi.FieldStorage()
cname = form.getvalue('cname')
print(cname)
port=65000
p_op=sp.getoutput("sudo netstat -tnlp | awk '{ print $4}'")
while(1):
	if str(port) in p_op:
		port=port-1
	else:
                break
print(port)
#print(cname , imgname)

#docker_launch_output = sp.getstatusoutput("sudo docker run -dit --name  {c} -p {port}:4200 {i}".format(c=cname,port=port,i=imgname))
#print(docker_launch_output)
m_op=sp.getstatusoutput("sudo docker run -dit --name {} -p {}:4200 jk_python:v4".format(cname,port))
print ("hi",m_op[0])
i_op=sp.getstatusoutput("sudo docker exec -di {} shellinaboxd -t -s'/:simmi:root:/:/usr/bin/python36'".format(cname))
print ("hi2",i_op[0])
c_op=sp.getstatusoutput("sudo docker inspect -f '{{ .NetworkSettings.IPAddress }}' %s" %cname)
print (c_op[1])
print("<a href='http://192.168.43.200/file/fire.py' download>download to run shell</a>")
