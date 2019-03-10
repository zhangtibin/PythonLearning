# coding=utf-8
from selenium import webdriver
import time
from lxml import etree
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

"""
PEP8 Python编程规范
https://www.douban.com/note/134971609/

"""
# 获取浏览器驱动
driver = webdriver.Firefox()
driver.maximize_window()
webUrl = 'http://www.lovewzly.com/jiaoyou.html'
driver.get(webUrl)

# 等15秒，我来手动做一下筛选条件。，女性，21-30左右，学历本科，\
# 本来想通过js代码，来自动执行，但无奈对js真的不熟，也没有太多时间去整了，凑合看看.
time.sleep(15)

"""
下拉滚动条，从1开始到3结束 分2次加载完每页数据

"""
while True:

    for i in range(1, 20):
        height = 1000 * i  # 每次滑动20000像素
        strword = "window.scrollBy(0," + str(height) + ")"
        driver.execute_script(strword)
        time.sleep(3)

        s = etree.HTML(driver.page_source)
        selectors = s.xpath('//*[@id="hibox"]/table/tbody/tr/td/div')

        with open('内心读白.txt', 'a') as f:
            for selector in selectors:
                img = selector.xpath('./div[1]/img/@src')
                nick = selector.xpath('./div[2]/p[1]/span/text()')
                age = selector.xpath('./div[2]/p[2]/span[1]/text()')
                height = selector.xpath('./div[2]/p[2]/span[2]/text()')
                address = selector.xpath('./div[2]/p[2]/span[3]/text()')
                heart = selector.xpath('./div[2]/p[3]/text()')

                img = img[0] if len(img) > 0 else ''
                nick = nick[0] if len(nick) > 0 else ''
                age = age[0] if len(age) > 0 else ''
                height = height[0] if len(height) > 0 else ''
                address = address[0] if len(address) > 0 else ''
                heart = heart[0] if len(heart) > 0 else ''
                print(nick, age, height, address, heart, img)
                f.write(heart)
