#版本1
#学习使用logging模块，logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
#设置日志打印的级别，以及日志打印的格式
#使用logging.debug()将括号中的内容打印成日志
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

def factorial(n):
    logging.debug('debug start.factorial(%s)' %(n))
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug('i is:'+str(i)+',total is:'+str(total))
    print(total)
    logging.debug('debug end.')
factorial(5)

# 版本2
# 学习将log日志存储到文件当中
# 学习日志的级别分为：
# debug(用于调试用的)，info(记录普通的信息)，warning(现在没有问题，但是以后可能有问题)，
# error(记录错误，该错误导致程序部分失败)，critical(导致程序崩溃)
# 日志的级别debug<info<warning<error<critical
import logging
logging.basicConfig(filename='factorial.log',level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')


# 版本3
# 学习日志级别，打印不同级别的日志
# basicConfig中配置的level是什么，打出的日志只会高于这个level
# logging.disable(logging.INFO),disable中设置的级别，打印的时候，会禁掉这个级别以下的日志
# PS：禁止日志包含禁止括号内的日志，禁止日志是从禁止设置行下面的一行才开始禁止，上面的不看
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('debug')
#---------#
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('see me!')
logging.disable(logging.INFO)
logging.debug('see me!')
logging.info('info')
logging.error('error')