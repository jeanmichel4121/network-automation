# pylint: disable=unused-variable
__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

import NetLib
from abc import ABC,abstractmethod,abstractproperty,ABCMeta
from NetLib.NetClasses.NetException.NetException import NetException
from NetLib.NetClasses.NetClassParatemter.NetClassParameter import NetClassParameterContains,NetClassParameterUnique,NetClassParameterCombine
from NetLib.NetClasses.NetBase.NetBase import NetTypeBase,NetTypeExcpetionBase,NetExceptionBase,NetBase
import re
import os
import json
import yaml
from filelock import Timeout, FileLock



class NetTypeConfigDict(NetTypeBase):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeConfigDict,self).__new__(self,*param_no_named,**param_named)

class NetTypeConfigList(NetTypeBase):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeConfigList,self).__new__(self,*param_no_named,**param_named)

class NetTypeConfigDictType(NetTypeBase):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeConfigDictType,self).__new__(self,*param_no_named,**param_named)

class NetTypeConfigListType(NetTypeBase):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeConfigListType,self).__new__(self,*param_no_named,**param_named)

class NetTypeConfigDictRegex(NetTypeBase):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeConfigDictRegex,self).__new__(self,*param_no_named,**param_named)

class NetTypeConfigListRegex(NetTypeBase):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeConfigListRegex,self).__new__(self,*param_no_named,**param_named)

class NetTypeConfig(NetTypeBase):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeConfig,self).__new__(self,*param_no_named,**param_named)

class NetTypeExcpetionConfig(NetTypeExcpetionBase):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeExcpetionConfig,self).__new__(self,*param_no_named,**param_named)

class NetExceptionConfig(NetExceptionBase,metaclass=NetTypeExcpetionConfig):
    __metaclass__=NetTypeExcpetionConfig
     
    def __init__(self,*param_no_named,**param_named):
        super(NetExceptionConfig,self).__init__(*param_no_named,**param_named)
        self._config['exception']['content']['class_name']='NetConfig'

    def __str__(self):
        return super(NetExceptionConfig,self).__str__()
    

