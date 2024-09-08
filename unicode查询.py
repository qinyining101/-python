import unicodedata

def is_printable(char):
    """判断字符是否可打印"""
    category = unicodedata.category(char)
    # 跳过控制字符、非字符和其他不可打印字符
    if category.startswith('C'):
        return False
    return True

def get_control_char_description(char):
    """获取控制字符的用途"""

    control_char_descriptions = {
        0x0000: "NULL",
        0x0001: "START OF HEADING",
        0x0002: "START OF TEXT",
        0x0003: "END OF TEXT",
        0x0004: "END OF TRANSMISSION",
        0x0005: "ENQUIRY",
        0x0006: "ACKNOWLEDGE",
        0x0007: "BELL",
        0x0008: "BACKSPACE",
        0x0009: "HORIZONTAL TABULATION",
        0x000A: "LINE FEED",
        0x000B: "VERTICAL TABULATION",
        0x000C: "FORM FEED",
        0x000D: "CARRIAGE RETURN",
        0x000E: "SHIFT OUT",
        0x000F: "SHIFT IN",
        0x0010: "DATA LINK ESCAPE",
        0x0011: "DEVICE CONTROL ONE",
        0x0012: "DEVICE CONTROL TWO",
        0x0013: "DEVICE CONTROL THREE",
        0x0014: "DEVICE CONTROL FOUR",
        0x0015: "NEGATIVE ACKNOWLEDGE",
        0x0016: "SYNCHRONOUS IDLE",
        0x0017: "END OF TRANSMISSION BLOCK",
        0x0018: "CANCEL",
        0x0019: "END OF MEDIUM",
        0x001A: "SUBSTITUTE",
        0x001B: "ESCAPE",
        0x001C: "FILE SEPARATOR",
        0x001D: "GROUP SEPARATOR",
        0x001E: "RECORD SEPARATOR",
        0x001F: "UNIT SEPARATOR",
        0x007F: "DELETE",
        0x0080: "PADDING CHARACTER",
        0x0081: "HIGH OCTET PRESET",
        0x0082: "BREAK PERMITTED HERE",
        0x0083: "NO BREAK HERE",
        0x0084: "INDEX",
        0x0085: "NEXT LINE",
        0x0086: "START OF SELECTED AREA",
        0x0087: "END OF SELECTED AREA",
        0x0088: "CHARACTER TABULATION SET",
        0x0089: "CHARACTER TABULATION WITH JUSTIFICATION",
        0x008A: "LINE TABULATION SET",
        0x008B: "PARTIAL LINE FORWARD",
        0x008C: "PARTIAL LINE BACKWARD",
        0x008D: "REVERSE LINE FEED",
        0x008E: "SINGLE SHIFT TWO",
        0x008F: "SINGLE SHIFT THREE",
        0x0090: "DEVICE CONTROL STRING",
        0x0091: "PRIVATE USE ONE",
        0x0092: "PRIVATE USE TWO",
        0x0093: "SET TRANSMIT STATE",
        0x0094: "CANCEL CHARACTER",
        0x0095: "MESSAGE WAITING",
        0x0096: "START OF PROTECTED AREA",
        0x0097: "END OF PROTECTED AREA",
        0x0098: "START OF STRING",
        0x0099: "SINGLE CHARACTER INTRODUCER",
        0x009A: "CONTROL SEQUENCE INTRODUCER",
        0x009B: "STRING TERMINATOR",
        0x009C: "OPERATING SYSTEM COMMAND",
        0x009D: "PRIVACY MESSAGE",
        0x009E: "APPLICATION PROGRAM COMMAND",
        0x009F: "SPECIAL MESSAGE"
    }

    return control_char_descriptions.get(ord(char), "未知控制字符")

def get_char_description(char):
    """获取字符的描述"""
    try:
        name = unicodedata.name(char)
        return f"[{name}]"
    except ValueError:
        return "[没有分配名称的字符]"

def get_unicode_line(input_value):
    """根据输入的字符或 Unicode 代码，输出对应的一整行"""
    try:
        if isinstance(input_value, str):
            char=[]
            char1=''
            return_value=[]
            if input_value.startswith("0x") or input_value.startswith("0X"):
                code_point = int(input_value, 16)
                char1 = chr(code_point)
                if is_printable(char1):
                    description = get_char_description(char1)
                    return f"U+{code_point:04X} - [ {char1} ] {description}"
                description = get_control_char_description(char1)
                if description == "未知控制字符":
                    return f"U+{code_point:04X} - 未分配字符的点位"
                else:
                    return f"U+{code_point:04X} - 控制字符类型 - {description}"
            else:
                for c in input_value:
                    char.append(ord(c))
                    if is_printable(c):
                        description = get_char_description(c)
                        return_value.append(f"U+{ord(c):04X} - [ {c} ] {description}")
                    description = get_control_char_description(c)
                    if description == "未知控制字符":
                        return_value.append(f"U+{ord(c):04X} - 未分配字符的点位")
                    else:

                        return_value.append(f"U+{ord(c):04X} - 控制字符类型 - {description}")
        return return_value
    except ValueError:
        return "无效的输入"
while True:
    input_value = input("请输入 Unicode 代码(0x开头的4-6位十六进制)或字符串(不以0x或0X开头，不为exit)进行查询，输入 exit 退出：")
    if input_value == "exit":
        break
    output_value='\n'
    ans=get_unicode_line(input_value)
    for i in range(len(ans)):
        if len(input_value)!=1:
            if i%2==0:
                output_value+=ans[i]+'\n'
        else:
            if i%2==0:
                output_value+=ans[i]
    print("查询结果:"+output_value)