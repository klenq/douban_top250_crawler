# @Time : 2021/12/12 14:54
# @Author : klenq
# @File : testXwlt.py
# @Software : PyCharm

import xlwt

'''
workbook = xlwt.Workbook(encoding='utf-8',)

worksheet = workbook.add_sheet('sheet1')

worksheet.write(0,0,'hello')
workbook.save('student.xls')
'''
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')

for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d "%(i+1,j+1,(i+1)*(j+1)))
        
workbook.save('student.xls')