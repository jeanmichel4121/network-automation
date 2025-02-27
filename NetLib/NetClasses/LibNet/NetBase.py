__author__ = 'Jean-Michel Cuvelier'

from Lib.Functions.LibControl.NetControlParameter import NetClassParameterUnique
from Lib.Classes.LibNotification.NetNotification import NetTypeNotification
from Lib.Classes.LibData.NetUserBase import NetUserBase
import getpass
import types
import paramiko

class TypeNetBase(NetTypeNotification):
    def __new__ (obj,name,list_hierachy,dict_parameters):
        return super(TypeNetBase,obj).__new__(obj,name,list_hierachy,dict_parameters)

class NetBase():
    __metaclass__=TypeNetBase
    
    def __init__(self,*param_no_name,**param_name):
        try: 
            dict_param_name=dict(param_name)
            list_param_no_name=list(param_no_name)
            self.__user=NetUserBase()
            
            self.__user.user="user"
            self.__user.password="password"
            
            if "user" in dict_param_name.keys():               
                self.__user.user=dict_param_name["user"]
                
            if "password" in dict_param_name.keys():               
                self.__user.password=dict_param_name["password"]
                
            if "host" in dict_param_name.keys():               
                self.__host=dict_param_name["host"]
                
            if "port" in dict_param_name.keys():               
                self.__port=dict_param_name["port"]
                
        except BaseException as ex:
            raise ex
        return
