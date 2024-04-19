#!/usr/bin/env python
# -*- encoding=utf8 -*-
import os
import json
 
class Config(object):
   def __init__(self):
       # Map the environment variable names to the sections and options
       api_jd_url = 'https://api.m.jd.com/client.action?functionId=msgEntranceV710&lmt=0&t=1713508052050&appid=MessageCenter&clientVersion=12.1.0&build=98891&client=android&partner=google&sdkVersion=32&lang=zh_CN&harmonyOs=0&networkType=wifi&uts=0f31TVRjBSv9oJbOZmJ1wC1Ir%2FNBWDpPlcjOuJbvYsl%2Fpeb9A4PU84dy%2FXwxu1ctIL6N1pRdLLUvB3uKLHhbpd1q5L1WydgaiBg%2B2a9gQhUlBNAUTXB%2BEGEMjxGry2pyxcgwxZ3PgMD3KqtZ6SK2M8ePFdv3pZ8FjV69fq809QLdf8zdNEIBuMIfk1u0epjXeMI2ERJfLnwadhTw71Z6Kg%3D%3D&uemps=0-0-0&ext=%7B%22prstate%22%3A%220%22%2C%22pvcStu%22%3A%221%22%2C%22cfgExt%22%3A%22%7B%5C%22privacyOffline%5C%22%3A%5C%220%5C%22%7D%22%7D&avifSupport=1&eid=eidAf5508122b4sfnNDZOC%2FORny15ZCeKQMzT5zQ2schF1BmwV7plcDbyJrh9dOUOx5cyGhzRMf7%2Bs51oKoePthxW1714WxwUzp1SSHfIngcRfHGgD5r&ef=1&ep=%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1713508035802%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22area%22%3A%22CJvpCJY2Dv8zDtS2D18zDtS3DG%3D%3D%22%2C%22d_model%22%3A%22U00jUzunCJK%3D%22%2C%22wifiBssid%22%3A%22dW5hbw93bq%3D%3D%22%2C%22osVersion%22%3A%22CJS%3D%22%2C%22d_brand%22%3A%22U2Pjc3VkZm%3D%3D%22%2C%22screen%22%3A%22CtU2CMenDNGm%22%2C%22uuid%22%3A%22EQG3YtO1DzZuYWSzYtDtYq%3D%3D%22%2C%22aid%22%3A%22EQG3YtO1DzZuYWSzYtDtYq%3D%3D%22%2C%22openudid%22%3A%22EQG3YtO1DzZuYWSzYtDtYq%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D&sign=f95e3c230d03d075bdfcb5740173bd56fa1ca3a9d7ae311630b4ac5f270a5146&x-api-eid-token=0&oaid=0'
       self.config = {
           'config': {
               'local_cookies': os.getenv('LOCAL_COOKIES'),
               'local_jec': os.getenv('LOCAL_JEC'),
               'local_jdgs': os.getenv('LOCAL_JDGS'),
               'api_jd_url': api_jd_url,
               'continue_time': 10,
               'work_count': 2,
               'fp': os.getenv('FP'),
               'task': [{"name" :"maotai", "sku_id" :"100012043978", "make_reserve_time" :"10:07:00", "buy_time" :"11:59:57",}],
               'address_id': os.getenv('ADDRESS_ID'),
               'push_token': os.getenv('PUSH_TOKEN'),
           }
       }
 
   def get(self, section, name):
       # Return the value for the given section and name or an empty string if not found
       return self.config.get(section, {}).get(name, '')
 
   def getRaw(self, section, name):
       # If you need the raw value, you can return it directly
       return self.get(section, name)
 
# Use the global_config object to access configuration settings
global_config = Config()
 
# Example usage:
# tasks = global_config.get('config', 'task')
# continue_time = global_config.get('config', 'continue_time')

# 以下为原始代码

# import configparser
# import os


# class Config(object):
#     def __init__(self, config_file='config.ini'):
#         self._path = os.path.join(os.getcwd(), config_file)
#         if not os.path.exists(self._path):
#             raise FileNotFoundError("No such file: config.ini")
#         self._config = configparser.ConfigParser()
#         self._config.read(self._path, encoding='utf-8-sig')
#         self._configRaw = configparser.RawConfigParser()
#         self._configRaw.read(self._path, encoding='utf-8-sig')

#     def get(self, section, name):
#         return self._config.get(section, name)

#     def getRaw(self, section, name):
#         if self._configRaw.has_option(section, name):
#             return self._configRaw.get(section, name)
#         else:
#             return ''


# global_config = Config()
