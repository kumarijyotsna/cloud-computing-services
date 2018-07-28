#!/usr/bin/python36
print("content-type: text/html")
print("")
import subprocess as sp
import cgi
form = cgi.FieldStorage()
dname = form.getvalue('dname')
dname1 = form.getvalue('dname1')
#dir_name=input("enter directory name to be created on server")

y=sp.getstatusoutput("sudo ansible-playbook staas.yml --extra-vars='n={}'".format(dname))
print (y[1])
if y[0]==0:
#    dir_client=input("enter directory name to created on client to mount")
    dir_op=sp.getstatusoutput("sudo mkdir /media/{}".format(dname1))
    op=sp.getstatusoutput("sudo mount 192.168.43.50:/cloud/{}  /media/{}".format(dname,dname1))
    if op[0]==0:
        print("staas service successfully started!!!")
    else:
        print("error")

else:
   print("cloud not configured properly!!!")
