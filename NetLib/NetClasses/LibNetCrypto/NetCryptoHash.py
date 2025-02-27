__author__ = 'Jean-Michel Cuvelier'

from Lib.Functions.LibControl.NetControlParameter import NetClassParameterUnique
from Lib.Classes.LibNetCrypto.NetCryptoBase import TypeNetCryptoBase,NetCryptoBase

class TypeNetCryptoHash(TypeNetCryptoBase):
    def __new__ (obj,name,list_hierachy,dict_parameters):
        return super(TypeNetCryptoHash,obj).__new__(obj,name,list_hierachy,dict_parameters)

class NetCryptoHash(NetCryptoBase):
        __metaclass__=TypeNetCryptoHash
            
        @NetClassParameterUnique(password=str)
        def __init__(self,*param_no_name,**param_name):
            try: 
                dict_param_name=dict(param_name)
                list_param_no_name=list(param_no_name)
                
                self.__password=dict_param_name["password"]
            except BaseException as ex:
                raise ex
            return
        
        def __setnull(self,param):
            print(str(param)+ " can't define on read only parameter")
            return

