__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

import time
import re

def NetUniqueClassParameterController(*c_param_no_named,**c_param_named):
    def decorator(execute_function):
        def checktype(obj,*param_no_named,**param_named): 
            #PARAMETERS NO NAMED
            if len(c_param_no_named) != len(param_no_named):
                raise TypeError("{0} parameter(s) no named received instead {1} expected => {2}".format(str(len(param_no_named)),str(len(c_param_no_named)),re.sub(" *\<class *'(?P<NAME>[^'\>]*)' *\> *","\g<NAME>",str(c_param_no_named))))                       
            for i in range(0,len(param_no_named)):
                if issubclass(type(param_no_named[i]),c_param_no_named[i]) == False:
                    raise TypeError("parameter {0} \"{1}\" with the value {2} is not target type \"{3}\"".format(i+1,type (param_no_named[i]),str(param_no_named[i]),c_param_no_named[i]))
                
            #PARAMETERS NAMED
            for key in c_param_named:
                if key not in param_named:
                    raise TypeError("variable name : \"{0}\" must be defined with type \"{1}\"".format(str(key),str(c_param_named[key])))
            for key in param_named:
                if key not in c_param_named:
                    raise TypeError("variable name : \"{0}\" must not be defined".format(str(key)))
                if issubclass(type(param_named[key]),c_param_named[key]) == False:
                    raise TypeError("variable name : \"{0}\" with the value \"{1}\" is not target type \"{2}\"".format(str(key),str(param_named[key]),c_param_named[key]))
            return execute_function(obj,*param_no_named,**param_named)
        return checkType
    return Decorator

def NetUniqueFunctionParameterController(*c_param_no_named,**c_param_named):
    def decorator(execute_function):
        def checktype(*param_no_named,**param_named): 
            #PARAMETERS NO NAMED
            if len(c_param_no_named) != len(param_no_named):
                raise TypeError("{0} parameter(s) no named received instead {1} expected => {2}".format(str(len(param_no_named)),str(len(c_param_no_named)),re.sub(" *\<class *'(?P<NAME>[^'\>]*)' *\> *","\g<NAME>",str(c_param_no_named))))                       
            for i in range(0,len(param_no_named)):
                if issubclass(type(param_no_named[i]),c_param_no_named[i]) == False:
                    raise TypeError("parameter {0} \"{1}\" with the value {2} is not target type \"{3}\"".format(i+1,type (param_no_named[i]),str(param_no_named[i]),c_param_no_named[i]))
                
            #PARAMETERS NAMED
            for key in c_param_named:
                if key not in param_named:
                    raise TypeError("variable name : \"{0}\" must be defined with type \"{1}\"".format(str(key),str(c_param_named[key])))
            for key in param_named:
                if key not in c_param_named:
                    raise TypeError("variable name : \"{0}\" must not be defined".format(str(key)))
                if issubclass(type(param_named[key]),c_param_named[key]) == False:
                    raise TypeError("variable name : \"{0}\" with the value \"{1}\" is not target type \"{2}\"".format(str(key),str(param_named[key]),c_param_named[key]))
            return execute_function(*param_no_named,**param_named)
        return checkType
    return Decorator

def NetContainsClassParameterController(*c_param_no_named,**c_param_named):
    def decorator(execute_function):
        def checktype(obj,*param_no_named,**param_named):            
            
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
                    if issubclass(type(expected_parameter),key) == True:
                        if key in dict_read_parameter.keys():
                            dict_read_parameter[key]=dict_read_parameter[key]+1
                        else:
                            dict_read_parameter[key]=1
            
            #compare dictinnary
            for expected_parameter in dict_expected_parameter.keys():
                if expected_parameter in dict_read_parameter.keys():
                    if dict_expected_parameter[expected_parameter] > dict_read_parameter[expected_parameter]:
                        raise TypeError("{0} parameter(s) \"{1}\" is required but {2} is received".format(str(dict_expected_parameter[expected_parameter]),str(expected_parameter),str(dict_read_parameter[expected_parameter])))
                else:
                    raise TypeError("{0} parameter(s) \"{1}\" is required None is received".format(str(dict_expected_parameter[expected_parameter]),str(expected_parameter)))
                        
            #PARAMETERS NAMED
            for key in c_param_named:
                if key not in param_named:
                    raise TypeError("variable name : \"{0}\" must be defined with type \"{1}\"".format(str(key),str(c_param_named[key])))
                elif issubclass(type(param_named[key]),c_param_named[key]) == False:
                    raise TypeError("variable name : \"{0}\" with the value \"{1}\" is not target type \"{2}\"".format(str(key),str(param_named[key]),c_param_named[key]))
                
            return execute_function(obj,*param_no_named,**param_named)
        return checkType
    return Decorator

def NetContainsFunctionParameterController(*c_param_no_named,**c_param_named):
    def decorator(execute_function):
        def checktype(*param_no_named,**param_named):            
            
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
                    if issubclass(type(expected_parameter),key) == True:
                        if key in dict_read_parameter.keys():
                            dict_read_parameter[key]=dict_read_parameter[key]+1
                        else:
                            dict_read_parameter[key]=1 
            
            #compare dictinnary
            for expected_parameter in dict_expected_parameter.keys():
                if expected_parameter in dict_read_parameter.keys():
                    if dict_expected_parameter[expected_parameter] > dict_read_parameter[expected_parameter]:
                        raise TypeError("{0} parameter(s) \"{1}\" is required but {2} is received".format(str(dict_expected_parameter[expected_parameter]),str(expected_parameter),str(dict_read_parameter[expected_parameter])))
                else:
                    raise TypeError("{0} parameter(s) \"{1}\" is required None is received".format(str(dict_expected_parameter[expected_parameter]),str(expected_parameter)))
                        
            #PARAMETERS NAMED
            for key in c_param_named:
                if key not in param_named:
                    raise TypeError("variable name : \"{0}\" must be defined with type \"{1}\"".format(str(key),str(c_param_named[key])))
                elif issubclass(type(param_named[key]),c_param_named[key]) == False:
                    raise TypeError("variable name : \"{0}\" with the value \"{1}\" is not target type \"{2}\"".format(str(key),str(param_named[key]),c_param_named[key]))
                
            return execute_function(*param_no_named,**param_named)
        return checkType
    return Decorator


