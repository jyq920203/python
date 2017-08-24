def boxPrint(symbol,width,height):
    if len(symbol)>1:
        raise Exception('the length of symbol is larger than 1')
    if width <= 2:
        raise Exception('please input a number of width larger than 2')
    if height <= 2:
        raise Exception('please input a number of height larger than 2')
    else:
        print (symbol*width)
        for i in range(height-2):
            print(symbol+(width-2)*' '+symbol)
        print(symbol * width)

for sym,wid,hei in (('*',4,4),('0',20,5),('x',1,3),('zz',3,3)):
    try:
        boxPrint(sym,wid,hei)
    except Exception as err:
        print('An error happened:'+ str(err))


