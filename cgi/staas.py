#!/usr/bin/python36
print("content-type: text/html")
print("")
import subprocess as sp
print("""
<form action="stass.py">
<table align="center" width='80%' border='1'>
<tr>
<tr><td>enter directory name for cloud: <input type="text" name="dname" />
<tr><td>enter directory name for client: <input type="text" name="dname1"/>
<tr align="center"><td> <input type="submit"></td></tr>
""")
#dir_name=input("enter directory name to be created on server")


