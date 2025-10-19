# 测试OS使用
import os


# 测试OS使用  操作系统交互
def test_os():
    abspath = os.path.abspath(".")
    print(os.name)
    print(os.environ)
    print(os.environ.get("PATH"))
    print(abspath)
    print(os.path.join(abspath, "resources"))
    print(os.path.split(abspath))
    print(os.path.splitext(abspath))
    print(os.path.exists("resources"))
    print(os.path.dirname(abspath))
    print(os.path.basename(abspath))


# 测试SYS 使用 (程序与python交互)
import sys


def test_sys():
    print(sys.argv)
    print(sys.path)
    print(sys.version)  # python版本
    print(sys.platform)
    print(sys.getdefaultencoding())
    print(sys.getfilesystemencoding())
    print(sys.getsizeof(1))
    print(sys.getrecursionlimit())


# 测试TIME模块
import time


def test_time():
    print(time.time())
    print(time.localtime())
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(time.strptime("2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"))
    print(time.mktime(time.strptime("2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")))
    print(time.sleep(1))
    print(time.perf_counter())
    print(time.process_time())
    print(time.monotonic())
    print(time.asctime())


import logging


# 测试LOGGING模块
def test_logging():
    logging.basicConfig(filename="logs/log.log", level=logging.NOTSET,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")
    logging.fatal("fatal")


import random


# 测试RANDOM模块
def test_random():
    print(random.randint(1, 10))
    print(random.uniform(1, 10))
    print(random.choice([1, 2, 3, 4, 5]))
    print(random.sample([1, 2, 3, 4, 5], 3))
    print(random.shuffle([1, 2, 3, 4, 5]))
    print(random.random())
    print(random.randrange(1, 100, 2))


if __name__ == "__main__":
    test_random()
