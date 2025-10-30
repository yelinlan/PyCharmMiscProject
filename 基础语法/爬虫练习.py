# coding=utf-8
import base64
import re
import time
from re import findall

import requests
from fake_useragent import UserAgent
from lxml import etree


def test01():
    url = 'https://spiderbuf.cn/web-scraping-practice/requests-lxml-for-scraping-beginner'
    html = requests.get(url).text
    analysis_html(html)


def analysis_html(html: str, thead="/html/body/main/div[2]/table/thead/tr/th"
                  , tbody="/html/body/main/div[2]/table/tbody/tr"):
    root = etree.HTML(html)
    thds = root.xpath(thead)
    print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), thds))))
    trs = root.xpath(tbody)
    for tr in trs:
        tds = tr.xpath('./td')
        print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), tds))))


def test02():
    url = 'https://spiderbuf.cn/web-scraping-practice/scraper-http-header'
    html = requests.get(url, headers={"User-Agent": UserAgent().random}).text
    analysis_html(html)


def test03():
    url = 'https://spiderbuf.cn/web-scraping-practice/lxml-xpath-advanced'
    html = requests.get(url, headers={"User-Agent": UserAgent().random}).text
    analysis_html(html)


def test04():
    url = 'https://spiderbuf.cn/web-scraping-practice/web-pagination-scraper'
    html = requests.get(url, headers={"User-Agent": UserAgent().random}).text
    root = etree.HTML(html)
    total = root.xpath("/html/body/main/div[2]/div/nav/ul/li[1]/span");
    page_num = findall(r'\d+', total[0].text)

    page_url = "https://spiderbuf.cn/web-scraping-practice/web-pagination-scraper?pageno=%d"

    for i in range(1, int(page_num[0]) + 1):
        print("正在爬取第%d页..." % i)
        html1 = requests.get(page_url % i, headers={"User-Agent": UserAgent().random}).text
        analysis_html(html)


def test05():
    url = 'https://spiderbuf.cn/web-scraping-practice/scraping-images-from-web'
    html = requests.get(url, headers={"User-Agent": UserAgent().random}).text
    root = etree.HTML(html)
    imgs = root.xpath("//img/@src")
    for img in imgs:
        img_url = "https://spiderbuf.cn" + img
        img_data = requests.get(img_url, headers={"User-Agent": UserAgent().random}).content
        with open("resources/%s" % img.split('/')[-1], "wb") as f:
            f.write(img_data)


def test06():
    url = 'https://spiderbuf.cn/web-scraping-practice/inner'
    html = requests.get(url, headers={"User-Agent": UserAgent().random}).text
    root = etree.HTML(html)
    thds = root.xpath("/html/body/table/thead/tr/th")
    print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), thds))))
    trs = root.xpath("/html/body/table/tbody/tr")
    for tr in trs:
        tds = tr.xpath('./td')
        print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), tds))))


def test08():
    url = 'https://spiderbuf.cn/web-scraping-practice/scraper-via-http-post'
    html = requests.post(url, headers={"User-Agent": UserAgent().random}
                         , data={"level": 8}).content.decode()
    analysis_html(html)


def test09():
    url = 'https://spiderbuf.cn/web-scraping-practice/scraper-login-username-password/login'
    html = requests.post(url, headers={"User-Agent": UserAgent().random}
                         , data={"username": "admin", "password": "123456"}).content.decode()
    analysis_html(html)


def test10():
    url = 'https://spiderbuf.cn/web-scraping-practice/web-scraping-with-captcha/list'
    html = requests.get(url, headers={"User-Agent": UserAgent().random,
                                      "Cookie": "admin=ffda8e1c2842eef729b5140c6e974b8e"}
                        , data={"username": "admin", "password": "123456"}).content.decode()
    analysis_html(html)


