import tkinter.filedialog
import tkinter.messagebox as messagebox
from tkinter import *

from ReadConfig import ReadConfig
from xmlParse import xmlParse


class AppConfig(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.zhuntongguanvar=IntVar()
        self.fangzhenonevar = IntVar()
        self.ceshionevar = IntVar()
        self.xuanzhong = None
        self.filename = None
        self.configFile = None


        self.zhuntongguan = Checkbutton(text='准通关',variable=self.zhuntongguanvar, onvalue=1,offvalue=0,command=self.xuanze)
        self.zhuntongguan.grid(row=0,column=0,sticky=W)

        self.fangzhen = Checkbutton(text='测试',variable=self.fangzhenonevar, onvalue=1,offvalue=0,command=self.xuanze)
        self.fangzhen.grid(row=1, column=0, sticky=W)

        self.ceshi = Checkbutton(text='仿真',variable=self.ceshionevar, onvalue=1,offvalue=0,command=self.xuanze)
        self.ceshi.grid(row=2, column=0, sticky=W)

        self.xuanzexiugaiwenjian = Button(text='选择用例管理文件',command=self.lujing)
        self.xuanzexiugaiwenjian.grid(row=3, column=0, sticky=W)

        self.lb = Label(text = '')
        self.lb.grid(row=4, column=0, sticky=W)

        self.xuanzepeizhiwenjian = Button(text='选择配置文件', command=self.peizhilujing)
        self.xuanzepeizhiwenjian.grid(row=6, column=0, sticky=W)

        self.lbpeizhi = Label(text='')
        self.lbpeizhi.grid(row=7, column=0, sticky=W)

        self.queren = Button(text='确定',command=self.Config)
        self.queren.grid(row=8, column=0, sticky=W)



    def xuanze(self):
        if (self.zhuntongguanvar.get() == 1) & (self.fangzhenonevar.get() == 0)& (self.ceshionevar.get() == 0):
            self.xuanzhong = 0
        elif (self.zhuntongguanvar.get() == 0) & (self.fangzhenonevar.get() == 1)& (self.ceshionevar.get() == 0):
            self.xuanzhong = 1
        elif (self.zhuntongguanvar.get() == 0) & (self.fangzhenonevar.get() == 0)& (self.ceshionevar.get() == 1):
            self.xuanzhong = 2
        else:
            messagebox.showerror(title="慢慢来",message="一次只能选择一个,不选或者多选无效哦")
        print(self.xuanzhong)

    def lujing(self):
        self.filename = tkinter.filedialog.askopenfilename()
        if self.filename != '':
            self.lb.config(text="您选择的用例文件是：" + self.filename)
        else:
            self.lb.config(text="您没有选择任何用例文件")

    def peizhilujing(self):
        self.configFile = tkinter.filedialog.askopenfilename()
        if self.configFile != '':
            self.lbpeizhi.config(text="您选择的配置文件是：" + self.configFile)
        else:
            self.lbpeizhi.config(text="您没有选择任何配置文件")

    def Config(self):
        if self.xuanzhong==None or self.filename == None:
            messagebox.showerror(title="慢慢来", message="未选择环境或者是需要的文件！")
        else:
            list=['准通关','测试','仿真']
            print(list[self.xuanzhong])
            readconfig = ReadConfig(list[self.xuanzhong],self.configFile)
            readconfig.read()

            for key in readconfig.dictINuse:
                print(key)
                print(readconfig.dictINuse[key])
                xmlp = xmlParse()
                xmlp.modifyEle(self.filename,key, readconfig.dictINuse[key])
            messagebox.showinfo(title="配置",message="配置刷新完成！")



app = AppConfig()
app.master.title('修改配置')
app.master.geometry('500x300')
app.mainloop()
