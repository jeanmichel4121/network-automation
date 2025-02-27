# pylint: disable=unused-variable
__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

import NetLib
from abc import ABC,abstractmethod,abstractproperty,ABCMeta
from NetLib.NetClasses.NetException.NetException import NetException
from NetLib.NetClasses.NetClassParatemter.NetClassParameter import NetClassParameterContains,NetClassParameterUnique,NetClassParameterCombine
from NetLib.NetClasses.NetConfig.NetConfig import NetTypeConfig,NetTypeExcpetionConfig,NetExceptionConfig,NetConfig
import re
import os
import json
import yaml

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler,FileSystemEventHandler
from filelock import Timeout, FileLock


class NetTypeConfigFile(NetTypeConfig):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeConfigFile,self).__new__(self,*param_no_named,**param_named)

class NetTypeExcpetionConfigFile(NetTypeExcpetionConfig):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeExcpetionConfigFile,self).__new__(self,*param_no_named,**param_named)

class NetExceptionConfigFile(NetExceptionConfig,metaclass=NetTypeExcpetionConfigFile):
    __metaclass__=NetTypeExcpetionConfigFile
     
    def __init__(self,*param_no_named,**param_named):
        super(NetExceptionConfigFile,self).__init__(*param_no_named,**param_named)
        self._config['exception']['content']['class_name']='NetConfigFile'
    def __str__(self):
        return super(NetExceptionConfigFile,self).__str__()
    
