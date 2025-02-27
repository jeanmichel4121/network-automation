__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

from NetLib.NetClasses.NetException.NetException import NetException,NetTypeException,NetTypeException
from NetLib.NetClasses.NetNotification.NetTypeNotification import NetTypeNotification

import time
import re
import json

class NetTypeExcpetionClassParameter(NetTypeException):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeExcpetionClassParameter,self).__new__(self,*param_no_named,**param_named)

class NetTypeExcpetionClassParameterInside(NetTypeException):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeExcpetionClassParameterInside,self).__new__(self,*param_no_named,**param_named)


class NetExceptionClassParameterInside(Exception,metaclass=NetTypeExcpetionClassParameterInside):
    __metaclass__=NetTypeExcpetionClassParameterInside      
    def __init__(self,*param_no_named,**param_named):
        try:        
            super(NetExceptionClassParameterInside,self).__init__(*param_no_named,**param_named)
        except Exception as ex:
            raise ex      
    def __str__(self):
        return super(NetExceptionClassParameterInside,self).__str__()

class NetExceptionClassParameter(NetException,metaclass=NetTypeExcpetionClassParameter):
    __metaclass__=NetTypeExcpetionClassParameter
    
    def __setnull(self,param):
        try:
            ex=Exception(str(param)+ ' cannot be defined the parameter is on read only')
            raise ex
        except Exception as ex:
            raise ex
        return None  
    
    def __init__(self,*param_no_named,**param_named):
        try:        
            super(NetExceptionClassParameter,self).__init__(*param_no_named,**param_named)
            self._config['exception']['content']['class_name']='NetClassParameter'
        except Exception as ex:
            raise ex
          
    def __str__(self):
        return super(NetExceptionClassParameter,self).__str__()

