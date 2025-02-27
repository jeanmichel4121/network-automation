# pylint: disable=unused-variable
__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

import NetLib
from NetLib.NetClasses.NetException.NetException import NetException
from NetLib.NetClasses.NetConfig.NetConfigFile.NetConfigFile import NetTypeConfigFile,NetTypeExcpetionConfigFile,NetExceptionConfigFile,NetConfigFile
from NetLib.NetClasses.NetClassParatemter.NetClassParameter import NetClassParameterContains,NetClassParameterUnique,NetClassParameterCombine
import re
import os
import json
import yaml
import base64
import requests
import urllib3

from logging import Logger
from abc import ABC,abstractmethod,abstractproperty,ABCMeta
from lxml import etree
import xmltodict

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from filelock import Timeout, FileLock


class NetTypeRequests(NetTypeConfigFile):
    def __new__( self, classname, superclasses, attributdict):
        return super(NetTypeRequests,self).__new__(classname, superclasses, attributdict)

class NetTypeExcpetionRequests(NetTypeExcpetionConfigFile):
    def __new__( self, classname, superclasses, attributdict):
        return super(NetTypeExcpetionRequests,self).__new__(classname, superclasses, attributdict)

class NetExceptionRequests(NetExceptionConfigFile,metaclass=NetTypeExcpetionRequests):
    __metaclass__=NetTypeExcpetionRequests
     
    def __init__(self,*param_no_named,**param_named):
        list_param_no_named=list(param_no_named)
        dict_param_named=dict(param_named)
                                    
        super(NetExceptionRequests,self).__init__(*list_param_no_named,**dict_param_named)
        self._config['exception']['content']['class_name']='NetRequests'
    def __str__(self):
        return super(NetExceptionRequests,self).__str__()
    

