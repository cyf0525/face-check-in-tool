#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask,request,render_template, redirect,url_for
import pymysql
from lib.manage import Manage

app = Flask(__name__)


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
