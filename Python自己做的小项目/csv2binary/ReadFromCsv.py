import csv
import hashlib

class ReadFROMCSV:
    def readfromcsv(self,fileName):
        with open(fileName) as f:
            sourcelist=[]
            f_csv = csv.reader(f)
            while True:
                try:
                    a = next(f_csv)
                    sourcelist.append(a)
                except StopIteration as e:
                    break
            return sourcelist

    def trans2list2string(self,sourcelist):
        finallist = []
        for i in sourcelist:
            for a in i:
                finallist.append(a)

        finalStr=','.join(finallist)
        return finalStr


class WRITE2BINARY:
    def encode(self,s):
        return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

    def decode(self,s):
        return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

    def write2binary(self,source,writefile):
        with open(writefile, 'w') as f:
            f.write(self.encode(source))

    def write2file(self,source,writefile):
        with open(writefile, 'a') as f:
            f.write('\n')
            f.write(source)


class MD5232:
    def tans232(self,stringneedencode):
        sha256 = hashlib.sha256()
        sha256.update(stringneedencode.encode('utf-8'))
        print(sha256.hexdigest())
        return sha256.hexdigest()
    # 32位，256bit，4位一个16进制数字，64个十六进制的数字
    def combineString(self,prefix,binarystring):
        return prefix+binarystring






