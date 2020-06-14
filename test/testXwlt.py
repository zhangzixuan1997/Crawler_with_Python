#-*- coding = utf-8 -*-
#@Time : 6/13/20 11:50 PM
#@Author : Sean Zhang
#@File : testXwlt.py
#@Software : PyCharm

import xlwt


workbook = xlwt.Workbook(encoding='utf-8') # create the workbook object
worksheet = workbook.add_sheet("sheet1") # create the sheet
worksheet.write(0,0,"hello") #row column and content
workbook.save("hello.xls")


#The rest is just for fun.

'''
workbook = xlwt.Workbook(encoding='utf-8') # create the workbook object
worksheet = workbook.add_sheet("sheet1") # create the sheet
for i in range(1,10):
    for j in range(1,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(i,j,i*j))
workbook.save("99.xls")
'''

