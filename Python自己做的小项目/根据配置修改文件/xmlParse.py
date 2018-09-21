import xml.etree.ElementTree as ET

class xmlParse(object):
    def __init__(self):
        pass

    def modifyEle(self,xuanzefilname,attri,ConfigValue):
        tree = ET.ElementTree(file=xuanzefilname)
        if attri != 'DateSourceFileName':
            xpathString = ".//testcase[@reportlevel='Info;20']/parameters/param[@name='{0}']".format(attri)
            print(xpathString)
            elem=tree.find(xpathString)
            print(elem)
            print(ConfigValue)
            elem.set('value', ConfigValue)
        elif attri == 'DateSourceFileName':
            xpathString = ".//DataSource"
            elem = tree.findall(xpathString)
            print(elem)
            print(ConfigValue)
            for eleall in elem:
                eleall.set('filename', ConfigValue)
        tree.write(xuanzefilname)






# ha = xmlParse('dirPath','1')
# ha.modifyEle()