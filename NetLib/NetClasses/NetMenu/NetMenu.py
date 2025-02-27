# pylint: disable=unused-variable

__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

import NetLib
from NetLib.NetClasses.NetClassParatemter.NetClassParameter import NetClassParameterUnique,NetClassParameterContains,NetClassParameterCombine
from NetLib.NetClasses.NetException.NetException import NetException
from NetLib.NetClasses.NetConfig.NetConfigFile.NetConfigFile import NetTypeConfigFile,NetTypeExcpetionConfigFile,NetExceptionConfigFile,NetConfigFile

import re
import sys
import os

if sys.platform[:3] == 'win':
    import msvcrt
elif sys.platform[:3] == 'lin':
    import termios
class NetTypeMenu(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeMenu,self).__new__(self,*param_no_named,**param_named)

class NetTypeExcpetionMenu(NetTypeExcpetionConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeExcpetionMenu,self).__new__(self,*param_no_named,**param_named)

class NetExceptionMenu(NetExceptionConfigFile,metaclass=NetTypeExcpetionMenu):
    __metaclass__=NetTypeExcpetionMenu
    
    def __init__(self,*param_no_named,**param_named):            
        super(NetExceptionMenu,self).__init__(*param_no_named,**param_named)
        self._config['exception']['content']['class_name']='NetMenu'
            
    def __str__(self):
        return super(NetExceptionMenu,self).__str__()


