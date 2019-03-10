import urllib.request
from bs4 import BeautifulSoup
import re
import csv
import chardet
import ssl

csvFile = open("/Users/zhangtibin/Downloads/数据存储/TPY.csv", "w", newline="")
writer = csv.writer(csvFile)
#writer.writerow(("店名称", "描述", "地址", "部门经理", "联系电话"))
writer.writerow(("店名称", "地址", "联系电话"))

total = 0
sumPage = 9
pageIndex = 1
while (pageIndex <= sumPage):

    url = 'http://www.pacific.sh.cn/shows.asp?base_id=2&second_id=&third_id=&pageIndex='+ str(pageIndex)
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    #获取页面相应的标签
    storeInfoList = soup.findAll(attrs={"class": "txt"})
    #本页店面的数量
    storeNum = len(storeInfoList)
    print('本页店面的数量' +  str(storeNum))

    for storeInfo in storeInfoList:
        storeName = storeInfo.find("h6").find("a").get_text()
        #storeIntro = storeInfo.find(attrs={"class": "intro"}).get_text()
        storeBaseInfo = storeInfo.findAll("p")
        storeAddress = storeBaseInfo[1].get_text()
        #storeManager = storeBaseInfo[3].get_text()
        storeMobile = storeBaseInfo[4].get_text()
        #writer.writerow((storeName, str(storeIntro.encode('utf-8')), storeAddress.encode('utf-8')[5:], storeManager.encode('utf-8')[5:],storeMobile.encode('utf-8')[5:]))
        writer.writerow((storeName, storeAddress[5:], storeMobile[5:]))

    pageIndex = pageIndex + 1
    total = total + storeNum



csvFile.close()

print(total)