def NetClassParameterCombine(*c_param_no_named,**c_param_named):
    def decorator(execute_function):
        def check_parameters_combine(obj,*param_no_named,**param_named):            

            def check_parameters_contains(obj,*c_param_no_named,**c_param_named):            
                exception={}
 
                parameter_expected='( '
                expected=list()
                for elem in c_param_no_named:
                    expected.append(re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(elem)))                
                for elem in expected:               
                    parameter_expected=parameter_expected+elem+', '            
                for keys in sorted(c_param_named.keys(),key=str.lower):
                    parameter_expected=parameter_expected+keys+'= '+re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(c_param_named[keys]))+', '
                
                parameter_expected=re.sub(', $','',parameter_expected)
                parameter_expected=parameter_expected+' )'
                                
                exception['parameters_expected']=parameter_expected

                #PARAMETERS NO NAMED
                dict_expected_parameter=dict()
                dict_read_parameter=dict()
                
                #reading expected number parameter 
                for expected_parameter in c_param_no_named:
                    if expected_parameter in dict_expected_parameter.keys():
                        dict_expected_parameter[expected_parameter]=dict_expected_parameter[expected_parameter]+1
                    else:
                        dict_expected_parameter[expected_parameter]=1
                
                #reading received number parameter 
                for expected_parameter in param_no_named:
                    for key in dict_expected_parameter.keys():
                        if issubclass(type(expected_parameter),key) == True or issubclass(type(type(expected_parameter)),key) == True:
                            if key in dict_read_parameter.keys():
                                dict_read_parameter[key]=dict_read_parameter[key]+1
                            else:
                                dict_read_parameter[key]=1
                
                #compare dictinnary
                for expected_parameter in dict_expected_parameter.keys():
                    if expected_parameter in dict_read_parameter.keys():
                        if dict_expected_parameter[expected_parameter] > dict_read_parameter[expected_parameter]:
                            exception['message']="{0} \"no named parameter(s)\" as type \"{1}\" is required. Only {2} is received".format(str(dict_expected_parameter[expected_parameter]),re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(expected_parameter)),str(dict_read_parameter[expected_parameter]))              
                            raise NetExceptionClassParameterInside(exception)                                                
                    else:
                        exception['message']="{0} \"no named parameter(s)\" as type \"{1}\" is required. Only 0 is received".format(str(dict_expected_parameter[expected_parameter]),re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(expected_parameter)))              
                        raise NetExceptionClassParameterInside(**exception) 
                                                
                #PARAMETERS NAMED
                for key in c_param_named:
                    if key not in param_named:
                        exception['message']="\"named parameter\" \"{0}\" is required".format(str(key))                                        
                        raise NetExceptionClassParameterInside(exception)                                        
                    elif issubclass(type(param_named[key]),c_param_named[key]) == False and issubclass(type(type(param_named[key])),c_param_named[key]) == False:            
                        exception['message']="\"named parameter\" \"{0}\" is not the required type of \"{1}\"".format(str(key),re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(c_param_named[key])))                                                                                                   
                        raise NetExceptionClassParameterInside(exception)              

            def check_parameters_unique(obj,*c_param_no_named,**c_param_named): 
                #PARAMETERS NO NAMED
                exception={}

                parameter_expected='( '
                expected=list()
                for elem in c_param_no_named:
                    expected.append(re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(elem)))                
                for elem in expected:
                    parameter_expected=parameter_expected+elem+', '            
                for keys in sorted(c_param_named.keys(),key=str.lower):
                    parameter_expected=parameter_expected+keys+'= '+re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(c_param_named[keys]))+', '
                
                parameter_expected=re.sub(', $','',parameter_expected)
                parameter_expected=parameter_expected+' )'
                                
                exception['parameters_expected']=parameter_expected

                if len(c_param_no_named) != len(param_no_named):

                    exception['message']="{0} \"no named parameter(s)\" received instead {1} required".format(str(len(param_no_named)),str(len(c_param_no_named)))                
                        
                    raise NetExceptionClassParameterInside(exception)
                for i in range(0,len(param_no_named)):

                    if issubclass(type(param_no_named[i]),c_param_no_named[i]) == False and issubclass(type(type(param_no_named[i])),c_param_no_named[i]) == False:
                        
                        exception['message']="\"no named parameter\" \"{0}\" is not the required type of \"{1}\"".format(i+1,re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(c_param_no_named[i])))    
                        raise NetExceptionClassParameterInside(exception)                    

                #PARAMETERS NAMED
                for key in c_param_named:
                    if key not in param_named:
                        
                        exception['message']="\"named parameter\" \"{0}\" is required".format(str(key))                                        
                        raise NetExceptionClassParameterInside(exception)
                    
                for key in param_named:
                    if key not in c_param_named:
                        
                        exception['message']="\"named parameter\" \"{0}\" not wanted".format(str(key))                                                                                                   
                        raise NetExceptionClassParameterInside(exception)                     
                                            
                    if issubclass(type(param_named[key]),c_param_named[key]) == False and issubclass(type(type(param_named[key])),c_param_named[key]) == False:
                        exception['message']="\"named parameter\" \"{0}\" is not the required type of \"{1}\"".format(str(key),re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(c_param_named[key])))                                                                                                   
                        raise NetExceptionClassParameterInside(exception) 

            exception={
                'function':execute_function.__name__,
                'class_source':type(obj).__name__,
                'parameters_expected':[],
                'paramaters_inspected':'',
                'message':[]
                }                      

            parameter_received='( '
            received=list()
            for elem in param_no_named:
                received.append(re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(type(elem))))                
            for elem in received:
                parameter_received=parameter_received+elem+', '
            for keys in sorted(param_named.keys(),key=str.lower):
                parameter_received=parameter_received+keys+'= '+re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(type(param_named[keys])))+', '
                            
            parameter_received=re.sub(', $','',parameter_received)
            parameter_received=parameter_received+' )'

            exception['paramaters_inspected']=parameter_received


            for elem in c_param_no_named:
                if type(elem) is list:
                    for fct in elem:
                        try:
                            function_name=re.sub('^(?P<NAME>[^\\.][^\\.]*)\\..*$','\g<NAME>',fct.__qualname__)
                            if function_name == 'NetClassParameterContains':
                                check_parameters_contains(obj,*fct.__closure__[1].cell_contents,**fct.__closure__[0].cell_contents)
                                return execute_function(obj,*param_no_named,**param_named)
                            elif function_name == 'NetClassParameterUnique':
                                check_parameters_unique(obj,*fct.__closure__[1].cell_contents,**fct.__closure__[0].cell_contents)
                                return execute_function(obj,*param_no_named,**param_named)
                            else:
                                exception={
                                    'function':execute_function.__name__,
                                    'class_source':type(obj).__name__,
                                    'functions_expected': 'NetClassParameterContains | NetClassParameterUnique',
                                    'functions_received': function_name,
                                    'message': function_name+' function not found'
                                    }
                                raise NetExceptionClassParameter(**exception) 
                        
                        except NetExceptionClassParameterInside as ex:
                            message=ex.args[0]
                            exception['parameters_expected'].append(message['parameters_expected'])
                            exception['message'].append(message['message'])

                        except Exception as ex:
                            raise ex
                    raise NetExceptionClassParameter(**exception)
            return execute_function(obj,*param_no_named,**param_named)
        return check_parameters_combine
    return decorator