def test11():
    page_url = "https://spiderbuf.cn/web-scraping-practice/scraping-random-pagination"
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
    root = etree.HTML(html)
    page_url_list = root.xpath("//ul/li/a/@href")

    for (index, item) in enumerate(page_url_list, 1):
        print("正在爬取第%d页..." % index)
        html = requests.get("https://spiderbuf.cn" + item, headers={"User-Agent": UserAgent().random}).text
        analysis_html(html)


def test12():
    page_url = "https://spiderbuf.cn/web-scraping-practice/user-agent-referrer"
    html = requests.get(page_url,
                        headers={"User-Agent": UserAgent().random, 'Referer': 'https://spiderbuf.cn/list'}).text
    root = etree.HTML(html)
    divList = root.xpath("/html/body/main/div[2]/div[2]/div/div")
    for div in divList:
        print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), div))))


def test13():
    page_url = "https://spiderbuf.cn/web-scraping-practice/scraping-css-confuse-offset"
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
    root = etree.HTML(html)
    divList = root.xpath("/html/body/main/div[2]/div/div/div")
    for div in divList:
        outputStr = []
        for (index, item) in enumerate(div, 1):
            temp = item.xpath('string(.)').strip()
            if index == 1 or index == 2:
                outputStr.append(temp[1: 2] + temp[0:1] + temp[2:])
                continue
            else:
                outputStr.append(temp)
        print(" | ".join(list(outputStr)))


def test14():
    page_url = "https://spiderbuf.cn/web-scraping-practice/scraping-images-base64"
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
    root = etree.HTML(html)
    img = root.xpath("/html/body/main/div[2]/div/div[2]/div/img/@src")
    print(img)
    for item in img:
        # item 是获取到的base64字符串
        item = item.replace('data:image/png;base64,', '')
        str_bytes = item.encode('raw_unicode_escape')  # str 转 bytes
        decoded = base64.b64decode(str_bytes)
        img = open('resources/n02.png', 'wb')
        img.write(decoded)
        img.close()


def test15():
    page_url = "https://spiderbuf.cn/web-scraping-practice/scraper-bypass-request-limit/18"
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
    root = etree.HTML(html)
    divList = root.xpath("/html/body/main/div[2]/div/div/div/nav/ul/li/a/@href")
    for (index, item) in enumerate(divList, 1):
        print("正在爬取第%d页..." % index)
        html = requests.get("https://spiderbuf.cn" + item, headers={"User-Agent": UserAgent().random}).text
        analysis_html(html, "/html/body/main/div[2]/div/div/table/thead/tr/th"
                      , "/html/body/main/div[2]/div/div/table/tbody/tr")
        time.sleep(1)


def test16():
    page_url = "https://spiderbuf.cn/web-scraping-practice/scraping-douban-movies-xpath-advanced"
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
    root = etree.HTML(html)
    movies = root.xpath("/html/body/div/div[@style='margin-top: 10px;']")
    for (index, movie) in enumerate(movies, 1):
        if index % 2 == 1:
            print("正在爬取第%d部电影..." % (index / 2 + 1))
            print("电影名称:", movie.xpath("./div/h2")[0].text)
            print("豆瓣评分:",
                  movie.xpath("./div/div/span[contains(text(),'豆瓣电影评分:')]/following::text()[1]")[0])
            print("导演:", movie.xpath("./div/div/span/span[contains(text(),'导演')]/following::text()")[1:3])
            print("编剧:", movie.xpath("./div/div/span/span[contains(text(),'编剧')]/following::text()")[1:3])
            print("主演:", movie.xpath("./div/div/span/span[contains(text(),'主演')]/following::text()")[1:3])
            print("类型:", movie.xpath("./div/div/span/span[contains(text(),'类型')]/following::text()")[0:2])
            print("制片国家/地区:",
                  movie.xpath("./div/div/span/span[contains(text(),'制片国家/地区:')]/following::text()")[0:2])
            print("语言:", movie.xpath("./div/div/span/span[contains(text(),'语言:')]/following::text()")[0:2])
            print("上映日期:",
                  movie.xpath("./div/div/span/span[contains(text(),'上映日期:')]/following::text()")[0:2])
            print("片长:", movie.xpath("./div/div/span/span[contains(text(),'片长:')]/following::text()")[0])
            print("又名:", movie.xpath("./div/div/span/span[contains(text(),'又名:')]/following::text()")[0:2])
            print("IMDb:", movie.xpath("./div/div/span[contains(text(),'IMDb:')]/following::text()")[0])
        else:
            print("简介:", movie.xpath("./div/text()")[0])


