# -*- coding: utf-8 -*-
from aip import AipFace
import base64
import pymysql

connection = pymysql.connect("localhost", "root", "csss331331", "ecommerce", charset='utf8' )
cursor = connection.cursor(pymysql.cursors.DictCursor)

#你的 APPID AK SK
APP_ID = '16817866'
API_KEY = 'knoeO8eEGIWvLIHuFczaAWlv'
SECRET_KEY = '6SKGY0ExOECGM0fGboDsScrOmAolHCo5'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)