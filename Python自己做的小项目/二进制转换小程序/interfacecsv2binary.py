import tkinter.filedialog
import tkinter.messagebox as messagebox
from tkinter import font

import win32com.client
import win32con

from loadfont import *
from ReadFromCsv import *
from SysCheck import *


class AppConfig(Frame):
    def __init__(self, master=None):
        self.root = Tk()
        # 设置字体
        Loadsourcetool=LoadSource()
        relafile= Loadsourcetool.resource_path("SC.otf")
        Loadsourcetool.loadfont(relafile)
        self.Myfont = font.Font(family='思源黑体 Normal', size=11)
        self.root.wm_attributes('-topmost', 0)
        # 设置小图标
        icofile = Loadsourcetool.resource_path("A.ico")
        self.root.iconbitmap(icofile)
        Frame.__init__(self, master)

        self.grid()
        self.filename = None
        self.lb = Label(text='')
        self.lb.grid(row=4, column=0, sticky=W)

        self.selectFile = Button(text='选择需要转化的文件', command=self.SelectFIleB,font=self.Myfont)
        self.selectFile.grid(row=3, column=0, sticky=W)

        self.queren = Button(text='确定', command=self.Config,font=self.Myfont)
        self.queren.grid(row=8, column=0, sticky=W)

    def SelectFIleB(self):
        default_dir = os.getcwd()
        self.filename = tkinter.filedialog.askopenfilename(title=u"选择文件",
                    initialdir=(os.path.expanduser(default_dir)),filetypes=[("CSV Files",".csv")])
        if self.filename != '':
            self.lb.config(text="您选择的文件是：" + self.filename,font=app.Myfont)
        else:
            self.lb.config(text="您没有选择任何文件",font=app.Myfont)

    def Config(self):
        if self.filename != None and self.filename != '':
            default_dir = os.getcwd()
            writefile = tkinter.filedialog.asksaveasfilename(title=u"转换为",
                        initialdir=(os.path.expanduser(default_dir)), initialfile='dsn', filetypes=[("BIN Files",".bin")])+'.bin'
            if writefile is None or writefile=='.bin':
                return

            sample = ReadFROMCSV()
            writetofile = WRITE2BINARY()
            md32 = MD5232()

            # 从csv中读取数据并转化为string
            list = sample.trans2list2string(sample.readfromcsv(self.filename))
            writetofile.write2binary(list, writefile)
            prefixString = 'SALT'
            string_32 = md32.tans232(md32.combineString(prefixString,writetofile.encode(list)))
            writetofile.write2file(string_32,writefile)

            messagebox.showinfo(title="完成", message="二进制文件转换完成！")
        else:
            messagebox.showinfo(title="提示", message="请先选择文件！")

syscheck = SysCheck()
realsysprocesslist = syscheck.checkSysprocess()
print(realsysprocesslist)

if realsysprocesslist == []:
    app = AppConfig()
    app.master.title('二进制验证码生成器')
    app.master.geometry('500x300')
    app.mainloop()
else:
    if len(realsysprocesslist)>=1:
        hw = syscheck.get_hwnds_for_pid(int(realsysprocesslist[1]))
        print(hw)
        if hw == 0:
            app = AppConfig()
            app.master.title('二进制验证码生成器')
            app.master.geometry('500x300')
            app.mainloop()
        else:
            # 不然会报错 no available message,需要给屏幕发送一个按键，这里发送的是alt按键
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32gui.ShowWindow(hw, win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(hw)
