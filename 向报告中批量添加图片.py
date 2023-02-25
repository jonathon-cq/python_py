#!/usr/bin/env python3
#-*- coding:utf-8-*-
"""
@Time    : 2023/2/16 20:39 
@Author  : 12093
@File    : 向报告中批量添加图片.py
@Software: PyCharm
"""

# 导入必要的库
import os
import openpyxl
from openpyxl.drawing.image import Image

# 判断文件是否存在
if os.path.exists('example.xlsx'):
    # 打开excel文件
    wb = openpyxl.load_workbook('example.xlsx')
    # 获取名为 "Sheet1" 的工作表
    sheet = wb['Sheet1']
else:
    # 创建excel文件
    wb = openpyxl.Workbook()
    # 获取默认的工作表（也就是第一个工作表）
    sheet = wb.active

    # 将工作表命名为 "Sheet1"
    sheet.title = "Sheet1"
# 选择要添加图片的sheet
sheet = wb['Sheet1']

# 循环添加图片
for i in range(10):
    # 计算添加图片的位置
    row = i * 30 + 1
    # 创建图片对象
    img = Image('名.png')
    # 将图片添加到指定的单元格
    sheet.add_image(img, 'V' + str(row))
# 保存excel文件
wb.save('example.xlsx')
