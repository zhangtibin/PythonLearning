import urllib.request
from bs4 import BeautifulSoup
import re
import csv
import chardet
import ssl

csvFile = open("/Users/zhangtibin/Downloads/数据存储/JIMU.csv", 'w', newline="")
writer = csv.writer(csvFile)
writer.writerow(("标题", "标号", "方式", "年化利率", "项目期限"))

pageIndex = 1
totalPage = 10
while pageIndex < totalPage:
    url = "https://box.jimu.com/Project/List?rate=&guarantee=&range=&page="+str(pageIndex)+"&category=&status="
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    #获取对应标签
    storeInfoList = soup.findAll(attrs={"class": "invest-item"})
    #获取每页多少条
    offset = len(storeInfoList)
    for storeIno in storeInfoList:
        productTitle = storeIno.find("invest-item-title").find("title")
        bidNum = storeIno.find("invest-item-title").find("subtitle")
        interstStyle = storeIno.find("invest-item-subtitle").find("span").get_text()
        writer.writerow((productTitle, bidNum, interstStyle))
    pageIndex = pageIndex + 1
csvFile.close()