def NetClassParameterContains(*c_param_no_named,**c_param_named):
    def decorator(execute_function):
        def check_parameters_contains(obj,*param_no_named,**param_named):            
            exception={
                'function':execute_function.__name__,
                'class_source':type(obj).__name__
                }

            parameter_expected='( '
            expected=list()
            for elem in c_param_no_named:
                expected.append(re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(elem)))                
            for elem in expected:               
                parameter_expected=parameter_expected+elem+', '            
            for keys in sorted(c_param_named.keys(),key=str.lower):
                parameter_expected=parameter_expected+keys+'= '+re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(c_param_named[keys]))+', '
            
            parameter_expected=re.sub(', $','',parameter_expected)
            parameter_expected=parameter_expected+' )'
                            

            parameter_received='( '
            received=list()
            for elem in param_no_named:
                received.append(re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(type(elem))))                
            for elem in received:
                parameter_received=parameter_received+elem+', '
            for keys in sorted(param_named.keys(),key=str.lower):
                parameter_received=parameter_received+keys+'= '+re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(type(param_named[keys])))+', '
                            
            parameter_received=re.sub(', $','',parameter_received)
            parameter_received=parameter_received+' )'


            exception['parameters_expected']=parameter_expected
            exception['paramaters_inspected']=parameter_received


            #PARAMETERS NO NAMED
            dict_expected_parameter=dict()
            dict_read_parameter=dict()
            
            #reading expected number parameter 
            for expected_parameter in c_param_no_named:
                if expected_parameter in dict_expected_parameter.keys():
                    dict_expected_parameter[expected_parameter]=dict_expected_parameter[expected_parameter]+1
                else:
                    dict_expected_parameter[expected_parameter]=1
            
            #reading received number parameter 
            for expected_parameter in param_no_named:
                for key in dict_expected_parameter.keys():
                    if issubclass(type(expected_parameter),key) == True or issubclass(type(type(expected_parameter)),key) == True:
                        if key in dict_read_parameter.keys():
                            dict_read_parameter[key]=dict_read_parameter[key]+1
                        else:
                            dict_read_parameter[key]=1
            
            #compare dictinnary
            for expected_parameter in dict_expected_parameter.keys():
                if expected_parameter in dict_read_parameter.keys():
                    if dict_expected_parameter[expected_parameter] > dict_read_parameter[expected_parameter]:
                        exception['message']="{0} \"no named parameter(s)\" as type \"{1}\" is required. Only {2} is received".format(str(dict_expected_parameter[expected_parameter]),re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(expected_parameter)),str(dict_read_parameter[expected_parameter]))              
                        raise NetExceptionClassParameter(**exception)                                                
                else:
                    exception['message']="{0} \"no named parameter(s)\" as type \"{1}\" is required. Only 0 is received".format(str(dict_expected_parameter[expected_parameter]),re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(expected_parameter)))              
                    raise NetExceptionClassParameter(**exception) 
                                            
            #PARAMETERS NAMED
            for key in c_param_named:
                if key not in param_named:
                    exception['message']="\"named parameter\" \"{0}\" is required".format(str(key))                                        
                    raise NetExceptionClassParameter(**exception)                                        
                elif issubclass(type(param_named[key]),c_param_named[key]) == False and issubclass(type(type(param_named[key])),c_param_named[key]) == False:            
                    exception['message']="\"named parameter\" \"{0}\" is not the required type of \"{1}\"".format(str(key),re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(c_param_named[key])))                                                                                                   
                    raise NetExceptionClassParameter(**exception)  
                        
            return execute_function(obj,*param_no_named,**param_named)
        return check_parameters_contains
    return decorator

