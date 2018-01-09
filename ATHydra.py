#ATHydra

class ATHydra:
    def __banner(self):
        print("""
        ATHydra:
                To Easy To USE Hydra
                By SwordHeart Team
                Github  :https://github.com/DeeLMind
                Blog    :http://www.cnblogs.com/DeeLMind
        """)

    def __init__(self):
        self.__banner()
        pass

    def __del__(self):
        pass


    #private list of user
    __User = []
    __Pass = []

    def __load(self,path,Lst):
        with open(path,"r") as rFile:
            for line in rFile.readlines():
                Lst.append(line)

    def loadUser(self,path,lUser):
        self.__load(path,lUser)

    def loadPass(self,path,lPass):
        self.__load(path,lPass)


A = ATHydra()









