class Stack:
    def __init__(self, max_size=None):
        self.items = []  # 用列表来存储栈中的元素
        self.max_size = max_size  # 可选变量，栈的最大大小

    def is_empty(self):
        """判断栈是否为空"""
        return len(self.items) == 0

    def is_full(self):
        """判断栈是否已满"""
        return self.max_size is not None and len(self.items) >= self.max_size

    def push(self, item):
        """将一个元素压入栈顶"""
        if self.is_full():
            raise IndexError("栈已满，无法压入新元素")
        self.items.append(item)

    def pop(self):
        """从栈顶弹出一个元素"""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("弹出时栈为空")

    def peek(self):
        """查看栈顶元素但不弹出"""
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("查看时栈为空")

    def size(self):
        """返回栈的大小"""
        return len(self.items)

    def __str__(self):
        return str(self.items)  # 可以自定义输出格式
stack1=Stack()
stack2=Stack(max_size=5)