# pylint: disable=unused-variable
__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

import NetLib
from NetLib.NetClasses.NetException.NetException import NetException
from NetLib.NetClasses.NetRequests.NetRequests import NetRequests,NetTypeRequests,NetExceptionRequests,NetTypeExcpetionRequests
from NetLib.NetClasses.NetNotification.NetTypeNotification import NetTypeNotification
from NetLib.NetClasses.NetClassParatemter.NetClassParameter import NetClassParameterUnique,NetClassParameterContains
import re
import json
import requests
import urllib3
import os
from lxml import etree


class NetTypeInfoblox(NetTypeRequests):
    def __new__( self, classname, superclasses, attributdict):
        return super(NetTypeInfoblox,self).__new__(classname, superclasses, attributdict)

class NetTypeExcpetionInfoblox(NetTypeExcpetionRequests):
    def __new__( self, classname, superclasses, attributdict):
        return super(NetTypeExcpetionInfoblox,self).__new__(classname, superclasses, attributdict)

class NetExceptionInfoblox(NetExceptionRequests,metaclass=NetTypeExcpetionInfoblox):
    __metaclass__=NetTypeExcpetionInfoblox
    
    def __setnull(self,param):
        try:
            ex=Exception(str(param)+ ' cannot be defined the parameter is on read only')
            raise ex
        except Exception as ex:
            raise ex
        return None  

    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                
            if 'values' in dict_param_named.keys() and 'Error' in dict_param_named['values'].keys()  and 'code' in dict_param_named['values'].keys() and 'text' in dict_param_named['values'].keys() and 'trace' not in dict_param_named['values'].keys():
                dict_param_named['values']['trace']='debug mode is off'
            
            super(NetExceptionInfoblox,self).__init__(*list_param_no_named,**dict_param_named)
        except Exception as ex:
            raise ex
          
    def __str__(self):
        try:
            return super(NetExceptionInfoblox,self).__str__()
        except Exception as ex:
            raise ex