class NetRequests(NetConfigFile,metaclass=NetTypeRequests):
    __metaclass__=NetTypeRequests
    
    
    _DEFAULT_SOURCE=os.path.dirname(NetLib.NetClasses.NetRequests.__file__)+os.path.sep+'NetRequests.yml'
    
    _DEFAULT_TYPE_CONFIG={
                    'requests':{
                        'url': ':',
                        'ca': {
                            'trusted_ca': False,
                            'crt': '',
                            'key': ''
                            },
                        'headers': {},
                        'cookies': {},
                        'parameters': {},
                        'proxies': {
                            'http': '',
                            'https': ''
                            },
                        'parsers':{
                            'html': {},
                            'xml':{}
                        },
                        'authentication': {
                            'user': '',
                            'password': ''
                            }
                        }
                    }
    
    _DEFAULT_REGEX_CONFIG={
    }
    
    _BACKUP_CONFIG={
                'requests':{
                    'url': 'https://google.com',
                    'ca': {
                        'trusted_ca': False,
                        'crt': '',
                        'key': ''
                        },
                    'headers': {
                        'content-type': 'application/json'
                        },
                    'cookies': {},
                    'parameters': {},
                    'parsers':{
                        'html': {
                            'encoding': 'utf-8',
                            'remove_blank_text': True
                            },
                        'xml':{
                            'encoding': 'utf-8',
                            'ns_clean': True,
                            'remove_blank_text': True
                            }
                        },
                    'proxies': {
                        'http': '',
                        'https': ''
                        },
                    'authentication': {
                        'user': 'netautomation',
                        'password': 'PASSWORD'
                        }
                    }
                }

    
    @NetClassParameterUnique(config=dict)
    def _update_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            config=dict_param_named['config']
            
            self.__headers=config['requests']['headers'].copy()
            self.__cookies=config['requests']['cookies'].copy()
            self.__parameters=config['requests']['parameters'].copy()            
            
            if self._logger != None:
                self._logger.debug('NetRequests::_update_config => '+str(config))            
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception)        
    
    @NetClassParameterUnique(config=dict)    
    def _update_config_updated(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            config=dict_param_named['config']
            
            headers=self._dict_difference(diff=[ self._config['requests']['headers'], self.headers])
            cookies=self._dict_difference(diff=[ self._config['requests']['cookies'], self.cookies])
            parameters=self._dict_difference(diff=[ self._config['requests']['parameters'], self.parameters])
                        
            self.__headers=config['requests']['headers'].copy()
            self.__cookies=config['requests']['cookies'].copy()
            self.__parameters=config['requests']['parameters'].copy()            

            self.headers=headers
            self.cookies=cookies
            self.parameters=parameters                   
                        
            if self._logger != None:
                self._logger.debug('NetRequests::_update_config_Updated => '+str(config)) 
                
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception)


    @NetClassParameterUnique(load=dict)
    def _dict_load(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            super(NetRequests,self)._dict_load(*list_param_no_named,**dict_param_named)
            
            load=dict_param_named['load']
            
            attributes=[
            ]
            
            if self._logger != None:
                self._logger.debug('NetRequests::_dict_load => '+str(attributes))                
            
            for attribut in attributes:
                if attribut not in dict_param_named.keys():
                    exception={
                        'keys':'['+attribut+']',
                        'error':'missing key',
                        'message':'['+attribut+']'+' not in '+str(list(dict_param_named.keys()))
                        }
                
                    if self._logger != None:
                        self._logger.error('NetRequests::_dict_load => '+str(exception))                    
                        
                    raise NetExceptionRequests(self._logger,**exception)            
            return
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception)  
    def _dict_save(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            retour=super(NetRequests,self)._dict_save(*list_param_no_named,**dict_param_named)
            
            if self._logger != None:
                self._logger.debug('NetRequests::_dict_save => '+str(retour.keys()))  
            
            return retour
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception)  
      

    def __init__(self,*param_no_named,**param_named):
        try: 
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            super(NetRequests,self).__init__(*list_param_no_named,**dict_param_named)        
                        
            if self._logger != None:
                self._logger.debug('NetRequests::__init__ => Creating object')            
            
            
            self.__REQUESTS_KWARGS=self.__get_requests_kwargs(*list_param_no_named,**dict_param_named)           

        
            if self._logger != None:
                self._logger.info('NetRequests object created => '+"url => "+self._config['requests']['url'].replace('\n',' | ')+" :: "+"user => "+str(self._config['requests']['authentication']['user']))            
            
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception)  
    def __str__(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__str__ => Getting str')              
            
            return "url => "+self._config['requests']['url'].replace('\n',' | ')+" :: "+"user => "+str(self._config['requests']['authentication']['user'])
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception)  


    def __get_requests_kwargs(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            kwargs=[]
            
            for line in requests.request.__doc__.splitlines():
                  match=re.search('^ *:param  *(?P<KARGS>[^:][^:]*):.*',line)
                  if match:
                        kwargs.append(match.group('KARGS'))
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_requests_kwargs => '+str(kwargs))             
            
            return kwargs
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 


    @NetClassParameterUnique(dict)
    def __set_headers(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not dict:
                i=i+1
            headers=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_headers => '+str(headers))             
            
            self._config['requests']['headers']=self._dict_concatenation(fusion=[self.__headers,headers])          
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception)      
    def __get_headers(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_headers => '+str(self._config['requests']['headers']))             
            
            return self._config['requests']['headers']
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    headers=property(__get_headers,__set_headers)


    @NetClassParameterUnique(dict)
    def __set_cookies(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not dict:
                i=i+1
            cookies=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_cookies => '+str(cookies))            

            self._config['requests']['cookies']=self._dict_concatenation(fusion=[self._config['requests']['cookies'],cookies])          
    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception)      
    def __get_cookies(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_cookies => '+str(self._config['requests']['cookies']))              
            
            return self._config['requests']['cookies']
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    cookies=property(__get_cookies,__set_cookies)
    def clean_cookies(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            cookies=self._config['requests']['cookies'].copy()
            
            if self._logger != None:
                self._logger.debug('NetRequests::clean_cookies => '+str(cookies))             
            
            self._config['requests']['cookies']=cookies
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception)


    @NetClassParameterContains(dict)
    def __set_parameters(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not dict:
                i=i+1
            parameters=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_parameters => '+str(parameters))            
            
            self._config['requests']['parameters']=self._dict_concatenation(fusion=[self.__parameters,parameters])          
                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    def __get_parameters(self,*param_no_named,**param_named):
        try:    
            if self._logger != None:
                self._logger.debug('NetRequests::__get_parameters => '+str(self._config['requests']['parameters']))             
            
            return self._config['requests']['parameters']
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    parameters=property(__get_parameters,__set_parameters)


    @NetClassParameterUnique(str)
    def __set_proxy_http(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            http=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_proxy_http => '+str(http))             
            
            self._config['requests']['proxies']['http']=http
            self._upgrade_source(updated={'requests:':self._config['requests']})

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    def __get_proxy_http(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_proxy_http => '+str(self._config['requests']['proxies']['http']))             
            
            return self._config['requests']['proxies']['http']
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    proxy_http=property(__get_proxy_HTTP,__set_proxy_HTTP)


    @NetClassParameterUnique(str)
    def __set_proxy_https(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            https=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_proxy_httpS => '+str(https))                
            
            self._config['requests']['proxies']['https']=https
            self._upgrade_source(updated={'requests:':self._config['requests']})

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    def __get_proxy_https(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_proxy_httpS => '+str(self._config['requests']['proxies']['https']))             
            
            return self._config['requests']['proxies']['https']

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    proxy_https=property(__get_proxy_HTTPS,__set_proxy_HTTPS)


    @NetClassParameterUnique(dict)
    def __set_parser_html(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not dict:
                i=i+1
            html=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_parser_html => '+str(html))                
            
            self._config['requests']['parsers']['html']=html
            self._upgrade_source(updated={'requests:':self._config['requests']})

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    def __get_parser_html(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_parser_html => '+str(self._config['requests']['parsers']['html']))             
            
            return etree.HTMLParser(**self._config['requests']['parsers']['html'])

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    parser_html=property(__get_parser_HTML,__set_parser_HTML)


    @NetClassParameterUnique(dict)
    def __set_parser_xml(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not dict:
                i=i+1
            xml=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_parser_xml => '+str(xml))              
            
            self._config['requests']['parsers']['xml']=xml
            self._upgrade_source(updated={'requests:':self._config['requests']})
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    def __get_parser_xml(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_parser_xml => '+str(self._config['requests']['parsers']['xml']))               
            
            return etree.XMLParser(**self._config['requests']['parsers']['xml'])
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    parser_xml=property(__get_parser_XML,__set_parser_XML)


    @NetClassParameterUnique(str)
    def __set_authentication_user(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            user=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_authentication_user => '+str(user))            
            
            self._config['requests']['authentication']['user']=user
            self._upgrade_source(updated={'requests:':self._config['requests']})

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception)   
    def __get_authentication_user(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_authentication_user => '+str(self._config['requests']['authentication']['user']))              
            
            return self._config['requests']['authentication']['user']
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    authentication_user=property(__get_authentication_user,__set_authentication_user)


    @NetClassParameterUnique(str)
    def __set_authentication_password(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            password=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_authentication_password => '+str(password))             
            
            self._config['requests']['authentication']['password']=password
            self._upgrade_source(updated={'requests:':self._config['requests']})

        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception)    
    def __get_authentication_password(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_authentication_password => '+str(self._config['requests']['authentication']['password']))               
            
            return self._config['requests']['authentication']['password']
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    authentication_password=property(__get_authentication_password,__set_authentication_password)


    @NetClassParameterUnique(str)
    def __set_url(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            url=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_url => '+str(url))               
            
            self._config['requests']['url']=url
            self._upgrade_source(updated={'requests:':self._config['requests']})

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    def __get_url(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_url => '+str(self._config['requests']['url']))             
            
            return self._config['requests']['url']     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    url=property(__get_url,__set_url)


    @NetClassParameterUnique(bool)
    def __set_trusted_ca(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not bool:
                i=i+1
            verify=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_trusted_ca => '+str(verify))             
            
            self._config['requests']['ca']['trusted_ca']=verify
            self._upgrade_source(updated={'requests:':self._config['requests']})

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    def __get_trusted_ca(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_trusted_ca => '+str(self._config['requests']['ca']['trusted_ca']))                 
            
            return self._config['requests']['ca']['trusted_ca']

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    trusted_ca=property(__get_trusted_ca,__set_trusted_ca)


    @NetClassParameterUnique(str)
    def __set_path_certificate(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            crt=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_path_certificate => '+str(crt))              
            
            self._config['requests']['ca']['crt']=crt
            self._upgrade_source(updated={'requests:':self._config['requests']})

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    def __get_path_certificate(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_path_certificate => '+str(self._config['requests']['ca']['crt']))             
            
            return self._config['requests']['ca']['crt']
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    path_certificate=property(__get_path_certificate,__set_path_certificate)
   
    
    @NetClassParameterUnique(str)
    def __set_path_key(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            key=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetRequests::__set_path_key => '+str(key))                
            
            self._config['requests']['ca']['key']=key 
            self._upgrade_source(updated={'requests:':self._config['requests']})
    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    def __get_path_key(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetRequests::__get_path_key => '+str(self._config['requests']['ca']['key']))             
            
            return self._config['requests']['ca']['key']

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    path_key=property(__get_path_key,__set_path_key)


    def _requests_config(self,*param_no_named,**param_named):
        try:
            retour={}
            retour['headers']=self._config['requests']['headers'].copy()
            retour['cookies']=self._config['requests']['cookies'].copy()
            retour['params']=self._config['requests']['parameters'].copy()
            retour['verify']=self._config['requests']['ca']['trusted_ca']
            retour['proxies']=self._config['requests']['proxies'].copy()               
            
            if self._config['requests']['ca']['crt'] != '' and self._config['requests']['ca']['key'] != '':
                retour['cert']=(self._config['requests']['ca']['crt'],self._config['requests']['ca']['key'])
            elif self._config['requests']['ca']['crt'] != '':
                retour['cert']=self._config['requests']['ca']['crt']
            else:
                retour['cert']=''
            
            if self._logger != None:
                self._logger.debug('NetRequests::_requests_config => '+str(retour)) 
                            
            return retour
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 

    @abstractproperty
    def api(self):
        pass
    @abstractmethod
    def _init_session(self,*param_no_named,**param_named):
        pass
    def init_connection(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetRequests::init_connection => '+str(self._config['requests']['url']))
                            
            self._init_session(*list_param_no_named,**dict_param_named)
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 

    @NetClassParameterContains(uri=str)
    def get(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            request_config=self._requests_config(*list_param_no_named,**dict_param_named)
            
            for param in dict_param_named.keys():
                if param != 'uri' and param in self.__REQUESTS_KWARGS:
                    request_config[param]=dict_param_named[param]
                elif param == 'uri':
                    request_config['url']=self.api+'/'+dict_param_named[param]
            
            if self._logger != None:
                self._logger.debug('NetRequests::get => '+str(request_config))             
            
            response=requests.get(**request_config)
                            
            if response.status_code < 200 or response.status_code > 299:
         
                exception={
                    'url':str(response.url),
                    'response':response
                    }
                
                if self._logger != None:
                    self._logger.error('NetRequests::get => '+str(exception))                  
                
                raise NetExceptionRequests(self._logger,**exception)

            if self._logger != None:
                self._logger.info('NetRequests::get => '+str(request_config['url'])) 

            
            return response
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    @NetClassParameterContains(uri=str)
    def post(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            request_config=self._requests_config(*list_param_no_named,**dict_param_named)
            for param in dict_param_named.keys():
                if param != 'uri' and param in self.__REQUESTS_KWARGS:
                    request_config[param]=dict_param_named[param]
                elif param == 'uri':
                    request_config['url']=self.api+'/'+dict_param_named[param]
            
            if self._logger != None:
                self._logger.debug('NetRequests::post => '+str(request_config))              
            
            response=requests.post(**request_config)

            if response.status_code < 200 or response.status_code > 299:
                                
                exception={
                    'url':str(response.url),
                    'response':response
                    }
                
                if self._logger != None:
                    self._logger.error('NetRequests::post => '+str(exception))                 
                
                raise NetExceptionRequests(self._logger,**exception)
            
            return response
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    @NetClassParameterContains(uri=str)
    def options(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            request_config=self._requests_config(*list_param_no_named,**dict_param_named)
            for param in dict_param_named.keys():
                if param != 'uri' and param in self.__REQUESTS_KWARGS:
                    request_config[param]=dict_param_named[param]
                elif param == 'uri':
                    request_config['url']=self.api+'/'+dict_param_named[param]

            if self._logger != None:
                self._logger.debug('NetRequests::options => '+str(request_config))  

            response=requests.options(**request_config)

            if response.status_code < 200 or response.status_code > 299:
                                
                exception={
                    'url':str(response.url),
                    'response':response
                    }
                
                if self._logger != None:
                    self._logger.error('NetRequests::options => '+str(exception))                 
                
                raise NetExceptionRequests(self._logger,**exception)
            
            return response
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    @NetClassParameterContains(uri=str)
    def head(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            request_config=self._requests_config(*list_param_no_named,**dict_param_named)
            for param in dict_param_named.keys():
                if param != 'uri' and param in self.__REQUESTS_KWARGS:
                    request_config[param]=dict_param_named[param]
                elif param == 'uri':
                    request_config['url']=self.api+'/'+dict_param_named[param]
            
            if self._logger != None:
                self._logger.debug('NetRequests::head => '+str(request_config))              
            
            response=requests.head(**request_config)

            if response.status_code < 200 or response.status_code > 299:
                                
                exception={
                    'url':str(response.url),
                    'response':response
                    }
                
                if self._logger != None:
                    self._logger.error('NetRequests::head => '+str(exception))                 
                
                raise NetExceptionRequests(self._logger,**exception)
            
            return response
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    @NetClassParameterContains(uri=str)
    def put(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            request_config=self._requests_config(*list_param_no_named,**dict_param_named)
            for param in dict_param_named.keys():
                if param != 'uri' and param in self.__REQUESTS_KWARGS:
                    request_config[param]=dict_param_named[param]
                elif param == 'uri':
                    request_config['url']=self.api+'/'+dict_param_named[param]
            
            if self._logger != None:
                self._logger.debug('NetRequests::put => '+str(request_config))              
            
            response=requests.put(**request_config)

            if response.status_code < 200 or response.status_code > 299:
                                
                exception={
                    'url':str(response.url),
                    'response':response
                    }
                
                if self._logger != None:
                    self._logger.error('NetRequests::put => '+str(exception))                 
                
                raise NetExceptionRequests(self._logger,**exception)
            
            return response
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
   
   
    def print_data(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                        
            for data in list_param_no_named:
                
                if type(data) is dict:
                    print(json.dumps(data,indent=3))
                elif type(data) is etree._Element:
                    print(etree.tostring(data,encoding='utf-8',pretty_print=True).decode('utf-8'))
                elif type(data) is list:
                    simple_list=True
                    for elem in data:
                        if type(elem) is not int and type(elem) is not float and type(elem) is not str:
                            simple_list=False
                    
                    if simple_list is True:
                        print(str(data))
                    else:
                        for elem in data:
                            self.print_data(elem)                    
                else:
                    print(str(data))
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    
    @NetClassParameterUnique(etree._Element)
    def parse_xml_to_json(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not etree._Element:
                i=i+1
            xml=list_param_no_named[i]
            
            return dict(xmltodict.parse(etree.tostring(xml,encoding='utf-8',pretty_print=True).decode('utf-8'),encoding='utf-8',attr_prefix='@',cdata_key='#text', dict_constructor=dict))
          
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
            
    @NetClassParameterUnique(etree._Element)
    def parse_xml_to_str(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not etree._Element:
                i=i+1
            xml=list_param_no_named[i]
            
            return etree.tostring(xml,encoding='utf-8',pretty_print=True).decode('utf-8')
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
            
    @NetClassParameterUnique(dict)
    def parse_json_to_xml(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not dict:
                i=i+1
            data=list_param_no_named[i]
            
            return etree.fromstring(xmltodict.unparse(data,encoding='utf-8',attr_prefix='@',cdata_key='#text').encode())
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionRequests(self._logger,exception) 
    