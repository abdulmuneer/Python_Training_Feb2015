# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Networking: ssh, telnet, http
# Subprocess 

# <codecell>

import subprocess
ls = subprocess.Popen("ls",
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
x = ls.stdout.readlines()
print x

# <codecell>

import subprocess
ls = subprocess.Popen("lsss",
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
x = ls.stdout.readlines()
print x

# <codecell>

import subprocess
import sys

HOST="localhost"
# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND="uname -a"

ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result
    

# <markdowncell>

# ###Fabric
# 
# Fabric is a library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.
# 
# It provides a basic suite of operations for executing local or remote shell commands (normally or via sudo) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution.
# ####Basic Usage
# 
# Typical use involves creating a Python file named fabfile.py, containing one or more functions, then executing them via the fab command-line tool. Below is a small but complete fabfile.py containing a single task:

# <codecell>

from fabric.api import run

def host_type():
    run('uname -s')

# <markdowncell>

# ###paramiko

# <codecell>

import paramiko
import time
def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(1)
    # Clear the buffer on the screen
    output = remote_conn.recv(1000)
    return output

if __name__ == '__main__':


    # VARIABLES THAT NEED CHANGED
    ip = '1.1.1.16'
    username = 'testuser'
    password = 'password'

    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(
         paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip, username=username, password=password)
    print "SSH connection established to %s" % ip

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session established"

    # Strip the initial router prompt
    output = remote_conn.recv(1000)

    # See what we have
    print output

    # Turn off paging
    disable_paging(remote_conn)

    # Now let's try to send the router a command
    remote_conn.send("\n")
    remote_conn.send("show ip int brief\n")

    # Wait for the command to complete
    time.sleep(2)
    
    output = remote_conn.recv(5000)
    print output

# <markdowncell>

# ###telnet

# <codecell>

#telnet

import getpass
import sys
import telnetlib

HOST = "hostname"

user = raw_input("Enter your remote account: ")

password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")

tn.write(user + "\n")

if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")

tn.write("exit\n")

print tn.read_all()

# <markdowncell>

# ###http

# <codecell>

import requests

# <codecell>

x = requests.get("http://0.0.0.0:9999/")
print dir(x)

# <codecell>

print x.status_code

# <codecell>

print x.content

# <codecell>

help(requests.post)

# <codecell>

print x.text

# <codecell>

y= requests.post('http://0.0.0.0:9999/')

