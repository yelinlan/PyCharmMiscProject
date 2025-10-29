# coding=utf-8
from re import findall

import requests
from fake_useragent import UserAgent
from lxml import etree


def test01():
    url = 'https://spiderbuf.cn/web-scraping-practice/requests-lxml-for-scraping-beginner'
    html = requests.get(url).text
    root = etree.HTML(html)
    thds = root.xpath("/html/body/main/div[2]/table/thead/tr/th")
    print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), thds))))
    trs = root.xpath("/html/body/main/div[2]/table/tbody/tr")
    for tr in trs:
        tds = tr.xpath('./td')
        print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), tds))))


def test02():
    url = 'https://spiderbuf.cn/web-scraping-practice/scraper-http-header'
    html = requests.get(url, headers={"User-Agent": UserAgent().random}).text
    root = etree.HTML(html)
    thds = root.xpath("/html/body/main/div[2]/table/thead/tr/th")
    print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), thds))))
    trs = root.xpath("/html/body/main/div[2]/table/tbody/tr")
    for tr in trs:
        tds = tr.xpath('./td')
        print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), tds))))


def test03():
    url = 'https://spiderbuf.cn/web-scraping-practice/lxml-xpath-advanced'
    html = requests.get(url, headers={"User-Agent": UserAgent().random}).text
    root = etree.HTML(html)
    thds = root.xpath("/html/body/main/div[2]/table/thead/tr/th")
    print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), thds))))
    trs = root.xpath("/html/body/main/div[2]/table/tbody/tr")
    for tr in trs:
        tds = tr.xpath('./td')
        print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), tds))))


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
        root1 = etree.HTML(html1)
        thds1 = root1.xpath("/html/body/main/div[2]/table/thead/tr/th")
        print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), thds1))))
        trs1 = root1.xpath("/html/body/main/div[2]/table/tbody/tr")
        for tr in trs1:
            tds1 = tr.xpath('./td')
            print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), tds1))))


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
    root = etree.HTML(html)
    thds = root.xpath("/html/body/main/div[2]/table/thead/tr/th")
    print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), thds))))
    trs = root.xpath("/html/body/main/div[2]/table/tbody/tr")
    for tr in trs:
        tds = tr.xpath('./td')
        print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), tds))))


def test09():
    url = 'https://spiderbuf.cn/web-scraping-practice/scraper-login-username-password/login'
    html = requests.post(url, headers={"User-Agent": UserAgent().random}
                         , data={"username": "admin", "password": "123456"}).content.decode()
    root = etree.HTML(html)
    thds = root.xpath("/html/body/main/div[2]/table/thead/tr/th")
    print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), thds))))
    trs = root.xpath("/html/body/main/div[2]/table/tbody/tr")
    for tr in trs:
        tds = tr.xpath('./td')
        print(" | ".join(list(map(lambda x: x.xpath('string(.)').strip(), tds))))


test09()
