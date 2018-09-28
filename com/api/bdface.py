#!/usr/bin/env python
# -*- coding:utf-8 -*-


import requests
import base64
from com.api.my_redis import RedisManager


class Config(object):

    API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxx"
    SECRET_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ACCESS_TOKEN = "access_token"
    GRANT_TYPE = "client_credentials"

    URL_ACCESS_TOKEN = "https://aip.baidubce.com/oauth/2.0/token"
    URL_FACE_SEARCH = "https://aip.baidubce.com/rest/2.0/face/v3/search"

    FACE_GROUP_NAME = "group_test"
    FACE_IMAGE_TYPE = "BASE64"


class Token(object):

    @staticmethod
    def get_token():

        if not Token.is_expire():
            Token.get_token_from_server()
        return str(RedisManager.redis_get(Config.ACCESS_TOKEN))

    @staticmethod
    def is_expire():
        expires_in = RedisManager.redis_ttl(Config.ACCESS_TOKEN)
        return expires_in > 0

    @staticmethod
    def get_token_from_server():

        print("url")
        url = Config.URL_ACCESS_TOKEN
        params = 'grant_type=client_credentials&client_id=' + Config.API_KEY + '&client_secret=' + Config.SECRET_KEY
        result = requests.get(url, params)
        if result.status_code == 200:
            json_result = result.json()
            access_token = json_result.get("access_token")
            expires_in = json_result.get("expires_in")
            RedisManager.redis_setex(Config.ACCESS_TOKEN, access_token, expires_in)


class Face(object):

    @staticmethod
    def get_base_64():
        img_file = '20140043.png'
        with open(img_file, 'rb') as img:
            data = base64.b64encode(img.read())
            return data

    @staticmethod
    def search():

        params = {
            "image": Face.get_base_64(),
            "group_id_list": Config.FACE_GROUP_NAME,
            "image_type": Config.FACE_IMAGE_TYPE,
            "liveness_control": "NORMAL",
            "quality_control": "LOW"
        }

        token = Token.get_token()
        request_url = Config.URL_FACE_SEARCH + "?access_token=" + token

        result = requests.post(request_url, data=params)
        if result.status_code == 200:
            json = result.json()
            Face.parse_json(json)

    @staticmethod
    def parse_json(origin_data):
        error_code = origin_data.get('error_code')
        error_msg = origin_data.get('error_msg')
        result = origin_data.get('result')

        face_token = result.get('face_token')
        user_list = result.get('user_list')
        user_data = user_list[0]

        group_id = user_data.get('group_id')
        user_id = user_data.get('user_id')
        user_info = user_data.get('user_info')
        score = user_data.get('score')

        print("error_code:", error_code)
        print("error_msg:", error_msg)
        print("group_id:", group_id)
        print("user_id:", user_id)
        print("user_info:", user_info)
        print("score:", score)


if __name__ == "__main__":

    print(Face.search())