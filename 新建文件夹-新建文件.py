#!/usr/bin/env python3
#-*- coding:utf-8-*-
"""
@Time    : 2023/2/15 22:07 
@Author  : 12093
@File    : 新建文件夹-新建文件.py
@Software: PyCharm
"""
import os
import datetime

# 1.输入用户和密码
user=input("请输入用户名：")
pwd=input("请输入密码：")
now=datetime.datetime.now()  #导入当前创造时间


# 2.字符串格式化
line="\n创建时间:{}\n用户名:{}\n密  码:{}\n".format(now,user ,pwd)

# 3.确保目录存在(存在,直接用;不存在,创建)
folder_path=os.path.join("bd","account")
if not os.path.exists(folder_path ):
    os.makedirs(folder_path )

# 4.拼接获取文件的路径
file_path=os.path.join(folder_path,'users.txt')

# 5.在文件中实现注册(不存在,自动创建)
f=open(file_path ,mode='a',encoding='utf-8')
f.write(line)
f.close()