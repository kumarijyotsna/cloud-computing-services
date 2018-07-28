#!/usr/bin/python36
print("content-type: text/html")
print("")
import subprocess as sp
#img=input("enter name for image (eg: jk:v1): ")
#bimg=input("enter base-image name(eg: centos:latest)")
#user=input("enter username: ")
import cgi
#print("done")
form = cgi.FieldStorage()
#img = form.getvalue('img')
bimg=form.getvalue('bimg')
user=form.getvalue('user')
passwd=form.getvalue('passwd')
cname=form.getvalue('cname')
#passwd=input("enter password: ")
#cname=input("enter container name")
aop=sp.getstatusoutput('sudo ansible-playbook shell_docker.yml --extra-vars="bimg={} user={} passwd={} cname={}"'.format(bimg,user,passwd,cname))
print(aop)
if aop[0]==0:
    print("succefully done")
else:
    print("error")

"""cmd1= 'docker inspect  {}'.format(cname)
cmd='sshpass -p redhat ssh -o StrictHostKeyChecking=false -l root 192.168.43.116 {}'.format(cmd1)

cop=sp.getstatusoutput(cmd)
print (cop[1])"""

#sp.getoutput("firefox 192.168.43.116:4445")
