import os
from queue import Queue

a = 0


# 测试多线程 同步异步 join
def test_thread():
    # 是否同步
    isSynchronized = False
    import threading
    def run(n):
        for i in range(1000000):
            global a
            a += 1
        print("子线程" + n + " a=" + str(a))

    t1 = threading.Thread(target=run, args=("t1",))
    t2 = threading.Thread(target=run, args=("t2",))
    t1.start()
    if isSynchronized:
        t1.join()  # 等待t1执行完毕
    t2.start()
    if isSynchronized:
        t2.join()  # 等待t2执行完毕
    print("主线程")


# 测试多线程 同步异步 互斥锁
def test_mutex():
    import threading
    lock = threading.Lock()

    def run(n):
        lock.acquire()
        for i in range(1000000):
            global a
            a += 1
        lock.release()
        print("子线程" + n + " a=" + str(a))

    t1 = threading.Thread(target=run, args=("t1",))
    t2 = threading.Thread(target=run, args=("t2",))
    t1.start()
    t2.start()


def run(n):
    for i in range(1000000):
        global a
        a += 1
    print("子进程" + n + " a=" + str(a))


# 测试进程
def test_process():
    import multiprocessing

    p1 = multiprocessing.Process(target=run, args=("p1",))
    p2 = multiprocessing.Process(target=run, args=("p2",))
    p1.start()
    p2.start()
    print("p1.pid=" + str(p1.pid))
    print("p2.pid=" + str(p2.pid))
    print("主进程 a=" + str(os.getpid()))


# 测试队列 同步
def test_queue():
    import threading
    q = Queue()

    def put_elements(n):
        for i in range(1000):
            q.put(i)
            print("子线程" + n + " put " + str(i))

    def get_elements(n):
        for i in range(1000):
            q.get()
            print("子线程" + n + " get " + str(i))

    t1 = threading.Thread(target=put_elements, args=("t1",))
    t2 = threading.Thread(target=get_elements, args=("t2",))
    t1.start()
    t1.join()
    t2.start()
    t2.join()


# 测试协程 更轻量的线程，随意切换
def test_coroutine():
    import greenlet  # 协程 一个第三方的手动切换的框架
    def dance():
        print("跳舞开始")
        g2.switch()  # 切换到g2
        print("跳舞结束")

    def sing():
        print("唱歌开始")
        print("唱歌结束")
        g1.switch()  # 切换到g1

    g1 = greenlet.greenlet(dance)
    g2 = greenlet.greenlet(sing)
    g1.switch()  # 启动g1


# 测试协程 gevent
def test_gevent():
    import gevent
    def dance():
        print("跳舞开始")
        gevent.sleep(2)
        print("跳舞结束")

    def sing():
        print("唱歌开始")
        print("唱歌结束")
        gevent.sleep(3)

    g1 = gevent.spawn(dance)
    g2 = gevent.spawn(sing)
    gevent.joinall([g1, g2])
    print("主程序结束")


if __name__ == "__main__":
    test_gevent()
