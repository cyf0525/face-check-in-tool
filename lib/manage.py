# -*- coding: utf-8 -*-
import json
import conf


class Manage():
    def __init__(self,id, name, email, userId):
        self.id = id
        self.name = name
        self.email = email
        self.userId = userId

    def Create(self):
        sql_insert = 'insert into employee' \
                    '(id,name,email)' \
                    'values' \
                    '(\'%s\',\'%s\',\'%s\')' % (self.id, self.name, self.email)

        conf.cursor.execute(sql_insert)
        conf.connection.commit()
        # insert successfully will print this
        print "insert: \'%s\',\'%s\',\'%s\'" % (self.id, self.name, self.email)

        # 在百度人脸库里增加User照片
        conf.client.addUser(conf.image, conf.imageType, 'group1', self.userId, conf.options)
        add = conf.client.addUser(conf.image, conf.imageType, 'group1', self.userId, conf.options)
        if add['error_msg'] == 'SUCCESS':
            output = { "code": 0, "data" : "success"}
            print json.dumps(output)


    def Query(self):
        # 人脸库ID
        res = conf.client.search(conf.image, conf.imageType, 'group1')
        score = res['result']['user_list'][0]['score']
        ID = res['result']['user_list'][0]['user_id']

        if score > 90:
            # print score
            print ID + 'log in'