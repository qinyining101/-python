from wxauto import WeChat
import time as t
wx=WeChat()
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