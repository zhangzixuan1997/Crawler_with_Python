# -*- coding = utf-8 -*-
# @Time : 6/11/20 9:06 PM
# @Author : Sean Zhang
# @File : Spider.py
# @Software : PyCharm


from bs4 import BeautifulSoup
import re  # regularization
import urllib.request, urllib.error
import xlwt  # excel
import sqlite3

# find the link, image source, title, rate, number of rates, introduction of movie and movie related info.

findLink = re.compile(r'<a href="(.*?)">')  # less greedy re
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S ignores the \n, so \n in the link wont be ignored
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRate = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findNumOfRates = re.compile(r'<span>(\d*)人评价</span>')
findIntroOfMovie = re.compile(r'<span class="inq">(.*)</span>')
findContent = re.compile(r'<p class="">(.*?)</p>', re.S)


def getData(base_url):
    datalist = []
    for i in range(0, 10):
        url = base_url + str(i * 25)  # get the url for 250 movies here.
        html = askURL(url)  # Save the original code
        # analyze them one by one.
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            data = []  # create a list to store the info.
            item = str(item)

            # Use regular expressions to get the info we want
            link = re.findall(findLink, item)[0]
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            title = re.findall(findTitle, item)  # 1st Chinese, 2nd English
            # title needs some special treat
            if (len(title) == 2):
                ctitle = title[0]
                data.append(ctitle)
                etitle = title[1].replace("/", "")
                data.append(etitle)
            else:
                data.append(title[0])
                data.append("None")  # For future export to csv/excel

            rate = re.findall(findRate, item)[0]
            data.append(rate)

            numOfRates = re.findall(findNumOfRates, item)[0]
            data.append(numOfRates)

            introOfMovie = re.findall(findIntroOfMovie, item)
            if (len(introOfMovie) != 0):
                data.append(introOfMovie)
            else:
                data.append("None")

            content = re.findall(findContent, item)[0]
            cotent = re.sub('<br(\s+)?/>(\s+)?', " ", content)
            cotent = re.sub('/', " ", content).strip()
            data.append(content)

            datalist.append(data)

    return datalist


# 得到指定一个url的网页内容
def askURL(url):  # Fake Header
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.97 Safari/537.36 "
        # You can add all the accept parameters, cookies, etc there as well.
    }
    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveDataToExcel(datalist, save_path):
    # after we get the datalist, it is a list of list. Lets save it to excel first.
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)  # create the workbook object
    worksheet = workbook.add_sheet("Douban Movie Top 250", cell_overwrite_ok=True)  # create the sheet
    # Create a tuple for the col names
    col_names = (
    "link", "image source", "Chinese title", "English title", "rate", "number of rates", "introduction of movie",
    "movie related info")
    for i in range(0, 8):
        worksheet.write(0, i, col_names[i])  # col names
    for i in range(0, 250):
        print("Num %d" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            worksheet.write(i + 1, j, data[j])
    workbook.save(save_path)


def main():
    # 1. Scape the website.
    base_url = "https://movie.douban.com/top250?start="
    # askURL(base_url)
    save_path = "./douban_top250.xls"
    datalist = getData(base_url)
    saveDataToExcel(datalist, save_path)


if __name__ == "__main__":
    main()
