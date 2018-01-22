#!/usr/bin/python
# -*- coding: UTF-8 -*-
#ATHydra
#To Ease To Use It
#ATHydra.py -u user.txt -p pass.txt -protocal -t threads -v verbose

# Hydra Document
# Syntax: hydra [[[-l LOGIN|-L FILE] [-p PASS|-P FILE]] | [-C FILE]] [-e nsr] [-o FILE] [-t TASKS] [-M FILE [-T TASKS]] [-w TIME] [-W TIME] [-f] [-s PORT] [-x MIN:MAX:CHARSET] [-SuvVd46] [service://server[:PORT][/OPT]]
#
# Options:
#   -R        restore a previous aborted/crashed session
#   -S        perform an SSL connect
#   -s PORT   if the service is on a different default port, define it here
#   -l LOGIN or -L FILE  login with LOGIN name, or load several logins from FILE
#   -p PASS  or -P FILE  try password PASS, or load several passwords from FILE
#   -x MIN:MAX:CHARSET  password bruteforce generation, type "-x -h" to get help
#   -e nsr    try "n" null password, "s" login as pass and/or "r" reversed login
#   -u        loop around users, not passwords (effective! implied with -x)
#   -C FILE   colon separated "login:pass" format, instead of -L/-P options
#   -M FILE   list of servers to attack, one entry per line, ':' to specify port
#   -o FILE   write found login/password pairs to FILE instead of stdout
#   -f / -F   exit when a login/pass pair is found (-M: -f per host, -F global)
#   -t TASKS  run TASKS number of connects in parallel (per host, default: 16)
#   -w / -W TIME  waittime for responses (32s) / between connects per thread
#   -4 / -6   prefer IPv4 (default) or IPv6 addresses
#   -v / -V / -d  verbose mode / show login+pass for each attempt / debug mode
#   -q        do not print messages about connection erros
#   -U        service module usage details
#   server    the target: DNS, IP or 192.168.0.0/24 (this OR the -M option)
#   service   the service to crack (see below for supported protocols)
#   OPT       some service modules support additional input (-U for module help)
#
# Supported services: asterisk cisco cisco-enable cvs ftp ftps http[s]-{head|get} http[s]-{get|post}-form http-proxy http-proxy-urlenum icq imap[s] irc ldap2[s] ldap3[-{cram|digest}md5][s] mssql mysql nntp oracle-listener oracle-sid pcanywhere pcnfs pop3[s] postgres rdp redis rexec rlogin rsh s7-300 sip smb smtp[s] smtp-enum snmp socks5 ssh sshkey teamspeak telnet[s] vmauthd vnc xmpp

# Use HYDRA_PROXY_HTTP or HYDRA_PROXY - and if needed HYDRA_PROXY_AUTH - environment for a proxy setup.
# E.g.:  % export HYDRA_PROXY=socks5://127.0.0.1:9150 (or socks4:// or connect://)
#        % export HYDRA_PROXY_HTTP=http://proxy:8080
#        % export HYDRA_PROXY_AUTH=user:pass
#
# Examples:
#   hydra -l user -P passlist.txt ftp://192.168.0.1
#   hydra -L userlist.txt -p defaultpw imap://192.168.0.1/PLAIN
#   hydra -C defaults.txt -6 pop3s://[2001:db8::1]:143/TLS:DIGEST-MD5
#   hydra -l admin -p password ftp://[192.168.0.0/24]/
#   hydra -L logins.txt -P pws.txt -M targets.txt ssh

# add function
# crack Dialg pass
import sys
from optparse import OptionParser
import win32gui

class ATHydra:
    '''
    Automate to Attack Password By Hydra
    It is so easy for you to USE Hydra
    '''
    def __Banner(self):
        '''
        Banner
        :return: Null
        '''
        print("""
        ATHydra:
                To Easy To USE Hydra
                By SwordHeart Team
                Github  :https://github.com/DeeLMind
                Blog    :http://www.cnblogs.com/DeeLMind
        """)

    #Arguments
    __options = {}
    __args = []

    def __options(self):
        usege = "python ATHydra.py -u uname -p pass --rdp"
        parser = OptionParser(usege)
        parser.add_option("-u", "--user", dest="username",help="A single username")
        parser.add_option("-U", "--User", dest="userList",help="A file of username")
        parser.add_option("-p", "--pass", dest="password",help="A single password")
        parser.add_option("-P", "--Pass", dest="passList",help="A file of password")
        parser.add_option("-r","--rdp",dest="rdp",help="3389 port")
        (options, args) = parser.parse_args()
        self.__options = options
        self.__args = args
        parser.print_help()


    def __init__(self):
        self.__Banner()
        self.__options()
        pass

    def __del__(self):
        pass

    #private list of user password
    __User = []
    __Pass = []

    #read file of user or pass' file
    def __load(self,path,Lst):
        with open(path,"r") as rFile:
            for line in rFile.readlines():
                Lst.append(line)

    #load username to __User
    def loadUser(self,path,lUser=__User):
        self.__load(path,lUser)

    #load password to __Pass
    def loadPass(self,path,lPass=__Pass):
        self.__load(path,lPass)



    def Attack(self):



        pass

    def Test(self):
        print(self.__User)


if __name__ == "__main__":
    ath = ATHydra()
    ath.Attack()




