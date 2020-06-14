# -*- coding = utf-8 -*-
# @Time : 6/12/20 11:54 PM
# @Author : Sean Zhang
# @File : testBS4.py
# @Software : PyCharm

# BS will change HTML to a tree model. Every node is a python object.
# -tag
# -navigableString
# -beautiful soup
# -comment

from bs4 import BeautifulSoup

# Tag
file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")  # 解析文档，指定解析器
print(bs.title)
print(bs.a)
# Will return a bs.tag type element and it can only get the first one it found.

# If you want a string
print(bs.a.string)  # NavigableString
print(bs.a.attrs)  # Get a dictionary of all the attributes in a tag

# If you want to entire doc
print(bs.name)  # return the document type
print(bs)  # You will get entire  document

# Comment
print(bs.a.string)  # It is class bs4.element.Comment
# There is a special NavigableString
# But it ignores the comments in html file when it prints.

# -----------------------------------------------------

# Document Enumarate
print(bs.head.contents)  # It will give you the list of head elements
print(bs.head.contents[1])  # return the first meta
# Google Tree Model


# Document Searching

# (1) find_all()
# String Match
t_list = bs.find_all("a")  # return all the a tags in a list.
# Regularization Search
import re

t_list = bs.find_all(re.compile("a"))  # return all the tags and their content containing a.


# Method
def name_exists(tag):
    return tag.has_attr("name")


t_list = bs.find_all(name_exists)

# (2) kwargs
t_list = bs.find_all(id="head")
print(t_list)
t_list = bs.find_all(class_="True")
t_list = bs.find_all(href="True")

# (3) Text Parameter
t_list = bs.find_all(text=["baidu.com", "news"])
t_list = bs.find_all(text=re.compile("\d"))  # Find all the elements containing decimal type
t_list = bs.find_all(text=["baidu.com", "news"], limit=3)  # only return first 3.

# css find
# bs.select("title")  # search from tag
# bs.select(".mnav")  # Class name
# bs.select("#u1")  # ID
# bs.select("a[class='bri']")  # attribute  (a tag with attribute bri)
# bs.select("head > title > title")  # search according to  the parent-child structure. (children tag)
# t_list  = bs.select(".mnav ~ .bri") #Brother tag
# print(t_list[0].get_text())

