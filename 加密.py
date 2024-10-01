import os
import hashlib
from crypto.Cipher import AES
from crypto.Util.Padding import pad, unpad

# 生成随机IV
def generate_random_iv():
    return os.urandom(16)

# 将IV转换为字符串
def iv_to_string(iv):
    return ''.join(format(byte, '02x') for byte in iv)

# 解析IV字符串并输出位置
def output_iv_positions(iv_str):
    for i, char in enumerate(iv_str):
        print(f"字符 '{char}' 在位置 {i}")

# 加密示例
def keyword_encrypt(text, keyword):
    key = hashlib.sha256(keyword.encode('utf-8')).digest()
    iv = generate_random_iv()  # 随机生成IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_text = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
    return iv, encrypted_text

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
    text = input("请输入要加密的文本: ")
    keyword = input("请输入加密关键词: ")

    # 加密
    iv, encrypted_text = keyword_encrypt(text, keyword)

    # 将IV转换为字符串并存储
    iv_str = iv_to_string(iv)
    print(f"生成的IV: {iv_str}")

    # 输出对应位置
    output_iv_positions(iv_str)

    # 打印加密结果（将IV与加密文本结合）
    encrypted_bytes = iv + encrypted_text  # 将IV和加密文本组合
    print("加密后的文本（16进制 密文）: ", encrypted_bytes.hex())
    print("加密后的文本（2进制 密文）: ", ''.join(format(byte, '08b') for byte in encrypted_bytes))

