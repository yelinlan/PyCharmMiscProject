# 测试读文件
def test_read_file():
    f = open("resources/古诗.txt", "r", encoding="utf-8")
    print(f.read())
    f.close()


# 测试写文件
def test_write_file():
    f = open("resources/记事本.txt", "w", encoding="utf-8")
    f.write("天朗气清，惠风和畅！\n")
    f.close()


# 测试追加文件
def test_append_file():
    f = open("resources/记事本.txt", "a", encoding="utf-8")
    f.write("渺沧海之一粟，羡长江之无穷！\n")
    f.close()


# 测试二进制文件
def test_read_binary_file():
    f = open("resources/死或生.jpg", "rb")
    print(f.read())
    f.close()


# 测试自动关闭
def test_with_file():
    with open("resources/死或生.jpg", "rb") as f:
        print(f.read())


# 测试复制图片
def test_copy_file():
    f = open("resources/死或生.jpg", "rb")
    with open("resources/死或生_copy.jpg", "wb") as f_copy:
        f_copy.write(f.read())
        f.close()

# 测试文件夹操作
def test_folder_operation():
    import os
    if os.path.exists("resources/死或生_copy.jpg"):
        os.remove("resources/死或生_copy.jpg")
    else:
        print("文件不存在")
        os.mkdir("resources/死或生")
        os.rename("resources/死或生", "resources/死或生1")
        print(os.listdir("resources"))
        print(os.path.exists("resources/死或生1"))
        os.rmdir("resources/死或生1")
        print(os.getcwd())

if __name__ == "__main__":
    test_folder_operation()