def NetClassParameterUnique(*c_param_no_named,**c_param_named):
    def decorator(execute_function):
        def check_parameters_unique(obj,*param_no_named,**param_named): 
            #PARAMETERS NO NAMED
            exception={
                'function':execute_function.__name__,
                'class_source':type(obj).__name__
                }

            parameter_expected='( '
            expected=list()
            for elem in c_param_no_named:
                expected.append(re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(elem)))                
            for elem in expected:
                parameter_expected=parameter_expected+elem+', '            
            for keys in sorted(c_param_named.keys(),key=str.lower):
                parameter_expected=parameter_expected+keys+'= '+re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(c_param_named[keys]))+', '
            
            parameter_expected=re.sub(', $','',parameter_expected)
            parameter_expected=parameter_expected+' )'
                            

            parameter_received='( '
            received=list()
            for elem in param_no_named:
                received.append(re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(type(elem))))                
            for elem in received:
                parameter_received=parameter_received+elem+', '
            for keys in sorted(param_named.keys(),key=str.lower):
                parameter_received=parameter_received+keys+'= '+re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(type(param_named[keys])))+', '
                            
            parameter_received=re.sub(', $','',parameter_received)
            parameter_received=parameter_received+' )'

            exception['parameters_expected']=parameter_expected
            exception['paramaters_inspected']=parameter_received

            if len(c_param_no_named) != len(param_no_named):

                exception['message']="{0} \"no named parameter(s)\" received instead {1} required".format(str(len(param_no_named)),str(len(c_param_no_named)))                
                    
                raise NetExceptionClassParameter(**exception)
            for i in range(0,len(param_no_named)):
                if issubclass(type(param_no_named[i]),c_param_no_named[i]) == False and issubclass(type(type(param_no_named[i])),c_param_no_named[i]) == False:
                    
                    exception['message']="\"no named parameter\" \"{0}\" is not the required type of \"{1}\"".format(i+1,re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(c_param_no_named[i])))    
                    raise NetExceptionClassParameter(**exception)                    
                    
            #PARAMETERS NAMED
            for key in c_param_named:
                if key not in param_named:
                    
                    exception['message']="\"named parameter\" \"{0}\" is required".format(str(key))                                        
                    raise NetExceptionClassParameter(**exception)
                
            for key in param_named:
                if key not in c_param_named:
                    
                    exception['message']="\"named parameter\" \"{0}\" not wanted".format(str(key))                                                                                                   
                    raise NetExceptionClassParameter(**exception)                     
              
                if issubclass(type(param_named[key]),c_param_named[key]) == False and issubclass(type(type(param_named[key])),c_param_named[key]) == False:
                    exception['message']="\"named parameter\" \"{0}\" is not the required type of \"{1}\"".format(str(key),re.sub("<class '(?P<CLASS>[^'][^']*)'>",'\\g<CLASS>',str(c_param_named[key])))                                                                                                   
                    raise NetExceptionClassParameter(**exception)
            return execute_function(obj,*param_no_named,**param_named)
        return check_parameters_unique
    return decorator