class NetConfigFile(NetConfig,metaclass=NetTypeConfigFile):
    __metaclass__=NetTypeConfigFile
    

    @NetClassParameterUnique(old_config=dict,new_config=dict)
    def _update_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            super(NetConfigFile,self)._update_config(*param_no_named,**param_named)
            
            old_config=dict_param_named['old_config']
            new_config=dict_param_named['new_config']

            if self._config_file != None and self._config_file != "" and self._config_file.upper() != "N/A":

                if self._logger is not None:
                    self._logger.debug('NetConfigFile@'+ self._id +' ::_update_config -> '+'save_config => '+str(self._config_file)) 

                if os.path.isfile(self._config_file):
                    statbuf = os.stat(self._config_file)
                    self.__old_config_file_st_mtime = statbuf.st_mtime

                self._save_dictionary_file(file=self._config_file,dictionary=new_config)
            
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
            
            super(NetConfigFile,self)._update_config_type(*param_no_named,**param_named)

            old_config_type=dict_param_named['old_config_type']
            new_config_type=dict_param_named['new_config_type']    

            if self._config_file_type != None and self._config_file_type != "" and self._config_file_type.upper() != "N/A":

                if self._logger is not None:
                    self._logger.debug('NetConfigFile@'+ self._id +' ::_update_config_type -> '+'save_config_type => '+str(self._config_file_type))  

                if os.path.isfile(self._config_file_type):
                    statbuf = os.stat(self._config_file_type)
                    self.__old_config_file_type_st_mtime = statbuf.st_mtime

                self._save_dictionary_file(file=self._config_file_type,dictionary=new_config_type)                                         

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
            
            super(NetConfigFile,self)._update_config_regex(*param_no_named,**param_named)

            old_config_regex=dict_param_named['old_config_regex']
            new_config_regex=dict_param_named['new_config_regex']

            if self._config_file_regex != None and self._config_file_regex != "" and self._config_file_regex.upper() != "N/A":

                if self._logger is not None:
                    self._logger.debug('NetConfigFile@'+ self._id +' ::_update_config_regex -> '+'save_config_regex => '+str(self._config_file_regex)) 

                if os.path.isfile(self._config_file_regex):
                    statbuf = os.stat(self._config_file_regex)
                    self.__old_config_file_regex_st_mtime = statbuf.st_mtime

                self._save_dictionary_file(file=self._config_file_regex,dictionary=new_config_regex)                                         
                                        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfig(self._logger,exception)                        


    @NetClassParameterUnique(old_config_file=dict,new_config_file=dict)
    def _update_config_file(self,*param_no_named,**param_named):
        try:      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            old_config_file=dict_param_named['old_config_file']
            new_config_file=dict_param_named['new_config_file']

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::_update_config_file -> '+'old_config_file => '+ str(old_config_file) + ' || '+'new_config_file => '+ str(new_config_file))    
            
            self.config=new_config_file

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)
    @NetClassParameterUnique(old_config_file_type=dict,new_config_file_type=dict)
    def _update_config_file_type(self,*param_no_named,**param_named):
        try:      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            old_config_file_type=dict_param_named['old_config_file_type']
            new_config_file_type=dict_param_named['new_config_file_type']

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::_update_config_file_type -> '+'old_config_file_type => '+ str(old_config_file_type) + ' || '+'new_config_file_type => '+ str(new_config_file_type))    
            
            self.config_type=new_config_file_type

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)
    @NetClassParameterUnique(old_config_file_regex=dict,new_config_file_regex=dict)
    def _update_config_file_regex(self,*param_no_named,**param_named):
        try:      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            old_config_file_regex=dict_param_named['old_config_file_regex']
            new_config_file_regex=dict_param_named['new_config_file_regex']

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::_update_config_file_regex -> '+'old_config_file_regex => '+ str(old_config_file_regex) + ' || '+'new_config_file_regex => '+ str(new_config_file_regex))    
            
            self.config_regex=new_config_file_regex

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)


    @NetClassParameterUnique(old_path_config_file=str,new_path_config_file=str)
    def _update_path_config_file(self,*param_no_named,**param_named):
        try:      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            old_path_config_file=dict_param_named['old_path_config_file']
            new_path_config_file=dict_param_named['new_path_config_file']

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::_update_path_config_file -> '+'old_path_config_file => '+ str(old_path_config_file) + ' || '+'new_path_config_file => '+ str(new_path_config_file))    
            
            if new_path_config_file != None and new_path_config_file != "" and new_path_config_file.upper() != "N/A":
                if os.path.isfile(new_path_config_file):
                    self.config=self.__old_config_file
                else:
                    self._save_dictionary_file(file=self._config_file,dictionary=self._config)  
                    statbuf = os.stat(self._config_file)
                    self.__old_config_file_st_mtime = statbuf.st_mtime                                      

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)
    @NetClassParameterUnique(old_path_config_file_type=str,new_path_config_file_type=str)
    def _update_path_config_file_type(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            old_path_config_file_type=dict_param_named['old_path_config_file_type']
            new_path_config_file_type=dict_param_named['new_path_config_file_type']

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::_update_path_config_file_type -> '+'old_path_config_file_type => '+ old_path_config_file_type + ' || '+'new_path_config_file_type => '+ new_path_config_file_type )    

            if new_path_config_file_type != None and new_path_config_file_type != "" and new_path_config_file_type.upper() != "N/A":
                if os.path.isfile(new_path_config_file_type):
                    self.config_type=self.__old_config_file_type
                else:
                    self._save_dictionary_file(file=self._config_file_type,dictionary=self._config_type)                                         
                    statbuf = os.stat(self._config_file_type)
                    self.__old_config_file_type_st_mtime = statbuf.st_mtime



        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)
    @NetClassParameterUnique(old_path_config_file_regex=str,new_path_config_file_regex=str)
    def _update_path_config_file_regex(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            old_path_config_file_regex=dict_param_named['old_path_config_file_regex']
            new_path_config_file_regex=dict_param_named['new_path_config_file_regex']

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::_update_path_config_file_type -> '+'old_path_config_file_regex => '+ old_path_config_file_regex + ' || '+'new_path_config_file_regex => '+ new_path_config_file_regex )  

            if new_path_config_file_regex != None and new_path_config_file_regex != "" and new_path_config_file_regex.upper() != "N/A":
                if os.path.isfile(new_path_config_file_regex):
                    self.config_regex=self.__old_config_file_regex
                else:
                    self._save_dictionary_file(file=self._config_file_regex,dictionary=self._config_regex)                      
                    statbuf = os.stat(self._config_file_regex)
                    self.__old_config_file_regex_st_mtime = statbuf.st_mtime


        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)    


    @NetClassParameterUnique(new_path_config_file=str)
    def __update_path_config_file(self,*param_no_named,**param_named):
        try:      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            new_path_config_file=dict_param_named['new_path_config_file']

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::__update_path_config_file -> '+'new_path_config_file => '+ str(new_path_config_file))    
            
            if new_path_config_file != None and new_path_config_file != "" and new_path_config_file.upper() != "N/A":
                if os.path.isfile(new_path_config_file):
                    self.__old_config_file=self._load_dictionary_file(file=new_path_config_file)

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)
    @NetClassParameterUnique(new_path_config_file_type=str)
    def __update_path_config_file_type(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            new_path_config_file_type=dict_param_named['new_path_config_file_type']

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::_update_path_config_file_type -> '+'new_path_config_file_type => '+ new_path_config_file_type )    

            if new_path_config_file_type != None and new_path_config_file_type != "" and new_path_config_file_type.upper() != "N/A":
                if os.path.isfile(new_path_config_file_type):
                    self.__old_config_file_type=self._load_dictionary_file(file=new_path_config_file_type)

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)
    @NetClassParameterUnique(new_path_config_file_regex=str)
    def __update_path_config_file_regex(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            new_path_config_file_regex=dict_param_named['new_path_config_file_regex']

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::_update_path_config_file_type -> '+'new_path_config_file_regex => '+ new_path_config_file_regex )  

            if new_path_config_file_regex != None and new_path_config_file_regex != "" and new_path_config_file_regex.upper() != "N/A":
                if os.path.isfile(new_path_config_file_regex):
                    self.__old_config_file_regex=self._load_dictionary_file(file=new_path_config_file_regex)

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)                        
                    

    def __event_config_file(self,*param_no_named,**param_named):
        try:

            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            event=list_param_no_named[0]
            
            statbuf = os.stat(event.src_path)
            new_config_st_mtime = statbuf.st_mtime
            diff_st_mtime=new_config_st_mtime - self.__old_config_file_st_mtime
            
            if diff_st_mtime > 0.5:

                if self._logger != None:
                    self._logger.debug('NetConfigFile@'+ self._id +' ::__event_config_file -> '+'config_file => '+self._config_file) 

                new_config_file=self._load_dictionary_file(file=event.src_path)
                old_config_file=self._parse_original(source=self.__old_config_file)

                self.__old_config_file=self._parse_original(source=new_config_file)

                self._update_config_file(old_config_file=old_config_file,new_config_file=new_config_file)


            self.__old_config_file_st_mtime=new_config_st_mtime
                                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)       
    def __set_observer_config_file(self,*param_no_named,**param_named):
        try:            
            directory=os.path.dirname(self._config_file)
            if directory == '.':
                directory = directory + '/'

            config={
                'patterns':[self._config_file],
                'ignore_directories':True,
                'case_sensitive':True
                }

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::__set_observer_config_file -> '+'config_file => '+str(self._config_file))              
            
            if self.__observer_config_file is not None:
                self.__observer_config_file.stop()
                self.__observer_config_file.join()
                
            event=PatternMatchingEventHandler(**config)
            event.on_modified = self.__event_config_file
            
            self.__observer_config_file=Observer()
            self.__observer_config_file.schedule(event_handler=event,path=directory,recursive=False)
            self.__observer_config_file.start()
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)  

    def __event_config_file_type(self,*param_no_named,**param_named):
        try:

            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            event=list_param_no_named[0]
            
            statbuf = os.stat(event.src_path)
            new_config_st_mtime = statbuf.st_mtime
            diff_st_mtime=new_config_st_mtime - self.__old_config_file_type_st_mtime
            
            if diff_st_mtime > 0.5:

                if self._logger != None:
                    self._logger.debug('NetConfigFile@'+ self._id +' ::__event_config_file_type -> '+'config_file_type => '+self._config_file_type) 

                new_config_file_type=self._load_dictionary_file(file=event.src_path)
                old_config_file_type=self._parse_original(source=self.__old_config_file_type)

                self.__old_config_file_type=self._parse_original(source=new_config_file_type)

                self._update_config_file_type(old_config_file_type=old_config_file_type,new_config_file_type=new_config_file_type)


            self.__old_config_file_type_st_mtime=new_config_st_mtime
                                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)       
    def __set_observer_config_file_type(self,*param_no_named,**param_named):
        try:            
            directory=os.path.dirname(self._config_file_type)
            if directory == '.':
                directory = directory + '/'

            config={
                'patterns':[self._config_file_type],
                'ignore_directories':True,
                'case_sensitive':True
                }

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::__set_observer_config_file_type -> '+'config_file_type => '+str(self._config_file_type))              
            
            if self.__observer_config_file_type is not None:
                self.__observer_config_file_type.stop()
                self.__observer_config_file_type.join()
                
            event=PatternMatchingEventHandler(**config)
            event.on_modified = self.__event_config_file_type
            
            self.__observer_config_file_type=Observer()
            self.__observer_config_file_type.schedule(event_handler=event,path=directory,recursive=False)
            self.__observer_config_file_type.start()
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)  

    def __event_config_file_regex(self,*param_no_named,**param_named):
        try:

            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            event=list_param_no_named[0]
            
            statbuf = os.stat(event.src_path)
            new_config_st_mtime = statbuf.st_mtime
            diff_st_mtime=new_config_st_mtime - self.__old_config_file_regex_st_mtime
            
            if diff_st_mtime > 0.5:

                if self._logger != None:
                    self._logger.debug('NetConfigFile@'+ self._id +' ::__event_config_file_regex -> '+'config_file_regex => '+self._config_file_regex) 

                new_config_file_regex=self._load_dictionary_file(file=event.src_path)
                old_config_file_regex=self._parse_original(source=self.__old_config_file_regex)

                self.__old_config_file_regex=self._parse_original(source=new_config_file_regex)

                self._update_config_file_regex(old_config_file_regex=old_config_file_regex,new_config_file_regex=new_config_file_regex)


            self.__old_config_file_regex_st_mtime=new_config_st_mtime
                                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)       
    def __set_observer_config_file_regex(self,*param_no_named,**param_named):
        try:            
            directory=os.path.dirname(self._config_file_regex)
            if directory == '.':
                directory = directory + '/'

            config={
                'patterns':[self._config_file_regex],
                'ignore_directories':True,
                'case_sensitive':True
                }

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::__set_observer_config_file_regex -> '+'config_file_regex => '+str(self._config_file_regex))              
            
            if self.__observer_config_file_regex is not None:
                self.__observer_config_file_regex.stop()
                self.__observer_config_file_regex.join()
                
            event=PatternMatchingEventHandler(**config)
            event.on_modified = self.__event_config_file_regex
            
            self.__observer_config_file_regex=Observer()
            self.__observer_config_file_regex.schedule(event_handler=event,path=directory,recursive=False)
            self.__observer_config_file_regex.start()
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)  


    @NetClassParameterUnique(load=dict)
    def _dict_load(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            super(NetConfig,self)._dict_load(*param_no_named,**param_named)
            
            load=dict_param_named['load']
            
            attributes=[
                'old_config_file',
                'old_config_file_type',
                'old_config_file_regex',
                'config_file',
                'config_file_type',
                'config_file_regex'
            ]
         
            if self._logger is not None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::_dict_load -> '+'attributes => '+str(attributes))          
            
            for attribut in attributes:
                if attribut not in load.keys():
                    exception={
                        'keys':'['+attribut+']',
                        'error':'missing key',
                        'message':'['+attribut+']'+' not in '+str(list(load.keys()))
                        }
                    
                    if self._logger is not None:
                        self._logger.error('NetConfigFile::_dict_load -> '+'exception => '+str(exception))                    
                        
                    raise NetExceptionConfig(self._logger,**exception)
                      
            self.__old_config_file=load['old_config_file']
            self.__old_config_file_type=load['old_config_file_type']
            self.__old_config_file_regex=load['old_config_file_regex']

            self.config_file=load['config_file']
            self.config_file_type=load['config_file_type']
            self.config_file_regex=load['config_file_regex']


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

            retour['old_config_file']=self._parse_original(source=self.__old_config_file)
            retour['old_config_file_type']=self._parse_original(source=self.__old_config_file_type)
            retour['old_config_file_regex']=self._parse_original(source=self.__old_config_file_regex)
            retour['config_file']=self._config_file
            retour['config_file_type']=self._config_file_type
            retour['config_file_regex']=self._config_file_regex


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

            self.__old_config_file_st_mtime=0
            self.__old_config_file_type_st_mtime=0
            self.__old_config_file_regex_st_mtime=0

            self.__old_config_file={}
            self.__old_config_file_type={}
            self.__old_config_file_regex={}

            self.__observer_config_file=None
            self.__observer_config_file_type=None
            self.__observer_config_file_regex=None

            self._config_file="N/A"
            self._config_file_type="N/A"
            self._config_file_regex="N/A"

            super(NetConfigFile,self).__init__(*param_no_named,**param_named)
         
            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::__init__ -> Creating object')            

            if 'config_file' in dict_param_named.keys() and type(dict_param_named['config_file']) is str:
                self.config_file=dict_param_named['config_file']

            if 'config_file_type' in dict_param_named.keys() and type(dict_param_named['config_file_type']) is str:
                self.config_file_type=dict_param_named['config_file_type']
  
            if 'config_file_regex' in dict_param_named.keys() and type(dict_param_named['config_file_regex']) is str:
                self.config_file_regex=dict_param_named['config_file_regex']
                      
            if self._logger is not None:
                self._logger.info('NetConfigFile@'+ self._id +' :: object created -> '+'id => ' +self._id + ' || '+'config_file => '+str(self._config_file))            


        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)  
 
    @NetClassParameterUnique(str)
    def __set_config_file(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            config_file=list_param_no_named[i]
            old_path_config_file=self._config_file
                 
            if len(config_file.split(os.path.sep)) == 1 and config_file != '' and config_file.upper() != 'N/A':
                config_file='.'+os.path.sep+config_file

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::__set_config_file -> '+'config_file => '+str(config_file))                  

            if config_file != '' and config_file.upper() != 'N/A':

                directory=os.path.sep.join(config_file.split(os.path.sep)[:-1])
                if os.path.isdir(directory):
                    self._config_file=config_file

                    self.__update_path_config_file(new_path_config_file=config_file)
                    self._update_path_config_file(old_path_config_file=old_path_config_file,new_path_config_file=config_file)
                    
                    self.__set_observer_config_file(*param_no_named,**param_named)
                else:
                    exception={
                        'error':'path is wrong',
                        'source_directory': directory,
                        'message':directory+" doesn't exist"
                        }
 
                    if self._logger is not None:
                        self._logger.error('NetConfigFile@'+ self._id +' ::__set_config_file -> '+'exception => '+str(exception))                         
                        
                    raise NetExceptionConfigFile(self._logger,**exception)
                    
       
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)        
    def __get_config_file(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::__get_config_file -> '+'config_file => '+str(self._config_file))             
            
            return self._config_file
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception) 
    config_file=property(__get_config_file,__set_config_file)

    @NetClassParameterUnique(str)
    def __set_config_file_type(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            config_file_type=list_param_no_named[i]
            old_path_config_file_type=self._config_file_type

                 
            if len(config_file_type.split(os.path.sep)) == 1 and config_file_type != '' and config_file_type.upper() != 'N/A':
                config_file_type='.'+os.path.sep+config_file_type

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::__set_config_file_type -> '+'config_file_type => '+str(config_file_type))                  

            if config_file_type != '' and config_file_type.upper() != 'N/A':

                directory=os.path.sep.join(config_file_type.split(os.path.sep)[:-1])
                if os.path.isdir(directory):
                    self._config_file_type=config_file_type
                    self.__update_path_config_file_type(new_path_config_file_type=config_file_type)
                    self._update_path_config_file_type(old_path_config_file_type=old_path_config_file_type,new_path_config_file_type=config_file_type)
                    
                    self.__set_observer_config_file_type(*param_no_named,**param_named)
                else:
                    exception={
                        'error':'path is wrong',
                        'source_directory': directory,
                        'message':directory+" doesn't exist"
                        }
 
                    if self._logger is not None:
                        self._logger.error('NetConfigFile@'+ self._id +' ::__set_config_file_type -> '+'exception => '+str(exception))                         
                        
                    raise NetExceptionConfigFile(self._logger,**exception)
                 
       
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception)        
    def __get_config_file_type(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::__get_config_file_type -> '+'config_file_type => '+str(self._config_file_type))             
            
            return self._config_file_type
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception) 
    config_file_type=property(__get_config_file_type,__set_config_file_type)

    @NetClassParameterUnique(str)
    def __set_config_file_regex(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            config_file_regex=list_param_no_named[i]
            old_path_config_file_regex=self._config_file_regex


            if len(config_file_regex.split(os.path.sep)) == 1 and config_file_regex != '' and config_file_regex.upper() != 'N/A':
                config_file_regex='.'+os.path.sep+config_file_regex       

            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::__set_config_file_regex -> '+'config_file_regex => '+str(config_file_regex)) 

            if config_file_regex != '' and config_file_regex.upper() != 'N/A':

                directory=os.path.sep.join(config_file_regex.split(os.path.sep)[:-1])
                if os.path.isdir(directory):
                    self._config_file_regex=config_file_regex

                    self.__update_path_config_file_regex(new_path_config_file_regex=config_file_regex)
                    self._update_path_config_file_regex(old_path_config_file_regex=old_path_config_file_regex,new_path_config_file_regex=config_file_regex)
                    
                    self.__set_observer_config_file_regex(*param_no_named,**param_named)
                else:
                    exception={
                        'error':'path is wrong',
                        'source_directory': directory,
                        'message':directory+" doesn't exist"
                        }
 
                    if self._logger is not None:
                        self._logger.error('NetConfigFile@'+ self._id +' ::__set_config_file_regex -> '+'exception => '+str(exception))                         
                        
                    raise NetExceptionConfigFile(self._logger,**exception)


                    
       
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:
                raise NetExceptionConfigFile(self._logger,exception)        
    def __get_config_file_regex(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetConfigFile@'+ self._id +' ::__get_config_file_regex -> '+'config_file_regex => '+str(self._config_file_regex))             
            
            return self._config_file_regex
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionConfigFile(self._logger,exception) 
    config_file_regex=property(__get_config_file_regex,__set_config_file_regex)


