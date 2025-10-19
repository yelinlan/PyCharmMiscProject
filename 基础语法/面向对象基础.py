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


if __name__ == "__main__":
    test_static_method()
