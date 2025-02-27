# pylint: disable=unused-variable
__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

import NetLib
from NetLib.NetClasses.NetException.NetException import NetException,NetTypeException
from NetLib.NetClasses.NetNotification.NetTypeNotification import NetTypeNotification
from NetLib.NetClasses.NetClassParatemter.NetClassParameter import NetClassParameterContains,NetClassParameterUnique,NetClassParameterCombine
import re
import os
from lxml import etree
from logging import Logger
from abc import ABC,abstractmethod,abstractproperty,ABCMeta
from filelock import Timeout, FileLock
import json


class NetTypeBase(ABCMeta,NetTypeNotification):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeBase,self).__new__(self,*param_no_named,**param_named)

class NetTypeExcpetionBase(NetTypeException):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeExcpetionBase,self).__new__(self,*param_no_named,**param_named)

class NetExceptionBase(NetException,metaclass=NetTypeExcpetionBase):
    __metaclass__=NetTypeExcpetionBase
     
    def __init__(self,*param_no_named,**param_named):                                    
        super(NetExceptionBase,self).__init__(*param_no_named,**param_named)
        self._config['exception']['content']['class_name']='NetBase'
    def __str__(self):
        return super(NetExceptionBase,self).__str__()
    

class NetBase(ABC,metaclass=NetTypeBase):
    __metaclass__=NetTypeBase

    _SPECIALS_CHARACTERS=[
        '\\',
        '.',
        '^',
        '$',
        '|',
        '*',
        '?',
        '(',
        ')',
        '[',
        ']'
    ]  

    __COUNTER=0

    @NetClassParameterUnique(source1=str,source2=str)
    def test(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            source1=dict_param_named['source1']                                               
            source2=dict_param_named['source2'] 

            return self._str_sub(source1=source1,source2=source2)                                              



        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  

    @NetClassParameterCombine([NetClassParameterUnique(source=dict),NetClassParameterUnique(source=list),NetClassParameterUnique(source=etree._Element),NetClassParameterUnique(source=etree._Attrib)])
    def _parse_original(self,*param_no_named,**param_named):

        @NetClassParameterUnique(source=etree._Element)
        def parse_original_xml_tag(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']   
                retour=etree.Element(source.tag)
                
                if issubclass(type(source.text),list):
                    retour.text=parse_original_list(self,source=source.text)
                elif issubclass(type(source.text),dict):
                    retour.text=parse_original_dict(self,source=source.text)
                else:
                    retour.text=source.text

                dictionary=parse_original_xml_attrib(self,source=source.attrib)
                for key in dictionary.keys():
                    retour.attrib[key]=dictionary[key]

                for child in source.getchildren():
                    retour.append(parse_original_xml_tag(self,source=child))

                return retour                  
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  

        @NetClassParameterUnique(source=etree._Attrib)
        def parse_original_xml_attrib(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']   
                retour=dict()

                for key in source.keys():
                    if issubclass(type(source[key]),list):              
                        retour[key]=parse_original_list(self,source=source[key])
                    elif issubclass(type(source[key]),dict):
                        retour[key]=parse_original_dict(self,source=source[key])
                    elif issubclass(type(source[key]),etree._Element):
                        retour[key]=parse_original_xml_tag(self,source=source[key])
                    elif issubclass(type(source[key]),etree._Attrib):
                        retour[key]=parse_original_xml_attrib(self,source=source[key])                        
                    else:
                        retour[key]=source[key]
                return retour
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception) 

        @NetClassParameterUnique(source=dict)
        def parse_original_dict(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']   
                retour=dict() 

                for key in source.keys():
                    if issubclass(type(source[key]),list):              
                        retour[key]=parse_original_list(self,source=source[key])
                    elif issubclass(type(source[key]),dict):
                        retour[key]=parse_original_dict(self,source=source[key])
                    elif issubclass(type(source[key]),etree._Element):
                        retour[key]=parse_original_xml_tag(self,source=source[key])
                    elif issubclass(type(source[key]),etree._Attrib):
                        retour[key]=parse_original_xml_attrib(self,source=source[key])                        
                    else:
                        retour[key]=source[key]
                return retour
                  
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  

        @NetClassParameterUnique(source=list)
        def parse_original_list(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']                           
                retour=list()

                for index,elem in enumerate(source):
                    if issubclass(type(elem),list):      
                        retour.append(parse_original_list(self,source=source[index]))
                    elif issubclass(type(elem),dict):
                        retour.append(parse_original_dict(self,source=source[index]))
                    elif issubclass(type(elem),etree._Element):
                        retour.append(parse_original_xml_tag(self,source=source[index]))    
                    elif issubclass(type(elem),etree._Attrib):
                        retour.append(parse_original_xml_attrib(self,source=source[index]))                                          
                    else:
                        retour.append(source[index])
                
                return retour            
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  
                
        try:                      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                
            source=dict_param_named['source']
            retour=None            
                                    
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_parse_original -> '+'source => '+str(source))                           
                            
            if issubclass(type(source),list):
                retour=parse_original_list(self,source=source)        
            elif issubclass(type(source),dict):
                retour=parse_original_dict(self,source=source)
            elif issubclass(type(source),etree._Element):
                retour=parse_original_xml_tag(self,source=source)
            elif issubclass(type(source),etree._Attrib):
                retour=parse_original_xml_attrib(self,source=source)
            else:
                retour=source
            
            return retour                
                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  

    @NetClassParameterUnique(source1=object,source2=object)
    def _check_same_object(self,*param_no_named,**param_named):
        
        @NetClassParameterUnique(source1=etree._Element,source2=object,path=str)
        def check_same_object_xml_tag(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source1=dict_param_named['source1']
                source2=dict_param_named['source2']
                path=dict_param_named['path']
                
                retour=True

                path="<'"+str(source1.tag)+">"
                if type(source2) is etree._Element:
                    
                    if str(source1.tag) != str(source2.tag):
                        retour=False
                        if self._logger is not None:
                            self._logger.debug('NetBase@'+ self._id +' ::check_same_object_xml_tag -> '+'path => '+str(path)+' || '+'source1.tag => '+str(source1.tag)+' || '+'source2.tag => '+str(source2.tag)+' || '+'retour => '+str(retour))   
                        return retour
                    
                    if str(source1.text) != str(source2.text):
                        retour=False
                        if self._logger is not None:
                            self._logger.debug('NetBase@'+ self._id +' ::check_same_object_xml_tag -> '+'path => '+str(path)+' || '+'source1.text => '+str(source1.text)+' || '+'source2.text => '+str(source2.text)+' || '+'retour => '+str(retour))
                        return retour

                    if str(source1.tail) != str(source2.tail):
                        retour=False
                        if self._logger is not None:
                            self._logger.debug('NetBase@'+ self._id +' ::check_same_object_xml_tag -> '+'path => '+str(path)+' || '+'source1.tail => '+str(source1.tail)+' || '+'source2.tail => '+str(source2.tail)+' || '+'retour => '+str(retour))
                        return retour


                    retour=check_same_object_xml_attrib(self,source1=source1.attrib,source2=source2.attrib,path=path)
                    
                    if retour is True:
                        if len(list(source1.getchildren())) != len(list(source2.getchildren())):
                            retour=False
                            if self._logger is not None:
                                self._logger.debug('NetBase@'+ self._id +' ::check_same_object_xml_tag -> '+'path => '+str(path)+' || '+'length_children_source1 => '+str(len(list(source1.getchildren())))+' || '+'length_children_source2 => '+str(len(list(source2.getchildren())))+' || '+'retour => '+str(retour))
                            return retour
                    
                        for index,child in enumerate(source1.getchildren()):        
                            retour=check_same_object_xml_tag(self,source1=child,source2=source2.getchildren()[index],path=path)
                            if retour is False:
                                return retour

                    path=path+"<'"+str(source1.tag)+"'/>"
                else:
                    retour=False
                    if self._logger is not None:
                            self._logger.debug('NetBase@'+ self._id +' ::check_same_object_xml_tag -> '+'path => '+str(path)+' || '+'source1 => '+str(type(source1))+' || '+'source2 => '+str(type(source2))+' || '+'retour => '+str(retour))
                    return retour                               

                return retour

            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  

        @NetClassParameterUnique(source1=etree._Attrib,source2=object,path=str)
        def check_same_object_xml_attrib(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source1=dict_param_named['source1']
                source2=dict_param_named['source2']
                path=dict_param_named['path']
                
                retour=True

                if type(source2) is etree._Attrib:
                    for key in source1.keys():
                        if key not in source2.keys():
                            retour=False
                            if self._logger is not None:
                                    self._logger.debug('NetBase@'+ self._id +' ::check_same_object_xml_attrib -> '+'path => '+str(path)+' || '+'source1 => '+str(key)+' || '+'source2 => '+'N/A'+' || '+'retour => '+str(retour))
                            return retour
                    for key in source2.keys():
                        if key not in source1.keys():
                            retour=False
                            if self._logger is not None:
                                    self._logger.debug('NetBase@'+ self._id +' ::check_same_object_xml_attrib -> '+'path => '+str(path)+' || '+'source1 => '+'N/A'+' || '+'source2 => '+str(key)+' || '+'retour => '+str(retour))
                            return retour
                    for key in source1.keys():
                        if type(source1[key]) is list:
                            retour=check_same_object_list(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")
                        elif type(source1[key]) is dict:
                            retour=check_same_object_dict(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")
                        elif type(source1[key]) is etree._Element:
                            retour=check_same_object_xml_tag(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")                               
                        elif type(source1[key]) is etree._Attrib:
                            retour=check_same_object_xml_attrib(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")                            
                        else:
                            retour=check_same_object(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")
                        
                        if retour is False:
                            return retour
                else:
                    retour=False
                    if self._logger is not None:
                            self._logger.debug('NetBase@'+ self._id +' ::check_same_object_xml_attrib -> '+'path => '+str(path)+' || '+'source1 => '+str(type(source1))+' || '+'source2 => '+str(type(source2))+' || '+'retour => '+str(retour))
                    return retour                               

                return retour

            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  

        @NetClassParameterUnique(source1=dict,source2=object,path=str)
        def check_same_object_dict(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source1=dict_param_named['source1']
                source2=dict_param_named['source2']
                path=dict_param_named['path']
                
                retour=True

                if type(source2) is dict:
                    for key in source1.keys():
                        if key not in source2.keys():
                            retour=False
                            if self._logger is not None:
                                    self._logger.debug('NetBase@'+ self._id +' ::check_same_object_dict -> '+'path => '+str(path)+' || '+'source1 => '+str(key)+' || '+'source2 => '+'N/A'+' || '+'retour => '+str(retour))
                            return retour
                    for key in source2.keys():
                        if key not in source1.keys():
                            retour=False
                            if self._logger is not None:
                                    self._logger.debug('NetBase@'+ self._id +' ::check_same_object_dict -> '+'path => '+str(path)+' || '+'source1 => '+'N/A'+' || '+'source2 => '+str(key)+' || '+'retour => '+str(retour))
                            return retour
                    for key in source1.keys():
                        if type(source1[key]) is list:
                            retour=check_same_object_list(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")
                        elif type(source1[key]) is dict:
                            retour=check_same_object_dict(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")
                        elif type(source1[key]) is etree._Element:
                            retour=check_same_object_xml_tag(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")                               
                        elif type(source1[key]) is etree._Attrib:
                            retour=check_same_object_xml_attrib(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")                             
                        else:
                            retour=check_same_object(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")
                        
                        if retour is False:
                            return retour
                else:
                    retour=False
                    if self._logger is not None:
                            self._logger.debug('NetBase@'+ self._id +' ::check_same_object_dict -> '+'path => '+str(path)+' || '+'source1 => '+str(type(source1))+' || '+'source2 => '+str(type(source2))+' || '+'retour => '+str(retour))
                    return retour                               

                return retour

            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  

        @NetClassParameterUnique(source1=list,source2=object,path=str)
        def check_same_object_list(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source1=dict_param_named['source1']
                source2=dict_param_named['source2']
                path=dict_param_named['path']

                retour=True

                if type(source2) is list:
                    if len(source1) != len(source2):
                        retour=False
                        if self._logger is not None:
                            self._logger.debug('NetBase@'+ self._id +' ::check_same_object_dict -> '+'path => '+str(path)+' || '+'length_source1 => '+str(len(source1))+' || '+'length_source2 => '+str(len(source2))+' || '+'retour => '+str(retour))
                        return retour
                    
                    for index,elem in enumerate(source1):
                        if type(elem) is list:
                            retour=check_same_object_list(self,source1=source1[index],source2=source2[index],path=path+"['"+str(index)+"']")
                        elif type(elem) is dict:
                            retour=check_same_object_dict(self,source1=source1[index],source2=source2[index],path=path+"['"+str(index)+"']")
                        elif type(elem) is etree._Element:
                            retour=check_same_object_xml_tag(self,source1=source1[index],source2=source2[index],path=path+"['"+str(index)+"']")    
                        elif type(elem) is etree._Attrib:
                            retour=check_same_object_xml_attrib(self,source1=source1[index],source2=source2[index],path=path+"['"+str(index)+"']")                                                       
                        else:
                            retour=check_same_object(self,source1=source1[index],source2=source2[index],path=path+"['"+str(index)+"']")
                        
                        if retour is False:
                            return retour
                else:
                    retour=False
                    if self._logger is not None:
                            self._logger.debug('NetBase@'+ self._id +' ::check_same_object_dict -> '+'path => '+str(path)+' || '+'source1 => '+str(type(source1))+' || '+'source2 => '+str(type(source2))+' || '+'retour => '+str(retour))
                    return retour
                
                return retour

            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  
                
        @NetClassParameterUnique(source1=object,source2=object,path=str)
        def check_same_object(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source1=dict_param_named['source1']
                source2=dict_param_named['source2']
                path=dict_param_named['path']

                retour=None
                if source1 == source2:
                    retour=True
                else:
                    retour=False

                if self._logger is not None:
                    self._logger.debug('NetBase@'+ self._id +' ::check_same_object -> '+'path => '+str(path)+' || '+'source1 => '+str(source1)+' || '+'source2 => '+str(source2)+' || '+'retour => '+str(retour))

                return retour

            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception) 

        try:
                              
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                
            source1=self._parse_original(source=dict_param_named['source1'])
            source2=self._parse_original(source=dict_param_named['source2'])

            retour=True

            if (( type(source1) is dict and len(source1.keys()) == 0 ) and ( type(source2) is dict and len(source2.keys()) == 0 )) or \
                (( type(source1) is list and len(source1) == 0 ) and ( type(source2) is list and len(source2) == 0 )):
                return True

            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_check_same_object -> source1 => '+str(source1)+' || '+'source2 => '+str(source2))                           
                
            if type(source1) is list:
                retour=check_same_object_list(self,source1=source1,source2=source2,path='')
            elif type(source1) is dict:
                retour=check_same_object_dict(self,source1=source1,source2=source2,path='')
            elif type(source1) is etree._Element:
                retour=check_same_object_xml_tag(self,source1=source1,source2=source2,path='')                
            else:
                retour=check_same_object(self,source1=source1,source2=source2,path='')

            if self._logger is not None:
                self._logger.info('NetBase@'+ self._id +' ::_check_same_object -> '+'retour => '+str(retour)+' || '+'source1 => '+str(source1)+' || '+'source2 => '+str(source2))                    

            return retour

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  

    @NetClassParameterUnique(expected_object=object,inspected_object=object)
    def _check_regex(self,*param_no_named,**param_named):
        
        @NetClassParameterUnique(expected_dict=dict,inspected_dict=dict,path=str)
        def check_regex_dict(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                expected_dict=dict_param_named['expected_dict']
                inspected_dict=dict_param_named['inspected_dict']
                path=dict_param_named['path']
                           
                for key in expected_dict.keys():
                    if key in inspected_dict.keys():
                        if type(expected_dict[key]) is list:
                            check_regex_list(self,expected_list=expected_dict[key],inspected_list=inspected_dict[key],path=path+"['"+str(key)+"']")
                        elif type(expected_dict[key]) is dict:
                            check_regex_dict(self,expected_dict=expected_dict[key],inspected_dict=inspected_dict[key],path=path+"['"+str(key)+"']")
                        else:
                            check_regex_str(self,expected_str=str(expected_dict[key]),inspected_str=str(inspected_dict[key]),path=path+"['"+str(key)+"']")
                    else:
                        exception={
                            'keys':path+"['"+str(key)+"']",
                            'error':'missing key',
                            'message':"'"+key+"' not defined in '"+path+"' with keys '"+str(list(inspected_dict.keys()))+"'"
                            }
                            
                        if self._logger is not None:
                            self._logger.error('NetBase@'+ self._id +' ::check_regex_dict -> '+'exception => '+str(exception))
                        
                        raise NetExceptionBase(self._logger,**exception)                        
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  

        @NetClassParameterUnique(expected_list=list,inspected_list=list,path=str)
        def check_regex_list(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                expected_list=dict_param_named['expected_list']
                inspected_list=dict_param_named['inspected_list']
                path=dict_param_named['path']


                if len(expected_list) > 0:
                    if len(expected_list) <= len(inspected_list):
                        if len(expected_list) == 1:
                            if type(expected_list[0]) is list:
                                for index,elem in enumerate(inspected_list):
                                    check_regex_list(self,expected_list=expected_list[0],inspected_list=inspected_list[index],path=path+'['+str(index)+']')
                            elif type(expected_list[0]) is dict:
                                for index,elem in enumerate(inspected_list):
                                    check_regex_dict(self,expected_dict=expected_list[0],inspected_dict=inspected_list[index],path=path+'['+str(index)+']')
                            else:
                                for index,elem in enumerate(inspected_list):
                                    check_regex_str(self,expected_str=str(expected_list[0]),inspected_str=str(inspected_list[index]),path=path+'['+str(index)+']')
                        else:
                            for index,elem in enumerate(expected_list):
                                if type(elem) is list:
                                    check_regex_list(self,expected_list=expected_list[index],inspected_list=inspected_list[index],path=path+'['+str(index)+']')
                                elif type(elem) is dict:
                                    check_regex_dict(self,expected_dict=expected_list[index],inspected_dict=inspected_list[index],path=path+'['+str(index)+']')
                                else:
                                    check_regex_str(self,expected_str=str(expected_list[index]),inspected_str=str(inspected_list[index]),path=path+'['+str(index)+']')
                    else:
                        exception={
                            'count_expected':str(len(expected_list)),
                            'count_inspected':str(len(inspected_list)),
                            'error':'wrong size',
                            'message': path+' wrong sizing '+str(str(len(expected_list)))+' element(s) expected'
                            }
                                
                        if self._logger is not None:
                            self._logger.error('NetBase@'+ self._id +' ::check_regex_list -> '+'exception => '+str(exception))
                            
                        raise NetExceptionBase(self._logger,**exception)                            
                                
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  
                
        @NetClassParameterUnique(expected_str=str,inspected_str=str,path=str)
        def check_regex_str(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                expected_str=dict_param_named['expected_str']
                inspected_str=dict_param_named['inspected_str']
                path=dict_param_named['path']

                match=re.search(expected_str,inspected_str)
                if match is None:
                    exception={
                        'regex_expected':expected_str,
                        'value_inspected':inspected_str,
                        'path':path,
                        'error':'mismatching regex',
                        'message': path+" regex '"+expected_str+"' not matching with '"+inspected_str+"'"
                        }
                            
                    if self._logger is not None:
                        self._logger.error('NetBase@'+ self._id +' ::check_regex_str -> '+'exception => '+str(exception))
                        
                    raise NetExceptionBase(self._logger,**exception)        
            
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception) 

        try:
                              
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                
            expected_object=self._parse_original(source=dict_param_named['expected_object'])
            inspected_object=self._parse_original(source=dict_param_named['inspected_object'])


            if ( type(expected_object) is dict and len(expected_object.keys()) > 0 ) or ( type(expected_object) is list and len(expected_object) > 0 ):

                if self._logger is not None:
                    self._logger.debug('NetBase@'+ self._id +' ::_check_regex -> expected => '+str(expected_object)+' || '+'inspected => '+str(inspected_object))                           
                
                if type(expected_object) is list:
                    check_regex_list(self,expected_list=expected_object,inspected_list=inspected_object,path='')
                elif type(expected_object) is dict:
                    check_regex_dict(self,expected_dict=expected_object,inspected_dict=inspected_object,path='')
                else:
                    check_regex_str(self,expected_str=str(expected_object),inspected_str=str(inspected_object),path='')

                if self._logger is not None:
                    self._logger.info('NetBase@'+ self._id +' ::_check_regex -> Success'+' || '+'expected => '+str(expected_object)+' || '+'inspected => '+str(inspected_object))                         
                                        
                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  

    @NetClassParameterUnique(expected_object=object,inspected_object=object)
    def _check_type(self,*param_no_named,**param_named):
        
        @NetClassParameterUnique(expected_dict=dict,inspected_dict=object,path=str)
        def check_type_dict(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                expected_dict=dict_param_named['expected_dict']
                inspected_dict=dict_param_named['inspected_dict']
                path=dict_param_named['path']
                           
                if len(expected_dict.keys()) > 0:
                    if type(inspected_dict) is dict:
                        for key in expected_dict.keys():
                            if key in inspected_dict.keys():
                                if type(expected_dict[key]) is list:
                                    check_type_list(self,expected_list=expected_dict[key],inspected_list=inspected_dict[key],path=path+"['"+str(key)+"']")
                                elif type(expected_dict[key]) is dict:
                                    check_type_dict(self,expected_dict=expected_dict[key],inspected_dict=inspected_dict[key],path=path+"['"+str(key)+"']")
                                else:
                                    check_type_data(self,expected_type=expected_dict[key],inspected_type=inspected_dict[key],path=path+"['"+str(key)+"']")
                            else:
                                exception={
                                    'keys':path+"['"+str(key)+"']",
                                    'error':'missing key',
                                    'message':"'"+key+"' not defined in '"+path+"' with keys '"+str(list(inspected_dict.keys()))+"'"
                                    }
                                    
                                if self._logger is not None:
                                    self._logger.error('NetBase@'+ self._id +' ::check_regex_dict -> '+'exception => '+str(exception))
                            
                                raise NetExceptionBase(self._logger,**exception)
                    else:
                        check_type_data(self,expected_type=expected_dict,inspected_type=inspected_dict,path=path)
                else:
                    check_type_data(self,expected_type=expected_dict,inspected_type=inspected_dict,path=path)
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  

        @NetClassParameterUnique(expected_list=list,inspected_list=object,path=str)
        def check_type_list(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                expected_list=dict_param_named['expected_list']
                inspected_list=dict_param_named['inspected_list']
                path=dict_param_named['path']
                
                if len(expected_list) > 0:
                    if type(inspected_list) is list:
                        if len(expected_list) <= len(inspected_list):
                            if len(expected_list) == 1:                                
                                if type(expected_list[0]) is list:
                                    for index,elem in enumerate(inspected_list):
                                        check_type_list(self,expected_list=expected_list[0],inspected_list=inspected_list[index],path=path+'['+str(index)+']')
                                elif type(expected_list[0]) is dict:
                                    for index,elem in enumerate(inspected_list):
                                        check_type_dict(self,expected_dict=expected_list[0],inspected_dict=inspected_list[index],path=path+'['+str(index)+']')
                                else:
                                    for index,elem in enumerate(inspected_list):
                                        check_type_data(self,expected_type=expected_list[0],inspected_type=inspected_list[index],path=path+'['+str(index)+']')                                                               
                            else:
                                for index,elem in enumerate(expected_list):
                                    if type(elem) is list:
                                        check_type_list(self,expected_list=expected_list[index],inspected_list=inspected_list[index],path=path+'['+str(index)+']')
                                    elif type(elem) is dict:
                                        check_type_dict(self,expected_dict=expected_list[index],inspected_dict=inspected_list[index],path=path+'['+str(index)+']')
                                    else:
                                        check_type_data(self,expected_type=expected_list[index],inspected_type=inspected_list[index],path=path+'['+str(index)+']')
                                    
                        else:
                            exception={
                                'count_expected':str(len(expected_list)),
                                'count_inspected':str(len(inspected_list)),
                                'error':'wrong size',
                                'message': path+' wrong sizing '+str(len(expected_list))+' element(s) expected'
                                }
                            if self._logger is not None:
                                self._logger.error('NetBase@'+ self._id +' ::check_type_list -> '+'exception => '+str(exception))
                                
                            raise NetExceptionBase(self._logger,**exception)
                    else:
                        check_type_data(self,expected_type=expected_list,inspected_type=inspected_list,path=path)                        
                else:
                    check_type_data(self,expected_type=expected_list,inspected_type=inspected_list,path=path)                 
                            
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  
                
        @NetClassParameterUnique(expected_type=object,inspected_type=object,path=str)
        def check_type_data(self,*param_no_named,**param_named):
            try:
                
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                expected_type=dict_param_named['expected_type']
                inspected_type=dict_param_named['inspected_type']
                path=dict_param_named['path']

                if type(expected_type) is not type(inspected_type):
                    exception={
                        'type_expected':type(expected_type),
                        'type_inspected':type(inspected_type),
                        'path':path,
                        'error':'mismatching type',
                        'message': path+" type '"+re.sub("^<class '(?P<TYPE>[^'][^']*)'.*",'\\g<TYPE>',str(type(expected_type)))+"' expected not matching with '"+str(inspected_type)+"' as type '"+re.sub("^<class '(?P<TYPE>[^'][^']*)'.*",'\\g<TYPE>',str(type(inspected_type)))+"'"
                        }
                            
                    if self._logger is not None:
                        self._logger.error('NetBase@'+ self._id +' ::check_type_data -> '+'exception => '+str(exception))
                        
                    raise NetExceptionBase(self._logger,**exception)
            
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception) 

        try:   
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            expected_object=self._parse_original(source=dict_param_named['expected_object'])
            inspected_object=self._parse_original(source=dict_param_named['inspected_object'])

            if ( type(expected_object) is dict and len(expected_object.keys()) > 0 ) or ( type(expected_object) is list and len(expected_object) > 0 ):

                if self._logger is not None:
                    self._logger.debug('NetBase@'+ self._id +' ::_check_type_data -> expected => '+str(expected_object)+' || '+'inspected => '+str(inspected_object))                           
                    
                if type(expected_object) is list:
                    check_type_list(self,expected_list=expected_object,inspected_list=inspected_object,path='')
                elif type(expected_object) is dict:
                    check_type_dict(self,expected_dict=expected_object,inspected_dict=inspected_object,path='')
                else:
                    check_type_data(self,expected_type=expected_object,inspected_type=inspected_object,path='')

                if self._logger is not None:
                    self._logger.info('NetBase@'+ self._id +' ::_check_type_data -> Success'+' || '+'expected => '+str(expected_object)+' || '+'inspected => '+str(inspected_object))                         
                

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  

    @NetClassParameterUnique(dictionary=dict)
    def _dict_get_all_keys(self,*param_no_named,**param_named):
        
        @NetClassParameterUnique(dictionary=dict)
        def get_dict_keys(self,*param_no_named,**param_named):  
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)

                dictionary=dict_param_named['dictionary']            
            
                if self._logger is not None:
                    self._logger.debug('NetBase@'+ self._id +' ::get_dict_keys -> '+'keys => '+str(dictionary.keys()))               
            
                retour=[]
                retour=retour+list(dictionary.keys())
                for key in dictionary.keys():
                    if type(dictionary[key]) is dict:
                        retour=retour+get_dict_keys(self,dictionary=dictionary[key])
                    elif type(dictionary[key]) is list:
                        retour=retour+get_list_keys(self,dictionary=dictionary[key])
            
                return retour
        
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)        
               
        @NetClassParameterUnique(dictionary=list)
        def get_list_keys(self,*param_no_named,**param_named):  
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)

                dictionary=dict_param_named['dictionary']            
            
                if self._logger is not None:
                    self._logger.debug('NetBase@'+ self._id +' ::get_list_keys -> '+'list => '+str(dictionary))               
            
                retour=[]
                for elem in dictionary:
                    if type(elem) is dict:
                        retour=retour+get_dict_keys(self,dictionary=elem)
                    elif type(elem) is list:
                        retour=retour+get_list_keys(self,dictionary=elem)
                return retour
        
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)          
        
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            dictionary=dict_param_named['dictionary']            
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_dict_get_all_keys -> '+'dictionary => '+str(dictionary))               
            
            retour=get_dict_keys(self,dictionary=dictionary)
            
            return retour
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)

    @NetClassParameterUnique(fusion=list)
    def _dict_concatenation(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            list_dict=dict_param_named['fusion']            
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_dict_concatenation -> '+'fusion => '+str(list_dict))               
            
            retour={}
            
            for elem in list_dict:
                if type(elem) is dict:
                    for keys in elem.keys():
                        if keys not in retour.keys():
                            retour[keys]=elem[keys]
                        else:
                            if type(retour[keys]) is not list:
                                if retour[keys] != elem[keys]:
                                    save=retour[keys]
                                    retour[keys]=list()
                                    retour[keys].append(save)
                                    retour[keys].append(elem[keys])
                            else:
                                if elem[keys] not in retour[keys]:
                                    retour[keys].append(elem[keys])                      
            
            
            return retour.copy()
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  

    @NetClassParameterUnique(diff=list)
    def _dict_difference(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            list_dict=dict_param_named['diff']            
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_dict_difference -> '+'diff => '+str(list_dict))               
            
            retour={}
            
            for elem in list_dict:
                if type(elem) is dict:
                    for key in elem.keys():
                        found=False
                        for compare in list_dict:
                            if compare != elem and type(compare) is dict:
                                if key in compare.keys():
                                    found=True
                        if found == False:
                            retour[key]=elem[key].copy()
            
            return retour.copy()
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  

    @NetClassParameterUnique(chain=str)
    def _str_specials_characters_as_str(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            retour=dict_param_named['chain']          
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_str_specials_characters_as_str -> '+'chain => '+retour+' || '+'specials_caracters => '+str(NetBase._SPECIALS_CHARACTERS))               
            
            for character in NetBase._SPECIALS_CHARACTERS:
                retour=retour.replace(character,'\\'+character)
            
            return retour
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception) 
    
    @NetClassParameterUnique(chain=str)
    def _str_specials_characters_as_regex(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            retour=dict_param_named['chain']
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_str_specials_characters_as_regex -> '+'chain => '+chain+' || '+'specials_caracters => '+str(NetBase._SPECIALS_CHARACTERS))               
            
            for character in NetBase._SPECIALS_CHARACTERS:
                retour=retour.replace('\\'+character,character)
            
            return retour
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)                  

    @NetClassParameterUnique(source1=str,source2=str)
    def _str_sub(self,*param_no_named,**param_named):
        
        @NetClassParameterUnique(source1=dict,source2=object,path=str)
        def _str_sub_dict(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source1=dict_param_named['source1']
                source2=dict_param_named['source2']
                path=dict_param_named['path']

                retour=source1.copy()
                           
                if len(source1.keys()) > 0:
                    if type(source2) is dict:
                        for key in source1.keys():
                            if key in source2.keys():
                                if type(source1[key]) is list:
                                    retour[key]=_str_sub_list(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")
                                elif type(source2[key]) is dict:
                                    retour[key]=_str_sub_dict(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")
                                else:
                                    retour[key]=_str_sub_data(self,source1=source1[key],source2=source2[key],path=path+"['"+str(key)+"']")
                    else:
                        retour=_str_sub_data(self,source1=source1,source2=source2,path=path)
                else:
                    retour=_str_sub_data(self,source1=source1,source2=source2,path=path)

                is_empty=True
                keys=list(retour.keys())
                for key in keys:
                    if str(retour[key]) != '':
                        is_empty=False
                    else:
                        del retour[key]
                if is_empty:
                    retour=''
                return retour
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  

        @NetClassParameterUnique(source1=list,source2=object,path=str)
        def _str_sub_list(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source1=dict_param_named['source1']
                source2=dict_param_named['source2']
                path=dict_param_named['path']

                retour=source1.copy()
                
                if len(source1) > 0:
                    if type(source2) is list:
                        if len(source2) == 1:
                            for index,elem in enumerate(source1):
                                if type(elem) is list:
                                    retour[index]=_str_sub_list(self,source1=source1[index],source2=source2[0],path=path+'['+str(index)+']')
                                elif type(elem) is dict:
                                    retour[index]=_str_sub_dict(self,source1=source1[index],source2=source2[0],path=path+'['+str(index)+']')
                                else:
                                    retour[index]=_str_sub_data(self,source1=source1[index],source2=source2[0],path=path+'['+str(index)+']')
                        else:
                            for index,elem in enumerate(source1):
                                if type(elem) is list:
                                    retour[index]=_str_sub_list(self,source1=source1[index],source2=source2[index],path=path+'['+str(index)+']')
                                elif type(elem) is dict:
                                    retour[index]=_str_sub_dict(self,source1=source1[index],source2=source2[index],path=path+'['+str(index)+']')
                                else:
                                    retour[index]=_str_sub_data(self,source1=source1[index],source2=source2[index],path=path+'['+str(index)+']')
                    else:
                        retour=_str_sub_data(self,source1=source1,source2=source2,path=path)                        
                else:
                    retour=_str_sub_data(self,source1=source1,source2=source2,path=path) 

                is_empty=True
                for elem in retour:
                    if str(elem) != '':
                        is_empty=False
                if is_empty:
                    retour=''
                return retour           
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception)  
                
        @NetClassParameterUnique(source1=object,source2=object,path=str)
        def _str_sub_data(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source1=str(dict_param_named['source1'])
                source2=str(dict_param_named['source2'])
                path=dict_param_named['path']

                retour=re.sub(source2,'',source1)
                            
                if self._logger is not None:
                    self._logger.debug('NetBase@'+ self._id +' ::_str_sub_data -> '+'path => '+path+' || '+'source1 => '+str(source1)+' || '+'source2 => '+str(source2)+' || '+'retour => '+retour)
                        
                return retour

            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionBase(self._logger,exception) 

        try:   
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            source1=dict_param_named['source1']
            source2=dict_param_named['source2']

            source1=str(source1).replace('"{','{').replace('}"','}').replace('"[','[').replace(']"',']').replace("'",'"')
            source1='{"root":'+str(source1)+'}'
            
            source2=str(source2).replace('"{','{').replace('}"','}').replace('"[','[').replace(']"',']').replace("'",'"')
            source2='{"root":'+str(source2)+'}'

            if re.search(":{|:\\[",source1) is None and re.search(":[0-9.,][0-9.,]*$",source1) is None :
                source1=re.sub(":",':"',source1,1)
                source1=re.sub("}$",'"}',source1,1)
            
            if re.search(":{|:\\[",source2) is None and re.search(":[0-9.,][0-9.,]*$",source2) is None :
                source2=re.sub(":",':"',source2,1)
                source2=re.sub("}$",'"}',source2,1)

            source1=json.loads(source1)
            source1=source1['root']

            source2=json.loads(source2)
            source2=source2['root']

            if (( type(source1) is dict and len(source1.keys()) > 0 ) or ( type(source1) is list and len(source1) > 0 ) and ( type(source2) is dict and len(source2.keys()) > 0 ) or ( type(source2) is list and len(source2) > 0 )):

                if self._logger is not None:
                    self._logger.debug('NetBase@'+ self._id +' ::_str_sub -> source1 => '+str(source1)+' || '+'source2 => '+str(source2))                           
                    
                if type(source1) is list:
                    retour=_str_sub_list(self,source1=source1,source2=source2,path='')
                elif type(source1) is dict:
                    retour=_str_sub_dict(self,source1=source1,source2=source2,path='')
                else:
                    retour=_str_sub_data(self,source1=source1,source2=source2,path='')

                return str(retour)
            else:
                retour=_str_sub_data(self,source1=str(source1),source2=str(source2),path='')

                return str(retour)                       
                

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  


    @NetClassParameterUnique(file=str,data=str,timeout=int)
    def _str_save_file(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            output_file=dict_param_named['file']
            data=dict_param_named['data']
            timeout=dict_param_named['timeout']

            lock_path=''
            lock=None
                        
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_str_save_file -> '+'output_file => '+str(output_file)+' || '+'data => '+data.replace('\n','')+' || '+'timeout => '+str(timeout))

            if len(output_file.split(os.path.sep)) > 1:
                directory=os.path.sep.join(output_file.split(os.path.sep)[:-1])
                if os.path.isdir(directory):

                    lock_path=output_file+'.lock'
                    lock= FileLock(lock_path, timeout=timeout)
                    with lock.acquire(timeout=timeout):     
                        with open(output_file, 'w') as file:
                            file.write(data)
                            file.close()
                        lock.release()
                else:

                    exception={
                        'error':'path is wrong',
                        'source_directory': directory,
                        'message':'folder '+directory+" doesn't exist"
                        }
 
                    if self._logger is not None:
                        self._logger.error('NetBase@'+ self._id +' ::_str_save_file -> '+'exception => '+str(exception))                         
                        
                    raise NetExceptionBase(self._logger,**exception)
            else:
                lock_path=output_file+'.lock'
                lock= FileLock(lock_path, timeout=timeout)
                with lock.acquire(timeout=timeout):                  
                    with open(output_file, 'w') as file:
                        file.write(data)
                        file.close()
                    lock.release()
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_str_save_file -> Success')               

        except Exception as exception:
            if lock is not None:
                lock.release()
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)

    @NetClassParameterUnique(file=str,timeout=int)
    def _str_load_file(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            retour=""

            lock_path=''
            lock=None            

            input_file=dict_param_named['file']
            timeout=dict_param_named['timeout']

            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_str_load_file -> '+'input_file => '+str(input_file)+' || '+'timeout => '+str(timeout))

            if len(input_file.split(os.path.sep)) > 1:
                directory=os.path.sep.join(input_file.split(os.path.sep)[:-1])
                if os.path.isdir(directory):
                    if os.path.isfile(input_file):
                        lock_path=input_file+'.lock'
                        lock= FileLock(lock_path, timeout=timeout)
                        with lock.acquire(timeout=timeout):
                            with open(input_file, 'r') as file:
                                retour = file.read()
                                file.close()
                            lock.release()  
                    else:
                        exception={
                            'error':'file not found',
                            'source_file': input_file,
                            'message':'file '+input_file+" doesn't exist"
                            }
    
                        if self._logger is not None:
                            self._logger.error('NetBase@'+ self._id +' ::_str_load_file -> '+'exception => '+str(exception))                         
                            
                        raise NetExceptionBase(self._logger,**exception)
                else:
                    exception={
                        'error':'path is wrong',
                        'source_directory': directory,
                        'message':'folder '+directory+" doesn't exist"
                        }
 
                    if self._logger is not None:
                        self._logger.error('NetBase@'+ self._id +' ::_str_load_file -> '+'exception => '+str(exception))                         
                        
                    raise NetExceptionBase(self._logger,**exception)
            else:
                if os.path.isfile(input_file):
                    lock_path=input_file+'.lock'
                    lock= FileLock(lock_path, timeout=self._lock_timeout)
                    with lock.acquire(timeout=self._lock_timeout):                
                        with open(input_file, 'r') as file:
                            retour = file.read()
                            file.close()
                        lock.release()
                else:
                    exception={
                        'error':'file not found',
                        'source_file': input_file,
                        'message':input_file+" doesn't exist"
                        }
    
                    if self._logger is not None:
                        self._logger.error('NetBase@'+ self._id +' ::_str_load_file -> '+'exception => '+str(exception))                         
                        
                    raise NetExceptionBase(self._logger,**exception)                           
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_str_load_file -> Success')    

            return retour

        except Exception as exception:
            if lock is not None:
                lock.release()                       
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)   

    @NetClassParameterContains(source=str,source_type=type)
    def _obj_get_args(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            source=dict_param_named['source']
            source_type=dict_param_named['source_type']

            retour=''
            if source in dict_param_named.keys():
                retour=dict_param_named[source]
            else:
                i=0
                while type(list_param_no_named[i]) is not source_type:
                    i=i+1
                retour=list_param_no_named[i]

            return retour

        except Exception as exception:                     
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception) 


    @NetClassParameterUnique(load=dict)
    def _dict_load(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            load=dict_param_named['load']
                        
            attributes=[
                'id'
            ]
         
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_dict_load -> '+'keys => '+str(attributes.keys()))          
            
            for attribut in attributes:
                if attribut not in load.keys():
                    exception={
                        'keys':'['+attribut+']',
                        'error':'missing key',
                        'message':'['+attribut+']'+' not in '+str(list(load.keys()))
                        }
                    
                    if self._logger is not None:
                        self._logger.error('NetBase@'+ self._id +' ::_dict_load -> '+'exception => '+str(exception))                    
                        
                    raise NetExceptionBase(self._logger,**exception)
            

            self._id=load['id']

            return
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)   
    def _dict_save(self,*param_no_named,**param_named):
        try:
            retour=dict()
            
            retour['id']=self._id
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_dict_save -> '+'keys => '+str(retour.keys()))              
            
            return retour
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  


    def __init__(self,*param_no_named,**param_named):
        try: 
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)       
            self._id='N/A' 
            
            self._logger=None

            if 'logger' in dict_param_named.keys() and issubclass(type(dict_param_named['logger']),Logger):
                self.logger=dict_param_named['logger']
            else:
                for elem in list_param_no_named:
                    if issubclass(type(elem),Logger):
                        self.logger=elem            
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::__init__ -> Creating object')            
            
            self._generate_id(self,*param_no_named,**param_named)

            if self._logger is not None:
                self._logger.info('NetBase@'+ self._id +' :: object created -> '+'id => ' +self._id+' || '+'logger => '+str(self._logger))


        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  
    def __getstate__(self):
        try:
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::__getstate__ -> Getting State')              
            
            state=dict(self._dict_save())
            state['dict']=self.__dict__
            return state
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  
    def __setstate__(self,state):
        try:
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::__setstate__ -> Setting State')                 
            
            if type(state) is dict:
                self.__dict__=state['dict']
                                
                self._dict_load(**state)
            return 
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  
    def __str__(self,*param_no_named,**param_named):
        try:
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::__str__ => Getting str')              
            return "logger => "+str(self._logger)
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)  


    @NetClassParameterCombine([NetClassParameterUnique(Logger),NetClassParameterUnique(type(None))])
    def __set_logger(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while not issubclass(type(list_param_no_named[i]),Logger) and type(list_param_no_named[i]) is not type(None):
                i=i+1
            logger=list_param_no_named[i]
            
            self._logger=logger
            return
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)
    def __get_logger(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::__get_logger -> logger write only parameter')            
            
            exception={
                'property':'logger',
                'error':'write only property',
                'message':'logger is only reachable as write only property'
                }
                        
            if self._logger is not None:
                self._logger.error('NetBase@'+ self._id +' ::__get_logger -> logger write only parameter')
            
            raise NetExceptionBase(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception) 
    logger=property(__get_logger,__set_logger)


    def _increment_id(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            NetBase.__COUNTER=NetBase.__COUNTER+1

            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_increment_id -> counter => '+str(NetBase.__COUNTER))            
                      
            counter="{:06d}".format(NetBase.__COUNTER)

            return counter

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)
    def _generate_id(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            id=self._increment_id(self,*param_no_named,**param_named)

            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::_generate_id -> id => '+id)

            self._id=id

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)
    def __set_id(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::__set_id -> id read only parameter')            
            
            exception={
                'property':'id',
                'error':'read only property',
                'message':'id is only reachable as read only property'
                }
                        
            if self._logger is not None:
                self._logger.error('NetBase@'+ self._id +' ::__set_id -> id read only parameter')
            
            raise NetExceptionBase(self._logger,**exception)

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception)
    def __get_id(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            if self._logger is not None:
                self._logger.debug('NetBase@'+ self._id +' ::__get_id -> id => '+self._id)

            return self._id
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionBase(self._logger,exception) 
    id=property(__get_id,__set_id)    
