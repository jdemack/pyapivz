#!/usr/bin/python3

import paramiko
import os

##shortcut to issuing commands
def commandissue(sshsession, command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

##shortcut to gathering targets
def gettargets():
    targetlist = []
    targetip = input('What IP address to connect to? ')
    targetlist.append(targetip)
    targetuser = input('What username? ')
    targetlist.append(targetuser)
    return targetlist



def main():
    ##begin collecting information to connect
    connectionlist = []
    while(True):
        connectionlist.append(gettargets()) ##creds to connect
        zvarquit = input('Do you want to continue? (y/N): ')
        if zvarquit.lower() == 'n' or (zvarquit == ''):
            break

    reqfile = input('What is the full path of the requirements file? (Press ENTER for default) ')
    if reqfile == '':
        reqfile = 'requirements.txt'

    sshsession = paramiko.SSHClient()
    mykey = paramiko.RSAKey.from_private_key_file('/home/student/.ssh/id_rsa')
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ##begin connection
    for x in range(len(connectionlist)):
        ##connectionlist == [10.10.2.3, bender][10.10.2.4, fry][10.10.2.5, zoidburg]
        sshsession.connect(hostname=connectionlist[x][0], username=connectionlist[x][1], pkey=mykey)
        print(commandissue(sshsession, 'ls'))
        ftp_client=sshsession.open_sftp()
        ftp_client.put(reqfile,reqfile)
        ftp_client.close()
        print(commandissue(sshsession, 'ls'))

        commandissue(sshsession, 'sudo apt-get update')
        commandissue(sshsession, 'sudo apt install python3-pip -y') #ensure pip is installed
        commandissue(sshsession, 'python3 -m pip install -r ' + reqfile)



if __name__ == '__main__':
    main()

    
