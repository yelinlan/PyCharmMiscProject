# coding=utf-8
import base64
import hashlib
import json
import random
import re
import time
from re import findall

import numpy as np
import requests
from fake_useragent import UserAgent
from lxml import etree
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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


def test24():
    page_url = "https://spiderbuf.cn/web-scraping-practice/scraping-form-rpa"
    html = requests.get(page_url,
                        headers={"User-Agent": UserAgent().random, 'Referer': 'https://spiderbuf.cn/list'}).text
    root = etree.HTML(html)
    print(root.xpath('//form/div/label[@for="username"]/text()')[0],
          root.xpath('//form/div/input[@name="username"]')[0].attrib["value"])
    print(root.xpath('//form/div/label[@for="password"]/text()')[0],
          root.xpath('//form/div/input[@name="password"]')[0].attrib["value"])
    print(root.xpath('//form/div/label[@for="email"]/text()')[0],
          root.xpath('//form/div/input[@name="email"]')[0].attrib["value"])
    print(root.xpath('//form/div/label[@for="website"]/text()')[0],
          root.xpath('//form/div/input[@name="website"]')[0].attrib["value"])
    print(root.xpath('//form/div/label[@for="date"]/text()')[0],
          root.xpath('//form/div/input[@name="date"]')[0].attrib["value"])
    print(root.xpath('//form/div/label[@for="time"]/text()')[0],
          root.xpath('//form/div/input[@name="time"]')[0].attrib["value"])
    number_ = root.xpath('//form/div/input[@name="number"]')[0]
    print(root.xpath('//form/div/label[@for="number"]/text()')[0],
          number_.attrib["value"] if "value" in number_.attrib else "")
    range_ = root.xpath('//form/div/input[@name="range"]')[0]
    print(root.xpath('//form/div/label[@for="range"]/text()')[0],
          range_.attrib["value"] if "value" in range_.attrib else "")
    color_ = root.xpath('//form/div/input[@name="color"]')[0]
    print(root.xpath('//form/div/label[@for="color"]/text()')[0],
          color_.attrib["value"] if "value" in color_.attrib else "")
    search_ = root.xpath('//form/div/input[@name="search"]')[0]
    print(root.xpath('//form/div/label[@for="search"]/text()')[0],
          search_.attrib["value"] if "value" in search_.attrib else "")
    print(root.xpath('//form/div/label[@for="textarea"]/text()')[0],
          root.xpath('//form/div/textarea[@name="textarea"]')[0].text)
    print(root.xpath('//form/div/label[@for="gender"]/text()')[0],
          root.xpath('//form/div/input[@name="gender" and @checked="true"]')[0].attrib["value"])
    interest = root.xpath('//form/div/input[@name="interest" and @checked]')
    print(root.xpath('//form/div/label[@for="interest"]/text()')[0],
          ",".join([item.attrib["value"] for item in interest]))
    print(root.xpath('//form/div/label[@for="country"]/text()')[0],
          root.xpath('//form/div/select/option[@selected]')[0].text)
    print(root.xpath('//form/div/p/text()')[0], " | ".join(root.xpath('//form/div/ul/li/a/text()')))


def test25():
    page_url = "https://spiderbuf.cn/web-scraping-practice/random-css-classname#google_vignette"
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
    root = etree.HTML(html)
    divs = root.xpath('//div[@class="FlDdlN" or @class="makOPE"]')
    for div in divs:
        print(div.xpath('string(.)').strip())


def test26():
    page_url = "https://spiderbuf.cn/web-scraping-practice/scraper-practice-c01"
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random
        , 'Referer': 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c01'}).text
    root = etree.HTML(html)
    divs = root.xpath('//li/a[contains(text(),"mnist")]')
    href_ = "https://spiderbuf.cn" + divs[0].attrib["href"]
    html1 = requests.get(href_, headers={"User-Agent": UserAgent().random
        , 'Referer': 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c01'
        ,
                                         'Cookie': '_ga=GA1.1.1615478358.1761312911; __cgf3t=G0gzgFKDRlLtmZH7NrzqOb1x4pek1xNQk12KKc4g21Y-1731624199; __gads=ID=f82407b378a1ce86:T=1761312909:RT=1761827398:S=ALNI_Maz3g1CvkLYyj5ZGiOwDwHpTyunXQ; __gpi=UID=000011a858720406:T=1761312909:RT=1761827398:S=ALNI_MYPrE9_2n-b1sLIQvWujnhtcJb7xQ; __eoi=ID=a01ab92a79a46f70:T=1761312909:RT=1761827398:S=AA-Afja7VCRfR75kLDj7Eg_SqCA8; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22d48a62e3-c494-4579-9f0f-e8f2022f2271%5C%22%2C%5B1761735673%2C853000000%5D%5D%22%5D%5D%5D; FCNEC=%5B%5B%22AKsRol99oM-NxTAg0NwEAnpV5nAB1hr5C9pSwI7giGi891Ofh-cl45Xbs1xP_962V-0-nWM77veT8SEPrNS_4h-jnReD3agfnmC49S7XBcMAQwYDHopHUlbW8iu6j402F61A-fYPHTanzkgFRwQXHDNIDMdLrHgaNQ%3D%3D%22%5D%5D; _ga_7B42BKG1QE=GS2.1.s1761822496$o6$g1$t1761827545$j47$l0$h0'}).text
    analysis_html(html1, "//table[@class='table']/thead/tr/th", "//table[@class='table']/tbody/tr")