class NetInfoblox(NetRequests,metaclass=NetTypeInfoblox):
    __metaclass__=NetTypeInfoblox

    __DEFAULT_CONFIG=os.path.dirname(NetLib.NetClasses.NetRequests.NetInfoblox.__file__)+os.path.sep+'NetInfoblox.yml'
    __BACKUP_CONFIG={
        "url": "https://URL",
        "ca": {
            " trusted_ca": False,
            "crt": "",
            "key": ""
            },
        "headers": {
            "content-type": "application/json"
            },
        "cookies": {},
        "parameters": {
            "_return_as_object": "1"
            },
        "proxies": {
            "http": "",
            "https": ""
            },
        "authentication": {
            "user": "netautomation",
            "password": "PASSWORD"
            }
        }

    __DEFAULT_VERSION='wapi/v1.0'
    
    __ADDITIONALS_ARGUMENTS=[
        '_max_results',
        '_return_fields',
        '_schema',
        '_return_as_object',
        '_paging'
    ]
    
    
    @NetClassParameterContains(config=dict,path_keys=list)
    def _check_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            minimum_config={
                "url": "https://URL",
                'ca': {
                    'trusted_ca': False,
                    'crt': '',
                    'key': ''
                    },
                'headers': {
                    "content-type": "application/json"
                    },
                'cookies': {},
                'parameters': { },
                'proxies': {
                    'http': '',
                    'https': ''
                    },
                'authentication': {
                    'user': 'netautomation',
                    'password': 'PASSWORD'
                    }
                }
            path_keys=dict_param_named['path_keys']
            config=dict_param_named['config']
            from_keys=''
            for line in path_keys:
                from_keys=from_keys+'['+line+']'

            for keys in path_keys:
                minimum_config=minimum_config[keys]
                             
            for keys in minimum_config.keys():
                str_keys=from_keys+'['+keys+']'  

                if keys not in config.keys():
                    exception={
                        'class_name':'NetInfoblox',
                        'method_name':'_check_config(self,*param_no_named,**param_named)',
                        'exception_source':'self',
                        'exception_type': type(NetExceptionInfoblox),
                        'values':{
                            'keys':str_keys,
                            'error':'missing key',
                            'message':keys+' not defined in '+from_keys+' with keys '+str(list(config.keys()))
                            }
                        }
                    ex=NetExceptionRequests(**exception)
                    raise ex
                else:
                    if type(minimum_config[keys]) is not type(config[keys]):                        
                        exception={
                            'class_name':'NetInfoblox',
                            'method_name':'_check_config(self,*param_no_named,**param_named)',
                            'exception_source':'self',
                            'exception_type': type(NetExceptionInfoblox),
                            'values':{
                                'keys':str_keys,
                                'error':'wrong type',
                                'expected_type': re.sub("<class '(?P<NAME>[^'][^']*)'>",'\\g<NAME>',str(type(minimum_config[keys]))),
                                'source_type': re.sub("<class '(?P<NAME>[^'][^']*)'>",'\\g<NAME>',str(type(config[keys]))),
                                'message':str_keys+' expected type : '+str(type(minimum_config[keys]))
                                }
                            }
                        ex=NetExceptionRequests(**exception)
                        raise ex
                    else:
                        if type(minimum_config[keys]) is dict and len(minimum_config[keys].keys()) > 0:
                            self._check_config(config=config[keys],path_keys=path_keys+[keys])
                        
            
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'_check_config(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)      
       
    
    def __setnull(self,param):
        try:
            exception={
                'class_name':'NetInfoblox',
                'method_name':'__setnull(self,param)',
                'exception_source':'self',
                'exception_type': type(NetExceptionInfoblox),
                'values':{
                    'property':param,
                    'error':'read only property',
                    'message':param+' is only reachable as read only property'
                }
            }
            ex=NetExceptionRequests(**exception)
            raise ex
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'__setnull(self,param)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception) 
    
      
    def __init__(self,*param_no_named,**param_named):    
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                        
            self.FILE_TIMEOUT=20
            self.__list_objects=None
            self.__list_versions=None
            self.__version=''
                        
            if 'path-source' in dict_param_named.keys() and type(dict_param_named['path-source'] is str):
                super(NetInfoblox,self).__init__(*list_param_no_named,**dict_param_named)

            else:
                dict_param_named['path-source']=self.__DEFAULT_CONFIG
                super(NetInfoblox,self).__init__(*list_param_no_named,**dict_param_named)
                        
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'__init__(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)
        
    @property
    def api(self):
        return self.url+'/'+self.version
        
    def _init_session(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            authentication=requests.auth.HTTPBasicAuth(username=self.authentication_user,password=self.authentication_password)            
            requests_config=self._requests_config(*param_no_named,**param_named)
            requests_config['auth']=authentication
            requests_config['url']=self.url+'/'+self.__DEFAULT_VERSION+'/'
            requests_config['params']['_schema']='1'
            
            urllib3.disable_warnings()
            
            r=requests.get(**requests_config)
            if r.status_code < 200 or r.status_code > 299:
                root = etree.HTML(r.text)
                if len(root) > 1:
                    title = re.sub("  *"," ",root[0][0].text)
                    body =  re.sub("  *"," ",root[1][1].text.replace('\n',' '))
                elif len(root) == 1:
                    title = "N/A"
                    body =  re.sub("  *"," ",root[0][1].text.replace('\n',' '))                    
                                    
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'_init_session(self,*param_no_named,**param_named)',
                    'exception_source':'self',
                    'exception_type': type(NetExceptionInfoblox),
                    'values':{
                        'response':r,
                        'title':title,
                        'body':body
                    }
                }
                ex=NetExceptionInfoblox(**exception)
                raise ex
                
        
            self.cookies=dict(r.cookies)
            
            data=r.json()['result']
            supported_versions=list()            
            for version in data['supported_versions']:
                supported_versions.append('wapi/v'+version)
            self.__list_versions=supported_versions
            
            self.version=self.__list_versions[-1]
                              
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'_init_session(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionInfoblox(**exception)
                
    def __get_list_objects(self,*param_no_named,**param_named):
        try:
            return self.__list_objects
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'__get_list_objects(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)
    list_objects=property(__get_list_objects,__setNULL)     
    def __get_list_versions(self,*param_no_named,**param_named):
        try:
            return self.__list_versions
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'__get_list_versions(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)
    list_versions=property(__get_list_versions,__setNULL)
        
    @NetClassParameterContains(str)
    def __set_version(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            version=list_param_no_named[i]
            
            if version in self.__list_versions:
                self.__version=version
                
                requests_config=self._requests_config(*param_no_named,**param_named)            
                requests_config['url']=self.url+'/'+self.__version+'/'
                requests_config['params']['_schema']='1'

                r=requests.get(**requests_config)
            
                data=r.json()['result']
                self.__list_objects=data['supported_objects']
                
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'__set_version(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)       
    def __get_version(self,*param_no_named,**param_named):
        try:
            return self.__version
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'__get_version(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)
    version=property(__get_version,__set_version)
    
    @NetClassParameterContains(resource=str)
    def get(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            retour=list()

            if '_paging' not in self.parameters.keys():
                self.parameters['_paging']='1'
            
            if '_max_results' not in self.parameters.keys():
                self.parameters['_max_results']='900'
            
            if 'data' in self.parameters.keys():
                self.parameters['json']=self.parameters['data']
                del self.parameters['data']
            
            end=False
            while end != True:
                end=True
                
                r=super(NetInfoblox,self).get(*list_param_no_named,**dict_param_named)
                
                data=r.json()
                if 'result' in data.keys():
                    retour=retour+data['result']
                
                if 'next_page_id' in data.keys():
                    end=False
                    self.parameters['_page_id']=data['next_page_id']
                              
            return retour
        
        except NetExceptionRequests as ex:    
            if ex.content['method_name'] == 'get(self,*param_no_named,**param_named)':
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'get(self,*param_no_named,**param_named)',
                    'exception_source':"self",
                    'exception_type': type(NetExceptionInfoblox),
                    'values':ex.content["values"]
                    }                 
                for keys in exception['values']['response'].json().keys():
                    exception['values'][keys]= exception['values']['response'].json()[keys]
    
                raise NetExceptionInfoblox(**exception)                                            
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'get(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)
    @NetClassParameterContains(resource=str)
    def post(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            retour=list()

            if '_paging' not in self.parameters.keys():
                self.parameters['_paging']='1'
            
            if '_max_results' not in self.parameters.keys():
                self.parameters['_max_results']='900'
            
            if 'data' in self.parameters.keys():
                self.parameters['json']=self.parameters['data']
                del self.parameters['data']
            
            end=False
            while end != True:
                end=True
                
                r=super(NetInfoblox,self).post(*list_param_no_named,**dict_param_named)
                
                data=r.json()
                if 'result' in data.keys():
                    retour=retour+data['result']
                
                if 'next_page_id' in data.keys():
                    end=False
                    self.parameters['_page_id']=data['next_page_id']       
              
            return retour
        except NetExceptionRequests as ex:    
            if ex.content['method_name'] == 'post(self,*param_no_named,**param_named)':
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'post(self,*param_no_named,**param_named)',
                    'exception_source':"self",
                    'exception_type': type(NetExceptionInfoblox),
                    'values':ex.content["values"]
                    }                 
                for keys in exception['values']['response'].json().keys():
                    exception['values'][keys]= exception['values']['response'].json()[keys]
    
                raise NetExceptionInfoblox(**exception)                                            
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'post(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)
    @NetClassParameterContains(resource=str)
    def options(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            retour=list()

            if '_paging' not in self.parameters.keys():
                self.parameters['_paging']='1'
            
            if '_max_results' not in self.parameters.keys():
                self.parameters['_max_results']='900'
            
            if 'data' in self.parameters.keys():
                self.parameters['json']=self.parameters['data']
                del self.parameters['data']
            
            end=False
            while end != True:
                end=True
                
                r=super(NetInfoblox,self).options(*list_param_no_named,**dict_param_named)
                
                data=r.json()
                if 'result' in data.keys():
                    retour=retour+data['result']
                
                if 'next_page_id' in data.keys():
                    end=False
                    self.parameters['_page_id']=data['next_page_id']       
              
            return retour
        except NetExceptionRequests as ex:    
            if ex.content['method_name'] == 'options(self,*param_no_named,**param_named)':
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'options(self,*param_no_named,**param_named)',
                    'exception_source':"self",
                    'exception_type': type(NetExceptionInfoblox),
                    'values':ex.content["values"]
                    }                 
                for keys in exception['values']['response'].json().keys():
                    exception['values'][keys]= exception['values']['response'].json()[keys]
    
                raise NetExceptionInfoblox(**exception)                                            
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'options(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)
    @NetClassParameterContains(resource=str)
    def head(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            retour=list()

            if '_paging' not in self.parameters.keys():
                self.parameters['_paging']='1'
            
            if '_max_results' not in self.parameters.keys():
                self.parameters['_max_results']='900'
            
            if 'data' in self.parameters.keys():
                self.parameters['json']=self.parameters['data']
                del self.parameters['data']
            
            end=False
            while end != True:
                end=True
                
                r=super(NetInfoblox,self).head(*list_param_no_named,**dict_param_named)
                
                data=r.json()
                if 'result' in data.keys():
                    retour=retour+data['result']
                
                if 'next_page_id' in data.keys():
                    end=False
                    self.parameters['_page_id']=data['next_page_id']       
              
            return retour
        except NetExceptionRequests as ex:    
            if ex.content['method_name'] == 'head(self,*param_no_named,**param_named)':
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'head(self,*param_no_named,**param_named)',
                    'exception_source':"self",
                    'exception_type': type(NetExceptionInfoblox),
                    'values':ex.content["values"]
                    }                 
                for keys in exception['values']['response'].json().keys():
                    exception['values'][keys]= exception['values']['response'].json()[keys]
    
                raise NetExceptionInfoblox(**exception)                                            
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'head(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)
    @NetClassParameterContains(resource=str)
    def put(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            retour=list()

            if '_paging' not in self.parameters.keys():
                self.parameters['_paging']='1'
            
            if '_max_results' not in self.parameters.keys():
                self.parameters['_max_results']='900'
            
            if 'data' in self.parameters.keys():
                self.parameters['json']=self.parameters['data']
                del self.parameters['data']
            
            end=False
            while end != True:
                end=True
                
                r=super(NetInfoblox,self).put(*list_param_no_named,**dict_param_named)
                
                data=r.json()
                if 'result' in data.keys():
                    retour=retour+data['result']
                
                if 'next_page_id' in data.keys():
                    end=False
                    self.parameters['_page_id']=data['next_page_id']       
              
            return retour
        except NetExceptionRequests as ex:    
            if ex.content['method_name'] == 'put(self,*param_no_named,**param_named)':
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'put(self,*param_no_named,**param_named)',
                    'exception_source':"self",
                    'exception_type': type(NetExceptionInfoblox),
                    'values':ex.content["values"]
                    }                 
                for keys in exception['values']['response'].json().keys():
                    exception['values'][keys]= exception['values']['response'].json()[keys]
    
                raise NetExceptionInfoblox(**exception)                                            
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'put(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)
    
    def print_objects(self,*param_no_named,**param_named):
        try:
            for obj in self.list_objects:
                print(obj)
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'print_objects(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)
    def print_versions(self,*param_no_named,**param_named):
        try:
            for version in self.list_versions:
                print(version)
        except Exception as ex:
            if issubclass(type(ex),NetException):
                raise ex
            else:            
                exception={
                    'class_name':'NetInfoblox',
                    'method_name':'print_versions(self,*param_no_named,**param_named)',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise NetExceptionRequests(**exception)