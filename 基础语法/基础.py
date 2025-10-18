# 测试数据类型
from 基础语法.hello.sayHello import say_hello as hi


def data_type():
    print(type(1))
    print(type(1.0))
    print(type(True))
    print(type(1 + 1j))
    print(type("linda"))


# 测试注释
def comment():
    """
    注释1
    注释2
    """
    multi_line = """
    多行字符串
    行1
    行2
    """
    print(multi_line)
    print('\t单引号字符串')


# 测试格式化字符串md

def format():
    a = 1
    print("{} {}".format("hello", "world"))
    print("%s %s" % ("hello", "world"))
    print(f"hello world{a}")


# 测试运算符
def operator():
    print(1 + 1)  # 2
    print(1 - 1)  # 0
    print(1 * 1)  # 1
    print(1 / 1)  # 1.0 浮点数
    print(1 // 1)  # 1  整除
    print(1 % 1)  # 0
    print(1 ** 1)  # 1
    print(1 << 1)  # 2
    print(1 >> 1)  # 0
    print(1 & 1)  # 1
    print(1 | 1)  # 1
    print(1 ^ 1)  # 0
    print(~1)  # -2    001->110 => -2


#  测试转义
def escape():
    print("hello\nworld")
    print("hello\tworld")
    print("hello\bworld")  # \b 退格
    print("hello\rworld")  # \r 回车


# 测试for
def for_loop():
    sum_Value = 0
    for i in range(1, 101):
        sum_Value += i
    print(sum_Value)


# 测试编码
def encoding():
    text = "123abc你好"
    custom_encoding = "utf-8"
    encode = text.encode(custom_encoding)
    print(encode, type(encode))
    decode = encode.decode(custom_encoding)
    print(decode, type(decode))


# 测试字符串
def string():
    print("hello" + "world")
    print("hello", "world", sep=" | ")
    print("@\t" * 5)
    parent_str = "0123456789"
    print("1" in parent_str)
    print("1" not in parent_str)
    print(parent_str[0])
    print(parent_str[-2])
    # 切片 从左往右切 ，步长默认1   [起始索引 ： 结束索引 ： 步长]
    print(parent_str[2:4])  # 23
    print(parent_str[:4])  # 0123
    print(parent_str[:])  # 0123456789

    print(parent_str[-3:-1])  # 78
    print(parent_str[:-1])  # 012345678

    # 改变步长
    print(parent_str[-1:-5])  # 步长为1 截取不到值
    print(parent_str[-1:-5:-1])  # 步长为-1 可以截取到值


# 测试字符串操作
def string_operation():
    parent_str = "\thello world\t"
    print(parent_str.upper())
    print(parent_str.lower())
    print(parent_str.capitalize())  # 字符串的首字母大写
    print(parent_str.title())  # 每个单词的首字母转换为大写
    print(parent_str.count("l"))
    print(parent_str.count("l", 4, 5))
    print(parent_str.find("l"))  # 未找到则返回-1
    print(parent_str.find("l", 4, 5))
    print(parent_str.index("l"))  # 未找到则抛出异常
    print(parent_str.index("l", 4, 5))  # 未找到则抛出异常
    print(parent_str.replace("l", "L"))
    print(parent_str.split(" "))
    print(parent_str.join(["hello", "world"]))  # 将列表["hello", "world"]中的元素用parent_str（即"hello world"）连接起来
    print(parent_str.strip())
    print(parent_str.lstrip())
    print(parent_str.rstrip())
    print(parent_str.center(20, "*"))  # 将字符串放在长度为20的区域内居中，两侧用"*"填充
    print(parent_str.zfill(20))
    print(parent_str.startswith("\thello"))
    print(parent_str.startswith("\thello", 0, 8))
    print(parent_str.endswith("world\t"))
    print(parent_str.endswith("world\t", 4))


# 测试列表
def list_property():
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [1, 2, 3, 4, 5]
    print(type(list_1))
    print(list_2, list_1)
    print(list_1 == list_2)
    print(list_1 is list_2)
    print(list_1 + list_2)
    print(list_1 * 2)
    print(len(list_1))
    print(list_1[0])
    print(list_1[-1])
    print(list_1[2:4])
    print(list_1[:4])
    print(list_1[:])
    print(list_1[-1:-5])
    print(list_1[-1:-5:-1])


# 测试列表操作
def list_operation():
    list_1 = [1, 2, 3, 4, 5]
    print(list_1)
    list_1.append(6)
    print(list_1)
    list_1.insert(0, 0)
    print(list_1)
    list_1.pop()
    print(list_1)
    list_1.pop(0)
    print(list_1)
    list_1.remove(1)  # 从列表中移除第一个值为1的元素
    print(list_1)
    list_1.reverse()
    print(list_1)
    list_1.sort()
    print(list_1)
    list_1.clear()


# 测试元组
def tuple_operation():
    tuple_2 = (1,)
    tuple_1 = (1, 2, 3, 4, 5)
    print(tuple_1)
    print(tuple_1[0])
    print(tuple_1[-1])
    print(tuple_1[2:4])
    print(tuple_1[:4])
    print(tuple_1[-1:-5])
    print(tuple_1[-1:-5:-1])
    print(tuple_1 + tuple_2)
    print(tuple_1 * 2)
    print(len(tuple_1))
    print(tuple_1.count(1))
    print(tuple_1.index(1))
    print(tuple_1.index(1, 0, 3))


# 测试字典
def dict_operation():
    dict_1 = {"name": "linda", "age": 18}
    print(dict_1)
    print(dict_1["name"])  # 会抛异常
    print(dict_1.get("name"))
    print(dict_1.keys())
    print(dict_1.values())
    print(dict_1.items())
    print(dict_1.pop("name"))
    print(dict_1)
    print(dict_1.popitem())
    print(dict_1)
    dict_1.clear()
    print(dict_1)
    dict_1.update({"name": "linda", "age": 18})
    print(dict_1)
    print(dict_1.setdefault("name", "linda"))
    print(dict_1.setdefault("sex", "male"))
    print(dict_1)
    print(dict_1.fromkeys(["name", "age"], "linda"))
    del dict_1["name"]
    del dict_1


# 测试集合
def set_operation():
    set_1 = {1, 2, 3, 4, 5}
    print(set_1)
    print(set_1 | {1, 2, 3})
    print(set_1 & {1, 2, 3})
    print(set_1 - {1, 2, 3})
    print(set_1 ^ {1, 2, 3})
    print(set_1.add(6))
    print(set_1)
    print(set_1.remove(6))
    print(set_1)
    print(set_1.discard(6))  # 删除元素
    print(set_1)
    print(set_1.pop())
    print(set_1)
    print(set_1.clear())
    print(set_1)
    set_1.update({1, 2, 3})
    print(set_1)

    print(hash(1))  # 整型不变
    print(hash('1'))


# 测试类型转换
def type_convert():
    print(int("1"))
    print(float("1"))
    print(str(1))
    print(bool(1))
    print(list("123456789"))
    print(tuple("123456789"))
    print(set("123456789"))
    print(chr(65))
    print(ord('A'))
    print(hex(10))
    print(oct(10))
    print(bin(10))
    print(eval("1+1"))
    print(type(1))
    print(type("1"))
    print(type(True))
    print(type([]))
    print(type(()))
    print(type({}))
    print(type(set()))
    print(type(chr(65)))
    print(type(hex(10)))
    print(type(oct(10)))
    print(type(bin(10)))
    print(type(eval("1+1")))


import copy


# 测试深浅拷贝
def copy_operation():
    list_1 = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5]]
    list_2 = list_1
    list_3 = copy.copy(list_1)
    # 赋值
    print(list_1)
    print(id(list_1))
    print(id(list_1[5]))
    print(list_2)
    print(id(list_2))
    print(id(list_2[5]))
    # 浅拷贝
    print(list_3)
    print(id(list_3))
    print(id(list_3[5]))
    # 深拷贝
    list_4 = copy.deepcopy(list_1)
    print(list_4)
    print(id(list_4))
    print(id(list_4[5]))


