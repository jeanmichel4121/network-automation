__author__ = 'Jean-Michel Cuvelier'

import sys

import types

def Notify_Function(fct_called, *param_no_named, **param_named):
    try:
        def function_base_notify(*param_no_named, **param_named):
            result = fct_called(*param_no_named, **param_named)
            #print("Notify_Function"+" : "+str(param_no_named)+str(param_named))
            return result
        return function_base_notify
    except BaseException as ex:
        raise ex
    return

def Notify_String(fct_called, *param_no_named, **param_named):
    try:
        def function_base_notify(*param_no_named, **param_named):            
            result = fct_called(*param_no_named, **param_named)
            #print("Notify_String"+" : "+str(param_no_named)+str(param_named))
            return result
        return function_base_notify
    except BaseException as ex:
        raise ex
    return

def Notify_Number(fct_called, *param_no_named, **param_named):
    try:
        def function_base_notify(*param_no_named, **param_named):            
            result = fct_called(*param_no_named, **param_named)
            #print("Notify_Number"+" : "+str(param_no_named)+str(param_named))
            return result
        return function_base_notify
    except BaseException as ex:
        raise ex
    return

def Notify_Dictionnary(fct_called, *param_no_named, **param_named):
    try:
        def function_base_notify(*param_no_named, **param_named):            
            result = fct_called(*param_no_named, **param_named)
            #print("Notify_Dictionnary"+" : "+str(param_no_named)+str(param_named))
            return result
        return function_base_notify
    except BaseException as ex:
        raise ex
    return

def Notify_List(fct_called, *param_no_named, **param_named):
    try:
        def function_base_notify(*param_no_named, **param_named):            
            result = fct_called(*param_no_named, **param_named)
            #print("Notify_List"+" : "+str(param_no_named)+str(param_named))
            return result
        return function_base_notify
    except BaseException as ex:
        raise ex
    return


class NetTypeNotification(type):    
    def __new__( self, *param_no_named,**param_named):

        dict_param_named=dict(param_named)
        list_param_no_named=list(param_no_named)

        classname=list_param_no_named[0]
        superclasses=list_param_no_named[1]
        attributdict=list_param_no_named[2]


        list_call_Notify_Function=list([types.FunctionType,types.MethodType,types.LambdaType])
        list_call_Notify_String=list([type(str)])
        list_call_Notify_Number=list([type(int),type(float)])
        list_call_Notify_Dictionnary=list([type(dict),type(tuple)])
        list_call_Notify_List=list([type(list)])

        for name_param, value_param in attributdict.items():            
            if type(value_param) in list_call_Notify_Function:
                attributdict[name_param] = Notify_Function(value_param)
                
            if type(value_param) in list_call_Notify_String:
                attributdict[name_param] = Notify_String(value_param)
                
            if type(value_param) in list_call_Notify_Number:
                attributdict[name_param] = Notify_Number(value_param)
                
            if type(value_param) in list_call_Notify_Dictionnary:
                attributdict[name_param] = Notify_Dictionnary(value_param)
                    
            if type(value_param) in list_call_Notify_List:
                attributdict[name_param] = Notify_List(value_param)            

        return super(NetTypeNotification,self).__new__(self,*param_no_named,**param_named)
        
    def __init__(self, *param_no_named, **param_named):
        try:                        
            super(NetTypeNotification,self).__init__(*param_no_named,**param_named)        
            
        except Exception as ex :
            raise ex