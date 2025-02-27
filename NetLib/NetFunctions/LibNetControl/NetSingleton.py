__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

def Singleton(defined_class):
    instances={}
    def getinstance(*param_no_name,**param_name):
        if defined_class not in instances:
            instances[defined_class]=defined_class(*param_no_name,**param_name)
        return instances[defined_class]
    return getInstance


