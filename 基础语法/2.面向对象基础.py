# 测试类


class Stu:
    # 公有属性
    slogan = "hello, world"

    # 私有属性
    __sex = "男"

    # 保护属性
    _age = 18

    # self  ---->  this
    def __init__(self, name, content):
        # 属性
        self.content = content
        print(f"初始化 name = {name} slogan={self.slogan}")

    def say_hello(self):
        print(self.__sex)
        print("hello, %s" % self.content)

    # 测试析构方法
    def __del__(self):
        print("对象被销毁")


class Monitor(Stu):
    pass


class Life(Stu):

    def __init__(self, name, content):
        super().__init__(name, content)
        print(" 调用父类构造器 ")

    def say_hello(self, over=""):
        print("hello, %s %s" % (self.content, over))


# 测试Stu构造方法
def test_stu():
    stu = Stu("张三", "steven!")
    stu.say_hello()
    print(stu._age)
    # print(stu._Stu__sex)


# 测试继承
def test_inherit():
    monitor = Monitor("张三", "steven!")
    monitor.say_hello()


# 测试重载
def test_overload():
    life = Life("张三", "steven!")
    life.say_hello("overload")


class A(Life, Monitor):
    pass


# 测试多继承
def test_multi_inherit():
    A("张三", "steven!")
    # mro   --->  方法重写顺序
    print(A.mro())


class Teacher:
    # 静态方法 不需要实例对象
    @staticmethod
    def hello():
        print("hello, world")

    # 类方法 可以访问类属性
    @classmethod
    def hello_class(cls):
        print("hello, class")


# 测试静态方法
def test_static_method():
    Teacher.hello()
    Teacher.hello_class()


class Principle(object):

    # 父类Object方法 创建对象 返回self给__init__
    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)

    # 初始化对象
    def __init__(self, name):
        print("init")
        self.name = name


# 测试__new__
def test_new():
    Principle("张三")


class Singleton(object):
    __instance = None
    __first_init = False
    __isSingleton = True

    def __new__(cls, *args, **kwargs):
        if cls.__isSingleton:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
        else:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not self.__first_init:
            print("初始化")
            print(self)
            self.__first_init = True
            self.name = "张三"


# 测试单例模式
def test_singleton():
    Singleton()
    Singleton()
    Singleton()


class Magic:
    def __init__(self):
        self.name = "张三"
        self.age = 18
        self.sex = "男"
        self.address = "中国"
        self.phone = "123456789"

    def __str__(self):
        return f"name={self.name} age={self.age} sex={self.sex} address={self.address} phone={self.phone}"


# 测试魔法方法
def test_magic():
    print(Magic())


if __name__ == "__main__":
    test_magic()
