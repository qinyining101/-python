import socket  
import requests  
from ipaddress import ip_network, IPv4Address  
import platform  # 导入platform模块
def get_local_ip():  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    try:  
        s.connect(("8.8.8.8", 80))  
        IP = s.getsockname()[0]  
    finally:  
        s.close()  
    return IP  

def scan_network(ip, netmask="255.255.255.0"):  
    network = ip_network(f"{ip}/{netmask}", strict=False)  
    print(f"Scanning network: {network}")  
    num_hosts = len(list(network.hosts()))  
    scaned_hosts = 0  
    for host in network.hosts():  
        scaned_hosts += 1  
        print(f"\rScanned {scaned_hosts}/{num_hosts} hosts",end=' ')
        host_ip = str(host)  
        try:  
            response = requests.get(f'http://{host_ip}', timeout=0.5)  
            if response.status_code == 200:  
                print(f"{host_ip} is alive and has an HTTP service running.")  
            else:  
                print(f"{host_ip} is alive but HTTP service responded with {response.status_code}.")  
        except requests.exceptions.RequestException as e:  
            continue  

if __name__ == "__main__":  
    local_ip = get_local_ip()  
    print(f"Local IP: {local_ip}")  
    scan_network(local_ip)
