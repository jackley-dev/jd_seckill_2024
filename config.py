#!/usr/bin/env python
# -*- encoding=utf8 -*-
import os
import json
 
class Config(object):
   def __init__(self):
       # Map the environment variable names to the sections and options
       self.config = {
           'config': {
               'local_cookies': os.environ.get('LOCAL_COOKIES'),
               'local_jec': os.environ.get('LOCAL_JEC'),
               'local_jdgs': os.environ.get('LOCAL_JDGS'),
               'api_jd_url': os.environ.get('API_JD_URL'),
               'continue_time': 10,
               'work_count': 2,
               'fp': os.environ.get('FP'),
               'task': [{"name" :"maotai", "sku_id" :"100012043978", "make_reserve_time" :"10:07:00", "buy_time" :"11:59:57",}],
               'address_id': os.environ.get('ADDRESS_ID'),
               'push_token': os.environ.get('PUSH_TOKEN'),
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