def test27():
    page_url = "https://spiderbuf.cn/web-scraping-practice/scraper-practice-c02"
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random
        , 'Referer': 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c01'}).text
    findall = re.findall("const encryptedData = \"(.+)\";", html)[0]
    list = json.loads(base64.b64decode(findall).decode())
    print("出发地", "目的地", "票价")
    for item in list["flights"]:
        print(item["from"], item["to"], item["price"])


def test28():
    width_list = []
    for page_num in range(1, 6):
        print(f"正在爬取第{page_num}页")
        random_value = random.randint(2000, 10000)
        timestamp = int(time.time())
        xorResult = page_num ^ timestamp
        hash_value = hashlib.md5(f"{xorResult}{timestamp}".encode('utf-8')).hexdigest()

        data = {
            "xorResult": xorResult,
            'random': random_value,
            "timestamp": timestamp,
            "hash": hash_value
        }
        page_url = "https://spiderbuf.cn/web-scraping-practice/scraper-practice-c03"
        html = requests.post(page_url, headers={"User-Agent": UserAgent().random
            , 'Referer': 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c03'
            ,
                                                'Cookie': '_ga=GA1.1.1615478358.1761312911; __cgf3t=G0gzgFKDRlLtmZH7NrzqOb1x4pek1xNQk12KKc4g21Y-1731624199; __gads=ID=f82407b378a1ce86:T=1761312909:RT=1761829624:S=ALNI_Maz3g1CvkLYyj5ZGiOwDwHpTyunXQ; __gpi=UID=000011a858720406:T=1761312909:RT=1761829624:S=ALNI_MYPrE9_2n-b1sLIQvWujnhtcJb7xQ; __eoi=ID=a01ab92a79a46f70:T=1761312909:RT=1761829625:S=AA-Afja7VCRfR75kLDj7Eg_SqCA8; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22d48a62e3-c494-4579-9f0f-e8f2022f2271%5C%22%2C%5B1761735673%2C853000000%5D%5D%22%5D%5D%5D; FCNEC=%5B%5B%22AKsRol9niu3ffqhe1knaof9r6Y1qk26PGDZ0QJ2P7Xcg5sslst61xMAxJtZUR0s85ngiqM9qRtUuXJxlPlcc0Tk-Z4evrmOisiz7NAovXKJaoZtWvKcnVqpdg5gfqY_ESQX6HrnNlKExXF1b_4pcMUR89UzZIX0RIA%3D%3D%22%5D%5D; _ga_7B42BKG1QE=GS2.1.s1761822496$o6$g1$t1761829748$j35$l0$h0'
                                                }
                             , json=data).text
        print(html)
        json_data = json.loads(html)
        for item in json_data:
            width_list.append(item["sepal_width"])
    print(width_list)
    print(f"平均值：{sum(width_list) / len(width_list)}")
    print(f"最大值：{max(width_list)}")
    print(f"最小值：{min(width_list)}")
    print(f"总和: {sum(width_list)}")


def test29():
    page_url = "https://spiderbuf.cn/static/js/c04/lhY3nm7.min.js"
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random
        , 'Referer': 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c01'}).text
    print(html)
    findall1 = re.findall("'from','(.+)','webdriver'", html)[0]
    list2 = json.loads(base64.b64decode(findall1).decode()[:-2])
    # 标题
    print("标题", "内容", "阅读数", "点赞数", "分享数", "评论数")
    view_comment = []
    for item in list2:
        print(item["title"], item["content"], item["reads"], item["likes"], item["shares"], item["comments"])
        view_comment.append(int(item["reads"]) + int(item["comments"]))

    print("平均阅读数：", sum(view_comment) / len(view_comment))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service("./chrome/chromedriver.exe")

def test30():
    base_url = 'https://spiderbuf.cn/web-scraping-practice/scraper-practice-c04'
    if __name__ == '__main__':
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

        options.add_argument('--disable-blink-features=AutomationControlled')  # 改变navigator.webdriver 属性值

        client = webdriver.Chrome(options=options, service=service)
        print('Getting page...')
        client.get(base_url)
        time.sleep(3)

        # 模拟用户在页面上滑动光标
        actionChains = ActionChains(client)
        actionChains.move_by_offset(430, 330)
        for i in range(20):
            step = random.randint(1, 10)
            actionChains.move_by_offset(step, step).perform()

        checkbox = client.find_element(By.ID, 'captcha')
        checkbox.click()
        print('Checkbox clicked...')
        time.sleep(3)
        html = client.page_source
        # print(html)
        client.quit()
        root = etree.HTML(html)
        items = root.xpath('//div[@class="stats"]')
        results = []
        for item in items:
            spans = item.xpath('.//span')
            s = ''.join(spans[3].xpath('string(.)'))
            results.append(int(re.findall('\d+', spans[0].text)[0]) + int(''.join(re.findall('\d+', s))))
        print(np.average(results))


test30()
