#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import path
from flask import Flask,request,render_template, redirect,url_for
import pymysql
from manage import Manage

connection = pymysql.connect("localhost", "root", "csss331331", "ecommerce", charset='utf8' )
cursor = connection.cursor(pymysql.cursors.DictCursor)

""" 你的 APPID AK SK """
APP_ID = '16817866'
API_KEY = 'knoeO8eEGIWvLIHuFczaAWlv'
SECRET_KEY = '6SKGY0ExOECGM0fGboDsScrOmAolHCo5'

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def info():
    if request.method=='POST':
        return redirect(url_for('info'))
    return render_template('upload.html')


@app.route("/upload",methods=['POST'])
def upload():
    if request.method=='POST':
        na = request.form["Name"]
        user_id = request.form['ID']
        em = request.form['Email']

        #添加照片到人脸库
        regi = Manage(user_id,na,em,user_id)
        regi.Create()

        return redirect(url_for('info'))

@app.route("/query",methods=['POST'])
def query():
    if request.method=='POST':

        regi = Manage('test', 'test', 'test', 'test')
        regi.Query()

        return redirect(url_for('query'))
    return render_template('query.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
