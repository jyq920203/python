import win32process
import win32gui
from subprocess import *


class SysCheck:
    processlist = []
    # 查看系统的进程
    def checkSysprocess(self):

        p = Popen('tasklist', stdin=PIPE, stdout=PIPE, stderr=PIPE,
                  shell=False, creationflags=0x08000000)
        outinfo, errinfo = p.communicate()
        outinfo = outinfo.decode('gbk')
        proclist = outinfo.splitlines()

        for pinfo in proclist:
            if '二进制验证码生成器.exe' in pinfo:
                infolist = pinfo.split(' ')
                # 去掉其中的空信息
                infolist = [info for info in infolist if info]
                # 进程ID是第2个元素
                pid = infolist[1]
                self.processlist.append(pid)
        return self.processlist

    # 根据pid获取窗口句柄
    def get_hwnds_for_pid(self, pid):
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
                if found_pid == pid:
                    hwnds.append(hwnd)
                return True

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        hwndy = 0
        if hwnds:
            hwndy = hwnds[0]
        return hwndy
