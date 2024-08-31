import requests # type: ignore
import tkinter.messagebox as tk # type: ignore
from tkinter import filedialog # type: ignore
import datetime as dt
import os
API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/bcd513d37a8f934e1fb26ce2b14ae2da/ai/run/"
headers = {"Authorization": "Bearer AggngFNvBULWcZOY4L9rClL8yF0ZvO8y0It5-A3P"}
start_time = dt.datetime.now()
formatted_start_time = start_time.strftime(r"%Y-%m-%d-%H.%M.%S")
chat_historys=[]

def save_history(history_file_path="",mode="a"):
    if len(history_file_path)==0:
        history_file_path = filedialog.askdirectory()
    
    with open("D:/"+formatted_start_time+".aichat", mode, encoding="utf-8") as f:
        for i in range(len(f)):
            f.write(chat_historys[i],end="")
def import_history():
    history_file_path = filedialog.askopenfilename(filetypes=[("chat history files", "*.aichat")])
    with open(history_file_path, "r", encoding="utf-8") as f:
        chat_history = f.readlines()
        for i in range(len(chat_history)):
            print(chat_history[i],end="")
            chat_historys[i]=chat_history[i].strip()
def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()
 


ans1=tk.askyesno("欢迎使用","是否导入聊天记录")
if ans1==True:
    import_history()

save_anytime=tk.askyesno("提示!","是否随时保存聊天记录")

while True:
    i=0

    try:
        inputs = [
            {"role": "system", "content": input("输入提示词：")}, 
            {"role": "user", "content": input("输入问题：")}
        ]
        output = run("@cf/openchat/openchat-3.5-0106", inputs)
        print("AI：" + output['result']['response'])
        chat_historys.append("提示词：" + inputs[0]['content'] + "\n")
        chat_historys.append("问题：" + inputs[1]['content'] + "\n")
        chat_historys.append("AI：" + output['result']['response']+"\n")
        i+=1
        if save_anytime==True:
            save_history(os.path.join("D:",formatted_start_time,".aichat"),"w")
    except Exception as e:
        print("发生错误！错误信息："+str(e))
        ans=tk.askyesno("错误!","是否保存聊天记录")
        if ans==True:
            save_history("D:/" + formatted_start_time + ".aichat", "w")
            print("聊天记录已保存！")
            print("程序退出！")
            break
        else:
            print("程序退出！")
            break
    if save_anytime==False:
        if i>=10:
            ans=tk.askyesno("提示!","是否保存聊天记录")
            if ans==True:
                save_history()