class NetConfig(NetBase,metaclass=NetTypeConfig):
    __metaclass__=NetTypeConfig

    class ConfigList(list,metaclass=NetTypeConfigList):
        __metaclass__=NetTypeConfigList
        @NetClassParameterUnique(root=object,mylist=list)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            self.__root=dict_param_named['root']
            list.__init__(self,dict_param_named['mylist'])

        def __setitem__(self, item, value):
            old_config=self.__root._parse_original(source=self.__root._config)

            add=None
            if type(value) is dict or type(value) is list:
                add=self.__root._parse_config(source=value)
            else:
                add=value

            if type(item) is int and item < len(self):
                list.__setitem__(self,item, add)
            else:
                if issubclass(type(add),list):
                    list.extend(self,add)
                else:
                    list.append(self,add)

            config=self.__root._parse_original(source=self.__root._config)
            if self.__root._check_same_object(source1=old_config,source2=config) is False:
                self.__root._check_config()
                self.__root._update_config(old_config=old_config,new_config=config)
    class ConfigDict(dict,metaclass=NetTypeConfigDict):
        __metaclass__=NetTypeConfigDict
        @NetClassParameterUnique(root=object,dictionary=dict)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            self.__root=dict_param_named['root']
            dict.__init__(self,dict_param_named['dictionary'])

        def __str__(self):
            return json.dumps(self,indent=2)

        def __getitem__(self, item):
            index=str(item)
            if index not in self.keys():
                add=NetConfig.ConfigDict(root=self.__root,dictionary=dict())
                dict.__setitem__(self,index, add)

                sort=dict()
                for key in self.keys():
                    sort[key]=dict.__getitem__(self,key)
                for key in sort.keys():
                    dict.__delitem__(self,key)
                for key in sorted(sort.keys(),key=str.lower):
                    dict.__setitem__(self,key, sort[key])

            return dict.__getitem__(self,index)

        def __setitem__(self, item, value):
            old_config=self.__root._parse_original(source=self.__root._config)

            if item in self.keys():
                dict.__delitem__(self,item)

            add=None
            if type(value) is dict or type(value) is list:
                add=self.__root._parse_config(source=value)
            else:
                add=value

            dict.__setitem__(self,item, add)
            sort=dict()
            for key in self.keys():
                sort[key]=dict.__getitem__(self,key)
            for key in sort.keys():
                dict.__delitem__(self,key)
            for key in sorted(sort.keys(),key=str.lower):
                dict.__setitem__(self,key, sort[key])

            config=self.__root._parse_original(source=self.__root._config)
            if self.__root._check_same_object(source1=old_config,source2=config) is False:
                self.__root._check_config()
                self.__root._update_config(old_config=old_config,new_config=config)
    class ConfigListType(list,metaclass=NetTypeConfigListType):
        __metaclass__=NetTypeConfigListType
        @NetClassParameterUnique(root=object,mylist=list)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            self.__root=dict_param_named['root']
            list.__init__(self,dict_param_named['mylist'])

        def __setitem__(self, item, value):
            old_config_type=self.__root._parse_original(source=self.__root._config_type)

            add=None
            if type(value) is dict or type(value) is list:
                add=self.__root._parse_config_type(source=value)
            else:
                add=value

            if type(item) is int and item < len(self):
                list.__setitem__(self,item, add)
            else:
                if issubclass(type(add),list):
                    list.extend(self,add)
                else:
                    list.append(self,add)

            config_type=self.__root._parse_original(source=self.__root._config_type)
            if self.__root._check_same_object(source1=old_config_type,source2=config_type) is False:
                self.__root._check_config()
                self.__root._update_config_type(old_config_type=old_config_type,new_config_type=config_type)
    class ConfigDictType(dict,metaclass=NetTypeConfigDictType):
        __metaclass__=NetTypeConfigDictType
        @NetClassParameterUnique(root=object,dictionary=dict)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            self.__root=dict_param_named['root']
            dict.__init__(self,dict_param_named['dictionary'])            

        def __str__(self):
            return json.dumps(self,indent=2)

        def __getitem__(self, item):
            index=str(item)
            if index not in self.keys():
                add=NetConfig.ConfigDictType(root=self.__root,dictionary=dict())
                dict.__setitem__(self,index, add)

                sort=dict()
                for key in self.keys():
                    sort[key]=dict.__getitem__(self,key)
                for key in sort.keys():
                    dict.__delitem__(self,key)
                for key in sorted(sort.keys(),key=str.lower):
                    dict.__setitem__(self,key, sort[key])


            return dict.__getitem__(self,index)

        def __setitem__(self, item, value):
            old_config_type=self.__root._parse_original(source=self.__root._config_type)

            if item in self.keys():
                dict.__delitem__(self,item)

            add=None
            if type(value) is dict or type(value) is list:
                add=self.__root._parse_config_type(source=value)
            else:
                add=value

            dict.__setitem__(self,item, add)
            sort=dict()
            for key in self.keys():
                sort[key]=dict.__getitem__(self,key)
            for key in sort.keys():
                dict.__delitem__(self,key)
            for key in sorted(sort.keys(),key=str.lower):
                dict.__setitem__(self,key, sort[key])

            config_type=self.__root._parse_original(source=self.__root._config_type)
            if self.__root._check_same_object(source1=old_config_type,source2=config_type) is False:
                self.__root._check_config()
                self.__root._update_config_type(old_config_type=old_config_type,new_config_type=config_type)
    class ConfigListRegex(list,metaclass=NetTypeConfigListRegex):
        __metaclass__=NetTypeConfigListRegex
        @NetClassParameterUnique(root=object,mylist=list)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            self.__root=dict_param_named['root']
            list.__init__(self,dict_param_named['mylist'])

        def __setitem__(self, item, value):
            old_config_regex=self.__root._parse_original(source=self.__root._config_regex)

            add=None
            if type(value) is dict or type(value) is list:
                add=self.__root._parse_config_regex(source=value)
            else:
                add=value

            if type(item) is int and item < len(self):
                list.__setitem__(self,item, add)
            else:
                if issubclass(type(add),list):
                    list.extend(self,add)
                else:
                    list.append(self,add)

            config_regex=self.__root._parse_original(source=self.__root._config_regex)
            if self.__root._check_same_object(source1=old_config_regex,source2=config_regex) is False:
                self.__root._check_config()
                self.__root._update_config_regex(old_config_regex=old_config_regex,new_config_regex=config_regex)
    class ConfigDictRegex(dict,metaclass=NetTypeConfigDictRegex):
        __metaclass__=NetTypeConfigDictRegex
        @NetClassParameterUnique(root=object,dictionary=dict)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            self.__root=dict_param_named['root']
            dict.__init__(self,dict_param_named['dictionary'])

        def __str__(self):
            return json.dumps(self,indent=2)       
            
        def __getitem__(self, item):
            index=str(item)
            if index not in self.keys():
                add=NetConfig.ConfigDictRegex(root=self.__root,dictionary=dict())
                dict.__setitem__(self,index, add)

                sort=dict()
                for key in self.keys():
                    sort[key]=dict.__getitem__(self,key)
                for key in sort.keys():
                    dict.__delitem__(self,key)
                for key in sorted(sort.keys(),key=str.lower):
                    dict.__setitem__(self,key, sort[key])


            return dict.__getitem__(self,index)

        def __setitem__(self, item, value):
            old_config_regex=self.__root._parse_original(source=self.__root._config_regex)

            if item in self.keys():
                dict.__delitem__(self,item)

            add=None
            if type(value) is dict or type(value) is list:
                add=self.__root._parse_config_regex(source=value)
            else:
                add=value

            dict.__setitem__(self,item, add)
            sort=dict()
            for key in self.keys():
                sort[key]=dict.__getitem__(self,key)
            for key in sort.keys():
                dict.__delitem__(self,key)
            for key in sorted(sort.keys(),key=str.lower):
                dict.__setitem__(self,key, sort[key])

            config_regex=self.__root._parse_original(source=self.__root._config_regex)
            if self.__root._check_same_object(source1=old_config_regex,source2=config_regex) is False:
                self.__root._check_config()
                self.__root._update_config_regex(old_config_regex=old_config_regex,new_config_regex=config_regex)

    @NetClassParameterCombine([NetClassParameterUnique(source=dict),NetClassParameterUnique(source=list)])
    def _parse_config(self,*param_no_named,**param_named):
        
        @NetClassParameterUnique(source=dict)
        def parse_config_dict(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']
                keys=list(source.keys())             
                for key in keys:
                    if type(source[key]) is list:              
                        source[key]=NetConfig.ConfigList(root=self,mylist=source[key])
                        parse_config_list(self,source=source[key])
                    
                    if type(source[key]) is dict:
                        source[key]=NetConfig.ConfigDict(root=self,dictionary=source[key])
                        parse_config_dict(self,source=source[key])                    
                    
                  
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionConfig(self._logger,exception)  

        @NetClassParameterUnique(source=list)
        def parse_config_list(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']

                for index,elem in enumerate(source):
                    if type(elem) is list:
                        
                        source[index]=NetConfig.ConfigList(root=self,mylist=elem)
                        parse_config_list(self,source=source[index])
                    
                    if type(elem) is dict:
                        source[index]=NetConfig.ConfigDict(root=self,dictionary=elem)
                        parse_config_dict(self,source=source[index])                    
                                   
                            
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionConfig(self._logger,exception)  
                
        try:                      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                
            source=dict_param_named['source']
            retour=source  

            if ( type(source) is dict and len(source.keys()) > 0 ) or ( type(source) is list and len(source) > 0 ):

                if self._logger is not None:
                    self._logger.debug('NetConfig@'+ self._id +' ::_parse_config -> '+'source => '+str(source))                           
                
                retour=source.copy()
                
                if type(source) is list:
                    retour=NetConfig.ConfigList(root=self,mylist=retour)
                    parse_config_list(self,source=retour)
                
                if type(source) is dict:
                    retour=NetConfig.ConfigDict(root=self,dictionary=retour)
                    parse_config_dict(self,source=retour)
            
            return retour                
                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)         
    @NetClassParameterCombine([NetClassParameterUnique(source=dict),NetClassParameterUnique(source=list)])
    def _parse_config_type(self,*param_no_named,**param_named):
        
        @NetClassParameterUnique(source=object)
        def parse_config_type_dict(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']
                keys=list(source.keys())             
                for key in keys:
                    if type(source[key]) is list:              
                        source[key]=NetConfig.ConfigListType(root=self,mylist=source[key])
                        parse_config_type_list(self,source=source[key])
                    
                    if type(source[key]) is dict:
                        source[key]=NetConfig.ConfigDictType(root=self,dictionary=source[key])
                        parse_config_type_dict(self,source=source[key])                    
                    
                  
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionConfig(self._logger,exception)  

        @NetClassParameterUnique(source=object)
        def parse_config_type_list(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']                           

                for index,elem in enumerate(source):
                    if type(elem) is list:
                        
                        source[index]=NetConfig.ConfigListType(root=self,mylist=elem)
                        parse_config_type_list(self,source=source[index])
                    
                    if type(elem) is dict:
                        source[index]=NetConfig.ConfigDictType(root=self,dictionary=elem)
                        parse_config_type_dict(self,source=source[index])                    
                                   
                            
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionConfig(self._logger,exception)  
                
        try:                      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                
            source=dict_param_named['source']            
            retour=source
            if ( type(source) is dict and len(source.keys()) > 0 ) or ( type(source) is list and len(source) > 0 ):

                if self._logger is not None:
                    self._logger.debug('NetConfig@'+ self._id +' ::_parse_config_type -> '+'source => '+str(source))      

                retour=source.copy()
                
                if type(source) is list:
                    retour=NetConfig.ConfigListType(root=self,mylist=retour)
                    parse_config_type_list(self,source=retour)
                
                if type(source) is dict:
                    retour=NetConfig.ConfigDictType(root=self,dictionary=retour)
                    parse_config_type_dict(self,source=retour)
            
            return retour                
                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)
    @NetClassParameterCombine([NetClassParameterUnique(source=dict),NetClassParameterUnique(source=list)])
    def _parse_config_regex(self,*param_no_named,**param_named):
        
        @NetClassParameterUnique(source=object)
        def parse_config_regex_dict(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']
                keys=list(source.keys())             
                for key in keys:
                    if type(source[key]) is list:              
                        source[key]=NetConfig.ConfigListRegex(root=self,mylist=source[key])
                        parse_config_regex_list(self,source=source[key])
                    
                    if type(source[key]) is dict:
                        source[key]=NetConfig.ConfigDictRegex(root=self,dictionary=source[key])
                        parse_config_regex_dict(self,source=source[key])                    
                    
                  
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionConfig(self._logger,exception)  

        @NetClassParameterUnique(source=object)
        def parse_config_regex_list(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']                           

                for index,elem in enumerate(source):
                    if type(elem) is list:
                        
                        source[index]=NetConfig.ConfigListRegex(root=self,mylist=elem)
                        parse_config_regex_list(self,source=source[index])
                    
                    if type(elem) is dict:
                        source[index]=NetConfig.ConfigDictRegex(root=self,dictionary=elem)
                        parse_config_regex_dict(self,source=source[index])                    
                                   
                            
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionConfig(self._logger,exception)  
                
        try:                      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                
            source=dict_param_named['source']
            retour=source
            if ( type(source) is dict and len(source.keys()) > 0 ) or ( type(source) is list and len(source) > 0 ):

                if self._logger is not None:
                    self._logger.debug('NetConfig@'+ self._id +' ::_parse_config_regex -> '+'source => '+str(source))          

                retour=source.copy()
                
                if type(source) is list:
                    retour=NetConfig.ConfigListRegex(root=self,mylist=retour)
                    parse_config_regex_list(self,source=retour)
                
                if type(source) is dict:
                    retour=NetConfig.ConfigDictRegex(root=self,dictionary=retour)
                    parse_config_regex_dict(self,source=retour)
            
            return retour                
                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)   
   
    def _check_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                                                 
            if self._config != None and issubclass(type(self._config),dict) and len(self._config.keys()) > 0 and ( \
                    self._config_regex != None and issubclass(type(self._config_regex),dict) and len(self._config_regex.keys()) > 0 or \
                    self._config_type != None and issubclass(type(self._config_type),dict) and len(self._config_type.keys()) > 0):
                
                config=self._config
                
                config_type={}
                if self._config_type != None and issubclass(type(self._config_type),dict) and len(self._config_type.keys()) > 0:
                    config_type=self._config_type
                
                config_regex={}
                if self._config_regex != None and issubclass(type(self._config_regex),dict) and len(self._config_regex.keys()) > 0:
                    config_regex=self._config_regex

                if self._logger is not None:
                    self._logger.debug('NetConfig@'+ self._id +' ::_check_config -> '+'inspect => '+str(config)+' || '+'config_type => '+str(config_type) +' || '+'config_regex => '+str(config_regex))
                
                if self._config_type != None and issubclass(type(self._config_type),dict) and len(self._config_type.keys()) > 0: 
                    self._check_type(expected_object=dict(self._config_type),inspected_object=dict(self._config))
            
                if self._config_regex != None and issubclass(type(self._config_regex),dict) and len(self._config_regex.keys()) > 0:
                    self._check_regex(expected_object=dict(self._config_regex),inspected_object=dict(self._config))
          
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)      

    @NetClassParameterUnique(old_config=dict,new_config=dict)
    def _update_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            old_config=dict_param_named['old_config']
            new_config=dict_param_named['new_config']

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::_update_config -> '+'old_config => '+str(old_config)+' || '+'new_config => '+str(new_config))            
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception) 
    @NetClassParameterUnique(old_config_type=dict,new_config_type=dict)
    def _update_config_type(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            old_config_type=dict_param_named['old_config_type']
            new_config_type=dict_param_named['new_config_type']    

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::_update_config_type -> '+'old_config_type => '+str(old_config_type)+' || '+'new_config_type => '+str(new_config_type))            
                                         
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)
    @NetClassParameterUnique(old_config_regex=dict,new_config_regex=dict)
    def _update_config_regex(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            old_config_regex=dict_param_named['old_config_regex']
            new_config_regex=dict_param_named['new_config_regex']

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::_update_config_regex -> '+'old_config_regex => '+str(old_config_regex)+' || '+'new_config_regex => '+str(new_config_regex))            
                                        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)                        


    @NetClassParameterUnique(load=dict)
    def _dict_load(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            super(NetConfig,self)._dict_load(*param_no_named,**param_named)
            
            load=dict_param_named['load']
            
            attributes=[
                'config',
                'config_type',
                'config_regex',
                'lock_timeout'
            ]
         
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::_dict_load -> '+'attributes => '+str(attributes))          
            
            for attribut in attributes:
                if attribut not in load.keys():
                    exception={
                        'keys':'['+attribut+']',
                        'error':'missing key',
                        'message':'['+attribut+']'+' not in '+str(list(load.keys()))
                        }
                    
                    if self._logger is not None:
                        self._logger.error('NetConfig::_dict_load -> '+'exception => '+str(exception))                    
                        
                    raise NetExceptionConfig(self._logger,**exception)
            
            self.config=load['config']
            self.config_type=load['config_type']
            self.config_regex=load['config_regex']
            self.lock_timeout=load['lock_timeout']
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)                
    def _dict_save(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            retour=super(NetConfig,self)._dict_save(*param_no_named,**param_named)

            retour['config']=self._parse_original(source=self._config)
            retour['config_type']=self._parse_original(source=self._config_type)
            retour['config_regex']=self._parse_original(source=self._config_regex)
            retour['lock_timeout']=self._lock_timeout
            
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::_dict_save -> '+'keys => '+str(retour.keys()))              
            
            return retour
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)  

    def __init__(self,*param_no_named,**param_named):
        try: 
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            self._config=NetConfig.ConfigDict(root=self,dictionary={})
            self._config_type=NetConfig.ConfigDictType(root=self,dictionary={})
            self._config_regex=NetConfig.ConfigDictRegex(root=self,dictionary={})

            self._lock_timeout=None

            super(NetConfig,self).__init__(*param_no_named,**param_named)

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__init__ -> Creating object')  

            if 'config' in dict_param_named.keys() and issubclass(type(dict_param_named['config']),dict):
                self.config=dict_param_named['config']

            if 'config_type' in dict_param_named.keys() and issubclass(type(dict_param_named['config_type']),dict):
                self.config_type=dict_param_named['config_type']

            if 'config_regex' in dict_param_named.keys() and issubclass(type(dict_param_named['config_regex']),dict):
                self.config_regex=dict_param_named['config_regex']
                    
            if 'lock_timeout' in dict_param_named.keys() and type(dict_param_named['lock_timeout']) is int:
                self.lock_timeout=dict_param_named['lock_timeout']
            else:
                self._lock_timeout=20 

            if self._logger is not None:
                self._logger.info('NetConfig@'+ self._id +' :: object created -> '+'id => ' +self._id)                         
                        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)  

    def __str__(self,*param_no_named,**param_named):
        try:
            
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__str__ -> Getting str')              
            
            return str(json.dumps(self._config,indent=3))
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)  
    def __dict__(self,*param_no_named,**param_named):
        try:
            
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__dict__ -> Getting dict')              
            
            return self._parse_original(source=self._config)
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)  


    @NetClassParameterUnique(str)
    def __getitem__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            index=list_param_no_named[i]

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__getitem__ -> '+'index => '+str(index))        
            
            return self._config[index]              
                        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)  
    @NetClassParameterUnique(str,object)         
    def __setitem__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            index=list_param_no_named[i]
            value=list_param_no_named[i+1]
            
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__setitem__ -> '+'index => '+str(index)+' || '+'value => '+str(value))        
            
            self._config[index]=value
                
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception) 
    @NetClassParameterUnique(str)     
    def __delitem__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            index=list_param_no_named[i]
            
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__delitem__ -> '+'index => '+str(index))        
            

            if index in self._config.keys():
                del self._config[index]

            if index in self._config_type.keys():
                del self._config_type[index]

            if index in self._config_regex.keys():
                del self._config_regex[index]                                

            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)                         

    def clone(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                        
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::copy -> '+'root => '+str(self.__tree.getroot().tag))               
            
            retour=NetConfig(logger=self._logger,config=self._config.copy(),config_type=self._config_type.copy(),config_regex=self._config_regex.copy(),lock_timeout=self._lock_timeout)
   
            return retour

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception) 


    @NetClassParameterCombine([NetClassParameterUnique(file=str),NetClassParameterUnique(str)])
    def load_config_regex(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            input_file=''
            if 'file' in dict_param_named.keys():
                input_file=dict_param_named['file']
            else:
                input_file=list_param_no_named[0]

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::load_config_regex -> '+'input_file => '+str(input_file))     

            self.config_regex=self._load_dictionary_file(file=input_file)

            if self._logger is not None:
                self._logger.info('NetConfig@'+ self._id +' ::load_config_regex -> Success'+' || '+'input_file => '+str(input_file)+' || '+'config_regex => '+str(self._config_regex))   


        except Exception as exception:           
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception) 
    @NetClassParameterCombine([NetClassParameterUnique(file=str),NetClassParameterUnique(str)])
    def load_config_type(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            input_file=''
            if 'file' in dict_param_named.keys():
                input_file=dict_param_named['file']
            else:
                input_file=list_param_no_named[0]

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::load_config_type -> '+'input_file => '+str(input_file))     

            self.config_type=self._load_dictionary_file(file=input_file)

            if self._logger is not None:
                self._logger.info('NetConfig@'+ self._id +' ::load_config_type -> Success'+' || '+'input_file => '+str(input_file)+' || '+'config_type => '+str(self._config_type))               

        except Exception as exception:           
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception) 
    @NetClassParameterCombine([NetClassParameterUnique(file=str),NetClassParameterUnique(str)])
    def load_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            input_file=''
            if 'file' in dict_param_named.keys():
                input_file=dict_param_named['file']
            else:
                input_file=list_param_no_named[0]

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::load_config -> '+'input_file => '+str(input_file))     

            self.config=self._load_dictionary_file(file=input_file)

            if self._logger is not None:
                self._logger.info('NetConfig@'+ self._id +' ::load_config -> Success'+' || '+'input_file => '+str(input_file)+' || '+'config => '+str(self._config))            

        except Exception as exception:           
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception) 


    @NetClassParameterCombine([NetClassParameterUnique(file=str),NetClassParameterUnique(str)])
    def save_config_regex(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            input_file=''
            if 'file' in dict_param_named.keys():
                input_file=dict_param_named['file']
            else:
                input_file=list_param_no_named[0]

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::save_config_regex -> '+'input_file => '+str(input_file))     

            self._save_dictionary_file(file=input_file,dictionary=self._config_regex)

            if self._logger is not None:
                self._logger.info('NetConfig@'+ self._id +' ::save_config_regex -> Success'+' || '+'input_file => '+str(input_file)+' || '+'config_regex => '+str(self._config_regex))             

        except Exception as exception:           
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)
    @NetClassParameterCombine([NetClassParameterUnique(file=str),NetClassParameterUnique(str)])
    def save_config_type(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            input_file=''
            if 'file' in dict_param_named.keys():
                input_file=dict_param_named['file']
            else:
                input_file=list_param_no_named[0]

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::save_config_type -> '+'input_file => '+str(input_file))     

            self._save_dictionary_file(file=input_file,dictionary=self._config_type)

            if self._logger is not None:
                self._logger.info('NetConfig@'+ self._id +' ::save_config_type -> Success'+' || '+'input_file => '+str(input_file)+' || '+'config_type => '+str(self._config_type))             

        except Exception as exception:           
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)
    @NetClassParameterCombine([NetClassParameterUnique(file=str),NetClassParameterUnique(str)])
    def save_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            input_file=''
            if 'file' in dict_param_named.keys():
                input_file=dict_param_named['file']
            else:
                input_file=list_param_no_named[0]

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::save_config -> '+'input_file => '+str(input_file))     

            self._save_dictionary_file(file=input_file,dictionary=self._config)

            if self._logger is not None:
                self._logger.info('NetConfig@'+ self._id +' ::save_config -> Success'+' || '+'input_file => '+str(input_file)+' || '+'config => '+str(self._config))     

        except Exception as exception:           
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception) 



    @NetClassParameterUnique(file=str)
    def _load_dictionary_file(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            extensions=[
                'json',
                'yml'
            ]

            input_file=dict_param_named['file']
            retour={}

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::_load_dictionary_file -> '+'input_file => '+str(input_file))           
                        
            extension=re.sub('.*\\.(?P<EXTENSION>[^\\.][^\\.]*)$','\\g<EXTENSION>',input_file).lower()
            if extension not in extensions:
                exception={
                    'error':'extension is not supported',
                    'expected_extensions':str(extensions),
                    'inspected_extension': extension,
                    'source_path':input_file,
                    'message':extension+" is not supported"
                    }

                if self._logger is not None:
                    self._logger.error('NetConfig@'+ self._id +' ::_load_dictionary_file -> '+'exception => '+str(exception))                         
                        
                raise NetExceptionConfig(self._logger,**exception)
            elif extension == 'json' :
                retour=self._str_load_file(file=input_file,timeout=self._lock_timeout)
                retour=json.loads(retour)        
            elif extension == 'yml':
                 retour=self._str_load_file(file=input_file,timeout=self._lock_timeout)
                 retour=yaml.safe_load(retour) 

            return retour

        except Exception as exception:           
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception) 
    @NetClassParameterUnique(file=str,dictionary=dict)
    def _save_dictionary_file(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            extensions=[
                'json',
                'yml'
            ]

            output_file=dict_param_named['file']
            dictionary=self._parse_original(source=dict_param_named['dictionary'])
           
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::_save_dictionary_file -> '+'output_file => '+str(output_file)+' || '+'dictionary => '+str(dictionary))           
                        
            extension=re.sub('.*\\.(?P<EXTENSION>[^\\.][^\\.]*)$','\\g<EXTENSION>',output_file).lower()
            if extension not in extensions:
                exception={
                    'error':'extension is not supported',
                    'expected_extensions':str(extensions),
                    'inspected_extension': extension,
                    'source_path':output_file,
                    'message':extension+" is not supported"
                    }

                if self._logger is not None:
                    self._logger.error('NetConfig@'+ self._id +' ::_save_dictionary_file -> '+'exception => '+str(exception))                         
                        
                raise NetExceptionConfig(self._logger,**exception)
            elif extension == 'json' :
                self._str_save_file(file=output_file,data=str(json.dumps(dictionary,indent=3,sort_keys=False)),timeout=self._lock_timeout)
            elif extension == 'yml':
                self._str_save_file(file=output_file,data=str(yaml.dump(dictionary,indent=3,sort_keys=False)),timeout=self._lock_timeout)


        except Exception as exception:           
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception) 
 

    @NetClassParameterUnique(int)
    def __set_lock_timeout(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not int:
                i=i+1
            timeout=list_param_no_named[i]
                 
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__set_lock_timeout -> '+'timeout => '+str(timeout))                  
            
            self._lock_timeout=timeout
       
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)        
    def __get_lock_timeout(self,*param_no_named,**param_named):
        try:
            
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__get_lock_timeout -> '+'timeout => '+str(self._lock_timeout))             
            
            return self._lock_timeout
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception) 
    lock_timeout=property(__get_lock_timeout,__set_lock_timeout)
    
    @NetClassParameterUnique(dict)
    def __set_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            old_config=self._parse_original(source=self._config)
            
            i=0
            while not issubclass(type(list_param_no_named[i]),dict):
                i=i+1

            config=self._parse_original(source=list_param_no_named[i])     

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__set_config -> '+'config => '+str(config))   

            self._config=self._parse_config(source=config)

            if self._logger is not None:
                self._logger.info('NetConfig@'+ self._id +' ::__set_config -> Success'+' || '+'config => '+str(config))    

            if self._check_same_object(source1=old_config,source2=config) is False:
                self._check_config()            
                self._update_config(old_config=old_config,new_config=config)



        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)    
    def __get_config(self,*param_no_named,**param_named):
        try:
            
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__get_config -> '+str(self._config))             
            
            return self._config
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)
    config=property(__get_config,__set_config)

    @NetClassParameterUnique(dict)
    def __set_config_regex(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            old_config_regex=self._parse_original(source=self._config_regex)

            i=0
            while not issubclass(type(list_param_no_named[i]),dict):
                i=i+1

            config_regex=self._parse_original(source=list_param_no_named[i])     

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__set_config_regex -> '+'config_regex => '+str(config_regex))      
             
            self._config_regex=self._parse_config_regex(source=config_regex)

            if self._logger is not None:
                self._logger.info('NetConfig@'+ self._id +' ::__set_config_regex -> Success'+' || '+'config_regex => '+str(config_regex))    

            if self._check_same_object(source1=old_config_regex,source2=config_regex) is False:
                self._check_config()                
                self._update_config_regex(old_config_regex=old_config_regex,new_config_regex=config_regex)


        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)    
    def __get_config_regex(self,*param_no_named,**param_named):
        try:
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__get_config_regex -> '+'regex => '+str(self._config_regex))             
            
            return self._config_regex
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)
    config_regex=property(__get_config_regex,__set_config_regex)

    @NetClassParameterUnique(dict)
    def __set_config_type(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            old_config_type=self._parse_original(source=self._config_type)

            i=0
            while not issubclass(type(list_param_no_named[i]),dict):
                i=i+1

            config_type=self._parse_original(source=list_param_no_named[i])     

            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__set_config_type -> '+'config_type => '+str(config_type))  
            
            self._config_type=self._parse_config_type(source=config_type)

            if self._logger is not None:
                self._logger.info('NetConfig@'+ self._id +' ::__set_config_type -> Success'+' || '+'config_type => '+str(config_type))              

            if self._check_same_object(source1=old_config_type,source2=config_type) is False:
                self._check_config()                
                self._update_config_type(old_config_type=old_config_type,new_config_type=config_type)


        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)    
    def __get_config_type(self,*param_no_named,**param_named):
        try:
            
            if self._logger is not None:
                self._logger.debug('NetConfig@'+ self._id +' ::__get_config_type -> '+str(self._config_type))             
            
            return self._config_type
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)
    config_type=property(__get_config_type,__set_config_type)

