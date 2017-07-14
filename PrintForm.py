tableDate=[['apple','orange','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['Dogs','Cats','Moose','Goose']]

def maxOflist(list1):
    len1= len(list1[0])
    for i in list1:
        if len(i)>=len1:
            len1=len(i)
            #return len1
    return len1


def printTable(a):
    colist=[0]*len(a)
    for i in range(len(a)):
        colist[i]=maxOflist(tableDate[i])

    for i in range(4):
        print(a[0][i].ljust(int(colist[0]))+'   '+a[1][i].ljust(int(colist[1]))
        +'   '+a[2][i].ljust(int(colist[2])))

printTable(tableDate)
