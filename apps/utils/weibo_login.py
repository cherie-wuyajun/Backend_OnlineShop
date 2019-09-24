#!/usr/bin/env python
# encoding: utf-8
'''
@author: cherie
@contact: cheriewuyajun@hotmail.com
@file: weibo_login.py
@time: 2019/7/16 18:28
@desc:
'''

def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "http://127.0.0.1:8000/complete/weibo/"
    auth_url = weibo_auth_url+"?client_id={client_id}&redirect_uri={re_url}".format(client_id=515431440, re_url=redirect_url)

    print(auth_url)


def get_access_token(code="468359b59244272ccf25b6b5424b434e"):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    import requests
    re_dict = requests.post(access_token_url,data={
        "client_id": "515431440",
        "client_secret": "cac8cfdc674f2b8944679aed24e81a60",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://127.0.0.1:8000/complete/weibo/",
    })


def get_user_info(access_token="", uid=""):
    user_url = "https://api.weibo.com/2/users/show.json?access_token={token}&uid={uid}".format(token=access_token, uid=uid)

    print(user_url)


if __name__ == "__main__":
    #get_auth_url()
    #get_access_token(code="468359b59244272ccf25b6b5424b434e")
    get_user_info(access_token="2.005WTvvB01QhsY000d626cdaFDKhlC", uid="1772082164")
#'{"access_token":"2.005WTvvB01QhsY000d626cdaFDKhlC","remind_in":"157679999","expires_in":157679999,"uid":"1772082164","isRealName":"true"}'