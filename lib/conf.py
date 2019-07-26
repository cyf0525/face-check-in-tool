# -*- coding: utf-8 -*-
from aip import AipFace
import base64
import pymysql

#Mysql
connection = pymysql.connect("localhost", "root", "csss331331", "ecommerce", charset='utf8' )
cursor = connection.cursor(pymysql.cursors.DictCursor)

#你的 APPID AK SK
APP_ID = '16817866'
API_KEY = 'knoeO8eEGIWvLIHuFczaAWlv'
SECRET_KEY = '6SKGY0ExOECGM0fGboDsScrOmAolHCo5'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

#上传照片路径
filepath = '/Users/yanfeng/Downloads/Upload/3.jpeg'

with open(filepath, "rb") as f:
    base64_data = base64.b64encode(f.read())
image = str(base64_data)
imageType = "BASE64"

#SDK可选参数
options = {}
options["quality_control"] = "NORMAL"
options["liveness_control"] = "LOW"
options["action_type"] = "REPLACE"
