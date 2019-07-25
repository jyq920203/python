import tkinter.filedialog
import tkinter.messagebox as messagebox
from tkinter import *
from ReadFromCsv import *


class AppConfig(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.filename = None
        self.lb = Label(text='')
        self.lb.grid(row=4, column=0, sticky=W)

        self.selectFile = Button(text='选择需要转化的文件', command=self.SelectFIleB)
        self.selectFile.grid(row=3, column=0, sticky=W)

        self.queren = Button(text='确定', command=self.Config)
        self.queren.grid(row=8, column=0, sticky=W)


    def SelectFIleB(self):
        self.filename = tkinter.filedialog.askopenfilename()
        if self.filename != '':
            self.lb.config(text="您选择的文件是：" + self.filename)
        else:
            self.lb.config(text="您没有选择任何文件")


    def Config(self):
        writefile = 'dsn.bin'
        prefixString = 'SALT'
        sample = ReadFROMCSV()
        writetofile = WRITE2BINARY()
        md32 = MD5232()
        list = sample.trans2list2string(sample.readfromcsv(self.filename))
        print(list)
        writetofile.write2binary(list, writefile)
        string_32 = md32.tans232(md32.combineString(prefixString,WRITE2BINARY().encode(list)))
        print(md32.combineString(prefixString,list))
        writetofile.write2file(string_32,writefile)
        messagebox.showinfo(title="完成", message="已转换为二进制文件完成！")

app = AppConfig()
app.master.title('CSV变换二进制文件')
app.master.geometry('500x300')
app.mainloop()