def test17():
    page_url = "https://spiderbuf.cn/web-scraping-practice/scraping-scroll-load"
    i = 0
    while True:
        i = i + 1
        html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
        root = etree.HTML(html)
        movies = root.xpath("//div[@style='margin-top: 10px;']")
        for (index, movie) in enumerate(movies, 1):
            if index % 2 == 1:
                print("正在爬取第%d页，第%d部电影..." % (i, index / 2 + 1))
                print("电影名称:", movie.xpath("./div/h2")[0].text)
                print("豆瓣评分:",
                      movie.xpath("./div/div/span[contains(text(),'豆瓣电影评分:')]/following::text()[1]")[0])
                print("导演:", movie.xpath("./div/div/span/span[contains(text(),'导演')]/following::text()")[1:3])
                print("编剧:", movie.xpath("./div/div/span/span[contains(text(),'编剧')]/following::text()")[1:3])
                print("主演:", movie.xpath("./div/div/span/span[contains(text(),'主演')]/following::text()")[1:3])
                print("类型:", movie.xpath("./div/div/span/span[contains(text(),'类型')]/following::text()")[0:2])
                print("制片国家/地区:",
                      movie.xpath("./div/div/span/span[contains(text(),'制片国家/地区:')]/following::text()")[0:2])
                print("语言:", movie.xpath("./div/div/span/span[contains(text(),'语言:')]/following::text()")[0:2])
                print("上映日期:",
                      movie.xpath("./div/div/span/span[contains(text(),'上映日期:')]/following::text()")[0:2])
                print("片长:", movie.xpath("./div/div/span/span[contains(text(),'片长:')]/following::text()")[0])
                print("又名:", movie.xpath("./div/div/span/span[contains(text(),'又名:')]/following::text()")[0:2])
                print("IMDb:", movie.xpath("./div/div/span[contains(text(),'IMDb:')]/following::text()")[0])
            else:
                print("简介:", movie.xpath("./div/text()")[0])
        if not root.xpath("//div[@hidden]/text()"):
            break
        page_url = "https://spiderbuf.cn/web-scraping-practice/scraping-scroll-load/" + \
                   root.xpath("//div[@hidden]/text()")[0]


def test18():
    page_url = "https://spiderbuf.cn/web-scraping-practice/javascript-confuse-encrypt-reverse"
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
    print(html)
    root = etree.HTML(html)
    divList = root.xpath("/html/body/main/div[2]/div/div/div/nav/ul/li/a/@href")
    for (index, item) in enumerate(divList, 1):
        print("正在爬取第%d页..." % index)
        html = requests.get("https://spiderbuf.cn" + item, headers={"User-Agent": UserAgent().random}).text
        analysis_html(html, "/html/body/main/div[2]/div/div/table/thead/tr/th"
                      , "/html/body/main/div[2]/div/div/table/tbody/tr")
        time.sleep(1)


def test19():
    page_url = "https://spiderbuf.cn/static/js/h04/udSL29.js"
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
    start = html.index("=") + 1
    end = html.index(";")
    list1 = eval(html[start:end])
    print(" | ".join(list1[0].keys()))
    for item in list1:
        print(" | ".join(list(map(lambda x: str(x), item.values()))))


def test20():
    page_url = "https://spiderbuf.cn/web-scraping-practice/javascript-reverse-timestamp/api/MTc2MTc5NTIzOCxhZjg4OWY0ZTJjNTg2MDAwMjRhZDYwOWJkY2Q5YjA3MQ=="
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
    list1 = eval(html)
    print(" | ".join(list1[0].keys()))
    for item in list1:
        print(" | ".join(list(map(lambda x: str(x), item.values()))))


