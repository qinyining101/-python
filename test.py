import random

def generate_random_simplified_chinese_string(length=14):
    # 简体中文字符的 Unicode 范围
    # 汉字的范围: 0x4E00 - 0x9FA5
    simplified_chinese_chars = [chr(i) for i in range(0x4E00, 0x4e05)]

    random_string = ''.join(random.choice(simplified_chinese_chars) for _ in range(length))
    return random_string

# 生成14个随机简体中文字符
random_simplified_chinese_string = generate_random_simplified_chinese_string()
print(random_simplified_chinese_string)
