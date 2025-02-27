__author__ = 'Jean-Michel Cuvelier'

from Lib.Functions.LibControl.NetControlParameter import NetClassParameterUnique
from Lib.Classes.LibNotification.NetNotification import NetTypeNotification
import getpass
import types
import paramiko

class TypeNetSSH(NetTypeNotification):
    def __new__ (obj,name,list_hierachy,dict_parameters):
        return super(TypeNetSSH,obj).__new__(obj,name,list_hierachy,dict_parameters)

class NetSSH():
    __metaclass__=TypeNetSSH
    
    def __init__(self,*param_no_name,**param_name):
        try: 
            dict_param_name=dict(param_name)
            list_param_no_name=list(param_no_name)
            
            self.__user="usr"
            if "user" in dict_param_name.keys():               
                self.__user=dict_param_name["user"]
                
            self.__password=""
            if "password" in dict_param_name.keys():               
                self.__password=dict_param_name["password"]
                
            self.__password="22"
            if "password" in dict_param_name.keys():               
                self.__password=dict_param_name["password"]
                
        except BaseException as ex:
            raise ex
        return

 