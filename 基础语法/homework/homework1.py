import random
import re
import zlib
from timeit import Timer


def test01():
    result = []
    result = [str(i) for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
    print(",".join(result))


def test02():
    n = input("请输入一个数：")
    sum = 1
    result = []
    for i in range(1, int(n) + 1):
        sum *= i
        result.append(str(sum))

    print(",".join(result))


def test03():
    n = input("请输入一个数：")
    result = [{i: i * i} for i in range(1, int(n) + 1)]
    print(result)


def test04():
    n = input("请输入数字序列（逗号隔开）：")
    numbers = re.findall(r"\d+", n)
    print(numbers)
    print(tuple(numbers))


class Teacher:

    def __init__(self):
        self.content = ""

    def my_input(self):
        self.content = input("请输入内容：")

    def my_ptint(self):
        print(self.content.upper())


def test05():
    t = Teacher()
    t.my_input()
    t.my_ptint()


def test07():
    m = input("请输入一个数：")
    n = input("请输入一个数：")
    result = [[i * j for j in range(0, int(n))] for i in range(0, int(m))]
    print(result)


def test08():
    n = input("请输入字符串（逗号隔开）：")
    split = re.split(r"\s+", n)
    print(" ".join(sorted(list(set(split)))))


def test09():
    n = input("请输入字符串（逗号隔开）：")
    split = re.split(r"\s+", n)
    print(" ".join(sorted(list(set(split)))))


def test10():
    s = "0110,1101,1101,1111,0011,0101"
    split = s.split(",")
    values = []
    for i in split:
        int1 = int(i, 2)
        if int1 % 5 == 0:
            values.append(i)

    print(",".join(values))


def test11():
    values = []
    for i in range(1000, 3001):
        if i % 10 % 2 == 0 and i // 10 % 2 == 0 and i // 100 % 2 == 0 and i // 1000 % 2 == 0:
            values.append(str(i))

    print(",".join(values))


def test12():
    world = "hello world! 123"
    total = [0, 0]
    for i in world:
        if i.isalpha():
            total[0] += 1
        elif i.isdigit():
            total[1] += 1

    print(f"字母{total[0]}数字{total[1]}")


def test13():
    a = 9
    sum1 = 0
    total = 0
    for i in range(4):
        sum1 += a * 10 ** i
        total += sum1
    print(total)


def test14():
    s = "1,2,3,4,5,6,7,8,9"
    odd = [i for i in s.split(",") if int(i) % 2 != 0]
    print(",".join(odd))


def test15():
    input1 = """
    OOL,96,85;
    HDKCVY,67,70;
    JFKKFR,84,20;
    MUQYKO,11,25;
    UKIBQ,82,77;
    WMBT,94,22;
    BOWR,11,17;
    PHHCEU,13,58;
    BJVKEX,69,90;
    TIV,70,54;
    """
    input1 = re.findall(r"[A-Z]+,\d+,\d+", input1)
    list1 = [tuple(i.words(",")) for i in input1]
    # 当需要按数值排序而非字符串排序时
    print(sorted(list1, key=lambda x: (x[0], int(x[1]), int(x[2]))))


def test16():
    def generate_number(n):
        for i in range(n):
            if i % 7 == 0:
                yield i

    for i in generate_number(100):
        print(i)


def test19():
    global words
    with open("../resources/英语文章.txt", "r", encoding="utf-8") as f:
        read_str = f.read()
        words = re.split(r"\s+", read_str)
        map1 = {i: words.count(i) for i in words}
        l = sorted(map1.items(), key=lambda x: x[0])
        for i in l:
            print(i[0] + ":" + str(i[1]))


def test21():
    inlines = sorted(dir(__builtins__))
    for i in inlines:
        print("################【  %s 开始 】###############\t\t" % i)
        print(eval(i).__doc__)
        print("################【  %s 结束 】###############\t\t" % i)


def test23():
    function = lambda x, y: x + y
    print(function(1, 2))


def test34():
    l = [i ** 2 for i in range(1, 21)]
    print(l[:5])
    print(l[-5:])
    print(l[5:])


def test38():
    # 元组+生成器
    tuple1 = tuple(i ** 2 for i in range(1, 21))
    print(tuple1)
    print(tuple1[:len(tuple1) // 2])
    print(tuple1[len(tuple1) // 2:])


def test39():
    t = tuple(i for i in range(10))
    t1 = tuple(i for i in t if i % 2 == 0)
    print(t1)


def test40():
    l = [i for i in range(1, 11)]
    print(list(map(lambda x: x ** 2, l)))
    print(list(filter(lambda x: x % 2 == 0, l)))


class Person:
    def __init__(self):
        pass

    @staticmethod
    def eat():
        print("吃吃吃")


class Chinese(Person):
    pass


def test45():
    l = [i for i in range(1, 11)]
    print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, l))))


class Geometry:
    def get_area(self):
        pass


class Circle(Geometry):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        print("半径为%d的圆的面积为%.2f" % (self.radius, self.radius ** 2 * 3.14))
        return 3.14 * self.radius ** 2


class Rectangle(Geometry):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        print("宽为%d，高为%d的矩形的面积为%.2f" % (self.width, self.height, self.width * self.height))
        return self.width * self.height


class Square(Geometry):
    def __init__(self, side):
        self.side = side
        if self.side <= 0:
            raise RuntimeError("边长必须大于0")

    def get_area(self):
        print("边长为%d的正方形的面积为%.2f" % (self.side, self.side ** 2))
        return self.side ** 2


def test50():
    geometry = Circle(5)
    geometry.get_area()
    geometry = Rectangle(5, 4)
    geometry.get_area()
    geometry = Square(5)
    geometry.get_area()
    # Square(-1)


def test51():
    try:
        f = 5 / 0
    except ZeroDivisionError:
        print("除数不能为0")


class MyException(Exception):
    def __init__(self, message):
        self.message = message


def test52():
    exception = MyException("自定义异常")
    raise exception


def test57():
    h = u"hello 琳达"
    print(h)
    encode = h.encode("utf-8")
    print(encode)
    print(encode.decode("utf-8"))


def test59():
    n = 5
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += i / (i + 1)

    print(sum1)


def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


def test61():
    print(f(7))


def test63():
    print("=====方式1======")
    # 生成器
    n = 10
    for i in (i for i in range(1, n + 1) if i % 2 == 0):
        print(i)
    m = 100
    print("=====方式2======")

    def gen(m):
        for i in range(0, m + 1):
            if i % 5 == 0 and i % 7 == 0:
                yield i

    for i in gen(m):
        print(i)


def test64():
    for i in [i for i in range(10) if i % 2 == 0]:
        assert i % 2 == 0


def test65():
    print(eval(input("请输入代码：")))


def test73():
    print(random.randint(1, 100))
    print(random.uniform(10, 100))
    print(random.randrange(0, 10, 2))
    print(random.choice([i for i in range(10) if i % 5 == 0 and i % 7 == 0]))
    print(random.sample(range(100, 201), 5))
    print(random.sample(range(100, 201, 2), 5))
    print(random.sample([i for i in range(1, 1001) if i % 5 == 0 and i % 7 == 0], 5))


def test74():
    s = "123"
    compress = zlib.compress(s.encode("utf-8"))
    print(compress)
    print(zlib.decompress(compress))


def test75():
    timer = Timer("for i in range(100):1+1")
    print(timer.timeit())


def test76():
    list1 = [i for i in range(10)]
    random.shuffle(list1)
    print(list1)


def test77():
    ls = [i for (x, i) in enumerate(range(10)) if x % 2 == 0]
    print(ls)


def test78():
    ls = [[[0 for i in range(10)] for i in range(10)] for i in range(10)]
    print(ls)


def test87():
    a = set(i for i in range(1, 11))
    b = set(i for i in range(5, 30))
    print(a & b)
    print(a | b)
    print(a - b)


# 列表推导
if __name__ == "__main__":
    test87()
