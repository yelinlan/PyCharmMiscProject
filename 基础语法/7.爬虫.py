import requests


# 测试requests
def test_requests():
    url = "https://www.baidu.com"
    response = requests.get(url)
    print(response)
    # print(response.text )
    print(response.content.decode())


if __name__ == '__main__':
    url = "https://i2.hdslb.com/bfs/archive/4730097e10a79e46ea66593fd642e5d64ae37e34.jpg"
    response = requests.get(url)
    with open("resources/ayaka.jpg", "wb") as f:
        f.write(response.content)
