import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.jianshu.com/")

reg = '<a class="title" target="_blank" href="(.*?)">(.*?)</a>[\n][\s]*'
reg += '<p class="abstract">[\n](.*)[\n][\s]*'
reg += '</p>[\n][\s]*<div class="meta">[\n][\s]*'
reg += '<a class="collection-tag" target="_blank" href="/c/.*?">(.*?)</a>[\n][\s]*'
reg += '<a target="_blank" href="/p/.*?">[\n][\s]*'
reg += '<i class="iconfont ic-list-read"></i> (.*)[\n]'
reg += '</a>[\s]*<a target="_blank" href="/p/.*?">[\n][\s]*'
reg += '<i class="iconfont ic-list-comments"></i> (.*)[\n]'
reg += '</a>[\s]*<span><i class="iconfont ic-list-like"></i> (.*)</span>[\n][\s]*'
reg += '<span><i class="iconfont ic-list-money"></i> (.*)</span>'

#当正则表达式过长时，我们选取这种方式将其分割

page = re.compile(reg)
artlist = re.findall(page,html)

for arts in artlist: #arts中包含了文件名，链接部分，阅读量等等
    for art in arts:
       if art.startswith("/p/"): #获取链接
         print "http://www.jianshu.com" + art
       else:
           print art