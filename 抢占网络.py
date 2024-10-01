import subprocess
import threading 
def ping(host):
    while True:
        try:
            # 使用 subprocess.run() 执行 ping 命令
            # 在 Windows 上使用 'ping -n 4'，在 Linux/Mac 上使用 'ping -c 4'
            result = subprocess.run(['ping', '-n', '4', host], capture_output=True, text=True)
        
            # 检查返回码
            if result.returncode == 0:
                print(f"Ping {host} succeeded:\n{result.stdout} return code: {result.returncode}")
            else:
                print(f"Ping {host} failed:\n{result.stderr} return code: {result.returncode}")
        except Exception as e:
            print(f"An error occurred: {e}")
def ping_multithreaded(hosts):  
    threads = []  
    
    thread = threading.Thread(target=ping, args=(target_host))  
    threads.append(thread)  
    thread.start()  
if __name__ == "__main__":
    target_host = "192.168.1.113"  
    ping(target_host)
