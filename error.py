"""
error.py综述:
定义了十个异常类，分别对应四种错误类型：
1. InputTooSmallError: "输入过小"
2. InputTooBigError: "输入过大"
3. RuntimeError: "普通超时错误"
4. TimeLimitExceededError: "严重超时错误"
5. InputTypeError: "输入类型错误"
6. NetworkTimeoutError: "网络请求超时错误"
7. FileOperationError: "文件操作错误"
8. DatabaseConnectionError: "数据库连接错误"
9. ValidationError: "数据验证错误"
10. UnknowError: "未知错误"

定义了七个装饰器：
1. Qin_time_limit_check: 用于检查函数运行时间是否超出阈值，并抛出对应的异常 使用方法: @Qin_time_limit_check(普通超时时间门槛(单位:秒),严重超时时间门槛(单位:秒))
2. Qin_input_type_check: 用于检查函数输入参数类型是否符合要求,并抛出对应的异常 使用方法: @Qin_input_type_check({参数名(类型为str):参数类型})
3. Qin_resource_check: 用于检查函数运行过程中CPU和内存资源是否超出阈值,并抛出对应的异常 使用方法: @Qin_resource_check(CPU最大使用率(0-100),内存最大使用率(0-100))
4. Qin_network_timeout_check: 用于检查函数网络请求超时,并抛出对应的异常 使用方法: @Qin_network_timeout_check(超时时间(单位:秒))
5. Qin_file_operation_check: 用于检查函数文件操作是否出错,并抛出对应的异常 使用方法: @Qin_file_operation_check(文件路径,读写模式) 
读写模式:{
    'r'：以只读模式打开文件。文件的指针将会放在文件的开头。这是默认模式;
    'w'：以写模式打开文件。如果文件存在，则覆盖其内容；如果文件不存在，则创建新文件;
    'x'：以独占创建模式打开文件。如果文件已经存在，则操作失败;
    'a'：以追加模式打开文件。如果文件存在，文件指针将会放在文件的结尾；如果文件不存在，则创建新文件;
    'b'：以二进制模式打开文件;'t'：以文本模式打开文件。这是默认模式;
    't'：以文本模式打开文件。这是默认模式;
    '+'：以读写模式打开文件。文件指针将会放在文件的开头。
} 读写模式可以组合使用，如'rb'表示以读写二进制模式打开文件。
6. Qin_database_connection_check: 用于检查函数数据库连接是否出错,并抛出对应的异常 使用方法: @Qin_database_connection_check(数据库配置)
7. Qin_validation_check: 用于检查函数输入参数是否符合要求,并抛出对应的异常 使用方法: @Qin_validation_check({参数名(类型为str):验证函数})
验证函数: 验证函数接受一个参数，返回True或False，True表示参数符合要求，False表示参数不符合要求。
装饰器后需要函数定义，装饰器会自动调用函数，并在函数运行过程中监控情况，并抛出对应的异常

8. Qin_too_big_too_small_input: 用于检查输入是否超出范围,并抛出对应的异常 使用方法: @Qin_too_big_too_small_input(最小值,最大值)
定义了两个类：
1. InputChecker: 用于检查输入是否超出范围，并抛出对应的异常
2. Qin_TooBig_TooSmall_input: 用于检查输入是否超出范围，并抛出对应的异常

"""
import requests
import time
import psutil
import os
class UnknowError(Exception):
    def __init__(self, message="未知错误"):
        self.message = message
        super().__init__(self.message)
class FileOperationError(Exception):
    def __init__(self, message="文件操作错误"):
        self.message = message
        super().__init__(self.message)
class InputChecker:
    def __init__(self, min_value, max_value):
        self.max_value = max_value
        self.min_value = min_value
    def check(self, value):
        if value > self.max_value:
            raise InputTooBigError()
        elif value <= self.min_value:
            raise InputTooSmallError()
class TimeLimitExceededError(Exception):
    def __init__(self, message="严重超时错误"):
        self.message = message
        super().__init__(self.message)
class NetworkTimeoutError(Exception):
    def __init__(self, message="网络请求超时错误"):
        self.message = message
        super().__init__(self.message)
class RuntimeError(Exception):
    def __init__(self, message="普通超时错误"):
        self.message = message
        super().__init__(self.message)
class InputTypeError(Exception):
    def __init__(self, message="输入类型错误,请检查输入或重试"):
        self.message = message
        super().__init__(self.message)
class ResourceExceededError(Exception):
    def __init__(self, message="资源占用过多"):
        self.message = message
        super().__init__(self.message)
class InputTooSmallError(Exception):
    def __init__(self, message="too small input,输入过小,请检查输入或重试"):
        self.message = message
        super().__init__(self.message)
class InputTooBigError(Exception):
    def __init__(self, message="too big input,输入过大,请检查输入或重试"):
        self.message = message
        super().__init__(self.message)
