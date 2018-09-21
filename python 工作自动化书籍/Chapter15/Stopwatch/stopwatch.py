# 按下enter键，开始计时，再次按下enter键盘，计时暂停
# print函数有个end参数，可以在每行的末尾输出，这里输入一个空，是为了防止我们输入回车的时候，显示换行符号

import time
#init
print("when you enter 'enter',the watch will start.When you enter again,the watch will stop. ")
input()
lapNum=1
starttime= time.time()
lasttime = starttime

#stop
try:
    while True:
        input()
        totalTime = round(time.time()-starttime,2)
        duringTime = round(time.time()- lasttime,2)
        print('总时间：%s ，这次持续时间：%s ，次数：%s' %(totalTime,duringTime,lapNum),end='nihao')
        lapNum+=1
        lasttime = time.time()
except KeyboardInterrupt:
    print('Done!')