# 测试函数
def function_operation():
    def function_1(a, b):
        return a, b  # 返回多个值

    print(function_1(1, 2))


# 测试默认值函数
def default_value_function():
    def function_1(a, b=2):
        return a, b

    print(function_1(1))


# 测试可变参数函数
def variable_function():
    def function_1(*args):
        print(args)
        for arg in args:
            print(arg)
        return args

    print(function_1(1, 2, 3, 4, 5))


# 测试关键字参数函数
def keyword_function():
    def function_1(**kwargs):
        print(kwargs)
        for key, value in kwargs.items():
            print(key, value)
        return kwargs

    print(function_1(a=1, b=2, c=3, d=4, e=5))


# 测试作用域
def scope_operation():
    a_inner = 1
    b_inner = 2

    def function_1():
        a_i_i = 2
        b_i_i = 3
        print(a_i_i, b_i_i)

    function_1()
    print(a_inner, b_inner)


# 测试匿名函数 （！！！不要使用！！！）
def anonymous_function():
    add = lambda a, b=1: a + b
    print(add(1))
    print(add(1, 2))


import builtins


# 测试内置函数
def builtin_function():
    print(dir(builtins))
    print(abs(-1))
    print(all([1, 2, 3, 4, 5]))
    print(any([0, 0, 0, 0, 1]))
    print(bin(10))
    print(bool(1))
    print(chr(65))
    print(ord('A'))
    print(divmod(10, 3))
    print(enumerate([1, 2, 3, 4, 5]))
    print(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
    print(hex(10))
    print(id(1))
    print(input("请输入："))
    print(len([1, 2, 3, 4, 5]))
    print(map(lambda x: x * x, [1, 2, 3, 4, 5]))
    print(max([1, 2, 3, 4, 5]))
    print(min([1, 2, 3, 4, 5]))
    print(oct(10))
    print(pow(2, 3))
    print(range(10))
    print(reversed([1, 2, 3, 4, 5]))
    print(round(10.5))
    print(sorted([1, 2, 3, 4, 5]))
    print(sum([1, 2, 3, 4, 5]))
    print(type(1))
    print(zip([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))


# 测试拆包
def unpacking_operation():
    a, *b, c = [1, 2, 3, 4, 5]
    print(a, b, c)
    print(*[1, 2, 3, 4, 5])
    print(*range(1, 10))
    print(*range(10))
    print(*"12345")
    print(*(1, 2, 3, 4, 5))
    print(*[[1, 2, 3], [4, 5, 6]])
    print(*(x for x in range(10)))
    print(*map(lambda x: x * x, [1, 2, 3, 4, 5]))
    print(*filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))


# 测试异常
def exception_operation():
    try:
        print(1 / 0)
    except Exception as e:
        print(e)
        # raise Exception("异常")
        # raise e
        # raise
    else:
        print(3)
    finally:
        print(4)


# pip换源
"""
# 清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 阿里源
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
# 腾讯源
pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple
# 豆瓣源
pip config set global.index-url http://pypi.douban.com/simple/# 换回默认源pip config unset global.index-url
"""


# 测试模块
def module_operation():
    hi("linda")


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    module_operation()
