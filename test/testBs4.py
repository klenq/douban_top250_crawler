# @Time : 2021/12/10 11:10
# @Author : klenq
# @File : testBs4.py
# @Software : PyCharm


from bs4 import BeautifulSoup
import re
file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")

# 标签及其内容
# print(bs.title)
# print(bs.a)
#
# print(bs.title.string)
#
# print(bs.a.attrs)
#
# print(bs.a.text)

# 文档遍历
# print(bs.head.contents[1])


# 文档搜索

# 字符串过滤, 查找与字符串完全匹配的内容
# t_list = bs.findAll("a")

# 正则表达式 使用search()
# t_list = bs.findAll(re.compile("a"))

# 函数
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)

# 参数
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)


# 文本参数
# t_list = bs.find_all(text = "hao123")


# limit 参数
# t_list = bs.find_all("a",limit=3)

# css 选择器
t_list = bs.select('title')

t_list = bs.select('#head')

t_list = bs.select("a[class='bri']")

t_list = bs.select("head > title")

t_list = bs.select(".mnav ~ .bri")



print(t_list)



