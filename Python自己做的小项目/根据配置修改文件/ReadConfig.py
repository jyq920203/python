import configparser
import Myconfig
class ReadConfig(object):

    def __init__(self,environments,configFile):
        self.filedir = configFile
        self.dictINuse={}
        self.environments = environments

    def read(self):
        config = Myconfig.Myconfig()
        config.read(self.filedir)


        # config = configparser.ConfigParser()
        # config.read(self.filedir)
        for yuan in config.items(self.environments):
            print(yuan[0])
            print(yuan[1])
            self.dictINuse[yuan[0]]=yuan[1]
        print(self.dictINuse)


# readDoc = ReadConfig()
# readDoc.read()
