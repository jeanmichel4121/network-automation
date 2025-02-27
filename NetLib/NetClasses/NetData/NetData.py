# pylint: disable=unused-variable
__author__ = 'Jean-Michel Cuvelier'

import sys
sys.path.insert(0,'./')

import NetLib
from NetLib.NetClasses.NetClassParatemter.NetClassParameter import NetClassParameterUnique,NetClassParameterContains,NetClassParameterCombine
from NetLib.NetClasses.NetException.NetException import NetException
from NetLib.NetClasses.NetConfig.NetConfigFile.NetConfigFile import NetTypeConfigFile,NetTypeExcpetionConfigFile,NetExceptionConfigFile,NetConfigFile
from lxml import etree
import xmltodict
import json
import yaml
import re
import os
import sys
from io import StringIO, BytesIO


class NetTypeDataElement(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeDataElement,self).__new__(self,*param_no_named,**param_named)
class NetTypeDataXMLtoDict(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeDataXMLtoDict,self).__new__(self,*param_no_named,**param_named)
class NetTypeDataXMLtoList(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeDataXMLtoList,self).__new__(self,*param_no_named,**param_named)
class NetTypeDataYAMLtoDict(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeDataYAMLtoDict,self).__new__(self,*param_no_named,**param_named)
class NetTypeDataYAMLtoList(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeDataYAMLtoList,self).__new__(self,*param_no_named,**param_named)
class NetTypeDataJSONtoDict(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeDataJSONtoDict,self).__new__(self,*param_no_named,**param_named)
class NetTypeDataJSONtoList(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeDataJSONtoList,self).__new__(self,*param_no_named,**param_named)
class NetTypeDataDictJSON(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeDataDictJSON,self).__new__(self,*param_no_named,**param_named)
class NetTypeDataDictYAML(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeDataDictYAML,self).__new__(self,*param_no_named,**param_named)        
class NetTypeData(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeData,self).__new__(self,*param_no_named,**param_named)
class NetTypeExcpetionData(NetTypeExcpetionConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeExcpetionData,self).__new__(self,*param_no_named,**param_named)
class NetExceptionData(NetExceptionConfigFile,metaclass=NetTypeExcpetionData):
    __metaclass__=NetTypeExcpetionData
    
    def __init__(self,*param_no_named,**param_named):
        try:        
            super(NetExceptionData,self).__init__(*param_no_named,**param_named)
            self._config['exception']['content']['class_name']='NetData'

        except Exception as ex:
            raise ex
          
    def __str__(self):
        return super(NetExceptionData,self).__str__()    
