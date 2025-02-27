__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

import NetRessources
from NetLib.NetClasses.NetNotification.NetTypeNotification import NetTypeNotification
from NetLib.NetClasses.NetClassParatemter.NetClassParameter import NetClassParameterUnique,NetClassParameterContains
from NetLib.NetClasses.NetException.NetException import NetException,NetTypeException
from NetLib.NetClasses.NetLog.NetLog import NetLog

import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


import re
import json
import yaml
import types
from datetime import datetime

class NetTypeHashBase(NetTypeNotification):
    def __new__( self, classname, superclasses, attributdict):
        return super(NetTypeHashBase,self).__new__(classname, superclasses, attributdict)

class NetTypeExcpetionHashBase(NetTypeException):
    def __new__( self, classname, superclasses, attributdict):
        return super(NetTypeExcpetionHashBase,self).__new__(classname, superclasses, attributdict)
    
class NetHashBase():
    __metaclass__=NetTypeHashBase
    
    DEFAULT_CONFIG=re.sub("[^/]*$","",NetRessources.__file__).replace("/","//")+"NetDefaultConfig//NetHashBase.yaml"
    
    def __getstate__(self):
        try:
            state=dict(self._config)
            state["dict"]=self.__dict__
            
            return state
        except NetTypeExcpetionHashBase as ex:
            raise ex
        except Exception as ex:
            raise ex
    
    def __setstate__(self,state):
        if type(state) is dict:
            
            self.__dict__=state["dict"]
            
            for handler in state["handlers"]:                
                match=re.match("^(?P<Module>.*)\.(?P<Class>[^\.]*)$",handler["handler"])
                if match:    
                    module = __import__(match.group("Module"))
                    class_ = getattr(module,match.group("Class"))
                    handler["handler"]=class_
                    
            self.dictload(**state)
        return    
    
    def __init__(self,*param_no_named,**param_named):
        
        list_param_no_named=list(param_no_named)
        dict_param_named=dict(param_named)
        
        if "log" in dict_param_named.keys() and issubclass(type(dict_param_named["log"],NetLog)) is True:
            self._log=dict_param_named["log"]
        else:
            self._log=NetLog()
        
        cryptography.hazmat.backends.
        digest = hashes.Hash(algorithm=hashes.MD5(),backend=default_backend())
        digest.update(b"Bonjour")
        msg_digest = digest.finalize()
        

        if len(list_param_no_named) > 0 or "path" in dict_param_named.keys():
            if len(list_param_no_named) > 0 and type(list_param_no_named[0]) is dict:
                self.dictload(**list_param_no_named[0])
            else:
                if "path" in dict_param_named.keys():
                    path=dict_param_named["path"]
                elif type(list_param_no_named[0]) is str:
                    path=list_param_no_named[0]
                else:
                    path=""
                match=re.search("\.(?P<EXTENSION>[^\.]*)$",path)
                if match:
                    extension=match.group("EXTENSION").lower()
                    if extension == "json":
                        self.loadjson(path)
                    elif extension == "yaml":
                        self.loadyaml(path)
                    else:
                        self.loadyaml(self.DEFAULT_CONFIG)
                else:
                    self.loadyaml(self.DEFAULT_CONFIG)
        else:                
            self.loadyaml(self.DEFAULT_CONFIG)


    def dictload(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            self._logger.handlers.clear()
            self._config["handlers"].clear()
                        
            self.name=dict_param_named["name"]
            self.level=dict_param_named["level"]
            if "base_level" in dict_param_named.keys():
                if dict_param_named["base_level"] in [NetLog.LEVEL_CRITICAL,NetLog.LEVEL_ERROR,NetLog.LEVEL_WARNING,NetLog.LEVEL_INFO,NetLog.LEVEL_DEBUG]:
                    self.baselevel=dict_param_named["base_level"]
            for elem in dict_param_named["handlers"]:
                self.addHandler(**elem)
                
        except NetTypeExcpetionHashBase as ex:
            raise ex
        except Exception as ex:
            raise ex
        return self 
    
    @NetClassParameterContains(str)
    def savejson(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            with open(list_param_no_named[0], 'w') as outfile:
                json.dump(self._config, fp=outfile, sort_keys=True, indent=2,ensure_ascii = False)
                outfile.close()
                
        except NetTypeExcpetionHashBase as ex:
            raise ex
        except Exception as ex:
            raise ex
        return
    
    @NetClassParameterContains(str)
    def loadjson(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            read=dict()
            
            with open(list_param_no_named[0], 'r') as outfile:
                read=json.load(outfile)
                
                for handler in read["handlers"]:                
                    match=re.match("^(?P<Module>.*)\.(?P<Class>[^\.]*)$",handler["handler"])
                    if match:    
                        module = __import__(match.group("Module"))
                        class_ = getattr(module,match.group("Class"))
                        handler["handler"]=class_
                self.dictload(**read)
            
        except NetTypeExcpetionHashBase as ex:
            raise ex
        except Exception as ex:
            raise ex
        return self

    @NetClassParameterContains(str)
    def saveyaml(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            with open(list_param_no_named[0], 'w') as outfile:
                stream=yaml.dump(self._config,outfile)
                outfile.close()
                
        except NetTypeExcpetionHashBase as ex:
            raise ex
        except Exception as ex:
            raise ex
        return

    @NetClassParameterContains(str)
    def loadyaml(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            read=dict()
                        
            with open(list_param_no_named[0], 'r') as outfile:
                read=yaml.load(outfile)
                
                for handler in read["handlers"]:                
                    match=re.match("^(?P<Module>.*)\.(?P<Class>[^\.]*)$",handler["handler"])
                    if match:    
                        module = __import__(match.group("Module"))
                        class_ = getattr(module,match.group("Class"))
                        handler["handler"]=class_
                self.dictload(**read)
            
        except NetTypeExcpetionHashBase as ex:
            raise ex
        except Exception as ex:
            raise ex
        return self







