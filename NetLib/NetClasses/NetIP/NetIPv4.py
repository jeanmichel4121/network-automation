# pylint: disable=unused-variable
__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

from NetLib.NetClasses.NetClassParatemter.NetClassParameter import NetClassParameterUnique,NetClassParameterContains,NetClassParameterCombine
from NetLib.NetClasses.NetException.NetException import NetException
from NetLib.NetClasses.NetConfig.NetConfigFile.NetConfigFile import NetTypeConfigFile,NetTypeExcpetionConfigFile,NetExceptionConfigFile,NetConfigFile
import re
import sys
from ipaddress import IPv4Address,IPv4Interface,IPv4Network
from logging import Logger


class NetTypeIPv4(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeIPv4,self).__new__(self,*param_no_named,**param_named)

class NetTypeExceptionIPv4(NetTypeExcpetionConfigFile):
    def __new__( self,*param_no_named,**param_named):
        return super(NetTypeExceptionIPv4,self).__new__(self,*param_no_named,**param_named)

class NetExceptionIPv4(NetExceptionConfigFile,metaclass=NetTypeExceptionIPv4):
    __metaclass__=NetTypeExceptionIPv4
    
    def __init__(self,*param_no_named,**param_named):
        super(NetExceptionIPv4,self).__init__(*param_no_named,**param_named)
        self._config['exception']['content']['class_name']='NetIPv4'
          
    def __str__(self):
        return super(NetExceptionIPv4,self).__str__()

