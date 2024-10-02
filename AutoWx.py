from wxauto import WeChat
import time as t
wx=WeChat()
listen_list=["资料","文件传输助手"]
while 1:
    if(t.time()):
        t.sleep(10)
    for peo in listen_list:
        wx.SendMsg(msg="hello",who=peo)