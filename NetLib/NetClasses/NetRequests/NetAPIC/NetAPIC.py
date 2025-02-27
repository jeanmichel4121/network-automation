# pylint: disable=unused-variable
__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

import NetLib
from NetLib.NetClasses.NetException.NetException import NetException
from NetLib.NetClasses.NetRequests.NetRequests import NetRequests,NetTypeRequests,NetExceptionRequests,NetTypeExcpetionRequests
from NetLib.NetClasses.NetClassParatemter.NetClassParameter import NetClassParameterUnique,NetClassParameterContains
import re
import json
from logging import Logger
import requests
import urllib3
import os
import lxml
from lxml import etree
import time
import xmltodict
import math

class NetTypeAPIC(NetTypeRequests):
    def __new__( self, classname, superclasses, attributdict):
        return super(NetTypeAPIC,self).__new__(classname, superclasses, attributdict)

class NetTypeExcpetionAPIC(NetTypeExcpetionRequests):
    def __new__( self, classname, superclasses, attributdict):
        return super(NetTypeExcpetionAPIC,self).__new__(classname, superclasses, attributdict)

class NetExceptionAPIC(NetExceptionRequests,metaclass=NetTypeExcpetionAPIC):
    __metaclass__=NetTypeExcpetionAPIC
    
    def __init__(self,*param_no_named,**param_named):
        list_param_no_named=list(param_no_named)
        dict_param_named=dict(param_named)
                
        super(NetExceptionAPIC,self).__init__(*list_param_no_named,**dict_param_named)
            
        self._config['exception']['content']['class_name']='NetAPIC'
 
          
    def __str__(self):
        return super(NetExceptionAPIC,self).__str__()
 

