from crypto.Util.Padding import unpad 
from crypto.Cipher import AES 
import hashlib
from error import Qin_resource_check,Qin_time_limit_check

iv = b'qwertyuiopasdfgh'
@Qin_resource_check(cpu=30,memory=30)
@Qin_time_limit_check(2,5)
def keyword_decrypt(encrypted_text, keyword):
    key = hashlib.sha256(keyword.encode('utf-8')).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(bytes.fromhex(encrypted_text))
    decrypted_text = unpad(bytearray(decrypted_bytes), AES.block_size)

    return decrypted_text.decode('utf-8')

encrypted_text = input("请输入加密后的文本: ")
keyword = input("请输入解密关键词: ")
print("解密结果: ", keyword_decrypt(encrypted_text, keyword))