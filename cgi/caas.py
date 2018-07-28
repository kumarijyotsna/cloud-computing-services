#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print("\n")
dockerImageList = sp.getoutput("sudo docker images")

dockerimage = dockerImageList.split("\n")
#print("done")
print("""
<form action="shell_docker.py">
<table align="center" width='80%' border='1'>
<tr>
<tr><td>select image to build from: <select type="text" name="bimg" />
""")
for i in dockerimage[1:] :
	print("<option>")
	j = i.split()
	print(j[0] + ":"  +  j[1])
	print("</option>")
print("""
</select>
</td></tr>
<tr><td>username: <input type="text" name="user" /></td></tr>
<tr><td>password: <input type="password" name="passwd" /></td></tr>
<tr><td>container name:<input type="text" name="cname" /></td></tr>
<tr align="center"><td><input type="submit" /></td></tr>
</table>
</form>
""")

