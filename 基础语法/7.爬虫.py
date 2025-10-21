from urllib.parse import quote, unquote

import requests
from fake_useragent import UserAgent


# 测试requests
def test_requests():
    url = "https://www.baidu.com"
    response = requests.get(url)
    print(response)
    # response.encoding = "utf-8"
    # print(response.text )
    print(response.content.decode())


def test_jpg():
    url = "https://i2.hdslb.com/bfs/archive/4730097e10a79e46ea66593fd642e5d64ae37e34.jpg"
    response = requests.get(url)
    with open("resources/ayaka.jpg", "wb") as f:
        f.write(response.content)


def test_header():
    url = "https://www.baidu.com"
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"})
    print(len(response.content.decode()))


def test_fake_agent():
    url = "https://www.baidu.com"
    response = requests.get(url, headers={"User-Agent": UserAgent().random})
    print(len(response.content.decode()))


def test_url_code():
    print(unquote("https://www.baidu.com/s?ie=UTF-8&wd=%E8%B1%86%E5%8C%85"))
    print(quote("豆包"))


def test_params():
    url = "https://www.baidu.com"
    s = input("请输入搜索内容：")
    response = requests.get(url, headers={"User-Agent": UserAgent().random}, params={"wd": s})
    print(response.content.decode())


def test_tieba():
    s = "犬夜叉"

    url = f"https://so.gamersky.com/?s={s}"

    response = requests.get(url, headers={"User-Agent": UserAgent().random})
    with open("resources/tieba.html", "w", encoding="utf-8") as f:
        f.write(response.content.decode())

import json
def test_only_grammar():
    post1 = requests.post("https://item-statistics.gamersky.com/ad/statistics/event/report/online/5.0.0",
                          headers={"User-Agent": UserAgent().random}, data={},
                          proxies={"http": "http://127.0.0.1:8888"})
    json_data = json.loads(post1.content.decode())


if __name__ == '__main__':
    test_only_grammar()
