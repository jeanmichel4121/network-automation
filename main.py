#!/usr/bin/python3
__author__ = 'Jean-Michel Cuvelier'

import sys
from filelock import logger
import logging
sys.path.insert(0,'./')
import urllib3
from NetLib.NetClasses.NetException.NetException import NetException
from NetLib.NetClasses.NetConfig.NetConfig import NetConfig
from NetLib.NetClasses.NetConfig.NetConfigFile.NetConfigFile import NetConfigFile
from NetLib.NetClasses.NetLog.NetLog import NetLog
from NetLib.NetClasses.NetIP.NetIPv4 import NetIPv4
from NetLib.NetClasses.NetMenu.NetMenu import NetMenu
from NetLib.NetClasses.NetData.NetData import NetData
from lxml import etree
from io import StringIO, BytesIO


import json
import re
import os
import time


def main():
      try:

            urllib3.disable_warnings()



            log=NetLog(generate_default_config=True,logger_name='file')



      except Exception as ex :
            print(ex)
            pass
      return
if __name__ == "__main__":
      
      main()
