#!/usr/bin/env python
# encoding: utf-8
'''
@author: cherie
@contact: cheriewuyajun@hotmail.com
@file: yunpian.py
@time: 2019/7/6 13:51
@desc:
'''
import json
import requests


class YunPian(object):

    def __int__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【慕学生鲜】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)

        return re_dict


if __name__ == "__main__":
    yun_pian = YunPian("9a7d9d1c5b7ef48b0e1d912d9f83c529")
    yun_pian.send_sms("2017","17744050844")