import random
import string

def generate_random_string(length=8):

    characters = string.ascii_letters + string.digits  
    return "fl" + ''.join(random.choice(characters) for _ in range(length - 2))

def create_random_string_array(size=100000, string_length=8):
    return [generate_random_string(string_length) for _ in range(size)]


random_strings = create_random_string_array()


with open("data.txt", "w") as f:
    f.write("[")
    for i, s in enumerate(random_strings):
        f.write("\"%s\"" % s)  # 只写入字符串s
        if i < len(random_strings) - 1:
            f.write(",")  # 添加逗号，除了最后一个元素
    f.write("]")