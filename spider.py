# @Time : 2021/12/9 20:09
# @Author : klenq
# @File : spider.py
# @Software : PyCharm

from bs4 import BeautifulSoup  # 网页解析
import re  # 正则表达式
import urllib.request, urllib.error  # 指定URL 获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 数据库


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页
    # 解析数据
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"

    # 保存数据
    # saveData(datalist,savepath)
    dbpath = "movie.db"
    # init_db(dbpath)
    saveData2DB(datalist, dbpath)
    # print(askURL(baseurl + "0"))


findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象, 表示规则(字符串模式), 非贪婪模式
findImgSrc = re.compile(r'<img alt=".*src="(.*?)"', re.S)  # re.S 让换行符包含再字符中
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def getData(baseurl):
    datalist = []
    # 解析数据
    for i in range(0, 10):  # 调用获取页面的信息函数, 共10次
        url = baseurl + str(i * 25)
        html = askURL(url)

        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串, 形成列表
            # 拿到了class属性为item的内容
            # print(item)
            data = []  # 一部电影的所有信息
            item = str(item)

            # 找链接
            data.append(findElement(findLink, item))
            data.append(findElement(findImgSrc, item))

            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')
            data.append(findElement(findRating, item))
            data.append(findElement(findJudge, item))
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")
            bd = findElement(findBd, item)
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉前后空格

            datalist.append(data)
    # print(datalist)
    return datalist


def findElement(re_expression, item):
    return re.findall(re_expression, item)[0]


# 得到指定url的网页内容
def askURL(url):
    headers = {  # 模拟头部信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    # 用户代理

    req = urllib.request.Request(url=url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


def saveData(datalist,savepath):
    # 保存数据
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接","影片中文名","影片外文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save(savepath)
    print("End")


def saveData2DB(datalist, dbpath):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            data[index] = '"'+data[index]+'"'
        sql = '''
            insert into movie250(
                info_link, pic_link, cname, ename, score, rated, introduction, info)
                values (%s)
        '''%",".join(data)
        cursor.execute(sql)
        conn.commit()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie250 
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        introduction text,
        info text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()



if __name__ == '__main__':
    # 程序执行时 调用函数
    main()
