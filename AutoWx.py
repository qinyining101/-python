from wxauto import WeChat
import time as t
wx=WeChat()
listen_list=["资料","文件传输助手"]
import time
from datetime import datetime
def main():
    while True:
        current_time = datetime.now()
        # 检查当前分钟是否为整点
        if current_time.second % 20 == 0:
            for i in listen_list:
                try:
                    wx.SendMsg(msg="机器人测试",who=i)
                    with open("log.txt","a",encoding="utf-8") as f:
                        f.write(f"sent message successfully at :{current_time} to {i}\n")
                except Exception as e:
                    with open("log.txt","a",encoding="utf-8") as f:
                        f.write(f"error happened at :{current_time} sending message to {i}, error log:{e}\n")
                t.sleep(10)
        else:
            continue
main()
listen_list=["资料","文件传输助手","MOZ"]
import time
from datetime import datetime
success_status=True
def main():
    while True:
        current_time = datetime.now()
        # 检查当前分钟是否为整点
        if current_time.second == 0:
                for i in listen_list:
                    if(not (wx.SendMsg(msg="机器人测试",who=i))):
                        success_status=False  
                    with open("log.txt","a") as f:
                        f.write(f"{current_time} 状态：{success_status} \n")
                    t.sleep(10)
        else:
            continue
main()