class NetAPIC(NetRequests,metaclass=NetTypeAPIC):
    __metaclass__=NetTypeAPIC
    
    __DEFAULT_VERSION='api'
    
    __ADDITIONALS_ARGUMENTS=[
        'query-target',
        'target-subtree-class',
        'query-target-filter',
        'rsp-subtree',
        'rsp-subtree-class',
        'rsp-subtree-filter',
        'rsp-subtree-include',
        'ordy-by'
    ]
        
    
    _DEFAULT_SOURCE=os.path.dirname(NetLib.NetClasses.NetRequests.NetAPIC.__file__)+os.path.sep+'NetAPIC.yml'
    
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
            
            super(NetAPIC,self)._update_config(*list_param_no_named,**dict_param_named)
            config=dict_param_named['config']
                        
            if self._logger != None:
                self._logger.debug('NetAPIC::_update_config => '+str(config))            
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception)        
    
    @NetClassParameterUnique(config=dict)    
    def _update_config_updated(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            super(NetAPIC,self)._update_config_updated(*list_param_no_named,**dict_param_named)
            config=dict_param_named['config']               
                        
            if self._logger != None:
                self._logger.debug('NetAPIC::_update_config_Updated => '+str(config)) 
                
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception)

    @NetClassParameterUnique(load=dict)
    def _dict_load(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            super(NetAPIC,self)._dict_load(*list_param_no_named,**dict_param_named)
            
            load=dict_param_named['load']
            
            attributes=[
            ]
            
            if self._logger != None:
                self._logger.debug('NetAPIC::_dict_load => '+str(attributes))                
            
            for attribut in attributes:
                if attribut not in dict_param_named.keys():
                    exception={
                        'keys':'['+attribut+']',
                        'error':'missing key',
                        'message':'['+attribut+']'+' not in '+str(list(dict_param_named.keys()))
                        }
                
                    if self._logger != None:
                        self._logger.error('NetAPIC::_dict_load => '+str(exception))                    
                        
                    raise NetExceptionAPIC(self._logger,**exception)            
            return
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception)  
    def _dict_save(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            retour=super(NetAPIC,self)._dict_save(*list_param_no_named,**dict_param_named)
            
            if self._logger != None:
                self._logger.debug('NetAPIC::_dict_save => '+str(retour.keys()))  
            
            return retour
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception)  
     
    
    def __init__(self,*param_no_named,**param_named):    
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            self.__version=self.__DEFAULT_VERSION+'/'+'node'
            self.__list_objects=None
              
            super(NetAPIC,self).__init__(*list_param_no_named,**dict_param_named)
                  
            if self._logger != None:
                self._logger.debug('NetAPIC::__init__ => Creating object')               
                        
                
            if self._logger != None:
                self._logger.info('NetAPIC object created => '+"url => "+self._config['requests']['url']+'/'+self.__version+" :: "+"user => "+str(self._config['requests']['authentication']['user']))                
                        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception)     
    def __str__(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetAPIC::__str__ => Getting str')              
            
            return "url => "+self._config['requests']['url']+'/'+self.__version+" :: "+"user => "+str(self._config['requests']['authentication']['user'])
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception)        
        
    @property
    def api(self):
        return self._config['requests']['url']+'/'+self.version
        
    def _init_session(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            urllib3.disable_warnings()
    
            if self._logger != None:
                self._logger.debug('NetAPIC::_init_session => '+str(self._config['requests']['url']+'/'+self.__DEFAULT_VERSION+'/'+'aaaLogin.xml'))    
            
            requests_config=self._requests_config(*param_no_named,**param_named)
            requests_config['url']=self._config['requests']['url']+'/doc/html/LeftSummary.html' 
            
            response=requests.get(**requests_config)
            root = etree.HTML(response.text,parser=self.parser_html)

            
            if response.status_code < 200 or response.status_code > 299:
                
                if response.status_code == 401:
                    title='401 Authorization Required'
                else:
                    title="N/A"
                
                exception={
                    'response':response,
                    'title':title,                    
                    }
                
                for elem in root.findall('./header/*'):
                    exception[elem.tag]=elem.findall('./*')  
                
                for elem in root.findall('./body/*'):
                    exception[elem.tag]=elem.findall('./*')                
                
                
                if self._logger != None:
                    self._logger.critical('NetAPIC::_init_session => '+title) 
                
                raise NetExceptionAPIC(self._logger,**exception)
            
            ''' Read all class objects '''
            self.__list_objects=list() 
            
                      
            for elem in root.xpath('./body/div[2]/div[1]/div[2]/table/tr/a/@href'):
                self.__list_objects.append(re.sub('^MO-(?P<CLASS>[^\\.][^\\.]*)\\.html','\\g<CLASS>',elem))
            
            

            ''' Authentication token '''
            authentication_data=etree.Element("aaaUser",name=self.authentication_user,pwd=self.authentication_password)
        
            requests_config['url']=self._config['requests']['url']+'/'+self.__DEFAULT_VERSION+'/'+'aaaLogin.xml'
            requests_config['data']=self.parse_xml_to_str(authentication_data)

            response=requests.post(**requests_config)
                        
            root=etree.XML(response.content,parser=self.parser_xml)
            if response.status_code < 200 or response.status_code > 299:
                                
                if response.status_code == 401:
                    title='401 Authorization Required'
                else:
                    title="N/A"
                
                exception={
                    'username':self.authentication_user,
                    'response':response,
                    'title':title,
                    root.tag:list(root)
                    }
                                              
                if self._logger != None:
                    self._logger.critical('NetAPIC::_init_session => '+title) 

                raise NetExceptionAPIC(self._logger,**exception)

        
            cookies = {
                'APIC-cookie':root.xpath('./aaaLogin/@token')[0]
            }
        
            if self._logger != None:
                self._logger.info('NetAPIC::_init_session => '+self._config['requests']['url']+' session established')           
        
            self.cookies=dict(response.cookies)
            
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception) 
    
    
    def __set_version(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetLog::__set_version => version read only property')            
            
            exception={
                'property':'version',
                'error':'read only property',
                'message':'version is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetLog::__set_version => version read only property')
                            
            raise NetExceptionAPIC(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception)    
    def __get_version(self,*param_no_named,**param_named):
        try:

            if self._logger != None:
                self._logger.debug('NetAPIC::__get_version => '+str(self.__version))             
            
            return self.__version
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception) 
    version=property(__get_version,__set_version)

    def __set_list_objects(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetLog::__set_list_objects => list_objects read only property')            
            
            exception={
                'property':'list_objects',
                'error':'read only property',
                'message':'list_objects is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetLog::__set_list_objects => list_objects read only property')
                            
            raise NetExceptionAPIC(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception)     
    def __get_list_objects(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetAPIC::__get_list_objects => '+' objects count => '+str(len(self.__list_objects)))              
            
            return self.__list_objects
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception) 
    list_objects=property(__get_list_objects,__set_list_objects)   

    @NetClassParameterContains(str)
    def __parse_uri(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            uri=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetAPIC::__parse_uri => '+str(uri))              
                        
            
            uri=re.sub('^[//]*class[//]','',uri)
            
            
            
            
            match=re.search("\\?",uri)
            if match:
                match=re.search("\\..json\\?",uri)
                if match:
                    uri=re.sub("\\.json\\?",".xml?",uri)
                match=re.search("\\.xml\\?",uri)
                if match is None:
                    uri=re.sub("\\?",".xml?",uri)
            else:
                match=re.search("\\.json$",uri)
                if match:
                    uri=re.sub("\\.json$",".xml",uri)                
                
                match=re.search("\\.xml$",uri)
                if match is None:
                    uri=uri+".xml"



            name_object=re.sub('(?P<NAME>[^\\.][^\\.]*)\\.xml','\\g<NAME>',uri)
            
            for line in self.__list_objects:
                if name_object.lower() == line.lower():
                    name_object=line
                    uri = re.sub('[^\\.][^\\.]*\\.xml',line+'.xml',uri)

            
            if name_object in self.__list_objects:
                uri='class/'+uri
            else:

                match=re.search("^mo/",uri)
                if match is None:
                    uri="mo/"+uri 
            
            return uri                                          
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception) 

    @NetClassParameterContains(uri=str)
    def get(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            retour=list()
            
            parser=self.parser_xml
            dict_param_named['parser']=parser
            
            if self._logger != None:
                self._logger.debug('NetAPIC::get => uri => '+str(dict_param_named['uri']))            
            
            root=self.__get_without_pagging(*list_param_no_named,**dict_param_named)

            if self._logger != None:
                self._logger.debug('NetAPIC::get => parsing response') 

                                                
            if self._logger != None:
                self._logger.info('NetAPIC response parsed => uri => '+str(dict_param_named['uri']))
                                        
            return root

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception) 
    @NetClassParameterContains(uri=str,parser=lxml.etree.XMLParser)
    def __get_without_pagging(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            retour=list()

            dict_param_named['uri']=self.__parse_uri(dict_param_named['uri'])
            parser=dict_param_named['parser']

            if self._logger != None:
                self._logger.debug('NetAPIC::__get_without_pagging => uri => '+str(dict_param_named['uri']))   

            response=super(NetAPIC,self).get(*list_param_no_named,**dict_param_named)            
            root=etree.XML(response.content,parser=parser)
        
            if self._logger != None:
                self._logger.info('NetAPIC::__get_without_pagging => '+str(response.url))
                
            return root             
                        
        except NetExceptionRequests as exception:  
            if type(exception.content['exception_type']) is type(NetExceptionRequests):
                exception.content={'username':self.authentication_user}
                
                root=etree.XML(exception.content['values']['response'].content,parser=self.parser_xml)
                self.print_data(root)
                
                                      
                if root.findall('./error'):
                    code=root.xpath('./error/@code')[0]
                    text=root.xpath('./error/@text')[0]
                
                    exception.content={'error_code':code,'error_text':text}
                    
                    if int(code) == 403 and text == 'Token was invalid (Error: Token timeout)':
                        
                        if self._logger != None:
                            self._logger.warning('NetAPIC::__get_without_pagging => token expired => '+str(self.cookies['APIC-cookie']))                          
                        
                        del self.cookies['APIC-cookie']
                                                
                        if self._logger != None:
                            self._logger.info('NetAPIC::__get_without_pagging => generating new token')                           
                        
                        self.init_connection(*list_param_no_named,**dict_param_named)
                        retour=retour+self.__get_without_pagging(*list_param_no_named,**dict_param_named)
                    
                    elif int(code) == 400 and text == 'Unable to process the query, result dataset is too big':
                        
                        if self._logger != None:
                            self._logger.warning('NetAPIC::__get_without_pagging => result dataset is too big')                              
                        
                        if self._logger != None:
                            self._logger.info('NetAPIC::__get_without_pagging => pagging REST call API is starting')                          
                        
                        retour=self.__get_with_pagging(*list_param_no_named,**dict_param_named)
                    else:
                        
                        if self._logger != None:
                            self._logger.error('NetAPIC::__get_without_pagging => code => '+str(code)+' :: '+'error => '+str(text))                          
                        
                        raise NetExceptionAPIC(exception)
                else:
                                        
                    exception.content={root.tag:list(root)}  
                    
                    if self._logger != None:
                        self._logger.error('NetAPIC::__get_without_pagging => '+str(exception.content['values']['response']))                     
                    
                    raise NetExceptionAPIC(exception)                        
            else:
                exception.logger=self._logger
                raise exception                                           
            
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception) 
                                 
    @NetClassParameterContains(uri=str,parser=lxml.etree.XMLParser)
    def __get_with_pagging(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            parser=dict_param_named['parser']
            retour=None
            
            min_page_size=1
            max_page_size=10240
            divisive_max=8
            

            if self._logger != None:
                self._logger.debug('NetAPIC::__get_with_pagging => uri => '+str(dict_param_named['uri']+' :: '+'min_page_size => '+str(min_page_size)+' :: '+'max_page_size => '+str(max_page_size)+' :: '+"divisive_max => "+str(divisive_max))) 

            dict_param_named['uri']=self.__parse_uri(dict_param_named['uri'])

            if 'page' not in self.parameters.keys():
                self.parameters['page']='0'
            
            if  'page-size' not in self.parameters.keys():
                self.parameters['page-size']=max_page_size

            end=False
            total_count=0
            read_objects=0
            page_size=int(self.parameters['page-size'])
            page=int(self.parameters['page'])
            while end != True:            
                try:
                    end=True
                    
                    if self._logger != None:
                        self._logger.debug('NetAPIC::__get_with_pagging => uri => '+str(dict_param_named['uri'])+' :: '+'read_objects => '+str(read_objects)+' :: '+'total_objects => '+str(total_count)+' :: '+'pages => '+str(page)+' :: '+'page_size => '+str(page_size)) 
                    
                    response=super(NetAPIC,self).get(*list_param_no_named,**dict_param_named)
                    root=etree.XML(response.content,parser=parser)                    
                    
                    if self._logger != None:
                        self._logger.info('NetAPIC::__get_with_pagging => '+str(response.url))                      
                    
                    read_objects=read_objects+page_size
                    page=page+1

                    if page_size < max_page_size and page % divisive_max == 0:

                        if self._logger != None:
                            self._logger.debug('NetAPIC::__get_with_pagging => growing up page size => '+str(page_size)+' * '+str(divisive_max)) 
                                                    
                        page_size=int(page_size*divisive_max)
                        self.parameters['page-size']=str(page_size)

                        page=int(page/divisive_max)
                             
                    self.parameters['page']=str(page)
                    
                    if total_count <= 0:
                        total_count=int(root.attrib['totalCount'])


                    if retour is None:
                        retour=root
                    else:                        
                        for elem in root:
                            retour.append(elem)

                    if read_objects <= total_count:
                        end=False
                                                                                
                                                                                
                except NetExceptionRequests as exception:  
                    if type(exception.content['exception_type']) is type(NetExceptionRequests):
                        exception.content={'username':self.authentication_user}
                        
                        root=etree.XML(exception.content['values']['response'].content,parser=parser)
                                                        
                        if root.findall('./error'):
                            code=root.xpath('./error/@code')[0]
                            text=root.xpath('./error/@text')[0]
                        
                            exception.content={'error_code':code,'error_text':text}

                            if int(code) == 403 and text == 'Token was invalid (Error: Token timeout)':
                                                                
                                if self._logger != None:
                                    self._logger.warning('NetAPIC::__get_with_pagging => token expired => '+str(self.cookies['APIC-cookie']))                          
                                
                                del self.cookies['APIC-cookie']
                                                        
                                if self._logger != None:
                                    self._logger.info('NetAPIC::__get_with_pagging => generating new token')                                   
                                
                                self.init_connection(*list_param_no_named,**dict_param_named)
                                end=False
                    
                            elif int(code) == 400 and text == 'Unable to process the query, result dataset is too big':
                                
                                if page_size > 1:
                                    gcd=math.gcd(page_size,divisive_max)                                
                                         
                                    if self._logger != None:
                                        self._logger.debug('NetAPIC::__get_with_pagging => growing down page size => '+str(page_size)+' / '+str(gcd))                                 
                                
                                    page_size=int(page_size/gcd)
                                    page=int(page*gcd)

                                    
                                    self.parameters['page-size']=str(page_size)
                                    self.parameters['page']=str(page)                                
                                
                                    if page_size >= min_page_size:                                    
                                        end=False
                                else:
                                    exception.content={
                                        'min_page_size':str(min_page_size),
                                        'max_page_size':str(max_page_size),
                                        'read_objects':str(read_objects),
                                        'page_size':str(page_size)
                                    }
                                                 
                                    if self._logger != None:
                                        self._logger.error('NetAPIC::__get_with_pagging => result dataset is too big :: min_page_size => '+str(min_page_size)+' :: max_page_size => '+str(max_page_size)+' :: read_objects => '+str(read_objects)+' :: page_size => '+str(page_size))  
                                         
                                    raise NetExceptionAPIC(exception)
                            else:
                                
                                if self._logger != None:
                                    self._logger.error('NetAPIC::__get_with_pagging => code => '+str(code)+' :: '+'error => '+str(text))                                 
                                
                                raise NetExceptionAPIC(exception)                                
                        else:
                            
                            exception.content={root.tag:list(root)}  
              
                            if self._logger != None:
                                self._logger.error('NetAPIC::__get_with_pagging => '+str(exception.content['values']['response']))                 
              
                            raise NetExceptionAPIC(exception)    
                    else:
                        exception.logger=self._logger
                        raise exception                          
                except Exception as exception:
                    raise exception
                
            return retour    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception) 
            
    def post(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            retour=list()

            if 'uni' not in dict_param_named.keys():
                dict_param_named['uni']='uni.xml'
            
            return super(NetAPIC,self).post(*list_param_no_named,**dict_param_named)
            
            if 'page' not in self.parameters.keys():
                self.parameters['page']='0'
            
            if  'page-size' not in self.parameters.keys():
                self.parameters['page-size']='5'
            
            if 'data' in self.parameters.keys():
                self.parameters['json']=self.parameters['data']
                del self.parameters['data']
            
            end=False
            while end != True:
                end=True
                
                r=super(NetAPIC,self).post(*list_param_no_named,**dict_param_named)
                self.parameters['page']=str(int(self.parameters['page'])+int(1))
                
                data=r.json()
                if 'imdata' in data.keys() and type(data['imdata']) is list and len(data['imdata']) > 0:

                    retour=retour+data['imdata']
                
                if 'totalCount' in data.keys() and total_count == 0:
                    total_count=int(data['totalCount'])
                
                if int(self.parameters['page'])*int(self.parameters['page-size']) <= total_count:
                    end=False     
              
        except NetExceptionAPIC as ex:    
            if ex.content['method_name'] == 'post(self,*param_no_named,**param_named)':
                
                exception={
                    'class_name':'NetAPIC',
                    'method_name':'post(self,*param_no_named,**param_named)',
                    'exception_source':"self",
                    'exception_type': type(NetExceptionAPIC),
                    'values':ex.content["values"]
                    }
                                
                if 'imdata' in exception['values']['response'].json().keys() and  type(exception['values']['response'].json()['imdata']) is list and type(exception['values']['response'].json()['imdata'][0]) is dict \
                 and 'error' in exception['values']['response'].json()['imdata'][0].keys() and type(exception['values']['response'].json()['imdata'][0]['error']) is dict \
                  and  'attributes' in exception['values']['response'].json()["imdata"][0]['error'].keys() \
                    and type(exception['values']['response'].json()["imdata"][0]['error']['attributes']) is dict:
                    
                    code=exception['values']['response'].json()["imdata"][0]['error']['attributes']['code']
                    text=exception['values']['response'].json()["imdata"][0]['error']['attributes']['text']

                    exception['values']['code']=code
                    exception['values']['text']=text

                else:
                    for keys in exception['values']['response'].json().keys():
                        exception['values'][keys]= exception['values']['response'].json()[keys]
    
                if int(code) == 403 and text == 'Token was invalid (Error: Token timeout)':
                    del self.cookies['APIC-cookie']
                    self.init_connection(*list_param_no_named,**dict_param_named)
                    retour=retour+self.post(*list_param_no_named,**dict_param_named)
                else:
                    raise NetExceptionAPIC(**exception)
            
            return retour                                           
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception) 
 
    def print_objects(self,*param_no_named,**param_named):
        try:
            for obj in self.list_objects:
                print(obj)
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionAPIC(self._logger,exception)