class NetMenu(NetConfigFile,metaclass=NetTypeMenu):
    __metaclass__=NetTypeMenu

    __DEFAULT_CONFIG={
        'header': 'Default Menu\n------------',
        'menu': {
            'a)':'value a',
            'b)':'value b',
            'c)':'value C'
            },
        'separator':' - '        
    }

    __DEFAULT_TYPE={
        'header': '',
        'menu': {},
        'separator':''        
    }

    __DEFAULT_REGEX={
    }

    def generate_default_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetLog@'+ self._id +' ::generate_default_config -> '+'default_config => '+str(NetMenu.__DEFAULT_CONFIG))   

            self.config=NetMenu.__DEFAULT_CONFIG

            return
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception)            

    @NetClassParameterUnique(load=dict)     
    def _dict_load(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            super(NetMenu,self)._dict_load(*list_param_no_named,**dict_param_named)
            
            load=dict_param_named['load']
            
            attributes=[
                'arrow'
            ]
            
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id +' ::_dict_load -> '+'attributes => '+str(attributes))                
            
            for attribut in attributes:
                if attribut not in dict_param_named.keys():
                    exception={
                        'keys':'['+attribut+']',
                        'error':'missing key',
                        'message':'['+attribut+']'+' not in '+str(list(dict_param_named.keys()))
                        }
                
                    if self._logger != None:
                        self._logger.error('NetMenu@'+ self._id +' ::_dict_load -> '+'exception => '+str(exception))                    
                        
                    raise NetExceptionMenu(self._logger,**exception)
            
            self.__arrow=load['arrow']

            return
                        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception)  
    def _dict_save(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            retour=super(NetMenu,self)._dict_save(*list_param_no_named,**dict_param_named)
            
            retour['arrow']=self.__arrow

            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id +' ::__dict_save -> '+'atributes => '+str(retour.keys()))
                
            return retour
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception)  

    def __init__(self,*param_no_named,**param_named):
        try: 
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            self.__arrow=0
            super(NetMenu,self).__init__(*list_param_no_named,**dict_param_named)

            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::__init__ -> Creating object')

            self.config_type=NetMenu.__DEFAULT_TYPE
            self.config_regex=NetMenu.__DEFAULT_REGEX     

            if 'generate_default_config' in dict_param_named.keys() and type(dict_param_named['generate_default_config']) is bool and dict_param_named['generate_default_config'] is True:
                self.generate_default_config(*param_no_named,**param_named)                         

            header='N/A'
            if 'header' in dict_param_named.keys() and type(dict_param_named['header']) is str:
                header=dict_param_named['header']
                self.header=dict_param_named['header']
                
            menu='N/A'
            if 'menu' in dict_param_named.keys() and type(dict_param_named['menu']) is dict:
                menu=str(dict_param_named['menu'])
                self.menu=dict_param_named['menu']

            separator='N/A'
            if 'separator' in dict_param_named.keys() and type(dict_param_named['separator']) is str:
                separator=dict_param_named['separator']
                self.separator=dict_param_named['separator']
            
            if self._logger != None:
                self._logger.info('NetMenu@'+ self._id +' :: '+'object created -> '+'id => ' + self._id +' || '+'header => '+header+' || '+'menu => '+ menu +' || '+'separator => '+ separator)
            
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception)             
    def __str__(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::__str__ -> Getting str')              
            
            return "header -> "+self._config['header']+" :: "+"menu -> "+str(self._config['menu'])
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception)

    @NetClassParameterUnique(str)
    def __set_header(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            header=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::__set_header -> header => '+ header)
                            
            self._config['header']=header

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception) 
    def __get_header(self,*param_no_named,**param_named):
        try:
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::__get_header -> header => '+self._config['header'])
                            
            return self._config['header']
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception) 
    header=property(__get_header,__set_header)

    @NetClassParameterUnique(str)
    def __set__separator(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            separator=list_param_no_named[i]            
            
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::__set__separator -> separator => '+ separator)            
            
            self._config['separator']=separator

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception)   
    def __get_separator(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::__get_separator -> separator => '+ self._config['separator'])               
            
            return self._config['separator']
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception)
    separator=property(__get_separator,__set__separator)  

    @NetClassParameterUnique(dict)
    def __set_menu(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            menu=list_param_no_named[i]                 
               
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::__set_menu -> menu => '+str(menu))                    
               
            self._config['menu']=menu

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception) 
    def __get_menu(self):
        try:
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::__get_menu -> menu => '+str(self._config['menu']))                    
            
            return self._config['menu'].copy()
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception) 
    menu=property(__get_menu,__set_menu) 

    def display_menu(self,*param_no_named,**param_named):
        try: 
            self.__arrow=0
            keyboard='a'
            keyboard_previous=None
            
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::display_menu -> Display Menu')                
            
            
            line=None
            while (str(keyboard) != '\\r' and sys.platform[:3] == 'win') or (keyboard != '\n' and str(keyboard) != '\\n'  and sys.platform[:3] == 'lin'):
                self.__clear_display(*param_no_named,**param_named)
                keyboard_previous=keyboard
                print(self._config['header'])
                
                
                list_key=list(self._config['menu'].keys())
                list_key.sort()
                for index,line in enumerate(list_key):
                    if index==self.__arrow:
                        print(' => '+str(line)+self._config['separator']+self._config['menu'][line])
                    else:
                        print('    '+str(line)+self._config['separator']+self._config['menu'][line])

                keyboard=self.__get__char(*param_no_named,**param_named)
                keyboard=re.sub("b'(?P<Save>[^']+)'",'\\g<Save>',str(keyboard))
                                        
                if sys.platform[:3] == 'lin' and str(keyboard_previous) == '[' and str(keyboard) == 'B':
                    self.__arrow_down(*param_no_named,**param_named)
                    
                if sys.platform[:3] == 'lin' and str(keyboard_previous) == '[' and str(keyboard) == 'A':
                    self.__arrow_up(*param_no_named,**param_named)
                
                if sys.platform[:3] == 'win' and str(keyboard_previous) == '\\xe0' and str(keyboard) == 'P':
                    self.__arrow_down(*param_no_named,**param_named)
                    
                if sys.platform[:3] == 'win' and str(keyboard_previous) == '\\xe0' and str(keyboard) == 'H':
                    self.__arrow_up(*param_no_named,**param_named)
            
            if self._logger != None:
                self._logger.info('NetMenu@'+ self._id + ' ::display_menu -> return '+str(list_key[self.__arrow])) 
                            
            return list_key[self.__arrow]
      
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception) 
                 
    def __arrow_down(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::__arrow_down -> arrow down')              
            
            if self.__arrow < len(self._config['menu'].keys())-1:
                self.__arrow=self.__arrow+1
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception) 
    def __arrow_up(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::__arrow_up -> arrow up')              
            
            if self.__arrow > 0:
                self.__arrow=self.__arrow-1
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception)  
    def __get__char(self,*param_no_named,**param_named):
        try:
            char=''
        
            if sys.platform[:3] == 'win':
                char=msvcrt.getch()
            elif sys.platform[:3] == 'lin':
                TERMIOS = termios
                fd = sys.stdin.fileno()
                old = termios.tcgetattr(fd)
                new = termios.tcgetattr(fd)
                new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
                new[6][TERMIOS.VMIN] = 1
                new[6][TERMIOS.VTIME] = 0
                termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
                char = None
                try:
                    char = os.read(fd, 1)
                finally:
                    termios.tcsetattr(fd, TERMIOS.TCSADRAIN, old)
                    
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::__get__char -> '+str(char)) 
                    
            return char
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception) 
    def  __clear_display(self,*param_no_named,**param_named): 
        try:
            
            if self._logger != None:
                self._logger.debug('NetMenu@'+ self._id + ' ::__clear_display -> Clear screen') 
                            
            if sys.platform[:3] == 'win':
                _=os.system('cls')
            elif sys.platform[:3] == 'lin':
                _=os.system('clear')
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionMenu(self._logger,exception) 
    
    
    
    