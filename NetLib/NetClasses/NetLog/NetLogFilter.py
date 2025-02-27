# pylint: disable=unused-variable
__author__ = 'Jean-Michel Cuvelier'

import sys

from NetLib.NetClasses.NetClassParatemter.NetClassParameter import NetClassParameterUnique,NetClassParameterContains
import logging
import re


class NetFilter_Lvl_Debug_Only(logging.Filter):
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            return
        except Exception as exception:
            raise exception
  
    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            record=list_param_no_named[0]
            if record.levelno ==  10:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False

class NetFilter_Lvl_Debug_Skip(logging.Filter):
    
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            record=list_param_no_named[0]
            if record.levelno ==  10:
                return False
            else:
                return True
        except Exception as exception:
            raise exception
        return False

class NetFilter_Lvl_Informal_Only(logging.Filter):
    
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            record=list_param_no_named[0]
            if record.levelno ==  20:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False

class NetFilter_Lvl_Informal_Skip(logging.Filter):
    
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            record=list_param_no_named[0]
            if record.levelno ==  20:
                return False
            else:
                return True
        except Exception as exception:
            raise exception
        return False

class NetFilter_Lvl_Warning_Only(logging.Filter):
    
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            record=list_param_no_named[0]
            if record.levelno ==  30:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False

class NetFilter_Lvl_Warning_Skip(logging.Filter):
    
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            record=list_param_no_named[0]
            if record.levelno ==  30:
                return False
            else:
                return True
        except Exception as exception:
            raise exception
        return False

class NetFilter_Lvl_Error_Only(logging.Filter):
    
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            record=list_param_no_named[0]
            if record.levelno ==  40:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False

class NetFilter_Lvl_Error_Skip(logging.Filter):
    
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            record=list_param_no_named[0]
            if record.levelno ==  40:
                return False
            else:
                return True
        except Exception as exception:
            raise exception
        return False

class NetFilter_Lvl_Critical_Only(logging.Filter):
    
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            record=list_param_no_named[0]
            if record.levelno ==  50:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False

class NetFilter_Lvl_Critical_Skip(logging.Filter):
    
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            record=list_param_no_named[0]
            if record.levelno ==  50:
                return False
            else:
                return True
        except Exception as exception:
            raise exception
        return False

class NetFilter_Message_Regex(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.msg)
            if match:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False

class NetFilter_Message_Regex_Reverse(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.msg)
            if match:
                return False
            else:
                return True
        except Exception as exception:
            raise exception
        return False

class NetFilter_Function_Regex(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.funcName)
            if match:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False

class NetFilter_Function_Regex_Reverse(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.funcName)
            if match:
                return False
            else:
                return True
        except Exception as exception:
            raise exception
        return False

class NetFilter_Thread_Regex(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.threadName)
            if match:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False

class NetFilter_Thread_Regex_Reverse(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.threadName)
            if match:
                return False
            else:
                return True
        except Exception as exception:
            raise exception
        return False

class NetFilter_Process_Regex(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.processName)
            if match:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False

class NetFilter_Process_Regex_Reverse(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.processName)
            if match:
                return False
            else:
                return True
        except Exception as exception:
            raise exception
        return False

class NetFilter_Name_Regex(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.name)
            if match:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False

class NetFilter_Name_Regex_Reverse(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.name)
            if match:
                return  False
            else:
                return True
        except Exception as exception:
            raise exception
        return False

class NetFilter_FileName_Regex(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.filename)
            if match:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False

class NetFilter_FileName_Regex_Reverse(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.filename)
            if match:
                return False
            else:
                return True
        except Exception as exception:
            raise exception
        return False

class NetFilter_PathName_Regex(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.pathname)
            if match:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False

class NetFilter_PathName_Regex_Reverse(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            match=re.search(self.__regex,record.pathname)
            if match:
                return False
            else:
                return True
        except Exception as exception:
            raise exception
        return False

class NetFilter_Line_Number_Regex(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            message=str(record.lineno)
            match=re.search(self.__regex,message)
            if match:
                return True
            else:
                return False
        except Exception as exception:
            raise exception
        return False
            
class NetFilter_Line_Number_Regex_Reverse(logging.Filter):
    
    @NetClassParameterContains(regex=str)
    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            self.__regex=dict_param_named['regex']
        
            return
        except Exception as exception:
            raise exception

    @NetClassParameterUnique(logging.LogRecord)
    def filter(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                     
            record=list_param_no_named[0]
            message=str(record.lineno)
            match=re.search(self.__regex,message)
            if match:
                return False
            else:
                return True
        except Exception as exception:
            raise exception
        return False
       