class NetData(NetConfigFile,metaclass=NetTypeData):
    __metaclass__=NetTypeData
    
    __DEFAULT_CONFIG={
        'default':{
            'encoding': 'utf-8',
            'mode': 'xml',
            'root_tag': 'root',
            'tostring':'xml'
        },
        'html':{
            'parser':{
                'parser':{
                    'encoding': 'utf-8',
                    'remove_blank_text': True
                },
                'base_url':''
            },
            'tostring':{
                'encoding': 'utf-8',
                'with_tail': True,
                'pretty_print': True,
                'xml_declaration': False,
                'method': 'html'                
            }       
        },
        'json':{
            'mode':'xml',
            'tostring':{
                'indent': 3,
                'sort_keys': False                
            }
        },
        'xml':{
            'indent':{
                'space': ' ',
                'level': 0                
            },
            'parser':{
                'parser':{
                    'encoding': 'utf-8',
                    'ns_clean': True,
                    'remove_blank_text': True  
                },
                'base_url':''
            },
            'tostring':{
                'encoding': 'utf-8',
                'with_tail': True,
                'xml_declaration': True,
                'pretty_print': True,
                'method': 'xml'                
            }
        },
        'xmltodict':{
            'mode':'xml',
            'parser':{
                'attr_prefix': '@',
                'cdata_key': 'text()',
                'process_namespaces': True,
                'encoding': 'utf-8'
            },
            'tostring':{
                'indent': 3,
                'sort_keys': False                
            }
        },
        'yaml':{
            'mode':'xmltodict',
            'tostring':{
                'indent': 3,
                'sort_keys': False                
            }
        }
    }
    
    __DEFAULT_TYPE={
        'default': {
            'encoding': '',
            'mode': '',
            'root_tag': '',
            'tostring': ''
        },
        'html': {
            'parser': {
                'base_url': '',
                'parser': {
                    'encoding': '',
                    'remove_blank_text': True
                }
            },
            'tostring': {
                'encoding': '',
                'with_tail': True,
                'pretty_print': True,
                'xml_declaration': False,
                'method': ''
            }
        },
        'json': {
            'mode': '',
            'tostring': {
                'indent': 3,
                'sort_keys': False
            }
        },
        'xml': {
            'indent': {
                'space': '',
                'level': 0
            },
            'parser': {
                'base_url': '',
                'parser': {
                    'encoding': '',
                    'ns_clean': True,
                    'remove_blank_text': True
                }
            },
            'tostring': {
                'encoding': '',
                'with_tail': True,
                'xml_declaration': True,
                'pretty_print': True,
                'method': ''
            }
        },
        'xmltodict': {
            'mode': '',
            'parser': {
                'attr_prefix': '',
                'cdata_key': '',
                'process_namespaces': True,
                'encoding': ''
            },
            'tostring': {
                'indent': 3,
                'sort_keys': False
            }
        },
        'yaml': {
            'mode': '',
            'tostring': {
                'indent': 3,
                'sort_keys': False
            }
        }
    }

    __DEFAULT_REGEX={
        'default': {
            'encoding': 'utf-8|ascii',
            'mode': 'html|xml',
            'root_tag': '\w',
            'tostring': 'html|xml'
        },
        'html': {
            'parser': {
                'base_url': '',
                'parser': {
                    'encoding': 'utf-8|ascii',
                    'remove_blank_text': 'True|False'
                }
            },
            'tostring': {
                'encoding': 'utf-8|ascii',
                'with_tail': 'True|False',
                'pretty_print': 'True|False',
                'xml_declaration': 'True|False',
                'method': 'html'
            }
        },
        'json': {
            'mode': 'html|xml',
            'tostring': {
                'indent': '^[0-9][0-9]*$',
                'sort_keys': 'True|False'
            }
        },
        'xml': {
            'indent': {
                'space': '^  *$',
                'level': '^[0-9][0-9]*$'
            },
            'parser': {
                'parser': {
                    'encoding': 'utf-8|ascii',
                    'ns_clean': 'True|False',
                    'remove_blank_text': 'True|False'
                }
            },
            'tostring': {
                'encoding': 'utf-8|ascii',
                'with_tail': 'True|False',
                'xml_declaration': 'True|False',
                'pretty_print': 'True|False',
                'method': 'xml'
            }
        },
        'xmltodict': {
            'mode': 'html|xml',
            'parser': {
                'attr_prefix': '@',
                'cdata_key': 'text()',
                'process_namespaces': 'True|False',
                'encoding': 'utf-8|ascii'
            },
            'tostring': {
                'indent': '^[0-9][0-9]*$',
                'sort_keys': 'True|False'
            }
        },
        'yaml': {
            'mode': 'json|xmltodict',
            'tostring': {
                'indent': '^[0-9][0-9]*$',
                'sort_keys': 'True|False'
            }
        }
    }

    class DataElement(etree.ElementBase,metaclass=NetTypeDataElement):
        __metaclass__=NetTypeDataElement
        def __str__(self):
            tree=''
            if self.root._mode_print != self.root._config['default']['mode']:
                if self.root._config['default']['mode'] == 'xml':
                
                    parser_tostring=self.root._config['html']['tostring']
                    parser=self.root._parse_original(source=self.root._config['html']['parser'])
                    parser['parser']=etree.HTMLParser(**self.root._config['html']['parser']['parser'])
                    tree=etree.HTML(etree.tostring(self,**parser_tostring),**parser)
                          
                elif self.root._config['default']['mode'] == 'html':

                    parser_tostring=self.root._config['xml']['tostring']
                    parser=self.root._parse_original(source=self.root._config['xml']['parser'])
                    parser['parser']=etree.XMLParser(**self.root._config['xml']['parser']['parser'])
                    tree=etree.XML(etree.tostring(self,**parser_tostring),**parser)   

            else:
                tree=self

            type_parser_tostring=''
            if self.root._mode_print == 'xml':
                type_parser_tostring='xml'
            elif self.root._mode_print == 'html':
                type_parser_tostring='html'

            parser_tostring=self.root._config[type_parser_tostring]['tostring']
            return etree.tostring(tree,**parser_tostring).decode(self.root._config[type_parser_tostring]['tostring']['encoding'])


        def init(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                setattr(self,'root','')
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionData(self._logger,exception) 
    class DataYAMLtoList(list,metaclass=NetTypeDataYAMLtoList):
        __metaclass__=NetTypeDataYAMLtoList
        @NetClassParameterUnique(root=object,mylist=list,parent=object)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            self.parent=None

            self.__root=dict_param_named['root']
            list.__init__(self,dict_param_named['mylist'])
            self.parent=dict_param_named['parent']

        def __setitem__(self, item, value):
            old_data_yaml=None
            if self.__root._config['yaml']['mode'] == 'xmltodict':
                old_data_yaml=self.__root._parse_original(source=self.__root._generate_xmltodict())
            elif self._root._config['yaml']['mode'] == 'json':           
                old_data_yaml=self.__root._parse_original(source=self.__root._generate_json())

            add=None
            if type(value) is dict or type(value) is list:
                add=self.__root._parse_data_yaml(source=value)
            else:
                add=value

            if type(item) is int and item < len(self):
                list.__setitem__(self,item, add)
            else:
                if issubclass(type(add),list):
                    list.extend(self,add)
                else:
                    list.append(self,add)

            cursor=self.parent
            data_yaml=cursor
            while cursor is not None:
                data_yaml=cursor
                cursor=cursor.parent
            
            if data_yaml is not None:
                data_yaml=self.__root._parse_original(source=data_yaml)
            else:
                data_yaml=self.__root._parse_original(source=self)

            if self.__root._check_same_object(source1=old_data_yaml,source2=data_yaml) is False:
                self.__root._update_data_yaml(old_data_yaml=old_data_yaml,new_data_yaml=data_yaml)
    class DataYAMLtoDict(dict,metaclass=NetTypeDataYAMLtoDict):
        __metaclass__=NetTypeDataYAMLtoDict
        @NetClassParameterUnique(root=object,dictionary=dict,parent=object)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            self.parent=None

            self.__root=dict_param_named['root']
            dict.__init__(self,dict_param_named['dictionary'])

            self.parent=dict_param_named['parent']

        def __str__(self):
            data=None
            if self.__root._config['yaml']['mode'] == 'xmltodict':
                data=self.__root._parse_original(source=self.__root._generate_xmltodict())
            elif self.__root._config['yaml']['mode'] == 'json':
                data=self.__root._parse_original(source=self.__root._generate_json())
                
            return yaml.dump(data,**self.__root._config['yaml']['tostring'])

        def __getitem__(self, item):
            index=str(item)
            if index not in self.keys():
                add=NetData.DataYAMLtoDict(root=self.__root,dictionary=dict(),parent=self)
                dict.__setitem__(self,index, add)

                sort=dict()
                for key in self.keys():
                    sort[key]=dict.__getitem__(self,key)
                for key in sort.keys():
                    dict.__delitem__(self,key)
                for key in sorted(sort.keys(),key=str.lower):
                    dict.__setitem__(self,key, sort[key])

            return dict.__getitem__(self,index)

        def __setitem__(self, item, value):
            old_data_yaml=None
            if self.__root._config['yaml']['mode'] == 'xmltodict':
                old_data_yaml=self.__root._parse_original(source=self.__root._generate_xmltodict())
            elif self.__root._config['yaml']['mode'] == 'json':
                old_data_yaml=self.__root._parse_original(source=self.__root._generate_json())


            if item in self.keys():
                dict.__delitem__(self,item)

            add=None
            if type(value) is dict or type(value) is list:
                add=self.__root._parse_data_yaml(source=value)
            else:
                add=value

            dict.__setitem__(self,item, add)
            sort=dict()
            for key in self.keys():
                sort[key]=dict.__getitem__(self,key)
            for key in sort.keys():
                dict.__delitem__(self,key)
            for key in sorted(sort.keys(),key=str.lower):
                dict.__setitem__(self,key, sort[key])
          
            cursor=self.parent
            data_yaml=cursor
            while cursor is not None:
                data_yaml=cursor
                cursor=cursor.parent
            
            if data_yaml is not None:
                data_yaml=self.__root._parse_original(source=data_yaml)
            else:
                data_yaml=self.__root._parse_original(source=self)

            if self.__root._check_same_object(source1=old_data_yaml,source2=data_yaml) is False:
                self.__root._update_data_yaml(old_data_yaml=old_data_yaml,new_data_yaml=data_yaml)
    class DataJSONtoList(list,metaclass=NetTypeDataJSONtoList):
        __metaclass__=NetTypeDataJSONtoList
        @NetClassParameterUnique(root=object,mylist=list,parent=object)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            self.parent=None

            self.__root=dict_param_named['root']
            list.__init__(self,dict_param_named['mylist'])
            self.parent=dict_param_named['parent']


        def __setitem__(self, item, value):
            old_data_json=self.__root._parse_original(source=self.__root._generate_json())

            add=None
            if type(value) is dict or type(value) is list:
                add=self.__root._parse_data_json(source=value)
            else:
                add=value

            if type(item) is int and item < len(self):
                list.__setitem__(self,item, add)
            else:
                if issubclass(type(add),list):
                    list.extend(self,add)
                else:
                    list.append(self,add)

            cursor=self.parent
            data_json=cursor
            while cursor is not None:
                data_json=cursor
                cursor=cursor.parent
            
            if data_json is not None:
                data_json=self.__root._parse_original(source=data_json)
            else:
                data_json=self.__root._parse_original(source=self)

            if self.__root._check_same_object(source1=old_data_json,source2=data_json) is False:
                self.__root._update_data_json(old_data_json=old_data_json,new_data_json=data_json)
    class DataJSONtoDict(dict,metaclass=NetTypeDataJSONtoDict):
        __metaclass__=NetTypeDataJSONtoDict
        @NetClassParameterUnique(root=object,dictionary=dict,parent=object)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            self.parent=None

            self.__root=dict_param_named['root']
            dict.__init__(self,dict_param_named['dictionary'])

            self.parent=dict_param_named['parent']

        def __str__(self):
            return json.dumps(self,**self.__root._config['json']['tostring'])

        def __getitem__(self, item):
            index=str(item)
            if index not in self.keys():
                add=NetData.DataJSONtoDict(root=self.__root,dictionary=dict(),parent=self)
                dict.__setitem__(self,index, add)

                sort=dict()
                for key in self.keys():
                    sort[key]=dict.__getitem__(self,key)
                for key in sort.keys():
                    dict.__delitem__(self,key)
                for key in sorted(sort.keys(),key=str.lower):
                    dict.__setitem__(self,key, sort[key])

            return dict.__getitem__(self,index)

        def __setitem__(self, item, value):
            old_data_json=self.__root._parse_original(source=self.__root._generate_json())

            if item in self.keys():
                dict.__delitem__(self,item)

            add=None
            if type(value) is dict or type(value) is list:
                add=self.__root._parse_data_json(source=value)
            else:
                add=value

            dict.__setitem__(self,item, add)
            sort=dict()
            for key in self.keys():
                sort[key]=dict.__getitem__(self,key)
            for key in sort.keys():
                dict.__delitem__(self,key)
            for key in sorted(sort.keys(),key=str.lower):
                dict.__setitem__(self,key, sort[key])
          
            cursor=self.parent
            data_json=cursor
            while cursor is not None:
                data_json=cursor
                cursor=cursor.parent
            
            if data_json is not None:
                data_json=self.__root._parse_original(source=data_json)
            else:
                data_json=self.__root._parse_original(source=self)

            if self.__root._check_same_object(source1=old_data_json,source2=data_json) is False:
                self.__root._update_data_json(old_data_json=old_data_json,new_data_json=data_json)
    class DataXMLtoList(list,metaclass=NetTypeDataXMLtoList):
        __metaclass__=NetTypeDataXMLtoList
        @NetClassParameterUnique(root=object,mylist=list,parent=object)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            self.parent=None

            self.__root=dict_param_named['root']
            list.__init__(self,dict_param_named['mylist'])
            self.parent=dict_param_named['parent']


        def __setitem__(self, item, value):
            old_data_xmltodict=self.__root._parse_original(source=self.__root._generate_xmltodict())

            add=None
            if type(value) is dict or type(value) is list:
                add=self.__root._parse_data_xmltodict(source=value)
            else:
                add=value

            if type(item) is int and item < len(self):
                list.__setitem__(self,item, add)
            else:
                if issubclass(type(add),list):
                    list.extend(self,add)
                else:
                    list.append(self,add)

            cursor=self.parent
            data_xmltodict=cursor
            while cursor is not None:
                data_xmltodict=cursor
                cursor=cursor.parent
            
            if data_xmltodict is not None:
                data_xmltodict=self.__root._parse_original(source=data_xmltodict)
            else:
                data_xmltodict=self.__root._parse_original(source=self)

            if self.__root._check_same_object(source1=old_data_xmltodict,source2=data_xmltodict) is False:
                self.__root._update_data_xmltodict(old_data_xmltodict=old_data_xmltodict,new_data_xmltodict=data_xmltodict)
    class DataXMLtoDict(dict,metaclass=NetTypeDataXMLtoDict):
        __metaclass__=NetTypeDataXMLtoDict
        @NetClassParameterUnique(root=object,dictionary=dict,parent=object)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            self.parent=None

            self.__root=dict_param_named['root']
            dict.__init__(self,dict_param_named['dictionary'])

            self.parent=dict_param_named['parent']

        def __str__(self):
            return json.dumps(self,**self.__root._config['xmltodict']['tostring'])

        def __getitem__(self, item):
            index=str(item)
            if index not in self.keys():
                add=NetData.DataXMLtoDict(root=self.__root,dictionary=dict(),parent=self)
                dict.__setitem__(self,index, add)

                sort=dict()
                for key in self.keys():
                    sort[key]=dict.__getitem__(self,key)
                for key in sort.keys():
                    dict.__delitem__(self,key)
                for key in sorted(sort.keys(),key=str.lower):
                    dict.__setitem__(self,key, sort[key])

            return dict.__getitem__(self,index)

        def __setitem__(self, item, value):
            old_data_xmltodict=self.__root._parse_original(source=self.__root._generate_xmltodict())

            if item in self.keys():
                dict.__delitem__(self,item)

            add=None
            if type(value) is dict or type(value) is list:
                add=self.__root._parse_data_xmltodict(source=value)
            else:
                add=value

            dict.__setitem__(self,item, add)
            sort=dict()
            for key in self.keys():
                sort[key]=dict.__getitem__(self,key)
            for key in sort.keys():
                dict.__delitem__(self,key)
            for key in sorted(sort.keys(),key=str.lower):
                dict.__setitem__(self,key, sort[key])
          
            cursor=self.parent
            data_xmltodict=cursor
            while cursor is not None:
                data_xmltodict=cursor
                cursor=cursor.parent
            
            if data_xmltodict is not None:
                data_xmltodict=self.__root._parse_original(source=data_xmltodict)
            else:
                data_xmltodict=self.__root._parse_original(source=self)

            if self.__root._check_same_object(source1=old_data_xmltodict,source2=data_xmltodict) is False:
                self.__root._update_data_xmltodict(old_data_xmltodict=old_data_xmltodict,new_data_xmltodict=data_xmltodict)
    class DataDictJSON(dict,metaclass=NetTypeDataDictJSON):
        __metaclass__=NetTypeDataDictJSON
        def __str__(self):
            return json.dumps(self,indent=2)
    class DataDictYAML(dict,metaclass=NetTypeDataDictYAML):
        __metaclass__=NetTypeDataDictYAML
        @NetClassParameterUnique(root=object,dictionary=dict)
        def __init__(self,*param_no_named,**param_named):
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            self.__root=dict_param_named['root']
            dict.__init__(self,dict_param_named['dictionary'])        
        
        def __str__(self):
            retour=self.__root._parse_original(source=dict(self))
            retour=yaml.dump(retour,indent=2)
            retour=re.sub(" *: *'* *",': ',retour)
            return retour         
      
    @NetClassParameterCombine([NetClassParameterUnique(source=dict),NetClassParameterUnique(source=list)])
    def _parse_data_yaml(self,*param_no_named,**param_named):
        
        @NetClassParameterUnique(source=object)
        def parse_data_yaml_dict(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']
                keys=list(source.keys())             
                for key in keys:
                    if type(source[key]) is list:              
                        source[key]=NetData.DataYAMLtoList(root=self,mylist=source[key],parent=source)
                        parse_data_yaml_list(self,source=source[key])
                    
                    if type(source[key]) is dict:
                        source[key]=NetData.DataYAMLtoDict(root=self,dictionary=source[key],parent=source)
                        parse_data_yaml_dict(self,source=source[key]) 
                  
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionData(self._logger,exception)  

        @NetClassParameterUnique(source=object)
        def parse_data_yaml_list(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']                           

                for index,elem in enumerate(source):
                    if type(elem) is list:
                        
                        source[index]=NetData.DataYAMLtoList(root=self,mylist=elem,parent=source)
                        parse_data_yaml_list(self,source=source[index])
                    
                    if type(elem) is dict:
                        source[index]=NetData.DataYAMLtoDict(root=self,dictionary=elem,parent=source)
                        parse_data_yaml_dict(self,source=source[index])                    
                                   
                            
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionData(self._logger,exception)  
                
        try:                      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                
            source=dict_param_named['source']            
            retour=source
            if ( type(source) is dict and len(source.keys()) > 0 ) or ( type(source) is list and len(source) > 0 ):

                if self._logger is not None:
                    self._logger.debug('NetData@'+ self._id +' ::_parse_data_yaml -> '+'source => '+str(source))      

                retour=source.copy()
                
                if type(source) is list:
                    retour=NetData.DataYAMLtoList(root=self,mylist=retour,parent=None)
                    parse_data_yaml_list(self,source=retour)
                
                if type(source) is dict:
                    retour=NetData.DataYAMLtoDict(root=self,dictionary=retour,parent=None)
                    parse_data_yaml_dict(self,source=retour)
            
            return retour                
                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    @NetClassParameterCombine([NetClassParameterUnique(source=dict),NetClassParameterUnique(source=list)])
    def _parse_data_json(self,*param_no_named,**param_named):
        
        @NetClassParameterUnique(source=object)
        def parse_data_json_dict(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']
                keys=list(source.keys())             
                for key in keys:
                    if type(source[key]) is list:              
                        source[key]=NetData.DataJSONtoList(root=self,mylist=source[key],parent=source)
                        parse_data_json_list(self,source=source[key])
                    
                    if type(source[key]) is dict:
                        source[key]=NetData.DataJSONtoDict(root=self,dictionary=source[key],parent=source)
                        parse_data_json_dict(self,source=source[key]) 
                  
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionData(self._logger,exception)  

        @NetClassParameterUnique(source=object)
        def parse_data_json_list(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']                           

                for index,elem in enumerate(source):
                    if type(elem) is list:
                        
                        source[index]=NetData.DataJSONtoList(root=self,mylist=elem,parent=source)
                        parse_data_json_list(self,source=source[index])
                    
                    if type(elem) is dict:
                        source[index]=NetData.DataJSONtoDict(root=self,dictionary=elem,parent=source)
                        parse_data_json_dict(self,source=source[index])                    
                                   
                            
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionData(self._logger,exception)  
                
        try:                      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                
            source=dict_param_named['source']            
            retour=source
            if ( type(source) is dict and len(source.keys()) > 0 ) or ( type(source) is list and len(source) > 0 ):

                if self._logger is not None:
                    self._logger.debug('NetData@'+ self._id +' ::_parse_data_json -> '+'source => '+str(source))      

                retour=source.copy()
                
                if type(source) is list:
                    retour=NetData.DataJSONtoList(root=self,mylist=retour,parent=None)
                    parse_data_json_list(self,source=retour)
                
                if type(source) is dict:
                    retour=NetData.DataJSONtoDict(root=self,dictionary=retour,parent=None)
                    parse_data_json_dict(self,source=retour)
            
            return retour                
                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    @NetClassParameterCombine([NetClassParameterUnique(source=dict),NetClassParameterUnique(source=list)])
    def _parse_data_xmltodict(self,*param_no_named,**param_named):
        
        @NetClassParameterUnique(source=object)
        def parse_data_xmltodict_dict(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']
                keys=list(source.keys())             
                for key in keys:
                    if type(source[key]) is list:              
                        source[key]=NetData.DataXMLtoList(root=self,mylist=source[key],parent=source)
                        parse_data_xmltodict_list(self,source=source[key])
                    
                    if type(source[key]) is dict:
                        source[key]=NetData.DataXMLtoDict(root=self,dictionary=source[key],parent=source)
                        parse_data_xmltodict_dict(self,source=source[key]) 
                  
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionData(self._logger,exception)  

        @NetClassParameterUnique(source=object)
        def parse_data_xmltodict_list(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source=dict_param_named['source']                           

                for index,elem in enumerate(source):
                    if type(elem) is list:
                        
                        source[index]=NetData.DataXMLtoList(root=self,mylist=elem,parent=source)
                        parse_data_xmltodict_list(self,source=source[index])
                    
                    if type(elem) is dict:
                        source[index]=NetData.DataXMLtoDict(root=self,dictionary=elem,parent=source)
                        parse_data_xmltodict_dict(self,source=source[index])                    
                                   
                            
            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionData(self._logger,exception)  
                
        try:                      
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
                
            source=dict_param_named['source']            
            retour=source
            if ( type(source) is dict and len(source.keys()) > 0 ) or ( type(source) is list and len(source) > 0 ):

                if self._logger is not None:
                    self._logger.debug('NetData@'+ self._id +' ::_parse_data_xmltodict -> '+'source => '+str(source))      

                retour=source.copy()
                
                if type(source) is list:
                    retour=NetData.DataXMLtoList(root=self,mylist=retour,parent=None)
                    parse_data_xmltodict_list(self,source=retour)
                
                if type(source) is dict:
                    retour=NetData.DataXMLtoDict(root=self,dictionary=retour,parent=None)
                    parse_data_xmltodict_dict(self,source=retour)
            
            return retour                
                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)

    @NetClassParameterUnique(old_data_yaml=dict,new_data_yaml=dict)
    def _update_data_yaml(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            old_data_yaml=dict_param_named['old_data_yaml']
            new_data_yaml=dict_param_named['new_data_yaml']

            if self._logger is not None:
                self._logger.debug('NetData@'+ self._id +' ::_update_data_yaml -> '+'old_data_yaml => '+str(old_data_yaml)+' || '+'new_data_yaml => '+str(new_data_yaml))     

            if self._config['yaml']['mode'] == 'xmltodict':
                self._update_data_xmltodict(old_data_xmltodict=old_data_yaml,new_data_xmltodict=new_data_yaml)
            elif self._config['yaml']['mode'] == 'json':
                self._update_data_json(old_data_json=old_data_yaml,new_data_json=new_data_yaml)
                                                           
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)                
    @NetClassParameterUnique(old_data_json=dict,new_data_json=dict)
    def _update_data_json(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            old_data_json=dict_param_named['old_data_json']
            new_data_json=dict_param_named['new_data_json']

            if self._logger is not None:
                self._logger.debug('NetData@'+ self._id +' ::_update_data_json -> '+'old_data_json => '+str(old_data_json)+' || '+'new_data_json => '+str(new_data_json))     


            parse_xmltodict=self._parse_original(source=self._config['xmltodict']['parser'])
            
            if 'process_namespaces' in parse_xmltodict.keys():
                del parse_xmltodict['process_namespaces']
            
            new_data_json=self._parse_json(data=new_data_json)

            if len(new_data_json.keys()) == 1:
                
                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                text_prefix=self._config['xmltodict']['parser']['cdata_key']
                root=list(new_data_json.keys())[0]

                text_prefix=self._str_specials_characters_as_str(chain=text_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^'+attribut_prefix,root) or re.search('^'+text_prefix+'$',root):
                    if self.__tree is not None:
                        new_data_json={
                            self.__tree.getroot().tag : new_data_json
                        }
                    else:
                        new_data_json={
                            self._config['default']['root_tag'] : new_data_json
                        }                    
            else:
                if self.__tree is not None:
                    new_data_json={
                        self.__tree.getroot().tag : new_data_json
                    }
                else:
                    new_data_json={
                        self._config['default']['root_tag'] : new_data_json
                    }

            if self._config['json']['mode'] == 'xml':
                self.xml=xmltodict.unparse(new_data_json,**parse_xmltodict)
            elif self._config['json']['mode'] == 'html':
                self.html=xmltodict.unparse(new_data_json,**parse_xmltodict)
                         
                                        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    @NetClassParameterUnique(old_data_xmltodict=dict,new_data_xmltodict=dict)
    def _update_data_xmltodict(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            old_data_xmltodict=dict_param_named['old_data_xmltodict']
            new_data_xmltodict=dict_param_named['new_data_xmltodict']

            if self._logger is not None:
                self._logger.debug('NetData@'+ self._id +' ::_update_data_xmltodict -> '+'old_data_xmltodict => '+str(old_data_xmltodict)+' || '+'new_data_xmltodict => '+str(new_data_xmltodict))     

            parse_xmltodict=self._parse_original(source=self._config['xmltodict']['parser'])
            if 'process_namespaces' in parse_xmltodict.keys():
                del parse_xmltodict['process_namespaces']
            
            if len(new_data_xmltodict.keys()) == 1:
                
                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                text_prefix=self._config['xmltodict']['parser']['cdata_key']
                root=list(new_data_xmltodict.keys())[0]
            
                text_prefix=self._str_specials_characters_as_str(chain=text_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^'+attribut_prefix,root) or re.search('^'+text_prefix+'$',root):
                    if self.__tree is not None:
                        new_data_xmltodict={
                            self.__tree.getroot().tag : new_data_xmltodict
                        }
                    else:
                        new_data_xmltodict={
                            self._config['default']['root_tag'] : new_data_xmltodict
                        }                    
            else:
                if self.__tree is not None:
                    new_data_xmltodict={
                        self.__tree.getroot().tag : new_data_xmltodict
                    }
                else:
                    new_data_xmltodict={
                        self._config['default']['root_tag'] : new_data_xmltodict
                    }

            if self._config['xmltodict']['mode'] == 'xml':
                self.xml=xmltodict.unparse(new_data_xmltodict,**parse_xmltodict)
            elif self._config['xmltodict']['mode'] == 'html':
                self.html=xmltodict.unparse(new_data_xmltodict,**parse_xmltodict)
                                                    
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
                
    def generate_default_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id +' ::generate_default_config -> '+'default_config => '+str(NetData.__DEFAULT_CONFIG))   

            self.config=NetData.__DEFAULT_CONFIG

            return
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 

    @NetClassParameterUnique(load=dict)
    def _dict_load(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            super(NetData,self)._dict_load(*list_param_no_named,**dict_param_named)
            
            load=dict_param_named['load']
            
            attributes=[
            ]
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::_dict_load -> '+str(attributes))                
            
            for attribut in attributes:
                if attribut not in dict_param_named.keys():
                    exception={
                        'keys':'['+attribut+']',
                        'error':'missing key',
                        'message':'['+attribut+']'+' not in '+str(list(dict_param_named.keys()))
                        }
                
                    if self._logger != None:
                        self._logger.error('NetData@'+ self._id + ' ::__dict_load -> '+str(exception))                    
                        
                    raise NetExceptionData(self._logger,**exception)            
            return
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)  
    def _dict_save(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            retour=super(NetData,self)._dict_save(*list_param_no_named,**dict_param_named)
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__dict_save -> '+str(retour.keys()))  
            
            return retour
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)  
          
    def __init__(self,*param_no_named,**param_named):
        try: 
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            self.__tree=None
            self._mode_print=''
            
            super(NetData,self).__init__(*list_param_no_named,**dict_param_named)  

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__init__ -> Creating object')    

            self.config_type=NetData.__DEFAULT_TYPE
            self.config_regex=NetData.__DEFAULT_REGEX                    

            if 'generate_default_config' in dict_param_named.keys() and type(dict_param_named['generate_default_config']) is bool and dict_param_named['generate_default_config'] is True:
                self.generate_default_config(*param_no_named,**param_named)                    

            if 'data' in dict_param_named.keys():
                self.data=dict_param_named['data']
            elif 'html' in dict_param_named.keys():
                self.html=dict_param_named['html']
            elif 'json' in dict_param_named.keys():
                self.json=dict_param_named['json']
            elif 'xml' in dict_param_named.keys():
                self.xml=dict_param_named['xml']
            elif 'xmltodict' in dict_param_named.keys():
                self.xmltodict=dict_param_named['xmltodict']
            elif 'yaml' in dict_param_named.keys():
                self.yaml=dict_param_named['yaml']                
            else:
                self.xmltodict={self._config['default']['root_tag']:{}}                                     

            root='n/'
            if self.__tree is not None:
                root=self.__tree.getroot().tag

            if self._logger != None:
                self._logger.info('NetData@'+ self._id +' || '+'object created -> '+'id => ' + self._id +' || '+'tag => '+str(root))  
                
        except Exception as ex:
                raise ex
    def __str__(self,*param_no_named,**param_named):
        try:
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__str__ -> Getting str')        
                
            if self.__tree is not None:
                if self._config['default']['tostring'] == 'html':
                    return str(self.html)
                elif self._config['default']['tostring'] == 'json':
                    return str(self.json)
                elif self._config['default']['tostring'] == 'xml':
                    return str(self.xml)                    
                elif self._config['default']['tostring'] == 'xmltodict':
                    return str(self.xmltodict)
                elif self._config['default']['tostring'] == 'yaml':
                    return str(self.yaml)                                                         

            else:
                return 'Data is not yet defined'
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 

    @NetClassParameterUnique(attributes=list,pattern=str)
    def __generate_xpath_multiples_attributes_insensitive(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            retour=[]

            pattern=dict_param_named['pattern']
            attributes=dict_param_named['attributes']

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__generate_xpath_multiples_attributes_insensitive -> pattern => '+pattern+' || '+'attributes => '+str(attributes))      

            parse=re.sub("@(?P<FIELD>[^*,][^*,]*)",'@*[re:match(local-name(),"^\g<FIELD>$","i")]',pattern)
            if parse is not None:
                pattern=parse

            regex=self._str_specials_characters_as_str(chain='re:match(@*[re:match(local-name(),"')+'([^\\"][^\\"]*)'+self._str_specials_characters_as_str(chain='"')
            found=re.findall(regex,pattern)
            retour.append(pattern)

            for elem in found:
                new_retour=[]
                for attribute in attributes:
                    match=re.search(elem,attribute,re.IGNORECASE)
                    if match:
                        regex=self._str_specials_characters_as_str(chain='re:match(@*[re:match(local-name(),"')+self._str_specials_characters_as_str(chain=elem)+self._str_specials_characters_as_str(chain='"')
                        new_chain='re:match(@*[re:match(local-name(),"^'+attribute+'$"'
                        for chain in retour:
                            new_pattern=re.sub(regex,new_chain,chain,1)
                            new_retour.append(new_pattern)
                retour=new_retour
                
            return retour

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterUnique(attributes=list,pattern=str)
    def __generate_xpath_multiples_attributes(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            retour=[]

            pattern=dict_param_named['pattern']
            attributes=dict_param_named['attributes']

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__generate_xpath_multiples_attributes -> pattern => '+pattern+' || '+'attributes => '+str(attributes))      

            parse=re.sub("@(?P<FIELD>[^*,][^*,]*)",'@*[re:match(local-name(),"^\g<FIELD>$")]',pattern)
            if parse is not None:
                pattern=parse

            regex=self._str_specials_characters_as_str(chain='re:match(@*[re:match(local-name(),"')+'([^\\"][^\\"]*)'+self._str_specials_characters_as_str(chain='"')
            found=re.findall(regex,pattern)
            retour.append(pattern)

            for elem in found:
                new_retour=[]
                for attribute in attributes:
                    match=re.search(elem,attribute)
                    if match:
                        regex=self._str_specials_characters_as_str(chain='re:match(@*[re:match(local-name(),"')+self._str_specials_characters_as_str(chain=elem)+self._str_specials_characters_as_str(chain='"')
                        new_chain='re:match(@*[re:match(local-name(),"^'+attribute+'$"'
                        for chain in retour:
                            new_pattern=re.sub(regex,new_chain,chain,1)
                            new_retour.append(new_pattern)
                retour=new_retour
                
            return retour

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterUnique(pattern=str)
    def __generate_xpath(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            pattern=dict_param_named['pattern']            
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__generate_xpath -> pattern => '+pattern)        

            tags=[]
            attributes=[]

            for elem in self.__tree.iter():
                if str(elem.tag) not in tags:
                    tags.append(elem.tag)
                for key in elem.attrib.keys():
                    if key not in attributes:
                        attributes.append(key)
                        
            xpath='' 
               
            for elem in pattern.split('/'):
                xpath_value=''                
                xpath_value_filter=''
                xpath_value_filter_final=''
                match=re.search('^ *(?P<VALUE>[^\\[][^\\[]*)(?P<FILTER>.*) *',elem)
                if match:
        
                    sub_match=re.search('^\\[(?P<FILTER>..*)\\]$',match.group('FILTER'))

                    if sub_match:

                        xpath_value_filter=sub_match.group('FILTER')
                        xpath_value_filter=re.sub('^ *\\[','',xpath_value_filter)
                        xpath_value_filter=re.sub('\\] *$','',xpath_value_filter)
                        xpath_value_filter=re.sub(' *\\) *',')',xpath_value_filter)
                        xpath_value_filter=re.sub(' *\\( *','(',xpath_value_filter)
                        xpath_value_filter=re.sub('\\" *or *(?P<NEXT>[^ ])','" or \g<NEXT>',xpath_value_filter)
                        xpath_value_filter=re.sub('\\" *and *(?P<NEXT>[^ ])','" and \g<NEXT>',xpath_value_filter)
                        xpath_value_filter=re.sub('\\) *or *(?P<NEXT>[^ ])',') or \g<NEXT>',xpath_value_filter)
                        xpath_value_filter=re.sub('\\) *and *(?P<NEXT>[^ ])',') and \g<NEXT>',xpath_value_filter)                            
                        xpath_value_filter=re.sub('^ *','',xpath_value_filter)
                        xpath_value_filter=re.sub(' *$','',xpath_value_filter)
          
                        if re.search('^[0-9][0-9]*$',xpath_value_filter) is None:                                       
                            lines=[]

                            for sub_line_1 in xpath_value_filter.split('") and '):
                                for sub_line_2 in sub_line_1.split('") or '):
                                    for sub_line_3 in sub_line_2.split('" and '):
                                        for sub_line_4 in sub_line_3.split('" or '):
                                            add=re.sub('^(?P<NAME>[^=][^=]*)=.*','\g<NAME>',sub_line_4)
                                            lines.append(add)
                            
                            for sub_filter in lines:
                                is_found=False
                            
                                if re.search('^@|^\\(\\(*@',sub_filter):

                                    compare=attributes
                                    is_attribute=True
                                    attribute='@'

                                    i=0
                                    while sub_filter[i] == '(' and i < len(sub_filter):
                                        i=i+1
                                    value_filter=sub_filter[i+len(attribute):]

                                else:
                                    compare=tags
                                    value_filter=sub_filter

                                    is_attribute=False
                                    is_text=False                      
                                    attribute=''

                                if re.search('^ *text *\\( *\\) *$|^ *\\(\\(* *text *\\( *\\) *$',value_filter) == None:

                                    if is_found == False:
                                        for sub_elem in compare:
                                            if value_filter == sub_elem:
                                                is_found=True
                            
                                    if is_found == False:
                                        for sub_elem in compare:
                                            if value_filter.lower() == sub_elem.lower():
                                                is_found=True
                                                xpath_value_filter=re.sub(attribute+value_filter+'=',attribute+sub_elem+'=',xpath_value_filter)
                                                

                                    if is_found == False:
                                        for sub_elem in compare:
                                            if re.search(value_filter,sub_elem):
                                                is_found=True                                    
                                        if is_found == True:
                                            specials_characters_filter=self._str_specials_characters_as_str(chain=value_filter)
                                            xpath_value_filter=re.sub(attribute+specials_characters_filter+'=',attribute+'*'+'[re:match(local-name(),"'+value_filter+'")]'+'=',xpath_value_filter)
                                        
                                    if is_found == False:
                                        for sub_elem in compare:
                                            if re.search(value_filter,sub_elem,re.IGNORECASE):
                                                is_found=True                       
                                        if is_found == True:
                                            specials_characters_filter=self._str_specials_characters_as_str(chain=value_filter)                                        
                                            xpath_value_filter=re.sub(attribute+specials_characters_filter+'=',attribute+'*'+'[re:match(local-name(),"'+value_filter+'","i")]'+'=',xpath_value_filter)
                            
                                    if is_found == False:
                                        exception=None
                                        if is_attribute == True:                            
                                            exception={
                                                'error':'attribute is not found',
                                                'expected_attribute': value_filter,
                                                'message':value_filter+" is not found"
                                            } 
                                        else:
                                            exception={
                                                'error':'tag is not found',
                                                'expected_tag': value_filter,
                                                'message':value_filter+" is not found"
                                            }                                                       

                                        if self._logger != None:
                                            self._logger.error('NetData@'+ self._id + ' ::__generate_xpath -> exception => '+str(exception))                         

                                        raise NetExceptionData(self._logger,**exception)

                            for sub_line_1 in xpath_value_filter.split('") and '):
                                for sub_line_2 in sub_line_1.split('") or '):
                                    for sub_line_3 in sub_line_2.split('" and '):
                                        for sub_line_4 in sub_line_3.split('" or '):

                                            name=re.sub('^(?P<NAME>[^=][^=]*)=.*','\g<NAME>',sub_line_4)
                                            if name[0] == '(':
                                                i=0
                                                parenthesis_opening=''
                                                while name[i] == '(' and i < len(name):
                                                    parenthesis_opening=parenthesis_opening+'('
                                                    i=i+1
                                                new_name=name[i:]

                                                specials_characters_filter=self._str_specials_characters_as_str(chain=name)                                                                            
                                                xpath_value_filter=re.sub(specials_characters_filter+'="'+'(?P<VALUE>[^"][^"]*)"',parenthesis_opening+'re:match('+new_name+',"'+'\g<VALUE>'+'")',xpath_value_filter) 
                                            else:                               
                                                specials_characters_filter=self._str_specials_characters_as_str(chain=name)                                                                            
                                                xpath_value_filter=re.sub(specials_characters_filter+'="'+'(?P<VALUE>[^"][^"]*)"','re:match('+name+',"'+'\g<VALUE>'+'")',xpath_value_filter)

                        xpath_value_filter_final=xpath_value_filter_final+xpath_value_filter

                        xpath_value_filter='['+xpath_value_filter_final+']'
                        
                    value=match.group('VALUE')
                    if value != '.' and value != '..' and value != '*' and value !='@*' and re.search('^ *text *\\( *\\) *$',value) == None:
                        compare=None
                        if value[0] == '@':
                            compare=attributes
                            value=value[1:]
                            is_attribute=True
                            attribute='@'
                        else:
                            compare=tags
                            is_attribute=False
                            attribute=''
                        
                        if xpath_value == '':
                            for sub_elem in compare:
                                if value == sub_elem:
                                    xpath_value=attribute+sub_elem+xpath_value_filter
                        
                        if xpath_value == '':
                            for sub_elem in compare:
                                if value.lower() == sub_elem.lower():
                                    xpath_value=attribute+sub_elem+xpath_value_filter

                        if xpath_value == '':
                            for sub_elem in compare:
                                if re.search(value,sub_elem):                                      
                                    xpath_value=attribute+'*'+'[re:match(local-name(),"'+value+'")]'+xpath_value_filter  

                        if xpath_value == '':
                            for sub_elem in compare:
                                if re.search(value,sub_elem,re.IGNORECASE):                                        
                                    xpath_value=attribute+'*'+'[re:match(local-name(),"'+value+'","i")]'+xpath_value_filter 
                        
                        if xpath_value == '':
                            exception=None
                            if is_attribute == True:                            
                                exception={
                                    'error':'attribute is not found',
                                    'expected_attribute': elem,
                                    'message':elem+" is not found"
                                } 
                            else:
                                exception={
                                    'error':'tag is not found',
                                    'expected_tag': elem,
                                    'message':elem+" is not found"
                                }                                                       
                            
                            if self._logger != None:
                                self._logger.error('NetData@'+ self._id + ' ::__generate_xpath -> exception => '+str(exception))                         
                        
                            raise NetExceptionData(self._logger,**exception)
                        
                    else:
                        xpath_value=value+xpath_value_filter
                else:
                    xpath_value=elem
                
                xpath=xpath+xpath_value+'/'

            xpath=re.sub('//*$','',xpath)
            if self._logger != None:
                self._logger.info('NetData@'+ self._id + ' ::__generate_xpath -> xpath => '+xpath)

            return xpath

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 

    @NetClassParameterUnique(xpath=str,element=etree._Element)
    def __generate_xpath_elements(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            xpath=dict_param_named['xpath']
            element=dict_param_named['element']


            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__generate_xpath_elements -> xpath => '+xpath)      

            search=[]
            xpath_sensitive=xpath
            search=element.xpath(xpath,namespaces={"re": "http://exslt.org/regular-expressions"})

            if len(search) == 0:
                xpath=re.sub('re:match\\( *local-name\\(\\) *, *"(?P<SAVE>[^"][^"]*)" *\\)','re:match(local-name(),"\g<SAVE>","i")',xpath)
                xpath_insensitive=xpath
                search=element.xpath(xpath,namespaces={"re": "http://exslt.org/regular-expressions"})

                if len(search) == 0:

                    attributes=list()
                    if self.__tree is not None:
                        for sub_element in element.iter():
                            for key in sub_element.keys():
                                if str(key) not in attributes:
                                    attributes.append(str(key)) 

                    xpath_list=self.__generate_xpath_multiples_attributes(attributes=attributes,pattern=xpath_sensitive)
                    for xpath in xpath_list:
                        new_search=element.xpath(xpath,namespaces={"re": "http://exslt.org/regular-expressions"})
                        for line_search in new_search:
                            if line_search not in search:
                                search.append(line_search)
                    if len(search) == 0:
                        xpath_list=self.__generate_xpath_multiples_attributes_insensitive(attributes=attributes,pattern=xpath_insensitive)
                        for xpath in xpath_list:
                            new_search=element.xpath(xpath,namespaces={"re": "http://exslt.org/regular-expressions"})
                            for line_search in new_search:
                                if line_search not in search:
                                    search.append(line_search)


            return search

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterUnique(element=etree._Element)
    def __generate_data(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            element=dict_param_named['element']

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__generate_data -> element => '+str(element.tag))      

            data=None

            if self._config['default']['mode'] == 'xml':
                data=NetData(logger=self._logger,config=self._config.copy(),config_type=self._config_type.copy(),config_regex=self._config_regex.copy(),lock_timeout=self._lock_timeout,config_file=self._config_file,config_file_type=self._config_file_type,config_file_regex=self._config_file_regex,xml=element)
            elif self._config['default']['mode'] == 'html':
                data=NetData(logger=self._logger,config=self._config.copy(),config_type=self._config_type.copy(),config_regex=self._config_regex.copy(),lock_timeout=self._lock_timeout,config_file=self._config_file,config_file_type=self._config_file_type,config_file_regex=self._config_file_regex,html=element)               

            return data

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 

    @NetClassParameterUnique(str)
    def __getitem__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            index=list_param_no_named[0]

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__getitem__ -> index => '+index)        

            retour=[]

            xpath=self.__generate_xpath(pattern=index)

            search=self.__generate_xpath_elements(xpath=xpath,element=self.__tree.getroot())
                             
            if len(search) > 0:
                
                if issubclass(type(search[0]),etree._Element):
                    
                    for elem in search:

                        data=self.__generate_data(element=elem)

                        retour.append(data)

                    if self._logger != None:
                        self._logger.info('NetData@'+ self._id + ' ::__getitem__ -> ['+index+'] -> '+str(len(search))+' element(s) found')

                    return retour

                if type(search[0]) is etree._ElementUnicodeResult:

                    retour=NetData.DataDictJSON()
                    tags=[]

                    for elem in search:

                        parent=elem.getparent()
                        if parent is not None and parent.tag  not in tags:
                            tags.append(parent.tag)

                        if elem.is_attribute == True:
        
                            if elem.attrname not in retour.keys():
                                retour[elem.attrname]=[]                        
                            if elem not in retour[elem.attrname]:
                                retour[elem.attrname].append(elem)
                        
                        if elem.is_text == True:

                            if self._config['xmltodict']['parser']['cdata_key'] not in retour.keys():
                                retour[self._config['xmltodict']['parser']['cdata_key']]=[]
                            if elem not in retour[self._config['xmltodict']['parser']['cdata_key']]:
                                retour[self._config['xmltodict']['parser']['cdata_key']].append(elem)
                    
                    if len(tags) > 0:
                        tags.sort()
                        retour['tags']=tags

            if self._logger != None:
                self._logger.info('NetData@'+ self._id + ' ::__getitem__ -> ['+index+'] -> '+str(len(search))+' element(s) found')

            return retour                    
                        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)  
    @NetClassParameterUnique(str,object)         
    def __setitem__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            index=list_param_no_named[0]
            value=list_param_no_named[1]

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__setitem__ => index -> '+index+' || '+'value => '+str(value))        
            
            xpath=self.__generate_xpath(pattern=index)

            search=self.__generate_xpath_elements(xpath=xpath,element=self.__tree.getroot())
                
            if len(search) > 0:
                if issubclass(type(search[0]),etree._Element):
                    if type(value) is list:
                        for elem in search:                    
                            parent=elem.getparent()
                            if parent is not None:
                                remove_element=False
                                i=1
                                for sub_value in value:
                                    if type(sub_value) is dict:
                                        for value_key in sub_value.keys():
                                            if value_key == self._config['xmltodict']['parser']['cdata_key']:
                                                elem.text=sub_value[value_key]
                                            else:
                                                elem.attrib[value_key]=sub_value[value_key]

                                    elif issubclass(type(sub_value),etree._ElementTree):
                                        parent.insert(parent.index(elem)+i,value.getroot())
                                        i=i+1
                                        remove_element=True
                                
                                    elif issubclass(type(sub_value),etree._Element):
                                        parent.insert(parent.index(elem)+i,value)
                                        i=i+1
                                        remove_element=True

                                    elif issubclass(type(type(sub_value)),NetTypeData):                                
                                        if self._config['default']['mode'] == 'xml':
                                            parent.insert(parent.index(elem)+i,sub_value.xml)
                                            i=i+1
                                            remove_element=True
                                        elif self._config['default']['mode'] == 'html':
                                            parent.insert(parent.index(elem)+i,sub_value.html)
                                            i=i+1
                                            remove_element=True
                                if remove_element:
                                    parent.remove(elem)

                    elif type(value) is dict:
                        for elem in search:
                            for value_key in value.keys():
                                if value_key == self._config['xmltodict']['parser']['cdata_key']:
                                    elem.text=value[value_key]
                                else:
                                    elem.attrib[value_key]=value[value_key]
                    elif issubclass(type(value),etree._ElementTree):
                        for elem in search:
                            parent=elem.getparent()
                            if parent is not None:
                                parent.insert(parent.index(elem)+1,value.getroot())
                                parent.remove(elem)
                    elif issubclass(type(value),etree._Element):
                        for elem in search:
                            parent=elem.getparent()
                            if parent is not None:
                                parent.insert(parent.index(elem)+1,value)
                                parent.remove(elem)
                    elif issubclass(type(type(value)),NetTypeData):
                        for elem in search:
                            parent=elem.getparent()
                            if parent is not None:
                                if self._config['default']['mode'] == 'xml':
                                    parent.insert(parent.index(elem)+1,value.xml)
                                    parent.remove(elem)
                                elif self._config['default']['mode'] == 'html':
                                    parent.insert(parent.index(elem)+1,value.html)
                                    parent.remove(elem)
                                
                    elif type(value) is str:
                        for elem in search:
                            elem.tag=value

                        
                if type(search[0]) is etree._ElementUnicodeResult:
                    value_text=None
                    value_attrib=None
                    
                    if type(value) is dict:
                        if self._config['xmltodict']['parser']['cdata_key'] in value.keys():
                            value_text=value[self._config['xmltodict']['parser']['cdata_key']]        
                            value_attrib={}
                            for key in value.keys():
                                if key != self._config['xmltodict']['parser']['cdata_key']:
                                    value_attrib[key]=value[key]
                        else:
                            value_attrib=value
                    else:
                        value_text=value
                        value_attrib=value

                    for elem in search:
                        if elem.is_attribute == True:
                            elem.getparent().attrib[elem.attrname]=str(value_attrib)
                        if elem.is_text == True:
                            if value_text is not None:
                                elem.getparent().text=str(value_text)
                        if elem.is_tail == True:
                            if value_text is not None:
                                elem.getparent().tail=str(value_text)

            if self._logger != None:
                self._logger.info('NetData@'+ self._id + ' ::__setitem__ -> ['+index+'] => '+str(len(search))+' element(s) found')            
                
            return self    
                
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterUnique(str)     
    def __delitem__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            index=list_param_no_named[0]
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__delitem__ -> index => '+index)        
            
            xpath=self.__generate_xpath(pattern=index)

            search=self.__generate_xpath_elements(xpath=xpath,element=self.__tree.getroot())

            if len(search) > 0:
                if issubclass(type(search[0]),etree._Element):
                    for elem in search:
                        parent=elem.getparent()
                        if parent is not None:
                            parent.remove(elem)

                if type(search[0]) is etree._ElementUnicodeResult:
                    for elem in search:
                        if elem.is_attribute == True:
                            del elem.getparent().attrib[elem.attrname]
                        elif elem.is_text == True:
                            elem.getparent().text=None
                        elif elem.is_tail == True:
                            elem.getparent().tail=None

            if self._logger != None:
                self._logger.info('NetData@'+ self._id + ' ::__delitem__ -> ['+index+'] => '+str(len(search))+' element(s) found')            
                
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)   
    @NetClassParameterUnique(str)
    def remove(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            xpath=list_param_no_named[0]
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::remove -> xpath => '+str(xpath))                
        
            del self[xpath]

            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 

    @NetClassParameterUnique(object)     
    def __add__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            obj=list_param_no_named[0]
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__add__ -> obj => '+str(obj)) 
            
            retour=self.copy(*param_no_named,**param_named)
            retour+=obj

            return retour

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)                                       
    @NetClassParameterUnique(object)     
    def __iadd__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            obj=list_param_no_named[0]
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__iadd__ -> obj => '+str(obj)) 
            
            add=None
            if issubclass(type(obj),list):
                for elem in obj:
                    self+=elem
                return self
            elif issubclass(type(obj),etree._Element):
                add=obj
            elif issubclass(type(obj),etree._ElementTree):
                add=obj.getroot()                            
            elif issubclass(type(type(obj)),NetTypeData):
                add=obj.xml
            else:               
                add=NetData(logger=self._logger,config=self._config.copy(),config_type=self._config_type.copy(),config_regex=self._config_regex.copy(),lock_timeout=self._lock_timeout,config_file=self._config_file,config_file_type=self._config_file_type,config_file_regex=self._config_file_regex,data=obj)
                add=add.xml

            if self.__tree.getroot().tag == str(add.tag):

                retour_attrib=dict(self.__tree.getroot().attrib)
                add_attrib=dict(add.attrib)

                if add.text is not None:
                    if self.__tree.getroot().text is None:
                        self.__tree.getroot().text=add.text
                    else:
                        self.__tree.getroot().text=str([
                            self.__tree.getroot().text,
                            add.text
                        ])
                
                if add.tail is not None:
                    if self.__tree.getroot().tail is None:
                        self.__tree.getroot().tail=add.tail
                    else:
                        self.__tree.getroot().tail=str([
                            self.__tree.getroot().tail,
                            add.tail
                        ])

                for key in add_attrib.keys():
                    if key in retour_attrib.keys():
                        if type(retour_attrib[key]) is not list:
                            save=retour_attrib[key]
                            retour_attrib[key]=[]
                            retour_attrib[key].append(save)

                        if type(add_attrib[key]) is list:
                            for elem in add_attrib[key]:
                                if elem not in retour_attrib[key]:
                                    retour_attrib[key].append(elem)
                        else:       
                            if add_attrib[key] not in retour_attrib[key]:
                                retour_attrib[key].append(add_attrib[key])

                    else:
                        retour_attrib[key]=add_attrib[key]
            
                for key in retour_attrib.keys():
                    self.__tree.getroot().attrib[key]=str(retour_attrib[key])

                for elem in add:
                    self.__tree.getroot().append(elem)
            else:
                self.__tree.getroot().append(add)
            
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    @NetClassParameterUnique(object)
    def add(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            add=list_param_no_named[0]
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::add -> add => '+str(add))                
        
            self+=add

            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 

    @NetClassParameterUnique(object)     
    def __sub__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            obj=list_param_no_named[0]
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__sub__ -> obj => '+str(obj)) 
            
            retour=self.copy(*param_no_named,**param_named)
            retour-=obj

            return retour

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterUnique(object)     
    def __isub__(self,*param_no_named,**param_named):

        @NetClassParameterUnique(source1=etree._Element,source2=etree._Element)
        def __isub___element(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                source1=dict_param_named['source1']
                source2=dict_param_named['source2']

                if self._check_same_object(source1=source1,source2=source2):
 
                    if source1.getparent() != None:
                        source1.getparent().remove(source1)
                        return

                if str(source1.tag) == str(source2.tag):

                    if source1.text is not None and source2.text is None:
                        source1.text=re.sub(str(source2.text),'',str(source1.text))

                    if source1.tail is not None and source2.tail is None:
                        source1.tail=re.sub(str(source2.tail),'',str(source1.tail)) 

                    for key in source2.attrib.keys():
                        if key in source1.attrib.keys():
                            source1.attrib[key]=self._str_sub(source1=source1.attrib[key],source2=source2.attrib[key]) 
                    
                    
                    keys=list(source1.attrib.keys())
                    for key in keys:
                        if source1.attrib[key] == '':
                            del source1.attrib[key]
                    
                    for source2_child in source2:
                        for source1_child in source1:
                            __isub___element(self,source1=source1_child,source2=source2_child)                              

            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionData(self._logger,exception) 

        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            obj=list_param_no_named[0]
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__isub__ -> obj => '+str(obj)) 
            

            sub=None
            if issubclass(type(obj),list):
                for elem in obj:
                    self-=elem
                return self
            elif issubclass(type(obj),etree._Element):
                sub=obj
            elif issubclass(type(obj),etree._ElementTree):
                sub=obj.getroot()                            
            elif issubclass(type(type(obj)),NetTypeData):
                sub=obj.xml
            else:               
                sub=NetData(logger=self._logger,config=self._config.copy(),config_type=self._config_type.copy(),config_regex=self._config_regex.copy(),lock_timeout=self._lock_timeout,config_file=self._config_file,config_file_type=self._config_file_type,config_file_regex=self._config_file_regex,data=obj)
                sub=sub.xml

            __isub___element(self,source1=self.xml,source2=sub)

            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterUnique(object)
    def sub(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            sub=list_param_no_named[0]
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::sub -> sub => '+str(sub))                
        
            self-=sub

            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 


    @NetClassParameterCombine([NetClassParameterUnique(str,str),NetClassParameterUnique(str,str,str)])
    def replace(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if len(list_param_no_named) == 3:
                path=list_param_no_named[0]
                old_str=list_param_no_named[1]
                new_str=list_param_no_named[2]

                if self._logger != None:
                    self._logger.debug('NetData@'+ self._id + ' ::replace -> path => '+path+' || '+'old_str => '+old_str+' || '+'new_str => '+new_str)

                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                text_prefix=self._config['xmltodict']['parser']['cdata_key']

                text_prefix=self._str_specials_characters_as_str(chain=text_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^ *'+text_prefix+'|^ *'+attribut_prefix,path.split('/')[-1]):
                    path='/'.join(path.split('/')[:-1])

                for elem in self[path]:
                    elem.replace(old_str,new_str)
            else:
                old_str=list_param_no_named[0]
                new_str=list_param_no_named[1]

                if self._config['default']['mode'] == 'xml':
                    self.xml=str(self.xml).replace(old_str,new_str)
                elif self._config['default']['mode'] == 'html':
                    self.html=str(self.html).replace(old_str,new_str)                    
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterCombine([NetClassParameterUnique(str,str),NetClassParameterUnique(str,str,str)])
    def replace_tag(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if len(list_param_no_named) == 3:
                path=list_param_no_named[0]
                old_tag=list_param_no_named[1]
                new_tag=list_param_no_named[2]

                if self._logger != None:
                    self._logger.debug('NetData@'+ self._id + ' ::replace_tag -> path => '+path+' || '+'old_tag => '+old_tag+' || '+'new_tag => '+new_tag)

                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                text_prefix=self._config['xmltodict']['parser']['cdata_key']

                text_prefix=self._str_specials_characters_as_str(chain=text_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^ *'+text_prefix+'|^ *'+attribut_prefix,path.split('/')[-1]):
                    path='/'.join(path.split('/')[:-1])

                for elem in self[path]:
                    elem.replace_tag(old_tag,new_tag)
            else:
                old_tag=list_param_no_named[0]
                new_tag=list_param_no_named[1]

                for elem in self.__tree.getroot().iter():
                    if elem.tag == old_tag:
                        elem.tag=new_tag
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterCombine([NetClassParameterUnique(str,str),NetClassParameterUnique(str,str,str)])
    def replace_text(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if len(list_param_no_named) == 3:
                path=list_param_no_named[0]
                old_text=list_param_no_named[1]
                new_text=list_param_no_named[2]

                if self._logger != None:
                    self._logger.debug('NetData@'+ self._id + ' ::replace_text -> path => '+path+' || '+'old_text => '+old_text+' || '+'new_text => '+new_text)

                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                text_prefix=self._config['xmltodict']['parser']['cdata_key']

                text_prefix=self._str_specials_characters_as_str(chain=text_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^ *'+text_prefix+'|^ *'+attribut_prefix,path.split('/')[-1]):
                    path='/'.join(path.split('/')[:-1])

                for elem in self[path]:
                    elem.replace_text(old_text,new_text)
            else:
                old_text=list_param_no_named[0]
                new_text=list_param_no_named[1]

                for elem in self.__tree.getroot().iter():
                    if str(elem.text) == old_text:
                        elem.text=new_text
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterCombine([NetClassParameterUnique(str,str),NetClassParameterUnique(str,str,str)])
    def replace_tail(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if len(list_param_no_named) == 3:
                path=list_param_no_named[0]
                old_tail=list_param_no_named[1]
                new_tail=list_param_no_named[2]

                if self._logger != None:
                    self._logger.debug('NetData@'+ self._id + ' ::replace_tail -> path => '+path+' || '+'old_tail => '+old_tail+' || '+'new_tail => '+new_tail)

                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                tail_prefix=self._config['xmltodict']['parser']['cdata_key']

                tail_prefix=self._str_specials_characters_as_str(chain=tail_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^ *'+tail_prefix+'|^ *'+attribut_prefix,path.split('/')[-1]):
                    path='/'.join(path.split('/')[:-1])

                for elem in self[path]:
                    elem.replace_tail(old_tail,new_tail)
            else:
                old_tail=list_param_no_named[0]
                new_tail=list_param_no_named[1]

                for elem in self.__tree.getroot().iter():
                    if str(elem.tail) == old_tail:
                        elem.tail=new_tail
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterCombine([NetClassParameterUnique(str,str),NetClassParameterUnique(str,str,str)])
    def replace_attribute(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if len(list_param_no_named) == 3:
                path=list_param_no_named[0]
                old_attribute=list_param_no_named[1]
                new_attribute=list_param_no_named[2]

                if self._logger != None:
                    self._logger.debug('NetData@'+ self._id + ' ::replace_attribute -> path => '+path+' || '+'old_attribute => '+old_attribute+' || '+'new_attribute => '+new_attribute)

                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                attribute_prefix=self._config['xmltodict']['parser']['cdata_key']

                attribute_prefix=self._str_specials_characters_as_str(chain=attribute_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^ *'+attribute_prefix+'|^ *'+attribut_prefix,path.split('/')[-1]):
                    path='/'.join(path.split('/')[:-1])

                for elem in self[path]:
                    elem.replace_attribute(old_attribute,new_attribute)
            else:
                old_attribute=list_param_no_named[0]
                new_attribute=list_param_no_named[1]

                for elem in self.__tree.getroot().iter():
                    for key in elem.attrib.keys():
                        if key == old_attribute:
                            save=elem.attrib[key]
                            del elem.attrib[key]
                            elem.attrib[new_attribute]=save
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterCombine([NetClassParameterUnique(str,str),NetClassParameterUnique(str,str,str)])
    def replace_value(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if len(list_param_no_named) == 3:
                path=list_param_no_named[0]
                old_value=list_param_no_named[1]
                new_value=list_param_no_named[2]

                if self._logger != None:
                    self._logger.debug('NetData@'+ self._id + ' ::replace_value -> path => '+path+' || '+'old_value => '+old_value+' || '+'new_value => '+new_value)

                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                value_prefix=self._config['xmltodict']['parser']['cdata_key']

                value_prefix=self._str_specials_characters_as_str(chain=value_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^ *'+value_prefix,path.split('/')[-1]):
                    path='/'.join(path.split('/')[:-1])
                
                if re.search('^ *'+attribut_prefix,path.split('/')[-1]):
                    attributes=re.sub('^ *'+attribut_prefix,'',path.split('/')[-1])

                    path='/'.join(path.split('/')[:-1])                    
                    for elem in self[path]:
                        for key in elem.xml.attrib.keys():
                            for attribute in attributes.split('|'):
                                if re.search(attribute,key):
                                    if elem.xml.attrib[key] == old_value:
                                        elem.xml.attrib[key]=new_value                        
                else:
                    for elem in self[path]:
                        elem.replace_value(old_value,new_value)
            else:
                old_value=list_param_no_named[0]
                new_value=list_param_no_named[1]

                for elem in self.__tree.getroot().iter():
                    for key in elem.attrib.keys():
                        if elem.attrib[key] == old_value:
                            elem.attrib[key]=new_value
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 


    @NetClassParameterCombine([NetClassParameterUnique(str,str),NetClassParameterUnique(str,str,str)])
    def regex(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if len(list_param_no_named) == 3:
                path=list_param_no_named[0]
                old_regex=list_param_no_named[1]
                new_regex=list_param_no_named[2]

                if self._logger != None:
                    self._logger.debug('NetData@'+ self._id + ' ::regex -> path => '+path+' || '+'old_regex => '+old_regex+' || '+'new_regex => '+new_regex)

                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                text_prefix=self._config['xmltodict']['parser']['cdata_key']

                text_prefix=self._str_specials_characters_as_str(chain=text_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^ *'+text_prefix+'|^ *'+attribut_prefix,path.split('/')[-1]):
                    path='/'.join(path.split('/')[:-1])

                for elem in self[path]:
                    elem.regex(old_regex,new_regex)
            else:
                old_regex=list_param_no_named[0]
                new_regex=list_param_no_named[1]

                if self._config['default']['mode'] == 'xml':
                    self.xml=re.sub(old_regex,new_regex,str(self.xml))

                elif self._config['default']['mode'] == 'html':
                    self.html=re.sub(old_regex,new_regex,str(self.html))  
                                      
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)   
    @NetClassParameterCombine([NetClassParameterUnique(str,str),NetClassParameterUnique(str,str,str)])
    def regex_tag(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if len(list_param_no_named) == 3:
                path=list_param_no_named[0]
                old_tag=list_param_no_named[1]
                new_tag=list_param_no_named[2]

                if self._logger != None:
                    self._logger.debug('NetData@'+ self._id + ' ::regex_tag -> path => '+path+' || '+'old_tag => '+old_tag+' || '+'new_tag => '+new_tag)

                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                tail_prefix=self._config['xmltodict']['parser']['cdata_key']

                tail_prefix=self._str_specials_characters_as_str(chain=tail_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^ *'+tail_prefix+'|^ *'+attribut_prefix,path.split('/')[-1]):
                    path='/'.join(path.split('/')[:-1])

                for elem in self[path]:
                    elem.regex_tag(old_tag,new_tag)
            else:
                old_tag=list_param_no_named[0]
                new_tag=list_param_no_named[1]

                for elem in self.__tree.getroot().iter():
                    elem.tag=re.sub(old_tag,new_tag,elem.tag)

            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterCombine([NetClassParameterUnique(str,str),NetClassParameterUnique(str,str,str)])
    def regex_text(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if len(list_param_no_named) == 3:
                path=list_param_no_named[0]
                old_text=list_param_no_named[1]
                new_text=list_param_no_named[2]

                if self._logger != None:
                    self._logger.debug('NetData@'+ self._id + ' ::regex_text -> path => '+path+' || '+'old_text => '+old_text+' || '+'new_text => '+new_text)

                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                tail_prefix=self._config['xmltodict']['parser']['cdata_key']

                tail_prefix=self._str_specials_characters_as_str(chain=tail_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^ *'+tail_prefix+'|^ *'+attribut_prefix,path.split('/')[-1]):
                    path='/'.join(path.split('/')[:-1])

                for elem in self[path]:
                    elem.regex_text(old_text,new_text)
            else:
                old_text=list_param_no_named[0]
                new_text=list_param_no_named[1]

                for elem in self.__tree.getroot().iter():
                    if elem.text is not None:
                        elem.text=re.sub(old_text,new_text,str(elem.text))

            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    @NetClassParameterCombine([NetClassParameterUnique(str,str),NetClassParameterUnique(str,str,str)])
    def regex_tail(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if len(list_param_no_named) == 3:
                path=list_param_no_named[0]
                old_tail=list_param_no_named[1]
                new_tail=list_param_no_named[2]

                if self._logger != None:
                    self._logger.debug('NetData@'+ self._id + ' ::regex_tail -> path => '+path+' || '+'old_tail => '+old_tail+' || '+'new_tail => '+new_tail)

                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                tail_prefix=self._config['xmltodict']['parser']['cdata_key']

                tail_prefix=self._str_specials_characters_as_str(chain=tail_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^ *'+tail_prefix+'|^ *'+attribut_prefix,path.split('/')[-1]):
                    path='/'.join(path.split('/')[:-1])

                for elem in self[path]:
                    elem.regex_tail(old_tail,new_tail)
            else:
                old_tail=list_param_no_named[0]
                new_tail=list_param_no_named[1]

                for elem in self.__tree.getroot().iter():
                    if elem.tail is not None:
                        elem.tail=re.sub(old_tail,new_tail,str(elem.tail))

            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    @NetClassParameterCombine([NetClassParameterUnique(str,str),NetClassParameterUnique(str,str,str)])
    def regex_attribute(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if len(list_param_no_named) == 3:
                path=list_param_no_named[0]
                old_attribute=list_param_no_named[1]
                new_attribute=list_param_no_named[2]

                if self._logger != None:
                    self._logger.debug('NetData@'+ self._id + ' ::regex_attribute -> path => '+path+' || '+'old_attribute => '+old_attribute+' || '+'new_attribute => '+new_attribute)

                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                attribute_prefix=self._config['xmltodict']['parser']['cdata_key']

                attribute_prefix=self._str_specials_characters_as_str(chain=attribute_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^ *'+attribute_prefix+'|^ *'+attribut_prefix,path.split('/')[-1]):
                    path='/'.join(path.split('/')[:-1])

                for elem in self[path]:
                    elem.regex_attribute(old_attribute,new_attribute)
            else:
                old_attribute=list_param_no_named[0]
                new_attribute=list_param_no_named[1]

                for elem in self.__tree.getroot().iter():
                    for key in elem.attrib.keys():
                        var=re.sub(old_attribute,new_attribute,key)
                        if var != key:
                            save=elem.attrib[key]
                            del elem.attrib[key]
                            elem.attrib[var]=save
                        
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    @NetClassParameterCombine([NetClassParameterUnique(str,str),NetClassParameterUnique(str,str,str)])
    def regex_value(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if len(list_param_no_named) == 3:
                path=list_param_no_named[0]
                old_value=list_param_no_named[1]
                new_value=list_param_no_named[2]

                if self._logger != None:
                    self._logger.debug('NetData@'+ self._id + ' ::regex_value -> path => '+path+' || '+'old_value => '+old_value+' || '+'new_value => '+new_value)

                attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
                value_prefix=self._config['xmltodict']['parser']['cdata_key']

                value_prefix=self._str_specials_characters_as_str(chain=value_prefix)
                attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

                if re.search('^ *'+value_prefix,path.split('/')[-1]):
                    path='/'.join(path.split('/')[:-1])
                
                if re.search('^ *'+attribut_prefix,path.split('/')[-1]):
                    attributes=re.sub('^ *'+attribut_prefix,'',path.split('/')[-1])

                    path='/'.join(path.split('/')[:-1])                    
                    for elem in self[path]:
                        for key in elem.xml.attrib.keys():
                            for attribute in attributes.split('|'):
                                if re.search(attribute,key):
                                
                                    var=re.sub(old_value,new_value,elem.xml.attrib[key])
                                    if elem.xml.attrib[key] != var:
                                        elem.xml.attrib[key]=var 

                else:
                    for elem in self[path]:
                        elem.regex_value(old_value,new_value)
            else:
                old_value=list_param_no_named[0]
                new_value=list_param_no_named[1]

                for elem in self.__tree.getroot().iter():
                    for key in elem.attrib.keys():

                        var=re.sub(old_value,new_value,elem.attrib[key])
                        if elem.attrib[key] != var:
                            elem.attrib[key]=var
                            
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)


    def clean(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::clean -> Cleaning Blank')                
            
            self.clean_blank_attributes(*param_no_named,**param_named)
            self.clean_blank_text(*param_no_named,**param_named)
            self.indent(*param_no_named,**param_named)

            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)     
    def clean_blank_attributes(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::clean_blank_Attributes -> Cleaning Attributes')                
            
            if self.__tree is not None:
                for element in self.__tree.iter():
                    for key in element.keys():
                        if re.search('^  *$',element.attrib[key]):
                            del element.attrib[key]
                        elif element.attrib[key] == '':
                            del element.attrib[key]
                        elif element.attrib[key] is None:
                            del element.attrib[key]
                            
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    def clean_blank_text(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::clean_blank_Text -> Cleaning Text')                
            
            if self.__tree is not None:
                for element in self.__tree.iter():
                    if element.text is not None and not element.text.strip():
                        element.text = None
                    if element.tail is not None and not element.tail.strip():
                        element.tail = None                        
            
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    def indent(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            indent=self._config['xml']['indent']
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::indent -> indent => '+str(indent))                
            
            if self.__tree is not None:
                etree.indent(self.__tree,**indent)
            
            return self

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 

    @NetClassParameterCombine([NetClassParameterUnique(file=str),NetClassParameterUnique(str)])
    def load_data(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
        
            extensions=[
                'html',
                'json',
                'xml',
                'yml'
            ]

            input_file=self._obj_get_args(*param_no_named,source='file',source_type=str,**param_named)

            if self._logger is not None:
                self._logger.debug('NetData@'+ self._id +' ::load_data -> '+'input_file => '+input_file)           
                        
            extension=re.sub('.*\\.(?P<EXTENSION>[^\\.][^\\.]*)$','\\g<EXTENSION>',input_file).lower()
            if extension not in extensions:
                exception={
                    'error':'extension is not supported',
                    'expected_extensions':str(extensions),
                    'inspected_extension': extension,
                    'source_path':input_file,
                    'message':extension+" is not supported"
                    }

                if self._logger is not None:
                    self._logger.error('NetData@'+ self._id +' ::load_data -> '+'exception => '+str(exception))                         
                        
                raise NetExceptionData(self._logger,**exception)
            elif extension == 'html' :
                self.html=self._str_load_file(file=input_file,timeout=self._lock_timeout)
            elif extension == 'json' :
                self.xmltodict=self._str_load_file(file=input_file,timeout=self._lock_timeout)
            elif extension == 'xml' :
                self.xml=self._str_load_file(file=input_file,timeout=self._lock_timeout)                
            elif extension == 'yml':
                status=self._config['yaml']['mode']
                self._config['yaml']['mode']='xmltodict'                
                self.yaml=self._str_load_file(file=input_file,timeout=self._lock_timeout)
                self._config['yaml']['mode']=status

            if self._logger is not None:
                self._logger.info('NetData@'+ self._id +' ::load_data -> '+'Success' +'  ||  '+'output_file => '+str(input_file)+' || '+'tag => '+self.__tree.getroot().tag)  

        except Exception as exception:           
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterCombine([NetClassParameterUnique(file=str),NetClassParameterUnique(str)])
    def save_data(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            extensions=[
                'html',
                'json',
                'xml',
                'yml'
            ]

            i=0

            output_file=self._obj_get_args(*param_no_named,source='file',source_type=str,**param_named)

            if self._logger is not None:
                self._logger.debug('NetData@'+ self._id +' ::save_data -> '+'output_file => '+str(output_file)+' || '+'tag => '+self.__tree.getroot().tag)           
                        
            extension=re.sub('.*\\.(?P<EXTENSION>[^\\.][^\\.]*)$','\\g<EXTENSION>',output_file).lower()
            if extension not in extensions:
                exception={
                    'error':'extension is not supported',
                    'expected_extensions':str(extensions),
                    'inspected_extension': extension,
                    'source_path':output_file,
                    'message':extension+" is not supported"
                    }

                if self._logger is not None:
                    self._logger.error('NetData@'+ self._id +' ::save_data -> '+'exception => '+str(exception))                         
                        
                raise NetExceptionData(self._logger,**exception)
            elif extension == 'html' :
                self._str_save_file(file=output_file,data=str(self.html),timeout=self._lock_timeout)
            elif extension == 'json' :
                self._str_save_file(file=output_file,data=str(self.xmltodict),timeout=self._lock_timeout)
            elif extension == 'xml' :
                self._str_save_file(file=output_file,data=str(self.xml),timeout=self._lock_timeout)
            elif extension == 'yml':
                status=self._config['yaml']['mode']
                self._config['yaml']['mode']='xmltodict'
                self._str_save_file(file=output_file,data=str(self.yaml),timeout=self._lock_timeout)
                self._config['yaml']['mode']=status
            
            if self._logger is not None:
                self._logger.info('NetData@'+ self._id +' ::save_data -> '+'Success' +'  ||  '+'output_file => '+str(output_file)+' || '+'tag => '+self.__tree.getroot().tag)  

        except Exception as exception:           
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 

    def copy(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::copy -> root => '+self.__tree.getroot().tag)               
            
            retour=None
            if self._config['default']['mode'] == 'xml':
                retour=NetData(logger=self._logger,config=self._config.copy(),config_type=self._config_type.copy(),config_regex=self._config_regex.copy(),lock_timeout=self._lock_timeout,config_file=self._config_file,config_file_type=self._config_file_type,config_file_regex=self._config_file_regex,xml=str(self.xml))
            elif self._config['default']['mode'] == 'html':
                retour=NetData(logger=self._logger,config=self._config.copy(),config_type=self._config_type.copy(),config_regex=self._config_regex.copy(),lock_timeout=self._lock_timeout,config_file=self._config_file,config_file_type=self._config_file_type,config_file_regex=self._config_file_regex,html=str(self.html))               

            return retour

        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 

    @NetClassParameterUnique(tag=str)
    def __doctype_attributes(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            tag=dict_param_named['tag']
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__doctype_attributes -> tag => '+tag)             


            #list same element whith theirs children
            attributes=list()
            for elem in self.__tree.getroot().iter(tag):
                for key in elem.attrib.keys():
                    if key not in attributes:
                        attributes.append(key)            

            retour=[]
            for key in attributes:
                mode='#REQUIRED'
                format_attribute='CDATA'

                values=[]
                for elem in self.__tree.getroot().iter(tag):
                    if key not in elem.attrib.keys():
                        mode='#IMPLIED'
                    else:
                        if elem.attrib[key] is None or elem.attrib[key] == '':
                            mode='#IMPLIED'
                        elif str(elem.attrib[key]) not in values:
                            values.append(str(elem.attrib[key]))
                
                is_valid=True
                value='|'
                if len(values) <= 4:
                    for elem in values:
                        if re.search('^[a-z][a-z]*$',elem) is None and re.search('^[A-Z][A-Z]*$',elem) is None:
                            is_valid=False
                        else:
                            value=value+elem+'|'
                if is_valid:
                    if value[1:-1] == 'yes' or value[1:-1] == 'no':
                        format_attribute='(yes|no)'
                    elif value[1:-1] == 'YES' or value[1:-1] == 'NO':
                        format_attribute='(YES|NO)'
                    else:             
                        format_attribute='('+value[1:-1]+')'


                line='<!ATTLIST '+tag+' '+str(key)+' '+str(format_attribute)+' '+str(mode)+'>'
                retour.append(line)
 
            return retour
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    @NetClassParameterUnique(tag=str)
    def __doctype_tag(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            tag=dict_param_named['tag']
            retour=[]
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__doctype_tag -> tag => '+tag)             

            is_PCDATA=False

            #list same element whith theirs children
            elements=list()
            for elem in self.__tree.getroot().iter(tag):
                
                if elem.text is not None and elem.text != '':
                    is_PCDATA=True

                if elem.tail is not None and elem.tail != '':
                    is_PCDATA=True                

                size=len(elem)
                if size > 0:
                    add=list()
                    for child in elem:
                        add.append(child.tag)
                    elements.append(add)
            
            if len(elements) > 0:

                #sort
                i=0
                while i < len(elements)-1:
                    k=i+1
                    while k < len(elements):
                        if len(elements[i]) > len(elements[k]):
                            permute=elements[i]
                            elements[i]=elements[k]
                            elements[k]=permute
                        k=k+1
                    i=i+1

                #regroups sames values
                line=0
                while line < len(elements):
                    init_str=0
                    size_str=1
                    while init_str+size_str < len(elements[line]):
                        if elements[line][init_str] == elements[line][init_str+size_str]:
                            while init_str+size_str < len(elements[line]) and elements[line][init_str] == elements[line][init_str+size_str]:
                                size_str=size_str+1

                            new_list=list()
                            if init_str > 0:
                                for elem in elements[line][:init_str]:
                                    new_list.append(elem)

                            new_reccord=str(elements[line][init_str])+'+'
                            new_list.append(new_reccord)

                            if init_str+size_str < len(elements[line]):
                                for elem in elements[line][init_str+size_str:]:
                                    new_list.append(elem)                            
                            elements[line]=new_list
                            size_str=1

                        init_str=init_str+1
                    
                    line=line+1

                #character +
                line=0
                while line < len(elements):
                    init_str=0
                    while init_str < len(elements[line]):
                        
                        if re.search('\\+$',elements[line][init_str]) is None:

                            line_compare=0
                            while line_compare < len(elements):
                                if line != line_compare:
                                    init_compare=0
                                    while init_compare < len(elements[line_compare]):
                                        if elements[line][init_str]+'+' == elements[line_compare][init_compare]:
                                            elements[line][init_str]=elements[line][init_str]+'+'
                                                        
                                        init_compare=init_compare+1

                                line_compare=line_compare+1

                        init_str=init_str+1

                    line=line+1

                #character *
                line=0
                while line < len(elements):
                    init_str=0
                    while init_str < len(elements[line]):
                    
                        if re.search('\\+$',elements[line][init_str]):
                            line_compare=0
                            while line_compare < len(elements):
                                found=False
                                if line != line_compare:
                                    init_compare=0
                                    
                                    while init_compare < len(elements[line_compare]):
                                        if elements[line][init_str] == elements[line_compare][init_compare]:
                                            found=True

                                        init_compare=init_compare+1

                                    if not found:
                                        elements[line][init_str]=re.sub('\\+$','*',elements[line][init_str])

                                line_compare=line_compare+1

                        init_str=init_str+1

                    line=line+1

                #character ?
                line=0
                while line < len(elements):
                    init_str=0
                    while init_str < len(elements[line]):
                    
                        if re.search('\\+$|\\*$|\\?$',elements[line][init_str]) is None:
                            line_compare=0
                            while line_compare < len(elements):
                                found=False
                                if line != line_compare:
                                    init_compare=0
                                    
                                    while init_compare < len(elements[line_compare]):
                                        if elements[line][init_str] == elements[line_compare][init_compare]:
                                            found=True

                                        init_compare=init_compare+1

                                    if not found:
                                        if re.search('\\?$',elements[line][init_str]) is None:
                                            elements[line][init_str]=elements[line][init_str]+'?'

                                line_compare=line_compare+1

                        init_str=init_str+1

                    line=line+1

                #sequence with parenthesis
                line=0
                while line < len(elements):
                    init_str=0
                    size_str=2

                    while init_str+size_str <= len(elements[line]):
                        init_compare=init_str+size_str
                        size_compare=size_str
                        
                        found=False
                        while init_compare+size_compare <= len(elements[line]) and not found:

                            if re.sub('\\+|\\*|\\?','',''.join(elements[line][init_str:init_str+size_compare])) == re.sub('\\+|\\*|\\?','',''.join(elements[line][init_compare:init_compare+size_compare])):
                                while init_compare+size_compare <= len(elements[line]) and re.sub('\\+|\\*|\\?','',''.join(elements[line][init_str:init_str+size_compare])) == re.sub('\\+|\\*|\\?','',''.join(elements[line][init_compare:init_compare+size_compare])):
                                    init_compare=init_compare+size_compare
                                init_compare=init_compare-size_compare

                                found=True
                            else:
                                init_compare=init_compare+1
                                size_compare=size_compare+1

                        if found:
                            new_list=list()
                            if init_str > 0:
                                for elem in elements[line][:init_str]:
                                    new_list.append(elem)

                            index=init_str
                            while index < init_str+size_compare:       
                                end=''

                                index_compare=init_str+size_compare
                                while index_compare < init_compare+size_compare:
                                    if re.sub('\\+|\\*|\\?','',elements[line][index]) == re.sub('\\+|\\*|\\?','',elements[line][index_compare]):
                                        last_character=elements[line][index][-1]
                                        last_character_compare=elements[line][index_compare][-1]
                                        
                                        if last_character != '+':
                                            if last_character_compare == '+':
                                                if last_character == '*':
                                                    elements[line][index]=elements[line][index][:-1]+last_character_compare
                                                else:
                                                    elements[line][index]=elements[line][index]+last_character_compare
                                            elif last_character == '*' and last_character_compare != '*' and last_character_compare != '?':
                                                elements[line][index]=elements[line][index][:-1]+'+'
                                            elif last_character == '?':
                                                if last_character_compare == '*':
                                                    elements[line][index]=elements[line][index][:-1]+'*'
                                                elif last_character_compare != '?':
                                                    elements[line][index]=elements[line][index][:-1]

                                    index_compare=index_compare+1

                                elements[line][index]=elements[line][index]+end                                              
                                index=index+1

                            new_reccord=', '.join(elements[line][init_str:init_str+size_compare])
                            new_reccord='('+new_reccord+')+'
                            new_list.append(new_reccord)

                            if init_str+size_str < len(elements[line]):
                                for elem in elements[line][init_compare+size_compare:]:
                                    new_list.append(elem)                            
                            elements[line]=new_list
                        else:  
                            init_str=init_str+1

                    line=line+1


                #group with parenthesis
                line=0
                while line < len(elements):
        
                    expected_found_str=len(elements)-(1+line)
                    found=False

                    while expected_found_str > 2:

                        init_str=0
                        size_str=2

                        while init_str+size_str <= len(elements[line]):

                            end=False
                            found=False        
                            while init_str+size_str <= len(elements[line]) and not end:

                                found_str=0
                                
                                line_compare=line+1
                                while line_compare <  len(elements):

                                    init_compare=init_str

                                    while init_compare+size_str <= len(elements[line_compare]) and elements[line][init_str:init_str+size_str] != elements[line_compare][init_compare:init_compare+size_str]:
                                        init_compare=init_compare+1

                                    if init_compare+size_str <= len(elements[line_compare]) and elements[line][init_str:init_str+size_str] == elements[line_compare][init_compare:init_compare+size_str]:
                                        found_str=found_str+1

                                    line_compare=line_compare+1

                                if found_str >= expected_found_str:
                                    size_str=size_str+1
                                    found=True
                                else:
                                    end=True

                            if found:

                                size_str=size_str-1
                                line_compare=line+1
                                while line_compare < len(elements):

                                    init_compare=init_str

                                    while init_compare+size_str <= len(elements[line_compare]) and elements[line][init_str:init_str+size_str] != elements[line_compare][init_compare:init_compare+size_str]:
                                        init_compare=init_compare+1

                                    if init_compare+size_str <= len(elements[line_compare]) and elements[line][init_str:init_str+size_str] == elements[line_compare][init_compare:init_compare+size_str]:
                                              
                                        new_list=list()

                                        if init_compare > 0:
                                            for elem in elements[line_compare][:init_compare]:
                                                new_list.append(elem)

                                        new_reccord=', '.join(elements[line_compare][init_compare:init_compare+size_str])
                                        new_reccord='('+new_reccord+')'
                                        new_list.append(new_reccord)

                                        if init_compare+size_str < len(elements[line_compare]):
                                            for elem in elements[line_compare][init_compare+size_str:]:
                                                new_list.append(elem)                            
                                        elements[line_compare]=new_list
                                        
                                    line_compare=line_compare+1

                                new_list=list()
                                if init_str > 0:
                                    for elem in elements[line][:init_str]:
                                        new_list.append(elem)

                                new_reccord=', '.join(elements[line][init_str:init_str+size_str])
                                new_reccord='('+new_reccord+')'
                                new_list.append(new_reccord)

                                if init_str+size_str < len(elements[line]):
                                    for elem in elements[line][init_str+size_str:]:
                                        new_list.append(elem)                            
                                elements[line]=new_list                

                                init_str=init_str+size_str

                            else:
                                init_str=init_str+1

                        expected_found_str=expected_found_str-1 

                    line=line+1

                max_size=0
                for elem in elements:
                    if len(elem) > max_size:
                        max_size=len(elem)

                index=0
                while index < max_size:                
                    line=0
                    while line < len(elements):
                        line_compare=0
                        found=0
                        while line_compare < len(elements):
                            if line != line_compare:
                                if index < len(elements[line]) and index < len(elements[line_compare]):
                                    if elements[line][index] == elements[line_compare][index]:
                                        found=found+1
                            line_compare=line_compare+1
                        if found > 0 and found < len(elements)-1:
                            line_compare=0
                            while line_compare < len(elements):
                                if line != line_compare:
                                    if re.search('\\?$|\\*$',elements[line][index]) and elements[line][index] not in elements[line_compare]:
                                        elements[line_compare].insert(index,elements[line][index])
                                        index=-1
                                line_compare=line_compare+1
                        line=line+1
                    index=index+1

                index=0
                while index < max_size:                
                    line=0
                    while line < len(elements):
                        line_compare=0
                        found=0
                        while line_compare < len(elements):
                            if line != line_compare:
                                if index < len(elements[line]) and index < len(elements[line_compare]):
                                    if elements[line][index] != elements[line_compare][index]:
                                        found=found+1
                            line_compare=line_compare+1
                        if found < len(elements):
                            line_compare=0
                            while line_compare < len(elements):
                                if line != line_compare:
                                    if  re.search('\\?$|\\*$',elements[line][index]) and elements[line][index] not in elements[line_compare]:
                                        elements[line_compare].insert(index,elements[line][index])
                                        index=-1
                                line_compare=line_compare+1
                        line=line+1
                    index=index+1

                for elem in elements:
                    if elem not in retour:
                        retour.append(elem)

                line=0
 
                max_line=len(retour)
                while line < max_line:
                    retour[line]=','.join(retour[line])
                    line=line+1

                if len(retour) > 1:
                    i=0
                    groups=''
                    for elem in retour:
                        groups=groups+'('+elem+')|'
                    retour=groups[:-1]
                else:
                    retour=retour[0]

                    if is_PCDATA:
                        retour='#PCDATA'+'|'+retour 

                retour='<!ELEMENT '+tag+' ('+retour+')>'
            
            else:
                if is_PCDATA:
                    retour='#PCDATA'
                    retour='<!ELEMENT '+tag+' ('+retour+')>'
                else:
                    retour='<!ELEMENT '+tag+' EMPTY>'
            
            return retour
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    def generate_doctype(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            retour=[]
            tags=[]

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::generate_doctype -> element => '+self.__tree.getroot().tag)    

            for elem in self.__tree.getroot().iter():
                if str(elem.tag) not in tags:
                    tags.append(str(elem.tag))
            
            for tag in tags:
                element=self.__doctype_tag(tag=tag)
                retour.append(element)

                for line in self.__doctype_attributes(tag=tag):
                    retour.append(line)
 
            str_retour=''
            for elem in retour:
                str_retour=str_retour+'\n'+elem
            str_retour=str_retour[1:]

            return str_retour
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)


    def __set_path(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            if self._logger is not None:
                self._logger.debug('NetData@'+ self._id +' ::__get_path -> path read only parameter')            
            
            exception={
                'property':'path',
                'error':'read only property',
                'message':'path is only reachable as read only property'
                }
                        
            if self._logger is not None:
                self._logger.error('NetData@'+ self._id +' ::__get_data -> path read only parameter')
            
            raise NetExceptionData(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    def __get_path(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__set_path -> element => '+self.__tree.getroot().tag)                
            
            parent=self.__tree.getroot()
            while parent.getparent() is not None:
                parent=parent.getparent()

            tree=etree.ElementTree(parent)
            retour=str(tree.getelementpath(self.__tree.getroot()))
            if retour != '.':
                retour=retour+'/.'

            retour='/'+str(parent.tag)+'/'+str(retour)

            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    path=property(__get_path,__set_path)

    def __set_docinfo(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            if self._logger is not None:
                self._logger.debug('NetData@'+ self._id +' ::__get_docinfo -> docinfo read only parameter')            
            
            exception={
                'property':'docinfo',
                'error':'read only property',
                'message':'docinfo is only reachable as read only property'
                }
                        
            if self._logger is not None:
                self._logger.error('NetData@'+ self._id +' ::__get_data -> docinfo read only parameter')
            
            raise NetExceptionData(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    def __get_docinfo(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__set_docinfo -> element => '+self.__tree.getroot().tag)                

            return self.__tree.docinfo
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    docinfo=property(__get_docinfo,__set_docinfo)

    def __set_attributes(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__set_attributes -> attributes read only property')            
            
            exception={
                'property':'attributes',
                'error':'read only property',
                'message':'attributes is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetData@'+ self._id + ' ::__set_attributes -> attributes read only property')
                            
            raise NetExceptionData(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    def __get_attributes(self,*param_no_named,**param_named):
        @NetClassParameterUnique(element=etree._Element,result=dict,path=list)
        def __get_attributes_element(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                element=dict_param_named['element']
                result=dict_param_named['result']
                path=dict_param_named['path']
                index=result

                for elem in path:
                    index=index[elem]

                tag=str(element.tag)
                if tag not in index.keys():
                    index[tag]=NetData.DataDictYAML(root=self,dictionary={})

                index=index[tag]
                path.append(tag)

                if 'attrib' not in index.keys():
                    index['attrib']=list()
                
                for attribute in element.attrib.keys():
                    if attribute not in index['attrib']:
                        index['attrib'].append(attribute)

                for child in element:
                    __get_attributes_element(self,element=child,result=result,path=path.copy())

            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionData(self._logger,exception) 
        @NetClassParameterUnique(result=dict)
        def __get_attributes_format(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                result=dict_param_named['result']

                if 'attrib' in result.keys():
                    attrib=re.sub('^\\[','',str(result['attrib']))
                    attrib=re.sub('\\]$','',attrib)
                    attrib=re.sub("'","",attrib)
                    attrib=re.sub(" *, *","|",attrib)
                    attrib='[ '+attrib+' ]'


                    result['attrib']=attrib

                    for key in result.keys():
                        if key != 'attrib':
                            __get_attributes_format(self,result=result[key])

            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionData(self._logger,exception) 

        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__get_attributes -> element => '+self.__tree.getroot().tag) 

            retour=NetData.DataDictYAML(root=self,dictionary={})

            __get_attributes_element(self,element=self.__tree.getroot(),result=retour,path=[])
            __get_attributes_format(self,result=retour[list(retour.keys())[0]])

            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    attributes=property(__get_attributes,__set_attributes)   

    def __set_tags(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__set_tags -> tags read only property')            
            
            exception={
                'property':'tags',
                'error':'read only property',
                'message':'tags is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetData@'+ self._id + ' ::__set_tags -> tags read only property')
                            
            raise NetExceptionData(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    def __get_tags(self,*param_no_named,**param_named):
 
        @NetClassParameterUnique(element=etree._Element,result=dict,path=list)
        def __get_tags_element(self,*param_no_named,**param_named):
            try:
                list_param_no_named=list(param_no_named)
                dict_param_named=dict(param_named)
                
                element=dict_param_named['element']
                result=dict_param_named['result']
                path=dict_param_named['path']
                index=result

                for elem in path:
                    index=index[elem]

                tag=str(element.tag)
                if tag not in index.keys():
                    index[tag]=NetData.DataDictYAML(root=self,dictionary={})

                index=index[tag]
                path.append(tag)

                if len(element) > 0:
                    for child in element:
                        __get_tags_element(self,element=child,result=result,path=path.copy())
                else:
                    index[tag]=''

            except Exception as exception:
                if issubclass(type(exception),NetException):
                    exception.logger=self._logger
                    raise exception
                else:            
                    raise NetExceptionData(self._logger,exception) 
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__get_tags -> element => '+self.__tree.getroot().tag) 

            retour=NetData.DataDictYAML(root=self,dictionary={})

            __get_tags_element(self,element=self.__tree.getroot(),result=retour,path=[])

            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    tags=property(__get_tags,__set_tags)  

    @NetClassParameterUnique(object)
    def __set_data(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            obj=list_param_no_named[0]

            attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
            text_prefix=self._config['xmltodict']['parser']['cdata_key']

            text_prefix=self._str_specials_characters_as_str(chain=text_prefix)
            attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__set_data -> '+'tree => '+str(obj))              

            if type(obj) is bytes:
                obj=obj.decode(self._config['default']['encoding'])

            if type(obj) is dict:
                
                keys=self._dict_get_all_keys(dictionary=obj)
                is_xmltodict=False
  
                for key in keys:
                    if re.search('^'+attribut_prefix+'|^'+text_prefix+'$',key):
                        is_xmltodict=True
                if is_xmltodict:
                    self.xmltodict=obj
                else:
                    self.json=obj
        
            elif issubclass(type(obj),etree._Element):
                if self._config['default']['mode'] == 'xml':
                    self.xml=obj
                elif self._config['default']['mode'] == 'html':
                    self.html=obj
          
            elif type(obj) is etree._ElementTree:
                if self._config['default']['mode'] == 'xml':
                    self.xml=obj.getroot()
                elif self._config['default']['mode'] == 'html':
                    self.html=obj.getroot()

            elif issubclass(type(type(obj)),NetTypeData):  
                if self._config['default']['mode'] == 'xml':
                    self.xml=obj.xml
                elif self._config['default']['mode'] == 'html':
                    self.html=obj.html              

            elif type(obj) is str:
                if os.path.isfile(obj):
                    self.load_data(file=obj)
                else:
                    try:
                        dictionary=json.loads(obj)
                        keys=self._dict_get_all_keys(dictionary=dictionary)
                        is_xmltodict=False
        
                        for key in keys:
                            if re.search('^'+attribut_prefix+'|^'+text_prefix+'$',key):
                                is_xmltodict=True
                        if is_xmltodict:
                            self.xmltodict=dictionary
                        else:
                            self.json=dictionary    

                    except json.decoder.JSONDecodeError as ex:
                        
                        dictionary=yaml.safe_load(obj)
                        if type(dictionary) is dict:
                            is_xmltodict=False
            
                            for key in keys:
                                if re.search('^'+attribut_prefix+'|^'+text_prefix+'$',key):
                                    is_xmltodict=True
                            if is_xmltodict:
                                self.xmltodict=dictionary
                            else:
                                self.json=dictionary  
                        else:
                            if self._config['default']['mode'] == 'xml':
                                self.xml=obj
                            elif self._config['default']['mode'] == 'html':
                                self.html=obj                          
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    def __get_data(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            if self._logger is not None:
                self._logger.debug('NetData@'+ self._id +' ::__get_data -> logger write only parameter')            
            
            exception={
                'property':'data',
                'error':'write only property',
                'message':'data is only reachable as write only property'
                }
                        
            if self._logger is not None:
                self._logger.error('NetData@'+ self._id +' ::__get_data -> logger write only parameter')
            
            raise NetExceptionData(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    data=property(__get_data,__set_data)

    @NetClassParameterCombine([NetClassParameterUnique(str),NetClassParameterUnique(etree._Element),NetClassParameterUnique(NetTypeData)])
    def __set_xml(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            xml=list_param_no_named[0]
            current_element=None
            element=None

            if type(xml) is NetData.DataElement:
                element=xml
            elif issubclass(type(type(xml)),NetTypeData):
                element=xml.xml
            else:
                parser_tostring=self._parse_original(source=self._config['xml']['tostring'])
                
                if issubclass(type(xml),etree._Element):
                    current_element=xml
                    xml=etree.tostring(xml,**parser_tostring).decode(self._config['xml']['tostring']['encoding'])
                else:
                    if self.__tree is not None:
                        current_element=self.__tree.getroot()
                    
                    if re.search('\\.xml$',xml) and os.path.isfile(xml):
                        xml=self._str_load_file(file=xml,timeout=self._lock_timeout)

                parser_xml=self._parse_original(source=self._config['xml']['parser'])
                
                if self._logger is not None:
                    self._logger.debug('NetData@'+ self._id +' ::__set_xml -> '+'xml => '+xml+' || '+'parser_xml => '+str(parser_xml) ) 

                parser_lookup = etree.ElementDefaultClassLookup(element=NetData.DataElement)
                parser_xml['parser']=etree.XMLParser(**self._config['xml']['parser']['parser'])
                parser_xml['parser'].set_element_class_lookup(parser_lookup)

                xml=re.sub('[^>]*$','',re.sub('^[^<]*','',xml))
                xml=xml.encode(self._config['xml']['tostring']['encoding'])

                element=etree.XML(xml,**parser_xml)

            if not hasattr(element, 'root'):
                element.init(*param_no_named,**param_named)
                element.root=self

            for elem in element.iter():
                if type(elem) is NetData.DataElement:
                    if not hasattr(elem, 'root'):
                        elem.init(*param_no_named,**param_named)
                        elem.root=self                    
                                            
            self.__tree=etree.ElementTree(element)
            
            if current_element is not None:
                parent=current_element.getparent()
                if parent is not None:
                    parent.insert(parent.index(current_element)+1,element)
                    parent.remove(current_element)

            self._config['default']['mode'] = 'xml'

            if self._logger is not None:
                self._logger.info('NetData@'+ self._id +' ::__set_xml -> Success'+' || '+'tag => '+ str(self.__tree.getroot().tag))    
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    def __get_xml(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named) 
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__get_xml -> '+self.__tree.getroot().tag)               

            self._mode_print='xml'

            return self.__tree.getroot()
                
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    xml=property(__get_xml,__set_xml)

    @NetClassParameterCombine([NetClassParameterUnique(str),NetClassParameterUnique(etree._Element),NetClassParameterUnique(NetTypeData)])
    def __set_html(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            html=list_param_no_named[0]
            current_element=None
            element=None

            if type(html) is NetData.DataElement:
                element=html
            elif issubclass(type(type(html)),NetTypeData):
                element=html.html
            else:
                parser_tostring=self._parse_original(source=self._config['html']['tostring']) 

                if issubclass(type(html),etree._Element):
                    current_element=html
                    html=etree.tostring(html,**parser_tostring).decode(self._config['html']['tostring']['encoding'])
                else:
                    if self.__tree is not None:
                        current_element=self.__tree.getroot()

                    if re.search('\\.html$',html) and os.path.isfile(html):
                        html=self._str_load_file(file=html,timeout=self._lock_timeout)              

                parser_html=self._parse_original(source=self._config['html']['parser'])
                
                if self._logger is not None:
                    self._logger.debug('NetData@'+ self._id +' ::__set_html -> '+'html => '+html+' || '+'parser_html => '+str(parser_html) ) 

                parser_lookup = etree.ElementDefaultClassLookup(element=NetData.DataElement)
                parser_html['parser']=etree.HTMLParser(**self._config['html']['parser']['parser'])
                parser_html['parser'].set_element_class_lookup(parser_lookup)

                html=re.sub('[^>]*$','',re.sub('^[^<]*','',html))
                html=html.encode(self._config['html']['tostring']['encoding'])

                element=etree.HTML(html,**parser_html)

            if not hasattr(element, 'root'):
                element.init(*param_no_named,**param_named)
                element.root=self

            for elem in element.iter():
                if type(elem) is NetData.DataElement:
                    if not hasattr(elem, 'root'):
                        elem.init(*param_no_named,**param_named)
                        elem.root=self                    
                                            
            self.__tree=etree.ElementTree(element)
            
            if current_element is not None:
                parent=current_element.getparent()
                if parent is not None:
                    parent.insert(parent.index(current_element)+1,element)
                    parent.remove(current_element)

            self._config['default']['mode'] = 'html'

            if self._logger is not None:
                self._logger.info('NetData@'+ self._id +' ::__set_html -> Success'+' || '+'tag => '+ str(element.tag))    
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    def __get_html(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named) 
            
            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__get_html -> '+self.__tree.getroot().tag)               
    
            self._mode_print='html'

            return self.__tree.getroot()
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    html=property(__get_html,__set_html)

    def _generate_xmltodict(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named) 
            
            parse_xmltodict=self._parse_original(source=self._config['xmltodict']['parser'])
            parse_xmltodict['dict_constructor']=dict
            
            parse_xmltostring=self._config['xml']['tostring']
                
            tree=etree.tostring(self.__tree.getroot(),**parse_xmltostring).decode(parse_xmltostring['encoding'])
            json=dict(xmltodict.parse(tree,**parse_xmltodict))

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::_generate_xmltodict -> json => '+str(json)+' || '+'xmltodict => '+str(parse_xmltodict)+' || '+'xmltostring => '+str(parse_xmltostring))               
                        
            return json
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterCombine([NetClassParameterUnique(str),NetClassParameterUnique(dict),NetClassParameterUnique(NetTypeData)])
    def __set_xmltodict(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            old_json_dict={}
            if self.__tree is not None:
                old_json_dict=self._generate_xmltodict(*param_no_named,**param_named)
            
            json_dict=list_param_no_named[0]

            if issubclass(type(json_dict),str):
                if re.search('\\.json$',json_dict) and os.path.isfile(json_dict):
                    json_dict=self._str_load_file(file=json_dict,timeout=self._lock_timeout)
            
                json_dict=json.loads(json_dict,encoding=self._config['xmltodict']['parser']['encoding'])
            
            elif issubclass(type(type(json_dict)),NetTypeData):
                json_dict={str(json_dict.xml.tag):json_dict.xmltodict}


            json_dict=self._parse_original(source=json_dict)     

            if self._logger is not None:
                self._logger.debug('NetData@'+ self._id +' ::__set_xmltodict -> '+'json_dict => '+str(json_dict))   

            if self._check_same_object(source1=old_json_dict,source2=json_dict) is False:
                self._update_data_xmltodict(old_data_xmltodict=old_json_dict,new_data_xmltodict=json_dict)

            if self._logger is not None:
                self._logger.info('NetData@'+ self._id +' ::__set_xmltodict -> Success'+' || '+'json_dict => '+str(json_dict))    
           
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    def __get_xmltodict(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named) 
            
            parse_xmltodict=self._parse_original(source=self._config['xmltodict']['parser'])
            parse_xmltodict['dict_constructor']=dict
            
            parse_xmltostring=self._config['xml']['tostring']
                
            tree=etree.tostring(self.__tree.getroot(),**parse_xmltostring).decode(parse_xmltostring['encoding'])
            json=self._parse_data_xmltodict(source=dict(xmltodict.parse(tree,**parse_xmltodict)))

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__get_xmltodict -> json => '+str(json)+' || '+'xmltodict => '+str(parse_xmltodict)+' || '+'xmltostring => '+str(parse_xmltostring))               

            if len(json.keys()) > 0:
                json=json[list(json.keys())[0]]

            return json
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    xmltodict=property(__get_xmltodict,__set_xmltodict)

    def _generate_json(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named) 
            
            parse_xmltodict=self._parse_original(source=self._config['xmltodict']['parser'])
            parse_xmltodict['dict_constructor']=dict
            parse_xmltodict['attr_prefix']=''

            parse_xmltostring=self._config['xml']['tostring']
                
            tree=etree.tostring(self.__tree.getroot(),**parse_xmltostring).decode(parse_xmltostring['encoding'])
            json=dict(xmltodict.parse(tree,**parse_xmltodict))

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::_generate_json -> json => '+str(json)+' || '+'xmltodict => '+str(parse_xmltodict)+' || '+'xmltostring => '+str(parse_xmltostring))               
                        
            return json
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception)
    @NetClassParameterUnique(data=object)                
    def _parse_json(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            

            data=dict_param_named['data']

            attribut_prefix=self._config['xmltodict']['parser']['attr_prefix']
            text_prefix=self._config['xmltodict']['parser']['cdata_key']

            text_prefix=self._str_specials_characters_as_str(chain=text_prefix)
            attribut_prefix=self._str_specials_characters_as_str(chain=attribut_prefix)

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::_parse_json -> data => '+str(data))    
            
            if type(data) is list:
                retour=[]
                for elem in data:
                    retour.append(self._parse_json(data=elem))
            
            elif type(data) is dict:
                retour={}
                for key in data.keys():
                    if re.search('^'+attribut_prefix,key) is None and re.search('^'+text_prefix+'$',key) is None:
                        if type(data[key]) is not dict and type(data[key]) is not list:
                            retour[attribut_prefix+key]=data.copy()[key]
                        else:
                            retour[key]=self._parse_json(data=data[key])
                    else:
                        retour[key]=data.copy()[key]
            else:
                retour=data
                        
            return retour
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    @NetClassParameterCombine([NetClassParameterUnique(str),NetClassParameterUnique(dict),NetClassParameterUnique(NetTypeData)])
    def __set_json(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            old_json_dict={}
            if self.__tree is not None:
                old_json_dict=self._generate_json(*param_no_named,**param_named)
            
            json_dict=list_param_no_named[0]

            if issubclass(type(json_dict),str):
                if re.search('\\.json$',json_dict) and os.path.isfile(json_dict):
                    json_dict=self._str_load_file(file=json_dict,timeout=self._lock_timeout)

                json_dict=json.loads(json_dict,encoding=self._config['xmltodict']['parser']['encoding'])
            
            elif issubclass(type(type(json_dict)),NetTypeData):
                json_dict={str(json_dict.xml.tag):json_dict.json}              

            json_dict=self._parse_original(source=json_dict)     
  
            if self._logger is not None:
                self._logger.debug('NetData@'+ self._id +' ::__set_config -> '+'json_dict => '+str(json_dict))   

            if self._check_same_object(source1=old_json_dict,source2=json_dict) is False:
                self._update_data_json(old_data_json=old_json_dict,new_data_json=json_dict)

            if self._logger is not None:
                self._logger.info('NetData@'+ self._id +' ::__set_json -> Success'+' || '+'json_dict => '+str(json_dict))    
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    def __get_json(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named) 
            
            parse_xmltodict=self._parse_original(source=self._config['xmltodict']['parser'])
            parse_xmltodict['dict_constructor']=dict
            parse_xmltodict['attr_prefix']=''
         
            parse_xmltostring=self._config['xml']['tostring']
                
            tree=etree.tostring(self.__tree.getroot(),**parse_xmltostring).decode(parse_xmltostring['encoding'])
            json=self._parse_data_json(source=dict(xmltodict.parse(tree,**parse_xmltodict)))

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__get_json -> json => '+str(json)+' || '+'xmltodict => '+str(parse_xmltodict)+' || '+'xmltostring => '+str(parse_xmltostring))               

            if len(json.keys()) > 0:
                json=json[list(json.keys())[0]]

            return json
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    json=property(__get_json,__set_json)

    @NetClassParameterCombine([NetClassParameterUnique(str),NetClassParameterUnique(dict),NetClassParameterUnique(NetTypeData)])
    def __set_yaml(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            old_yaml_dict={}
            if self.__tree is not None:
                if self._config['yaml']['mode'] == 'xmltodict':
                    old_yaml_dict=self._generate_xmltodict(*param_no_named,**param_named)
                elif self._config['yaml']['mode'] == 'json':
                    old_yaml_dict=self._generate_json(*param_no_named,**param_named)

            yaml_dict=list_param_no_named[0]

            if issubclass(type(yaml_dict),str):
                if re.search('\\.yml$',yaml_dict) and os.path.isfile(yaml_dict):
                    yaml_dict=self._str_load_file(file=yaml_dict,timeout=self._lock_timeout)

                yaml_dict=yaml.safe_load(yaml_dict)
            
            elif issubclass(type(type(yaml_dict)),NetTypeData):
                yaml_dict={str(yaml_dict.xml.tag):yaml_dict.yaml}                                

            yaml_dict=self._parse_original(source=yaml_dict)     

            if self._logger is not None:
                self._logger.debug('NetData@'+ self._id +' ::__set_config -> '+'yaml_dict => '+str(yaml_dict))   

            if self._check_same_object(source1=old_yaml_dict,source2=yaml_dict) is False:
                self._update_data_yaml(old_data_yaml=old_yaml_dict,new_data_yaml=yaml_dict)

            if self._logger is not None:
                self._logger.info('NetData@'+ self._id +' ::__set_yaml -> Success'+' || '+'yaml_dict => '+str(yaml_dict))    
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    def __get_yaml(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named) 
            
            parse_xmltodict=self._parse_original(source=self._config['xmltodict']['parser'])
            parse_xmltodict['dict_constructor']=dict

            if self._config['yaml']['mode'] == 'json':
                parse_xmltodict['attr_prefix']=''

            parse_xmltostring=self._config['xml']['tostring']
            tree=etree.tostring(self.__tree.getroot(),**parse_xmltostring).decode(parse_xmltostring['encoding'])
            data_yaml=self._parse_data_yaml(source=dict(xmltodict.parse(tree,**parse_xmltodict)))

            if self._logger != None:
                self._logger.debug('NetData@'+ self._id + ' ::__get_yaml -> data_yaml => '+str(data_yaml)+' || '+'xmltodict => '+str(parse_xmltodict)+' || '+'xmltostring => '+str(parse_xmltostring))               

            if len(data_yaml.keys()) > 0:
                data_yaml=data_yaml[list(data_yaml.keys())[0]]

            return data_yaml
        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionData(self._logger,exception) 
    yaml=property(__get_yaml,__set_yaml)
    