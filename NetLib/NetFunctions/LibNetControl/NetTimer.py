__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

import time

def TimerRunTimeController():
    def decorator(execute_function):
        def checktimer(*param_non_named,**param_named):            
            before=time.time()
            result_function=execute_function(*param_non_named,**param_named)
            after=time.time()
            runtime=after-before
            param_named["runtime"]=runtime
            
            return result_function
        return checkTimer
    return Decorator


