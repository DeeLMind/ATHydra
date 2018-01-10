#ATHydra
adfa
import sys
from optparse import OptionParser


class ATHydra:
    def __Banner(self):
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

ath = ATHydra()
ath.loadUser('name.txt')
ath.Attack()




