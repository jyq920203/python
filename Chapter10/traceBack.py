import traceback
try:
    raise Exception('an error.')
except:
    errfile = open('error.log','w')
    errfile.write(traceback.format_exc())
    errfile.close()
    print('the traceback was written into error.log')