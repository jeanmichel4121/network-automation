# pylint: disable=unused-variable
__author__ = 'Jean-Michel Cuvelier'



import sys
import platform
if sys.platform == 'win32':
    import wmi
import os

sys.path.insert(0,'./')

from NetLib.NetClasses.NetNotification.NetTypeNotification import NetTypeNotification


import NetLib
import socket
import inspect
import getpass
import re
import json
import yaml
from lxml import etree 
import xmltodict
from logging import Logger

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from filelock import Timeout, FileLock


import netifaces
from ipaddress import IPv4Network
import dns.resolver


class NetTypeException(NetTypeNotification):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeException,self).__new__(self,*param_no_named,**param_named)

class NetException(Exception,metaclass=NetTypeException):
    ''' Main Exception with all system information'''
    __metaclass__=NetTypeException

    __IGNORE_STACK_METODS=[
        'check_parameters_unique',
        'check_parameters_contains',
        'function_base_notify'
    ]

    __DEFAULT_CONFIG=os.path.dirname(NetLib.NetClasses.NetException.__file__)+os.path.sep+'NetException.yml'

    __BACKUP_CONFIG={
        'exception':{
            'exception_id': 'ExBase-000000',
            'separator': '\n',
            'content': {
                'values':{},
                'class_name': 'Not defined',
                'method': 'Not defined'
                },
            'context': {
                'environment': {
                    'enable': True,
                    'fields': {
                        'user': True,
                        'hostname': True,
                        'path-exec': True,
                        'path-lib': True
                        }
                    },
                'system': {
                    'enable': True,
                    'fields': {
                        'os': True,
                        'version': True,
                        'release': True
                        }
                    },
                'python': {
                    'enable': True,
                    'fields': {
                        'version': True,
                        'info': True,
                        'gcc': True,
                        'msc': True
                        }
                    },
                'network': {
                    'enable': True,
                    'fields': {
                        'interfaces': True,
                        'dns': True,
                        'hosts': True,
                        'routes': True
                        }
                    }
                }
            }
        }

    def __check_type(self,*param_no_named,**param_named):
        
        def check_type_dict(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                expected_dict=dict_param_named['expected_dict']
                inspected_dict=dict_param_named['inspected_dict']
                path=dict_param_named['path']
                           
                           
                if len(expected_dict.keys()) > 0:
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
                                'class_name':'NetException',
                                'method_name':'check_type_dict',
                                'exception_source':'self',
                                'exception_type': type(NetException),                                                             
                                'values':{
                                    'keys':path+"['"+str(key)+"']",
                                    'error':'missing key',
                                    'message':"'"+key+"' not defined in '"+path+"' with keys '"+str(list(inspected_dict.keys()))+"'"
                                    }
                                }
                                
                            if self._logger != None:
                                self._logger.error('NetException@'+ self.id +' ::check_regex_dict -> '+'exception => '+str(exception))
                            
                            raise Exception(exception) 
                else:
                    check_type_data(self,expected_type=expected_dict,inspected_type=inspected_dict,path=path)
            except Exception as ex:

                if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                    exception=dict(ex.args[0])            
                    
                    if 'method_name' in exception.keys() and exception['method_name'] != 'check_type_dict':
                        if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                            exception['method_parents']=list()                
                        exception['method_parents']= exception['method_parents']+['check_type_dict']                
                    
                    raise Exception(exception) 
                else:            
                    exception={
                        'class_name':'NetException',
                        'method_name':'check_type_dict',
                        'exception_source':ex,
                        'exception_type': type(ex)
                        }   
    
                    raise Exception(exception) 

        def check_type_list(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                expected_list=dict_param_named['expected_list']
                inspected_list=dict_param_named['inspected_list']
                path=dict_param_named['path']
                
                
                if len(expected_list) > 0:
                    if len(expected_list) <= len(inspected_list):
                        for index,elem in enumerate(expected_list):
                            if type(elem) is list:
                                check_type_list(self,expected_list=expected_list[index],inspected_list=inspected_list[index],path=path+'['+str(index)+']')
                            elif type(elem) is dict:
                                check_type_dict(self,expected_dict=expected_list[index],inspected_dict=inspected_list[index],path=path+'['+str(index)+']')
                            else:
                                check_type_data(self,expected_type=expected_list[index],inspected_type=inspected_list[index],path=path+'['+str(index)+']')
                                
                    else:
                        exception={
                            'class_name':'NetException',
                            'method_name':'check_type_list',
                            'exception_source':'self',
                            'exception_type': type(NetException),                            
                            'values':{                            
                                'count_expected':str(len(expected_list)),
                                'count_inspected':str(len(inspected_list)),
                                'error':'wrong size',
                                'message': path+' wrong sizing '+str(len(expected_list))+' element(s) expected'
                                }
                            }

                        if self._logger != None:
                            self._logger.error('NetException@'+ self.id +' ::check_type_list -> '+'exception => '+str(exception))

                        raise Exception(exception) 
                else:
                    check_type_data(self,expected_type=expected_list,inspected_type=inspected_list,path=path)                 
                            
            except Exception as ex:

                if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                    exception=dict(ex.args[0])            
                    
                    if 'method_name' in exception.keys() and exception['method_name'] != 'check_type_list':
                        if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                            exception['method_parents']=list()
                        exception['method_parents']= exception['method_parents']+['check_type_list']                
                    
                    raise Exception(exception) 
                else: 
                    exception={
                        'class_name':'NetException',
                        'method_name':'check_type_list',
                        'exception_source':ex,
                        'exception_type': type(ex)
                        }   
    
                    raise Exception(exception) 
                
        def check_type_data(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                expected_type=dict_param_named['expected_type']
                inspected_type=dict_param_named['inspected_type']
                path=dict_param_named['path']
                      
                if type(expected_type) is not type(inspected_type):
                    exception={
                        'class_name':'NetException',
                        'method_name':'check_type_data',
                        'exception_source':'self',
                        'exception_type': type(NetException),                        
                        'values':{                        
                            'type_expected':type(expected_type),
                            'type_inspected':type(inspected_type),
                            'path':path,
                            'error':'mismatching type',
                            'message': path+" type '"+re.sub("^<class '(?P<TYPE>[^'][^']*)'.*",'\\g<TYPE>',str(type(expected_type)))+"' expected not matching with '"+str(inspected_type)+"' as type '"+re.sub("^<class '(?P<TYPE>[^'][^']*)'.*",'\\g<TYPE>',str(type(inspected_type)))+"'"
                            }
                        }
                            
                    if self._logger != None:
                        self._logger.error('NetException@'+ self.id +' ::check_type_data -> '+'exception => '+str(exception))
                        
                    raise Exception(exception)        
            
            except Exception as ex:

                if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                    exception=dict(ex.args[0])            
                    
                    if 'method_name' in exception.keys() and exception['method_name'] != 'check_type_data':
                        if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                            exception['method_parents']=list()                
                        exception['method_parents']= exception['method_parents']+['check_type_data']                
                    
                    raise Exception(exception) 
                else:            
                    exception={
                        'class_name':'NetException',
                        'method_name':'__check_type',
                        'exception_source':ex,
                        'exception_type': type(ex)
                        }   
    
                    raise Exception(exception) 

        try:                      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            expected_object={
                'exception':{
                    'exception_id': '',
                    'separator': '\n',
                    'content': {
                        'values':{},
                        'class_name': '',
                        'method': ''
                        },
                    'ignore_stack_methods':[],
                    'context': {
                        'environment': {
                            'enable': False,
                            'fields': {
                                'user': True,
                                'hostname': True,
                                'path-exec': True,
                                'path-lib': True
                                }
                            },
                        'system': {
                            'enable': False,
                            'fields': {
                                'os': True,
                                'version': True,
                                'release': True
                                }
                            },
                        'python': {
                            'enable': False,
                            'fields': {
                                'version': True,
                                'info': True,
                                'gcc': True,
                                'msc': True
                                }
                            },
                        'network': {
                            'enable': False,
                            'fields': {
                                'interfaces': True,
                                'dns': True,
                                'hosts': True,
                                'routes': True
                                }
                            }
                        }
                    }
                }
            inspected_object=dict_param_named['inspected_object']

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__check_type_data -> expected => '+str(expected_object)+' || '+'inspected => '+str(inspected_object))                           
                
            if type(expected_object) is list:
                check_type_list(self,expected_list=expected_object,inspected_list=inspected_object,path='')
            elif type(expected_object) is dict:
                check_type_dict(self,expected_dict=expected_object,inspected_dict=inspected_object,path='')
            else:
                check_type_data(self,expected_type=expected_object,inspected_type=inspected_object,path='')

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__check_type_data -> Success')                         
                    
        except Exception as ex:

            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__check_type':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()
                    exception['method_parents']= exception['method_parents']+['__check_type']                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__check_type',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 

    def __environment_setup(self,*param_no_named,**param_named):
        try: 
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            retour=dict()
                                             
            setup=dict_param_named['setup']
            fields=dict_param_named['fields']
             
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__environment_setup -> setup => '+str(setup)+' || '+'fields => '+str(fields))                   
                  
            for keys in setup.keys():
                if keys in fields.keys():
                    if setup[keys] is True:
                        retour[keys]=fields[keys] 
        
            return retour
        except Exception as ex:

            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__environment_setup':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__environment_setup']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__environment_setup',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)  
    def __get_network(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            network=dict()

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_network -> Getting Network setting')   

            if sys.platform == 'win32':

                network=dict()
                network['interfaces']=dict()
                network['dns']=dns.resolver.Resolver().nameservers
                network['hosts']=self.__get_routehosts_windows()

                for interface_id in netifaces.interfaces():
                    request_wmi = wmi.WMI()
                    query_wmi ="SELECT Description FROM Win32_NetworkAdapterConfiguration WHERE SettingID=''+interface_id+''"
                    list_wmi= [ interface.Description for interface in request_wmi.query(query_wmi)]
                    if len (list_wmi)> 0:
                        interface=list_wmi[0]
                    else:
                        interface=interface

                    network['interfaces'][interface]=dict()

                    try:
                        network['interfaces'][interface]['mac']=netifaces.ifaddresses(interface_id)[netifaces.AF_LINK][0]['addr']
                        network['interfaces'][interface]['ipv4']=netifaces.ifaddresses(interface_id)[netifaces.AF_INET][0]['addr']+'/'+str(IPv4Network('0.0.0.0/'+netifaces.ifaddresses(interface_id)[netifaces.AF_INET][0]['netmask']).prefixlen)
                    except Exception as ex:
                        pass   
                    try:
                        network['interfaces'][interface]['ipv4']=netifaces.ifaddresses(interface_id)[netifaces.AF_INET][0]['addr']+'/'+str(IPv4Network('0.0.0.0/'+netifaces.ifaddresses(interface_id)[netifaces.AF_INET][0]['netmask']).prefixlen)
                    except Exception as ex:
                        pass              
                    try:
                        network['interfaces'][interface]['ipv4']=netifaces.ifaddresses(interface_id)[netifaces.AF_INET][0]['addr']+'/'+str(IPv4Network('0.0.0.0/'+netifaces.ifaddresses(interface_id)[netifaces.AF_INET][0]['netmask']).prefixlen)
                    except Exception as ex:
                        pass 
                    try:
                        for key in  netifaces.gateways().keys():
                            if key != 'default':
                                for gw in netifaces.gateways()[key]:
                                    if gw[1] == interface_id:
                                        network['interfaces'][interface]['gateways']=gw[0]
                    except Exception as ex:
                        pass
    
                    try:
                        network['interfaces'][interface]['ipv6']=list()
                        for ipv6 in netifaces.ifaddresses(interface_id)[netifaces.AF_INET6]:             
                            network['interfaces'][interface]['ipv6'].append(re.sub('%[^%][^%]*$','',ipv6['addr'])+'/'+re.sub('^[^/][^/]*/','',ipv6['netmask']))
                    except Exception as ex:
                        pass

                routes=self.__get_routev4_windows(*param_no_named,**param_named)

                updated_route=list()
                interface_ip=dict()
                for keys in network['interfaces'].keys():
                    if 'ipv4' in network['interfaces'][keys].keys():
                        interface_ip[re.sub('/[0-9][0-9]*$','',network['interfaces'][keys]['ipv4'])]=keys 

                for line in routes:
                    match=re.search('dev (?P<IP>[0-9][0-9]*\\.[0-9][0-9]*\\.[0-9][0-9]*\\.[0-9][0-9]*)',line)
                    if match:
                        ip=match.group('IP')
                        add=re.sub('dev '+ip,'dev '+interface_ip[ip],line)
                        updated_route.append(add)
                network['routes']=updated_route

            elif sys.platform == 'linux':

                
                network['interfaces']=dict()
                network['dns']=dns.resolver.Resolver().nameservers
                network['hosts']=self.__get_routehosts_linux(*param_no_named,**param_named)

                for interface in netifaces.interfaces():
                    try:
                        network['interfaces'][interface]=dict()

                        network['interfaces'][interface]['mac']=netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
                        network['interfaces'][interface]['ipv4']=netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']+'/'+str(IPv4Network('0.0.0.0/'+netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']).prefixlen)
                    except Exception as ex:
                        del network['interfaces'][interface]

                for key in  netifaces.gateways().keys():
                    if key != 'default':
                        for gw in netifaces.gateways()[key]:
                            if gw[1] in  network['interfaces'].keys():
                                network['interfaces'][gw[1]]['gateways']=gw[0]

                for interface in netifaces.interfaces():
                    if interface in network['interfaces'].keys(): 
                        network['interfaces'][interface]['ipv6']=list()
                        for ipv6 in netifaces.ifaddresses(interface)[netifaces.AF_INET6]:             
                            network['interfaces'][interface]['ipv6'].append(re.sub('%[^%][^%]*$','',ipv6['addr'])+'/'+re.sub('^[^/][^/]*/','',ipv6['netmask']))

                    network['routes']=self.__get_routev4_linux(*param_no_named,**param_named)


            return network
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_network':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_network']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_network',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)          
    def __get_python(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            python=dict()

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_python -> Getting Python setting')   


            if sys.platform == 'win32':

                python['version']=re.sub('\\).*',')',sys.version)
                python['info']=re.sub('\\)','',re.sub('sys.version_info\\(','',str(sys.version_info)))
                python['msc']=re.sub('.*\\[MSC (?P<SAVE>[^\\]][^\\]]*)\\].*','\\g<SAVE>',sys.version)

            elif sys.platform == 'linux':
                
                python['version']=re.sub('\\).*',')',sys.version.splitlines()[0])
                python['info']=re.sub('\\)','',re.sub('sys.version_info\\(','',str(sys.version_info)))
                python['gcc']=re.sub('.*\\[GCC (?P<SAVE>[^\\]][^\\]]*)\\].*','\\g<SAVE>',sys.version.splitlines()[1])


            return python
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_python':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_python']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_python',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)           
    def __get_system(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            system=dict()

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_system -> Getting System setting')  
                
            system['os']=platform.platform()
            system['version']=platform.version()
            system['release']=platform.release()

            return system
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_system':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_system']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_system',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)         
    def __get_environment(self,*param_no_named,**param_named):
        try:
            environment=dict()
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_environment -> Getting Environment setting') 

            environment['user']=getpass.getuser()
            environment['hostname']=socket.gethostname()
            path=''
            for line in sys.argv:
                path=path+ ' ' + line
            path=re.sub('^ *','',path)
            environment['path-exec']=path

            path_lib=list()
            for line in sys.path:
                if line not in path_lib:
                    path_lib.append(line)
            environment['path-lib']=path_lib

            return environment
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_environment':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_environment']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_environment',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
        
        
    def __get_routev4_windows(self,*param_no_named,**param_named):
        try:
            retour=list()
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_routev4_windows -> Getting Routes')             
            
            commands=os.popen('route print -4')
            cpt=0
            result = list()
            debut = 0
            fin=0
            for line in commands.readlines():
                route=line.replace('\n','')
                route=re.sub('  *',' ',route)
                route=re.sub('^ *','',route)
                result.append(route)
                match=re.search('^Network Destination',route)
                cpt=cpt+1
                if match:
                    debut=cpt
                if cpt > 0:
                    match=re.search('^==',route)
                if match:
                    fin=cpt-2
            for route in result[debut:fin]:
                add=route.split(' ')[0]+'/'+str(IPv4Network('0.0.0.0/'+route.split(' ')[1]).prefixlen)+' dev '+route.split(' ')[3]+' via '+route.split(' ')[2].replace('On-link','0.0.0.0')+' metric '+route.split(' ')[4]
                retour.append(add)

            retour.sort()
            return retour
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_routev4_windows':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_routev4_windows']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':' __get_routev4_windows',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    def __get_routev4_linux(self,*param_no_named,**param_named):
        try:
            retour=list()

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_routev4_linux -> Getting Routes')

            commands=os.popen('route -n')
            for line in commands.readlines()[2:]:
                route=line.replace('\n','')
                route=re.sub('  *',' ',route)
                add=route.split(' ')[0]+'/'+str(IPv4Network('0.0.0.0/'+route.split(' ')[2]).prefixlen)+' dev '+route.split(' ')[7]+' via '+route.split(' ')[1]+' metric '+route.split(' ')[4]
                retour.append(add)

            return retour
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_routev4_linux':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_routev4_linux']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_routev4_linux',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    def __get_routehosts_linux(self,*param_no_named,**param_named):
        try:
            retour=dict()
            
            files_path=[
                os.path.sep+'etc'+os.path.sep+'hosts'
            ]
            
            path=''
            for file in files_path:
                if os.path.exists(file):
                    path=file
                    
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_routehosts_linux -> '+path)                    
                    
            if path == '':
                
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_routehosts_linux',
                    'exception_source':'self',
                    'exception_type': type(NetException),
                    'values':{
                        'source_hosts':files_path,
                        'error':'hosts file not found',
                        'message':'hosts file not found in '+str(files_path)
                        }
                    }
                
                
                if self._logger != None:
                    self._logger.error('NetException@'+ self.id +' ::__get_routehosts_linux -> '+'exception => '+str(exception))                     
                
                
                raise Exception(exception)          

            with open(path, 'r') as f:
                for line in f.readlines():
                    host_line=line.lower().replace('\n','').replace('\t',' ').replace('\r','').strip()
                    match=re.search('^[0-9:a-f]',host_line)
                    if match:
                        hosts=host_line
                        ip=hosts.split(' ')[0]
                        host=''
                        for subhost in hosts.split(' ')[1:]:
                            host=host+' '+subhost
                        host=re.sub('^ *','',host)
                        host=re.sub(' *$','',host)
                        
                        if host in retour.keys():
                            if type(retour[host]) is list:
                                retour[host].append(ip)
                            else:
                                save=retour[host]
                                retour[host]=list()
                                retour[host].append(save)
                                retour[host].append(ip)
                        else:
                            retour[host]=ip
                f.close()
            return retour
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_routehosts_linux':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_routehosts_linux']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_routehosts_linux',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    def __get_routehosts_windows(self,*param_no_named,**param_named):
        try:
            retour=dict()
            
            files_path=[
                'C:'+os.path.sep+'Windows'+os.path.sep+'HOSTS',
                'C:'+os.path.sep+'windows'+os.path.sep+'system32'+os.path.sep+'drivers'+os.path.sep+'etc'+os.path.sep+'hosts',
                'C:'+os.path.sep+'winnt'+os.path.sep+'system32'+os.path.sep+'drivers'+os.path.sep+'etc'+os.path.sep+'hosts'
            ]
            
            path=''
            for file in files_path:
                if os.path.exists(file):
                    path=file
                    
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_routehosts_windows -> '+path)                       
                    
            if path == '':
                
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_routehosts_windows',
                    'exception_source':'self',
                    'exception_type': type(NetException),
                    'values':{
                        'source_hosts':files_path,
                        'error':'hosts file not found',
                        'message':'hosts file not found in '+str(files_path)
                        }
                    }
                
                if self._logger != None:
                    self._logger.error('NetException@'+ self.id +' ::__get_routehosts_windows -> '+'exception => '+str(exception))                  
                
                raise Exception(exception)                  
                         

            with open(path, 'r') as f:
                for line in f.readlines():
                    host_line=line.lower().replace('\n','').replace('\t',' ').replace('\r','').strip()
                    match=re.search('^ *[0-9:a-f]',host_line)
                    if match:
                        hosts=host_line
                        ip=hosts.split(' ')[0]
                        host=''
                        for subhost in hosts.split(' ')[1:]:
                            host=host+' '+subhost
                        host=re.sub('^ *','',host)
                        host=re.sub(' *$','',host)
                        
                        if host in retour.keys():
                            if type(retour[host]) is list:
                                retour[host].append(ip)
                            else:
                                save=retour[host]
                                retour[host]=list()
                                retour[host].append(save)
                                retour[host].append(ip)
                        else:
                            retour[host]=ip
                f.close()
            return retour
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_routehosts_windows':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_routehosts_windows']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_routehosts_windows',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 


    def __get_null(self,param):
        try:
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__getnull -> '+str(param))              
            
            exception={
                'class_name':'NetException',
                'method_name':'__get_null',
                'exception_source':'self',
                'exception_type': type(NetException),
                'values':{
                    'property':str(param),
                    'error':'read only property',
                    'message':str(param)+' is only reachable as read only property'
                }
            }

            if self._logger != None:
                self._logger.error('NetException@'+ self.id +' ::__get_null -> '+'exception => '+str(exception))

            raise Exception(exception) 
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_null':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_null']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__set_null',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    def __set_null(self,param):
        try:
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__set_null -> '+str(param))               
            
            exception={
                'class_name':'NetException',
                'method_name':'__set_null',
                'exception_source':'self',
                'exception_type': type(NetException),
                'values':{
                    'property':str(param),
                    'error':'read only property',
                    'message':str(param)+' is only reachable as read only property'
                }
            }

            if self._logger != None:
                self._logger.error('NetException@'+ self.id +' ::__set_null -> '+'exception => '+str(exception))

            raise Exception(exception) 
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__set_null':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__set_null']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__set_null',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 

    def __concatenation_dict(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            list_dict=dict_param_named['fusion']            
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__concatenation_dict -> '+' fusion => '+str(list_dict))               
            
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
        
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                if 'method_name' in exception.keys() and exception['method_name'] != '__concatenation_dict':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__concatenation_dict']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__concatenation_dict',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)  
    
    def __dict_load(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            attributes=[
                'source',
                'config',
                'file-timeout'
            ]
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__dict_load -> '+' attributes => '+str(attributes))              
            
            
            for attribut in attributes:
                if attribut not in dict_param_named.keys():
                    exception={
                        'class_name':'NetException',
                        'method_name':'__dict_load',
                        'exception_source':'self',
                        'exception_type': type(NetException),
                        'values':{
                            'keys':'['+str(attribut)+']',
                            'error':'missing key',
                            'message':'['+str(attribut)+']'+' not in '+str(list(dict_param_named.keys()))
                        }
                    }
                    
                    if self._logger != None:
                        self._logger.error('NetException@'+ self.id +' ::__dict_load -> '+'exception => '+str(exception))                     
                    
                    raise Exception(exception) 

            self.__source=dict_param_named['source']
            self._config=dict_param_named['config']
            self.FILE_TIMEOUT=dict_param_named['file-timeout']
            
            return
        
        except Exception as ex:
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__dict_load':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__dict_load']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__dict_load',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
    
                raise Exception(exception) 
    def __dict_save(self,*param_no_named,**param_named):
        try:
            retour=dict()


            retour['source']=self.__source
            retour['config']=self._config
            retour['file-timeout']=self.FILE_TIMEOUT
        
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__dict_save -> '+'attributes => '+str(retour.keys()))          
            
            return retour
            
        except Exception as ex:
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__dict_save':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__dict_save']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__dict_save',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 

    def __self_load(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__self_load -> '+'source => '+str(self.__source))            
            
            self.__load_config_updated(path=self.__source)
                        
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__self_load':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__self_load']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__self_load',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    def __set_observer(self,*param_no_named,**param_named):
        try:
            
            config={
                'patterns':['*.json','*.yml'],
                'ignore_directories':True,
                'case_sensitive':False
                }            

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__set_observer -> '+' config => '+str(config))   
            
            if self.__observer is not None:
                self.__observer.stop()
                self.__observer.join()

            event=PatternMatchingEventHandler(**config)
            event.on_modified = self.__self_load

            self.__observer=Observer()
            self.__observer.schedule(event_handler=event,path=os.path.dirname(str(self.__source)),recursive=False)
            self.__observer.start()

        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__set_observer':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__set_observer']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__set_observer',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 


    def __init__(self,*param_no_named,**param_named):
        try:
            dict_param_named=dict(param_named)
            list_param_no_named=list(param_no_named) 
            
            super(NetException,self).__init__(*param_no_named)
            self.FILE_TIMEOUT=20
            self.__source=None
            self._config=dict()
            self.__observer=None            

            self._logger=None
            if 'logger' in dict_param_named.keys() and issubclass(type(dict_param_named['logger']),Logger):
                self.logger=dict_param_named['logger']
            else:        
                for elem in list_param_no_named:
                    if issubclass(type(elem),Logger):
                        self.logger=elem
                        
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__init__ -> Creating object')

            if 'path-source' in dict_param_named.keys() and type(dict_param_named['path-source'] is str):
                path=dict_param_named['path-source']
            else:
                path=self.__DEFAULT_CONFIG

            self.source=path
            self.__increment_id(*param_no_named,**param_named)
            args=tuple()
            

            for elem in param_no_named:
                if issubclass(type(elem),Exception) is True and issubclass(type(elem),NetException) is False:
                    self._config['exception']['content']['exception_source']=elem
                    self._config['exception']['content']['exception_type']=type(elem)
                    args=args+(elem,)

                elif issubclass(type(elem),NetException) is True:
                    pass

                elif issubclass(type(elem),Logger):
                    pass                
                else:
                    args=args+(elem,)

            self.args=args 

            if 'exception_source' not in self._config['exception']['content'].keys():
                self._config['exception']['content']['exception_source']='self'          
                                
            if 'exception_type' not in self._config['exception']['content'].keys():
                self._config['exception']['content']['exception_type']=type(self) 
            
            self._config['exception']['content']['class_name']='NetException'
            
            method_parent=list()
            i=0
            regex=""
            if len (self._config['exception']['ignore_stack_methods']) > 0:
                for elem in self._config['exception']['ignore_stack_methods']:
                   regex=regex+elem+'|'
                regex=regex[:-1]
            else:
                regex='^$'
        
            for elem in inspect.stack()[4:-1]:
                match=re.search(regex,elem[3])        
                if  re.search('^ *super\\(NetException',elem[4][0]) is None and not match:
                    if i == 0:
                        msg=str(elem[3])+' => '
                        for subelem in elem[4]:
                            msg=msg+re.sub(' *$','',re.sub('^ *','',subelem).replace('\n',''))+' | '
                        msg=re.sub(' \\| ','',msg)
                        msg=msg+' => '+str(elem[2])+' => '+str(elem[1])
                    
                        self._config['exception']['content']['method']=msg
                    else:
                                            
                        msg="{:02d}".format(i)+') '+str(elem[3])+' => '
                        for subelem in elem[4]:
                            msg=msg+re.sub(' *$','',re.sub('^ *','',subelem).replace('\n',''))+' | '
                        msg=re.sub(' \\| ','',msg)
                        msg=msg+' => '+str(elem[2])+' => '+str(elem[1])              
                    
                        method_parent.append(msg)
                    i=i+1
                
            self._config['exception']['content']['method_parent']=method_parent

            content=dict()
            for keys in param_named.keys():
                if keys != 'path-source':
                    content[keys]=param_named[keys]
            self.content=content            
            
            if self._logger != None:
                self._logger.info('NetException object created => '+str(self._config['exception']['exception_id']))            
                    
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__init__':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__init__']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__init__',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    def __getstate__(self):
        try:
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__getstate__ -> Getting State')                
            
            state=dict(self.__dict_save())
            state['dict']=self.__dict__
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__getstate__':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__getstate__']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__getstate__',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    def __setstate__(self,state):
        try:
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__setstate__ -> Setting State') 
            
            if type(state) is dict:
                self.__dict__=state['dict']
                self.__dict_load(**state)
            return
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__setstate__':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__setstate__']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__setstate__',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)    
    def __str__(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__str__ -> Getting str')               

            retour=self.str_message_sorted
            return retour
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__str__':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__str__']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__str__',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)     
    
    
    def __parse_str_to_list(self,*param_no_named,**param_named):
        try:
            dict_param_named=dict(param_named)
            list_param_no_named=list(param_no_named)         
            list_environment=list()

            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            lines=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__parse_str_to_list -> '+'lines => '+str(lines))              
            

            for line in lines.split(self._config['exception']['separator']):
                list_environment.append(line)    
            return list_environment    
            
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__parse_str_to_list':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__parse_str_to_list']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__parse_str_to_list',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)                    

    def __parse_dict_to_str_lines(self,*param_no_named,**param_named):
        try:
            dict_param_named=dict(param_named)
            list_param_no_named=list(param_no_named)         
        
            if len (list_param_no_named) > 0:
                elem=list_param_no_named[0]
         
                if self._logger != None:
                    self._logger.debug('NetException@'+ self.id +' ::__parse_dict_to_str_lines -> '+str(elem))                                                   
                                            
                if type(elem) is list:
                    retour=''
                    for elm in elem:
                        if len(list_param_no_named) > 1:                        
                            retour=retour+str(self.__parse_dict_to_str_lines(elm,list_param_no_named[1]))
                        else:
                            retour=retour+str(self.__parse_dict_to_str_lines(elm))
                    return retour   
                elif type(elem) is dict:
                    retour=''
                    for keys in elem.keys():
                        if len(list_param_no_named) > 1:                        
                            retour=retour+str(self.__parse_dict_to_str_lines(elem[keys],list_param_no_named[1]+'['+keys+']'))
                        else:
                            retour=retour+str(self.__parse_dict_to_str_lines(elem[keys],'['+keys+']'))
                    return retour
                
                elif type(elem) is etree._Element:
                        if len(list_param_no_named) > 1:                        
                            return str(self.__parse_dict_to_str_lines(self.__parse_xml_to_dict(elem),list_param_no_named[1]))
                        else:
                            return str(self.__parse_dict_to_str_lines(self.__parse_xml_to_dict(elem)))
                           
                else:
                    if len(list_param_no_named) > 1:
                        return str(list_param_no_named[1]+': '+str(elem)+self._config['exception']['separator'])
                    else:
                        return str(str(elem)+self._config['exception']['separator'])            
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__parse_dict_to_str_lines':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__parse_dict_to_str_lines']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__parse_dict_to_str_lines',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 

    def __parse_xml_to_dict(self,*param_no_named,**param_named):
        try:
            dict_param_named=dict(param_named)
            list_param_no_named=list(param_no_named)
                        
            cpt=0
            while len(list_param_no_named) < cpt and type(list_param_no_named[cpt]) is not etree._Element:
                cpt=cpt+1
            xml=list_param_no_named[cpt]
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__parse_xml_to_dict -> '+str(xml))                   

            return dict(xmltodict.parse(etree.tostring(xml,encoding='utf-8',pretty_print=True).decode('utf-8'),encoding='utf-8',attr_prefix='',cdata_key='#text', dict_constructor=dict))
            
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__parse_xml_to_dict':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__parse_xml_to_dict']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__parse_xml_to_dict',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 


    def _load_dictionary_file(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            input_file=dict_param_named['file']
            retour={}

            if self._logger is not None:
                self._logger.debug('NetException@'+ self.id +' ::_load_dictionary_file -> '+'input_file => '+str(input_file))           
                        
            extension=re.sub('.*\\.(?P<EXTENSION>[^\\.][^\\.]*)$','\\g<EXTENSION>',input_file).lower()
            if extension != 'json' and extension != 'yml':
                exception={
                    'class_name':'NetException',
                    'method_name':'_load_dictionary_file',
                    'exception_source':'self',
                    'exception_type': type(NetException),
                    'values':{                        
                        'error':'extension is not supported',
                        'expected_extensions':'json | yml',
                        'inspected_extension': extension,
                        'source_path':input_file,
                        'message':extension+" is not supported"
                        }
                }

                if self._logger is not None:
                    self._logger.error('NetException@'+ self.id +' ::_load_dictionary_file -> '+'exception => '+str(exception))                         
                        
                raise Exception(exception)                           
            elif extension == 'json' :
                retour=self.__load_dictionary_file_json(file=input_file)
            elif extension == 'yml':
                retour=self.__load_dictionary_file_yaml(file=input_file)

            return retour

        except Exception as ex:                 
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '_load_dictionary_file':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['_load_dictionary_file']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':' _load_dictionary_file',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    def __load_dictionary_file_json(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            retour={}

            lock_path=''
            lock=None            
            
            input_file=dict_param_named['file']
                        
            extension=re.sub('.*\\.(?P<EXTENSION>[^\\.][^\\.]*)$','\\g<EXTENSION>',input_file).lower()
            if extension != 'json':
                input_file=input_file+'.json'

            if self._logger is not None:
                self._logger.debug('NetException@'+ self.id +' ::__load_dictionary_file_json -> '+'input_file => '+str(input_file))

            if len(input_file.split(os.path.sep)) > 1:
                directory=os.path.sep.join(input_file.split(os.path.sep)[:-1])
                if os.path.isdir(directory):
                    if os.path.isfile(input_file):
                        lock_path=input_file+'.lock'
                        lock= FileLock(lock_path, timeout=self.FILE_TIMEOUT)
                        with lock.acquire(timeout=self.FILE_TIMEOUT):
                            with open(input_file, 'r') as file:
                                retour = json.load(file)
                                file.close()
                            lock.release()
                    else:
                        exception={
                            'class_name':'NetException',
                            'method_name':'__load_dictionary_file_json',
                            'exception_source':'self',
                            'exception_type': type(NetException),
                            'values':{ 
                                'error':'file not found',
                                'source_file': input_file,
                                'message':input_file+" doesn't exist"
                                }
                        }
    
                        if self._logger is not None:
                            self._logger.error('NetException@'+ self.id +' ::__load_dictionary_file_json -> '+'exception => '+str(exception))                         
                        
                        raise Exception(exception)
                else:
                    exception={
                        'class_name':'NetException',
                        'method_name':'__load_dictionary_file_json',
                        'exception_source':'self',
                        'exception_type': type(NetException),
                        'values':{ 
                            'error':'path is wrong',
                            'source_directory': directory,
                            'message':directory+" doesn't exist"
                            }
                    }
 
                    if self._logger is not None:
                        self._logger.error('NetException@'+ self.id +' ::__load_dictionary_file_json -> '+'exception => '+str(exception))                         
                        
                    raise Exception(exception)
            else:
                if os.path.isfile(input_file):
                    lock_path=input_file+'.lock'
                    lock= FileLock(lock_path, timeout=self.FILE_TIMEOUT)
                    with lock.acquire(timeout=self.FILE_TIMEOUT):              
                        with open(input_file, 'r') as file:
                            retour = json.load(file)
                            file.close()
                        lock.release()
                else:
                    exception={
                        'class_name':'NetException',
                        'method_name':'__load_dictionary_file_json',
                        'exception_source':'self',
                        'exception_type': type(NetException),
                        'values':{                         
                            'error':'file not found',
                            'source_file': input_file,
                            'message':input_file+" doesn't exist"
                            }
                    }
    
                    if self._logger is not None:
                        self._logger.error('NetException@'+ self.id +' ::__load_dictionary_file_json -> '+'exception => '+str(exception))                         
                        
                    raise Exception(exception)
            
            if self._logger is not None:
                self._logger.debug('NetException@'+ self.id +' ::__load_dictionary_file_json -> Success')

            return retour           

        except Exception as ex:
            if lock is not None:
                lock.release()                      
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__load_dictionary_file_json':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__load_dictionary_file_json']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':' __load_dictionary_file_json',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
                raise Exception(exception)
    def __load_dictionary_file_yaml(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            retour={}

            lock_path=''
            lock=None            

            input_file=dict_param_named['file']
                        
            extension=re.sub('.*\\.(?P<EXTENSION>[^\\.][^\\.]*)$','\\g<EXTENSION>',input_file).lower()
            if extension != 'yml':
                input_file=input_file+'.yml'

            if self._logger is not None:
                self._logger.debug('NetException@'+ self.id +' ::__load_dictionary_file_yaml -> '+'input_file => '+str(input_file))

            if len(input_file.split(os.path.sep)) > 1:
                directory=os.path.sep.join(input_file.split(os.path.sep)[:-1])
                if os.path.isdir(directory):
                    if os.path.isfile(input_file):
                        lock_path=input_file+'.lock'
                        lock= FileLock(lock_path, timeout=self.FILE_TIMEOUT)
                        with lock.acquire(timeout=self.FILE_TIMEOUT):
                            with open(input_file, 'r') as file:
                                retour = yaml.safe_load(file.read())
                                file.close()
                            lock.release()  
                    else:
                        exception={
                            'class_name':'NetException',
                            'method_name':'__load_dictionary_file_yaml',
                            'exception_source':'self',
                            'exception_type': type(NetException),
                            'values':{                             
                                'error':'file not found',
                                'source_file': input_file,
                                'message':input_file+" doesn't exist"
                                }
                        }
    
                        if self._logger is not None:
                            self._logger.error('NetException@'+ self.id +' ::__load_dictionary_file_yaml -> '+'exception => '+str(exception))                         
                            
                        raise Exception(exception) 
                else:
                    exception={
                        'class_name':'NetException',
                        'method_name':'__load_dictionary_file_yaml',
                        'exception_source':'self',
                        'exception_type': type(NetException),
                        'values':{                          
                            'error':'path is wrong',
                            'source_directory': directory,
                            'message':directory+" doesn't exist"
                            }
                    }
                    if self._logger is not None:
                        self._logger.error('NetException@'+ self.id +' ::__load_dictionary_file_yaml -> '+'exception => '+str(exception))                         
                        
                    raise Exception(exception) 
            else:
                if os.path.isfile(input_file):
                    lock_path=input_file+'.lock'
                    lock= FileLock(lock_path, timeout=self.FILE_TIMEOUT)
                    with lock.acquire(timeout=self.FILE_TIMEOUT):                
                        with open(input_file, 'r') as file:
                            retour = yaml.safe_load(file.read())
                            file.close()
                        lock.release()
                else:
                    exception={
                        'class_name':'NetException',
                        'method_name':'__load_dictionary_file_yaml',
                        'exception_source':'self',
                        'exception_type': type(NetException),
                        'values':{                           
                            'error':'file not found',
                            'source_file': input_file,
                            'message':input_file+" doesn't exist"
                            }
                    }
    
                    if self._logger is not None:
                        self._logger.error('NetException@'+ self.id +' ::__load_dictionary_file_yaml -> '+'exception => '+str(exception))                         
                        
                    raise Exception(exception)                           
            if self._logger is not None:
                self._logger.debug('NetException@'+ self.id +' ::__save_dictionary_file_yaml -> Success')    

            return retour

        except Exception as ex:
            if lock is not None:
                lock.release()                      
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__load_dictionary_file_yaml':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__load_dictionary_file_yaml']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':' __load_dictionary_file_yaml',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
                raise Exception(exception)  


    def _save_dictionary_file(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            output_file=dict_param_named['file']
            dictionary=dict_param_named['dictionary']
           
            if self._logger is not None:
                self._logger.debug('NetException@'+ self.id +' ::_save_dictionary_file -> '+'output_file => '+str(output_file)+' || '+'dictionary => '+str(dictionary))           
                        
            extension=re.sub('.*\\.(?P<EXTENSION>[^\\.][^\\.]*)$','\\g<EXTENSION>',output_file).lower()
            if extension != 'json' and extension != 'yml':
                exception={
                    'class_name':'NetException',
                    'method_name':'_save_dictionary_file',
                    'exception_source':'self',
                    'exception_type': type(NetException),
                    'values':{                      
                        'error':'extension is not supported',
                        'expected_extensions':'json | yml',
                        'inspected_extension': extension,
                        'source_path':output_file,
                        'message':extension+" is not supported"
                        }
                }

                if self._logger is not None:
                    self._logger.error('NetException@'+ self.id +' ::_save_dictionary_file -> '+'exception => '+str(exception))                         
                        
                raise Exception(exception) 
            elif extension == 'json' :
                self.__save_dictionary_file_json(file=output_file,dictionary=dictionary)
            elif extension == 'yml':
                self.__save_dictionary_file_yaml(file=output_file,dictionary=dictionary)           

        except Exception as ex:           
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '_save_dictionary_file':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['_save_dictionary_file']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':' _save_dictionary_file',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)         
    def __save_dictionary_file_json(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            output_file=dict_param_named['file']
            dictionary=dict_param_named['dictionary']

            lock_path=''
            lock=None
                        
            extension=re.sub('.*\\.(?P<EXTENSION>[^\\.][^\\.]*)$','\\g<EXTENSION>',output_file).lower()
            if extension != 'json':
                output_file=output_file+'.json'

            if self._logger is not None:
                self._logger.debug('NetException@'+ self.id +' ::__save_dictionary_file_json -> '+'output_file => '+str(output_file)+' || '+'dictionary => '+str(dictionary))

            if len(output_file.split(os.path.sep)) > 1:
                directory=os.path.sep.join(output_file.split(os.path.sep)[:-1])
                if os.path.isdir(directory):

                    lock_path=output_file+'.lock'
                    lock= FileLock(lock_path, timeout=self.FILE_TIMEOUT)
                    with lock.acquire(timeout=self.FILE_TIMEOUT):     
                        with open(output_file, 'w') as file:
                            json.dump(dictionary, file,indent=3,sort_keys=False)
                            file.close()
                        lock.release()
                else:

                    exception={
                        'class_name':'NetException',
                        'method_name':'__save_dictionary_file_json',
                        'exception_source':'self',
                        'exception_type': type(NetException),
                        'values':{   
                            'error':'path is wrong',
                            'source_directory': directory,
                            'message':directory+" doesn't exist"
                            }
                    }
 
                    if self._logger is not None:
                        self._logger.error('NetException@'+ self.id +' ::__save_dictionary_file_json -> '+'exception => '+str(exception))                         
                        
                    raise Exception(exception)
            else:
                lock_path=output_file+'.lock'
                lock= FileLock(lock_path, timeout=self.FILE_TIMEOUT)
                with lock.acquire(timeout=self.FILE_TIMEOUT):                  
                    with open(output_file, 'w') as file:
                        json.dump(dictionary, file,indent=3,sort_keys=False)
                        file.close()
                    lock.release()
            
            if self._logger is not None:
                self._logger.debug('NetException@'+ self.id +' ::__save_dictionary_file_json -> Success')               

        except Exception as ex:
            if lock is not None:
                lock.release()                      
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__save_dictionary_file_json':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__save_dictionary_file_json']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':' __save_dictionary_file_json',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
                raise Exception(exception)
    def __save_dictionary_file_yaml(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            output_file=dict_param_named['file']
            dictionary=dict_param_named['dictionary']

            lock_path=''
            lock=None  

            extension=re.sub('.*\\.(?P<EXTENSION>[^\\.][^\\.]*)$','\\g<EXTENSION>',output_file).lower()
            if extension != 'yml':
                output_file=output_file+'.yml'

            if self._logger is not None:
                self._logger.debug('NetException@'+ self.id +' ::__save_dictionary_file_yaml -> '+'output_file => '+str(output_file)+' || '+'dictionary => '+str(dictionary))

            if len(output_file.split(os.path.sep)) > 1:
                directory=os.path.sep.join(output_file.split(os.path.sep)[:-1])
                if os.path.isdir(directory):

                    lock_path=output_file+'.lock'
                    lock= FileLock(lock_path, timeout=self.FILE_TIMEOUT)
                    with lock.acquire(timeout=self.FILE_TIMEOUT):  
                        with open(output_file, 'w') as file:
                            yaml.dump(dictionary, file,indent=3,sort_keys=False)
                            file.close()
                        lock.release()

                else:

                    exception={
                        'class_name':'NetException',
                        'method_name':'__save_dictionary_file_yaml',
                        'exception_source':'self',
                        'exception_type': type(NetException),
                        'values':{ 
                            'error':'path is wrong',
                            'source_directory': directory,
                            'message':directory+" doesn't exist"
                            }
                    }
 
                    if self._logger is not None:
                        self._logger.error('NetException@'+ self.id +' ::__save_dictionary_file_yaml -> '+'exception => '+str(exception))                         
                        
                    raise Exception(exception)
            else:
                lock_path=output_file+'.lock'
                lock= FileLock(lock_path, timeout=self.FILE_TIMEOUT)
                with lock.acquire(timeout=self.FILE_TIMEOUT):                
                    with open(output_file, 'w') as file:
                        yaml.dump(dictionary, file,indent=3,sort_keys=False)
                        file.close()
                    lock.release()

            if self._logger is not None:
                self._logger.debug('NetException@'+ self.id +' ::__save_dictionary_file_yaml -> Success')    

        except Exception as ex:
            if lock is not None:
                lock.release()                      
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__save_dictionary_file_yaml':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__save_dictionary_file_yaml']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':' __save_dictionary_file_yaml',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
                raise Exception(exception)
                               
    def __upgrade_source(self,*param_no_named,**param_named):
        try:
            lock=None
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            updated={
                'separator':self._config['exception']['separator']
            }
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__upgrade_source -> '+str(updated.keys()))              
            
            config=self._load_dictionary_file(file=self.__source)    
            
            for keys in updated.keys():
                if keys in config.keys():
                    config['exception'][keys]=updated[keys]
            
            self._save_dictionary_file(file=self.__source,dictionary=config)    
                                                                  
        except Exception as ex:

            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])

                if 'method_name' in exception.keys() and exception['method_name'] != '__upgrade_source':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__upgrade_source']
                
                raise Exception(exception)  

            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__upgrade_source',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise Exception(exception)            


    def __load_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            path=dict_param_named['path']
            

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__load_config -> '+str(path))             

            config=self._load_dictionary_file(file=path)
            self.__check_type(inspected_object=config)

                
            self._config=config.copy()
            self.__source=path
            
            if self._logger != None:
                self._logger.info('NetException config loaded :: '+str(path))            
        

        except Exception as ex:
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])

                if 'method_name' in exception.keys() and exception['method_name'] != '__load_config':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__load_config']
                
                raise Exception(exception)  
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__load_config',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise Exception(exception) 
    def __load_config_updated(self,*param_no_named,**param_named):
        try:
            lock=None
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            path=dict_param_named['path']
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__load_config_updated -> '+str(path))             
            
            config=self._load_dictionary_file(file=path)
                        
            self.__source=path
            self._config['exception']['separator']=config['exception']['separator']

            origin=config['exception']['exception_id']
            base=re.sub('[0-9][0-9]*$','',origin)
                                    
            self._config['exception']['exception_id']=re.sub('.*[^0-9](?P<NUMBER>[0-9][0-9]*)$',base+'\\g<NUMBER>',self._config['exception']['exception_id'])
            self._config['exception']['context']=config['exception']['context'].copy()
                
        
        except Exception as ex:
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])

                if 'method_name' in exception.keys() and exception['method_name'] != '__load_config_updated':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__load_config_updated']
                
                raise Exception(exception)  
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__load_config_updated',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise Exception(exception) 

  
    def save_json(self,*param_no_named,**param_named):
        try:
            lock=None
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1

            output=list_param_no_named[i]
                        
            extension=re.sub('.*\\.(?P<EXTENSION>[^\\.][^\\.]*)$','\\g<EXTENSION>',output).lower()
            if extension != 'json':
                output=output+'.json'

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::save_json -> '+str(output))

            directory=os.path.sep.join(output.split(os.path.sep)[:-1])
            if os.path.isdir(directory):

                with open(output, 'w') as file:
                    json.dump(self._config, file,indent=3,sort_keys=False)
                    
            else:                        
                exception={
                    'class_name':'NetException',
                    'method_name':'save_json',
                    'exception_source':'self',
                    'exception_type': type(NetException),                        
                    'values':{
                        'error':'path is wrong',
                        'source_directory': directory,
                        'message':directory+" doesn't exist"
                        }
                    }

                if self._logger != None:
                    self._logger.error('NetException@'+ self.id +' ::save_json -> '+str(exception))                         
                        
                raise Exception(exception)                      
                                       
        except Exception as ex:
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])

                if 'method_name' in exception.keys() and exception['method_name'] != 'save_json':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['save_json']
                
                raise Exception(exception)  
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'save_json',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise Exception(exception) 
    def save_yaml(self,*param_no_named,**param_named):
        try:
            lock=None
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1

            output=list_param_no_named[i]
                        
            extension=re.sub('.*\\.(?P<EXTENSION>[^\\.][^\\.]*)$','\\g<EXTENSION>',output).lower()
            if extension != 'yml':
                output=output+'.yml'


            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::save_yaml -> '+str(output))

            directory=os.path.sep.join(output.split(os.path.sep)[:-1])
            if os.path.isdir(directory):

                with open(output, 'w') as file:
                    yaml.dump(self._config, file,indent=3,sort_keys=False)
                    
            else:                        
                exception={
                    'class_name':'NetException',
                    'method_name':'save_yaml',
                    'exception_source':'self',
                    'exception_type': type(NetException),                        
                    'values':{
                        'error':'path is wrong',
                        'source_directory': directory,
                        'message':directory+" doesn't exist"
                        }
                    }

                if self._logger != None:
                    self._logger.error('NetException@'+ self.id +' ::save_yaml -> '+str(exception))                         
                        
                raise Exception(exception)                         

                                       
        except Exception as ex:
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])

                if 'method_name' in exception.keys() and exception['method_name'] != 'save_yaml':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['save_yaml']
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'save_yaml',
                    'exception_source':ex,
                    'exception_type': type(ex)
                }   
                raise Exception(exception)  
  
    def __increment_id(self,*param_no_named,**param_named):
        try:
            lock=None
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__increment_id -> increment '+self._config['exception']['exception_id'])
  
            config=self._load_dictionary_file(file=self.__source)
            match=re.search('(?P<NUMBER>[0-9][0-9]*)$',config['exception']['exception_id'])
            if match:
                size=len(match.group('NUMBER'))
                number=int(match.group('NUMBER'))
                number=number+1
                
                inc='{:0>'+str(size)+'d}'
                inc=inc.format(number)
                    
                config['exception']['exception_id']=re.sub('[0-9][0-9]*$',inc,config['exception']['exception_id'])
                
                self._save_dictionary_file(file=self.__source,dictionary=config)
                self._config['exception']['exception_id']=config['exception']['exception_id']
                
                    
        except Exception as ex: 
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__increment_id':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__increment_id']
                
                raise Exception(exception)                 
                
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__increment_id',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)        
    def __decrement_id(self,*param_no_named,**param_named):
        try:
            lock=None
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__decrement_id -> decrement '+self._config['exception']['exception_id'])
  
  
            config=self._load_dictionary_file(file=self.__source)
            match=re.search('(?P<NUMBER>[0-9][0-9]*)$',config['exception']['exception_id'])
            if match:
                size=len(match.group('NUMBER'))
                number=int(match.group('NUMBER'))
                if number > 0:
                    number=number-1
                
                inc='{:0>'+str(size)+'d}'
                inc=inc.format(number)
                    
                config['exception']['exception_id']=re.sub('[0-9][0-9]*$',inc,config['exception']['exception_id'])
                
                self._save_dictionary_file(file=self.__source,dictionary=config)
                self._config['exception']['exception_id']=config['exception']['exception_id']
                
                    
        except Exception as ex: 
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__decrement_id':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__decrement_id']
                
                raise Exception(exception)                 
                
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__decrement_id',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)            
            
                                    
    def __set_source(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            path=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__set_source -> '+str(path))                  
            
            self.__load_config(path=path)

            self.__set_observer()
            
        except Exception as ex:
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            

                if 'method_name' in exception.keys() and exception['method_name'] != '__set_source':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__set_source']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__set_source',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)      
    def __get_source(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_source -> '+str(self.__source))             
            
            return self.__source
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_source':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_source']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_source',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    source=property(__get_source,__set_source)     
    
        
    def __set_content(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            cpt=0
            while len(list_param_no_named) < cpt and type(list_param_no_named[cpt]) is not dict:
                cpt=cpt+1
            content=list_param_no_named[cpt]

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__set_content -> '+str(content))  

            fusion=[
                self._config['exception']['content']['values'],
                content
            ]
            self._config['exception']['content']['values']=self.__concatenation_dict(fusion=fusion)

                    
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__set_content':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__set_content']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__set_content',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    def __get_content(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_content -> '+str(self._config['exception']['content'])) 
       
            return self._config['exception']['content'].copy()
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_content':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_content']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_content',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    content=property(__get_content,__set_content)
    
    def __set_logger(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while not issubclass(type(list_param_no_named[i]),Logger) and list_param_no_named[i] is not None:
                i=i+1
            logger=list_param_no_named[i]
            
            self._logger=logger
            return
        except Exception as ex:    
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__set_logger':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__set_logger']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__set_logger',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)  
    logger=property(__get_null,__set_logger)
    
    
    def __set_separator(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            cpt=0
            while len(list_param_no_named) < cpt and type(list_param_no_named[cpt]) is not str:
                cpt=cpt+1
            separator=list_param_no_named[cpt]

            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__set_separator -> '+str(separator)) 

            self._config['exception']['separator']=separator
            self.__upgrade_source(*param_no_named,**param_named)
                    
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__set_separator':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__set_separator']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__set_separator',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    def __get_separator(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_separator -> '+str(self._config['exception']['separator']))             
            
            return self._config['exception']['separator']
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_separator':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_separator']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_separator',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)   
    separator=property(__get_separator,__set_separator)
    
    def __get_context(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            retour=dict()
            retour['context']=dict() 
            context=self._config['exception']['context']
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_context -> '+str(context)) 
                

            if 'environment' in context.keys() and 'enable' in context['environment'].keys() and context['environment']['enable'] is True :
                retour['context']['environment']=self.__environment_setup(setup=self._config['exception']['context']['environment']['fields'],fields=self.__get_environment(*param_no_named,**param_named))

            if 'system' in context.keys() and 'enable' in context['system'].keys() and context['system']['enable'] is True :
                retour['context']['system']=self.__environment_setup(setup=self._config['exception']['context']['system']['fields'],fields=self.__get_system(*param_no_named,**param_named))
                
            if 'python' in context.keys() and 'enable' in context['python'].keys() and context['python']['enable'] is True :
                retour['context']['python']=self.__environment_setup(setup=self._config['exception']['context']['python']['fields'],fields=self.__get_python(*param_no_named,**param_named))
            
            if 'network' in context.keys() and 'enable' in context['network'].keys() and context['network']['enable'] is True :
                retour['context']['network']=self.__environment_setup(setup=self._config['exception']['context']['network']['fields'],fields=self.__get_network(*param_no_named,**param_named))             

            return retour
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_context':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_context']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_context',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    context=property(__get_context,__set_null)

    def __get_id(self,*param_no_named,**param_named):
        try:
            exception_id="N/A"
            if self._config is not None and type(self._config) is dict and 'exception' in self._config.keys() and type(self._config['exception']) is dict and 'exception_id' in self._config['exception'].keys():
                exception_id=self._config['exception']['exception_id']
                        
            return exception_id
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_id':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_id']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_id',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    id=property(__get_id,__set_null)
    
    def __get_list_message(self,*param_no_named,**param_named):
        try:
            list_msg=list()
                  
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_list_message -> Getting list Message')                       
                  
                  
            for line in self.str_message.split(self._config['exception']['separator']):
                list_msg.append(line)
                
            for line in self.args:
                list_msg.append('[values][args]: '+str(line))
            return list_msg
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_list_message':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_list_message']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_list_message',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception)   
    list_message=property(__get_list_message,__set_null)    
    def __get_str_message(self,*param_no_named,**param_named):
        try:           
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_str_message -> Getting str Message')               
            

            str_msg=''
            content=self.content.copy()
            content['exception_id']=self._config['exception']['exception_id']


            lines=self.__parse_dict_to_str_lines(content)+self.__parse_dict_to_str_lines(self.context)

            str_msg=lines.split(self._config['exception']['separator'])[0]
            for line in lines.split(self._config['exception']['separator'])[1:-1]:
                str_msg=str_msg+self._config['exception']['separator']+line

            for line in self.args:
                str_msg=str_msg+self._config['exception']['separator']+'[values][args]: '+str(line)

            return str_msg
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_str_message':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_str_message']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_str_message',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    str_message=property(__get_str_message,__set_null)   
    def __get_str_message_sorted(self,*param_no_named,**param_named):
        try:           
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetException@'+ self.id +' ::__get_str_message_sorted -> Getting str Message sorted')               
            

            lines=self.str_message
            
            content=self.content.copy()

            content['exception_id']=self._config['exception']['exception_id']
            lines_content=self.__parse_dict_to_str_lines(content)
            lines_context=self.__parse_dict_to_str_lines(self.context)
            str_msg=''
            for line in sorted(lines_content.split(self._config['exception']['separator']),key=str.lower)[1:]:
                str_msg=str_msg+self._config['exception']['separator']+line                         
            
            for line in sorted(lines_context.split(self._config['exception']['separator']),key=str.lower)[1:]:
                str_msg=str_msg+self._config['exception']['separator']+line             
            
            
            return str_msg
        except Exception as ex:
            
            if len(ex.args) > 0 and type(ex.args[0]) is dict and 'class_name' in dict(ex.args[0]).keys() and dict(ex.args[0])['class_name'] == 'NetException':
                exception=dict(ex.args[0])            
                
                if 'method_name' in exception.keys() and exception['method_name'] != '__get_str_message_sorted':
                    if 'values' in exception.keys() and 'method_parents' not in exception.keys():
                        exception['method_parents']=list()                
                    exception['method_parents']= exception['method_parents']+['__get_str_message_sorted']                
                
                raise Exception(exception) 
            else:            
                exception={
                    'class_name':'NetException',
                    'method_name':'__get_str_message_sorted',
                    'exception_source':ex,
                    'exception_type': type(ex)
                    }   
 
                raise Exception(exception) 
    str_message_sorted=property(__get_str_message_sorted,__set_null) 