def test21():
    page_url = "https://spiderbuf.cn/web-scraping-practice/selenium-fingerprint-anti-scraper/api/MTc2MTc5NTc3NSxjY2E4NTlhMTQ2M2IwNDYzZDRmYjY2OTFiZWUyZDFiMA=="
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
    list1 = eval(html)
    print(" | ".join(list1[0].keys()))
    for item in list1:
        print(" | ".join(list(map(lambda x: str(x), item.values()))))


def test22():
    page_url = "https://spiderbuf.cn/web-scraping-practice/css-pseudo-elements"
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
    # 正则匹配 获取伪元素样式
    result = re.findall(r""".([a-z]{6}::before|[a-z]{6}::after) {\s+content: "(\d)";\s+}""", html)
    # 转成map
    result = dict(result)
    root = etree.HTML(html)
    movies = root.xpath("/html/body/div/div[@style='margin-top: 10px;']")
    for (index, movie) in enumerate(movies, 1):
        if not movie.xpath("./div[contains(text(),'简介：')]"):
            # 评分 从内存获取分数
            score = movie.xpath("./div/div/span[@class]")[0].attrib["class"].split(" ")
            print("电影名称:", movie.xpath("./div/h2")[0].text)
            print("豆瓣评分:", result[score[0] + "::before"] + "." + result[score[1] + "::after"])
            print("导演:", movie.xpath("./div/div/span/span[contains(text(),'导演')]/following::text()")[1:3])
            print("编剧:", movie.xpath("./div/div/span/span[contains(text(),'编剧')]/following::text()")[1:3])
            print("主演:", movie.xpath("./div/div/span/span[contains(text(),'主演')]/following::text()")[1:3])
            print("类型:", movie.xpath("./div/div/span/span[contains(text(),'类型')]/following::text()")[0:2])
            print("制片国家/地区:",
                  movie.xpath("./div/div/span/span[contains(text(),'制片国家/地区:')]/following::text()")[0:2])
            print("语言:", movie.xpath("./div/div/span/span[contains(text(),'语言:')]/following::text()")[0:2])
            print("上映日期:",
                  movie.xpath("./div/div/span/span[contains(text(),'上映日期:')]/following::text()")[0:2])
            print("片长:", movie.xpath("./div/div/span/span[contains(text(),'片长:')]/following::text()")[0])
            print("又名:", movie.xpath("./div/div/span/span[contains(text(),'又名:')]/following::text()")[0:2])
            print("IMDb:", movie.xpath("./div/div/span[contains(text(),'IMDb:')]/following::text()")[0])
        else:
            print("简介:", movie.xpath("./div/text()")[0])


def test23():
    class_map = {'sprite abcdef': '0',
                 'sprite ghijkl': '1',
                 'sprite mnopqr': '2',
                 'sprite uvwxyz': '3',
                 'sprite yzabcd': '4',
                 'sprite efghij': '5',
                 'sprite klmnop': '6',
                 'sprite qrstuv': '7',
                 'sprite wxyzab': '8',
                 'sprite cdefgh': '9'}
    page_url = "https://spiderbuf.cn/web-scraping-practice/css-sprites"
    html = requests.get(page_url,
                        headers={"User-Agent": UserAgent().random, 'Referer': 'https://spiderbuf.cn/list'}).text
    root = etree.HTML(html)
    divList = root.xpath("/html/body/main/div[2]/div[2]/div/div")
    for div in divList:
        ls = []
        for item in div:
            content = item.xpath('string(.)').strip()
            if "企业估值" in content:
                s = [class_map[item.attrib["class"]] for item in div.xpath("./p/span[@class]")]
                ls.append(content + "".join(s))
            else:
                ls.append(content)
        print(" | ".join(ls))


test23()
