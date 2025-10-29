# coding=utf-8
import base64
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
    html = requests.get(page_url, headers={"User-Agent": UserAgent().random}).text
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
    # score = root.xpath("/html/body/div[1]/div/div/div/span[contains(text(),'豆瓣电影评分')]/following::text()[1]")
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


test16()