class RuntimeError(Exception):
    def __init__(self, message="runtime error,普通超时错误,检查输入或重试"):
        self.message = message
        super().__init__(self.message)

class TimeLimitExceededError(Exception):
    def __init__(self, message="time limit exceeded,严重超时错误,检查输入或重试"):
        self.message = message
        super().__init__(self.message)

class ResourceExceededError(Exception):
    def __init__(self, message="ResourceExceededError,资源占用过多,检查输入或重试"):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionError(Exception):
    def __init__(self, message="数据库连接错误"):
        self.message = message
        super().__init__(self.message)

class ValidationError(Exception):
    def __init__(self, message="数据验证错误"):
        self.message = message
        super().__init__(self.message)

def Qin_file_operation_check(file_path, mode='r'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                with open(file_path, mode) as file:
                    result = func(*args, **kwargs)
            except FileNotFoundError as e:
                raise FileOperationError(f"文件未找到: {file_path},错误信息:{e}")
            except PermissionError as e:
                raise FileOperationError(f"权限错误: {file_path},错误信息:{e}")
            except IOError as e:
                raise FileOperationError(f"文件读写错误: {file_path},错误信息:{e}")
            except UnicodeDecodeError as e:
                raise FileOperationError(f"文件解码错误: {file_path},错误信息:{e}")
            except Exception as e:
                raise UnknowError(f"未知错误: {file_path},错误信息:{e}")
            return result
        return wrapper
    return decorator

def Qin_input_type_check(expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 将位置参数和关键字参数合并到一个字典中
            combined_args = dict(zip(func.__code__.co_varnames, args))
            combined_args.update(kwargs)

            for arg_name, arg_value in combined_args.items():
                if arg_name in expected_types and not isinstance(arg_value, expected_types[arg_name]):
                    raise InputTypeError(f"Input type error, 输入类型错误，错误参数为 {arg_name}, 输入类型为 {type(arg_value)}, 期望类型为 {expected_types[arg_name]}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

def Qin_time_limit_check(normal_threshold, severe_threshold):
    if normal_threshold > severe_threshold:
        raise ValueError("普通超时时间门槛必须大于严重超时时间门槛")
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time

            if elapsed_time > severe_threshold:
                raise TimeLimitExceededError(f"严重超时错误, 运行时间为 {elapsed_time} 秒, 超过了阈值 {elapsed_time - severe_threshold} 秒")
            elif elapsed_time > normal_threshold:
                raise RuntimeError(f"普通超时错误, 运行时间为 {elapsed_time} 秒, 超过了阈值 {elapsed_time - normal_threshold} 秒")

            return result

        return wrapper
    return decorator

def Qin_resource_check(cpu=30.0, memory=30.0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 获取当前进程的资源使用情况
            current_process = psutil.Process(os.getpid())
            cpu_percent = current_process.cpu_percent(interval=1)
            memory_info = current_process.memory_info()
            memory_percent = (memory_info.rss / psutil.virtual_memory().total) * 100

            if cpu_percent >= cpu:
                raise ResourceExceededError("CPU资源占用过多")
            if memory_percent > memory:
                raise ResourceExceededError("内存资源占用过多")

            return func(*args, **kwargs)
        return wrapper
    return decorator

def Qin_TooBig_TooSmall_input_check(min_value, max_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 将位置参数和关键字参数合并到一个字典中
            combined_args = dict(zip(func.__code__.co_varnames, args))
            combined_args.update(kwargs)

            for arg_name, arg_value in combined_args.items():
                if arg_name in min_value and arg_value < min_value[arg_name]:
                    raise InputTooSmallError(f"输入过小, {arg_name} 的值 {arg_value} 过小，小于阈值 {min_value[arg_name]-arg_value}")
                if arg_name in max_value and arg_value > max_value[arg_name]:
                    raise InputTooBigError(f"输入过大, {arg_name} 的值 {arg_value} 过大，超过了阈值 {max_value[arg_name]-arg_value}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

def Qin_network_timeout_check(timeout):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
            except requests.Timeout:
                end_time = time.time()
                elapsed_time = end_time - start_time
                raise NetworkTimeoutError(f"网络请求超时错误, 请求时间为 {elapsed_time} 秒, 超过了阈值 {elapsed_time - timeout} 秒")
            return result
        return wrapper
    return decorator

def Qin_database_connection_check(db_config):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                # 模拟数据库连接
                print(f"连接到数据库: {db_config}")
                result = func(*args, **kwargs)
            except Exception as e:
                raise DatabaseConnectionError(f"数据库连接错误: {e}")
            return result
        return wrapper
    return decorator

def Qin_validation_check(validation_rules):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg_name, arg_value in kwargs.items():
                if arg_name in validation_rules and not validation_rules[arg_name](arg_value):
                    raise ValidationError(f"数据验证错误: 参数 {arg_name} 的值 {arg_value} 不符合规则")
            return func(*args, **kwargs)
        return wrapper
    return decorator