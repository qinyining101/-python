import os
import hashlib
from crypto.Cipher import AES
from crypto.Util.Padding import pad, unpad


# 解密示例
def keyword_decrypt(encrypted_bytes, keyword):
    key = hashlib.sha256(keyword.encode('utf-8')).digest()
    # 提取IV（前16字节）
    iv = encrypted_bytes[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(encrypted_bytes[16:])
    return unpad(decrypted_bytes, AES.block_size).decode('utf-8')

# 主逻辑
if __name__ == "__main__":


    # 用户输入解密内容
    type=input("请输入密文类型（bin，hex）：")
    encrypted_text = input("请输入加密后的文本（密文）: ")
    keyword_for_decrypt = input("请输入解密关键词: ")
    if type=="hex":
    # 从十六进制字符串转换回字节
        encrypted_bytes = bytes.fromhex(encrypted_text)
    elif type=="bin":
        encrypted_bytes = bytearray(int(encrypted_text[i:i + 8], 2) for i in range(0, len(encrypted_text), 8))
    else:
        print("输入错误的密文类型，请重新输入！")
    # 解密
    decrypted_text = keyword_decrypt(encrypted_bytes, keyword_for_decrypt)
    print("解密后的文本: ", decrypted_text)
