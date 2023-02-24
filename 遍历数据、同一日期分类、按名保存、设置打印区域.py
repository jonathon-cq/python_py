#!/usr/bin/env python3
#-*- coding:utf-8-*-
"""
@Time    : 2023/2/23 16:17
@Author  : Jonathon
@File    : 遍历数据、同一日期分类、按名保存、设置打印区域.py
@Software: PyCharm
"""

import pandas as pd
# from openpyxl.utils import get_column_letter
import math

# 读取 Excel 文件，从第三行开始读取，将第三列设置为列名
df = pd.read_excel("D6-抗眩晕、器械训练场、综合训练楼及緑化区第1-45层.xlsx", sheet_name="台账", usecols='A:AC', skiprows=2, header=0)
print(df)
# print(df.columns)
# 只保留 AB 列都非空的行
# df = df.loc[df['开始日期'].notna()]
# # print(df)
#
# groups = df.groupby('委托日期')

# print(groups.groups.keys())

# 查看每个分组的大小
# print(groups.size())

# print(groups.mean())
# groups.head()


group_names = groups.groups.keys()
# group_name = list(groups.groups.keys())[0]

# 遍历每一组
for name in group_names:
    group = groups.get_group(name)
    page=group['页数'].sum().astype(int) #求和并转化为整数类型
    print(page)
    names_list=group['样品编号/报告编号'].tolist()
    num_list = [int(s[11:]) for s in names_list]

# 将整数类型的数字转换为字符串类型，并使用逗号连接起来
    book_name = names_list[0] + ',' + ','.join(map(str, num_list[1:]))
    print( book_name)
#     print(f"Group: {name}")
#     print(group)
