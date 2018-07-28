#!/usr/bin/python36

import subprocess as sp

print("content-type: text/html")
print("")
#print("done")
import cgi
form = cgi.FieldStorage()
port = form.getvalue('p')
#print(port)
print("<iframe name='cframe' width='100%' height='25%'>container console</iframe>")

list = sp.getoutput("sudo docker ps")
print(list)

flist = list.split("\n")

print("<table align='center' width='90%' border='1'>")

print("""
<tr>
<th>Status</th>
<th>Image Name</th>
<th>Container Name</th>
<th>start</th>
<th>stop</th>
<th>Console</th>
</tr>
""")

for i in flist[1:]:
	j = i.split()
	print("<tr>")
	print("<td>")
	op_s=sp.getstatusoutput("sudo docker exec -di {} shellinaboxd -t".format(j[-1]))
#	print(op_s)
#	uop=sp.getstatusoutput("sudo docker exec -di {} useradd simmi".format(j[-1]))
#	pop=sp.getstatusoutput("sudo docker exec {} echo simmi | passwd simmi --stdin".format(j[-1]))
#	print (pop,uop)
	op=sp.getstatusoutput("sudo docker inspect -f '{{ .NetworkSettings.IPAddress }}' %s" %j[-1])
#	print(op)
	print(op[1])
	if "Exited" in i:
		print("down")
	elif "Up" in i:
		print("up")
	else:
		print("unknown")
	print("</td>")

	print("<td>")
	print(j[1])
	print("</td>")

	print("<td>")
	print(j[-1])
	print("</td>")

	print("<td>")
	print("<a href='docker-start.py?x={}'>start</a>".format(j[-1]))
	print("</td>")

	print("<td>")
	print("<a href='docker-stop.py?x={}'>stop</a>".format(j[-1]))
	print("</td>")


	print("<td>")
#	print("console")
	print("<a target='cframe' href='http://192.168.43.200:{}'>console</a>".format(port))
	print("</td>")


	print("</tr>")


print("</table>")
