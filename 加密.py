from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad
import hashlib
from error import Qin_resource_check,Qin_time_limit_check
@Qin_resource_check(cpu=20,memory=30)
@Qin_time_limit_check(3,6)
def keyword_encrypt(text, keyword):
    # 使用关键词生成密钥
    key = hashlib.sha256(keyword.encode('utf-8')).digest()
    # 生成随机的初始化向量
    global iv
    iv=b'qwertyuiopasdfgh' #此字符建议不要更改，要更改请配合修改解密程序一起修改，建议使用默认值
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 加密文本
    encrypted_text = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
    return encrypted_text



text = input("请输入要加密的文本: ")
keyword = input("请输入加密关键词: ")
encrypted_text = keyword_encrypt(text, keyword)
print("加密后的文本: ", encrypted_text.hex())

