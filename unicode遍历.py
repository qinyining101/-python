import unicodedata

def int_to_unicode_escape(int_value):
    # 将整数转换为四位的十六进制字符串
    hex_value = f"{int_value:04X}"
    
    # 将十六进制数转换为 Unicode 转义序列
    unicode_escape = f"\\u{hex_value}"
    return unicode_escape



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

def traverse_unicode_characters():
    # 打开文件以写入模式，使用utf-8编码
    with open("Unicode对照表.txt", "w", encoding="utf-8") as file:
        # Unicode字符集的范围是从0到0x10FFFF
        for code_point in range(0x110000):
            try:
                # 将码点转换为字符
                char = chr(code_point)
                # 判断字符是否可打印
                if is_printable(char):
                    # 将字符及其码点写入文件
                    if char==chr(ord(" ")-1):
                        file.write(f"U+{code_point:04X} - [ {char} ]\n"+"[SPACE]")
                    else:
                        file.write(f"U+{code_point:04X} - [ {char} ]\n"+"["+unicodedata.name(chr(ord(char)+1))+"]")

                else:
                    # 获取控制字符的用途
                    description = get_control_char_description(char)
                    if description == "未知控制字符":
                        # 如果是未分配字符的码点
                        file.write(f"U+{code_point:04X} - 未分配字符的点位\n")
                    else:
                        # 将不可打印字符的信息写入文件
                        file.write(f"U+{code_point:04X} - 控制字符类型 - {description}\n")
            except ValueError:
                # 如果码点无效，则跳过
                continue

if __name__ == "__main__":
    traverse_unicode_characters()