class NetIPv4(NetConfigFile,metaclass=NetTypeIPv4):
    __metaclass__=NetTypeIPv4

    __DEFAULT_CONFIG={
    }

    __DEFAULT_TYPE={
        'ipv4':''
    }

    __DEFAULT_REGEX={
        'ipv4':'^(([0-9])|([1-9][0-9])|(1([0-9]{2}))|(2[0-4][0-9])|(25[0-5]))((\.(([0-9])|([1-9][0-9])|(1([0-9]{2}))|(2[0-4][0-9])|(25[0-5]))){3})$|^(([0-9])|([1-9][0-9])|(1([0-9]{2}))|(2[0-4][0-9])|(25[0-5]))((\.(([0-9])|([1-9][0-9])|(1([0-9]{2}))|(2[0-4][0-9])|(25[0-5]))){3})\/(([0-9])|([12][0-9])|(3[0-2]))$'
    }

    @NetClassParameterUnique(old_config=dict,new_config=dict)
    def _update_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            super(NetConfigFile,self)._update_config(*param_no_named,**param_named)
            old_config=dict_param_named['old_config']
            new_config=dict_param_named['new_config']

            if self._logger is not None:
                self._logger.debug('NetIPv4@'+ self._id +' ::_update_config -> '+'new_config => '+str(new_config)) 

            self.__interface=IPv4Interface(new_config['ipv4'])
                
            if self._logger != None:
                self._logger.info('NetIPv4@'+ self._id +' ::_update_config -> '+'Success')
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 


    @NetClassParameterUnique(load=dict)     
    def _dict_load(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            super(NetIPv4,self)._dict_load(*list_param_no_named,**dict_param_named)
            
            load=dict_param_named['load']
            
            attributes=[
            ]
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id +' ::_dict_load -> '+'attributes => '+str(attributes))                
            
            for attribut in attributes:
                if attribut not in dict_param_named.keys():
                    exception={
                        'keys':'['+attribut+']',
                        'error':'missing key',
                        'message':'['+attribut+']'+' not in '+str(list(dict_param_named.keys()))
                        }
                
                    if self._logger != None:
                        self._logger.error('NetIPv4@'+ self._id +' ::_dict_load -> '+'exception => '+str(exception))                    
                        
                    raise NetExceptionIPv4(self._logger,**exception)
            
            return
                        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)  
    def _dict_save(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            retour=super(NetIPv4,self)._dict_save(*list_param_no_named,**dict_param_named)
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id +' ::__dict_save -> '+'atributes => '+str(retour.keys()))
                
            return retour
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)  

    def __init__(self,*param_no_named,**param_named):    
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            self.__interface=None
            ipv4='N/A'

            super(NetIPv4,self).__init__(*list_param_no_named,**dict_param_named)        

            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__init__ -> Creating object') 

            self.config_type=NetIPv4.__DEFAULT_TYPE
            self.config_regex=NetIPv4.__DEFAULT_REGEX                   

            if 'ipv4' in dict_param_named.keys() and type(dict_param_named['ipv4'] is str):
                self.ipv4_interface=dict_param_named['ipv4']
                ipv4=dict_param_named['ipv4']

            if self._logger != None:
                self._logger.info('NetIPv4@'+ self._id +' :: '+'object created -> '+'id => ' + self._id +' || '+'ipv4_interface => '+ipv4)                

            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
 
    def __str__(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__str__ -> Getting str')             
            
            return str(self.__interface)
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    def generate_all_properties(self,*param_no_named,**param_named):
        try:
            
            retour=dict()

            if self.__interface is not None:
                ip_range=32-self.__interface.network.prefixlen

                retour['ipv4_address']=str(self.__interface.ip)
                retour['ipv4_network']=str(self.__interface.network)
                retour['ipv4_interface']=str(self.__interface)
                retour['ipv4_network_id']=str(self.__interface.network.network_address)
                retour['ipv4_prefix']=str(self.__interface.network.prefixlen)
                retour['ipv4_subnet']=str(self.__interface.network.netmask)
                retour['ipv4_wildcard']=str(self.__interface.hostmask)
                
                if ip_range > 1:
                    retour['ipv4_broadcast']=str(self.__interface.network[-1])
                    retour['ipv4_first_ip']=str(self.__interface.network[1])
                    retour['ipv4_last_ip']=str(self.__interface.network[-2])

                elif ip_range > 0:
                    retour['ipv4_broadcast']=str(self.__interface.network[-1])
                    retour['ipv4_first_ip']=str(self.__interface.network[1])
                    retour['ipv4_last_ip']=str(self.__interface.network[-1])
                else:
                    retour['ipv4_broadcast']=str(self.__interface.network[0])
                    retour['ipv4_first_ip']=str(self.__interface.network[0])
                    retour['ipv4_last_ip']=str(self.__interface.network[0])

                retour['ipv4_route_netmask']=str(self.__interface.network.network_address)+' '+str(self.__interface.network.netmask)
                retour['ipv4_route_prefix']=str(self.__interface.network.network_address)+'/'+str(self.__interface.network.prefixlen)
                retour['ipv4_acl_wildcard']=str(self.__interface.network.network_address)+' '+str(self.__interface.hostmask)

            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::generate_all_properties -> '+'retour => '+str(retour)) 

            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 

    def __set_ipv4_address(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_ipv4_address -> ipv4_address read only property')            
            
            exception={
                'property':'ipv4_address',
                'error':'read only property',
                'message':'ipv4_address is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetIPv4@'+ self._id + ' ::__set_ipv4_address -> ipv4_address read only property')
                            
            raise NetExceptionIPv4(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)
    def __get_ipv4_address(self,*param_no_named,**param_named):
        try:
            retour='N/A'
            if self.__interface is not None:
                retour=str(self.__interface.ip)
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_ipv4_address -> '+'ipv4_address => '+retour)            
            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    ipv4_address=property(__get_ipv4_address,__set_ipv4_address)            

    def __set_ipv4_network(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_ipv4_network -> ipv4_network read only property')            
            
            exception={
                'property':'ipv4_network',
                'error':'read only property',
                'message':'ipv4_network is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetIPv4@'+ self._id + ' ::__set_ipv4_network -> ipv4_network read only property')
                            
            raise NetExceptionIPv4(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)
    def __get_ipv4_network(self,*param_no_named,**param_named):
        try:
            retour='N/A'
            if self.__interface is not None:
                retour=str(self.__interface.network)            
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_ipv4_network -> '+'ipv4_network => '+retour)
                            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    ipv4_network=property(__get_ipv4_network,__set_ipv4_network)          
    
    @NetClassParameterContains(str)
    def __set_ipv4_interface(self,*param_no_named,**param_named):
        try:
            
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            ipv4=list_param_no_named[i]            
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_ipv4_interface -> '+ipv4)             
            
            self._config['ipv4']=ipv4
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)     
    def __get_ipv4_interface(self,*param_no_named,**param_named):
        try:
            retour='N/A'
            if self.__interface is not None:
                retour=str(self.__interface)              

            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_ipv4_interface -> '+'ipv4_interface => '+retour) 
            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    ipv4=property(__get_ipv4_interface,__set_ipv4_interface)      
  
    def __set_network_id(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_network_id -> network_id read only property')            
            
            exception={
                'property':'network_id',
                'error':'read only property',
                'message':'network_id is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetIPv4@'+ self._id + ' ::__set_network_id -> network_id read only property')
                            
            raise NetExceptionIPv4(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)
    def __get_network_id(self,*param_no_named,**param_named):
        try:
            retour='N/A'
            if self.__interface is not None:
                retour=str(self.__interface.network.network_address)                 

            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_network_id -> '+'network_id => '+retour)            
            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    network_id=property(__get_network_id,__set_network_id)

    def __set_prefix(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_prefix -> prefix read only property')            
            
            exception={
                'property':'prefix',
                'error':'read only property',
                'message':'prefix is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetIPv4@'+ self._id + ' ::__set_prefix -> prefix read only property')
                            
            raise NetExceptionIPv4(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)
    def __get_prefix(self,*param_no_named,**param_named):
        try:
            retour='N/A'
            if self.__interface is not None:
                retour=str(self.__interface.network.prefixlen)                
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_prefix -> '+'prefix => '+str(retour))              
            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    prefix=property(__get_prefix,__set_prefix) 

    def __set_subnet(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_subnet -> subnet read only property')            
            
            exception={
                'property':'subnet',
                'error':'read only property',
                'message':'subnet is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetIPv4@'+ self._id + ' ::__set_subnet -> subnet read only property')
                            
            raise NetExceptionIPv4(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)
    def __get_subnet(self,*param_no_named,**param_named):
        try:
            retour='N/A'
            if self.__interface is not None:
                retour=str(self.__interface.network.netmask)

            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_subnet -> '+'subnet => '+retour)              
            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    subnet=property(__get_subnet,__set_subnet)     

    def __set_wildcard(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_wildcard -> wildcard read only property')            
            
            exception={
                'property':'wildcard',
                'error':'read only property',
                'message':'wildcard is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetIPv4@'+ self._id + ' ::__set_wildcard -> wildcard read only property')
                            
            raise NetExceptionIPv4(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)
    def __get_wildcard(self,*param_no_named,**param_named):
        try:
            retour='N/A'
            if self.__interface is not None:
                retour=str(self.__interface.hostmask)

            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_wildcard -> '+'wildcard => '+retour)              
            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    wildcard=property(__get_wildcard,__set_wildcard)
    
    def __set_broadcast(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_broadcast -> broadcast read only property')            
            
            exception={
                'property':'broadcast',
                'error':'read only property',
                'message':'broadcast is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetIPv4@'+ self._id + ' ::__set_broadcast -> broadcast read only property')
                            
            raise NetExceptionIPv4(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)
    def __get_broadcast(self,*param_no_named,**param_named):
        try:
            ip_range=32-self.__interface.network.prefixlen
            retour='N/A'
            if self.__interface is not None:
                if ip_range > 0:
                    retour=str(self.__interface.network[-1])
                else:
                    retour=str(self.__interface.network[0])
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_broadcast -> '+'broadcast => '+retour)  
            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    broadcast=property(__get_broadcast,__set_broadcast)  

    def __set_last_ip(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_last_ip -> last_ip read only property')            
            
            exception={
                'property':'last_ip',
                'error':'read only property',
                'message':'last_ip is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetIPv4@'+ self._id + ' ::__set_last_ip -> last_ip read only property')
                            
            raise NetExceptionIPv4(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)
    def __get_last_ip(self,*param_no_named,**param_named):
        try:
            ip_range=32-self.__interface.network.prefixlen
            retour='N/A'
            if self.__interface is not None:
                if ip_range > 1:
                    retour=str(self.__interface.network[-2])
                elif ip_range > 0:
                    retour=str(self.__interface.network[-1])
                else:
                    retour=str(self.__interface.network[0])

            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_last_ip -> '+'last_ip => '+retour)              
            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    last_ip=property(__get_last_ip,__set_last_ip)    

    def __set_first_ip(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_first_ip -> first_ip read only property')            
            
            exception={
                'property':'first_ip',
                'error':'read only property',
                'message':'first_ip is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetIPv4@'+ self._id + ' ::__set_first_ip -> first_ip read only property')
                            
            raise NetExceptionIPv4(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)
    def __get_first_ip(self,*param_no_named,**param_named):
        try:
            ip_range=32-self.__interface.network.prefixlen
            retour='N/A'
            if self.__interface is not None:
                if ip_range > 0:
                    retour=str(self.__interface.network[1])
                else:
                    retour=str(self.__interface.network[0])

            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_first_ip -> '+'first_ip => '+retour)              
            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    first_ip=property(__get_first_ip,__set_first_ip)
    
    def __set_route_netmask(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_route_netmask -> route_netmask read only property')            
            
            exception={
                'property':'route_netmask',
                'error':'read only property',
                'message':'route_netmask is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetIPv4@'+ self._id + ' ::__set_route_netmask -> route_netmask read only property')
                            
            raise NetExceptionIPv4(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)
    def __get_route_netmask(self,*param_no_named,**param_named):
        try:
            retour='N/A'
            if self.__interface is not None:
                retour=str(self.__interface.network.network_address)+' '+str(self.__interface.network.netmask)

            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_route_netmask -> '+'route_netmask => '+retour)                
            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    route_netmask=property(__get_route_netmask,__set_route_netmask)    
    
    def __set_route_prefix(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_route_prefix -> route_prefix read only property')            
            
            exception={
                'property':'route_prefix',
                'error':'read only property',
                'message':'route_prefix is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetIPv4@'+ self._id + ' ::__set_route_prefix -> route_prefix read only property')
                            
            raise NetExceptionIPv4(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)
    def __get_route_prefix(self,*param_no_named,**param_named):
        try:
            retour='N/A'
            if self.__interface is not None:
                retour=str(self.__interface.network.network_address)+'/'+str(self.__interface.network.prefixlen)

            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_route_prefix -> '+'route_prefix => '+retour)             
            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    route_prefix=property(__get_route_prefix,__set_route_prefix)    
    
    def __set_acl_wildcard(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__set_acl_wildcard -> acl_wildcard read only property')            
            
            exception={
                'property':'acl_wildcard',
                'error':'read only property',
                'message':'acl_wildcard is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetIPv4@'+ self._id + ' ::__set_acl_wildcard -> acl_wildcard read only property')
                            
            raise NetExceptionIPv4(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception)    
    def __get_acl_wildcard(self,*param_no_named,**param_named):
        try:
            retour='N/A'
            if self.__interface is not None:
                retour=str(self.__interface.network.network_address)+' '+str(self.__interface.hostmask)

            if self._logger != None:
                self._logger.debug('NetIPv4@'+ self._id + ' ::__get_acl_wildcard -> '+'acl_wildcard => '+retour)               
            
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionIPv4(self._logger,exception) 
    acl_wildcard=property(__get_acl_wildcard,__set_acl_wildcard)    