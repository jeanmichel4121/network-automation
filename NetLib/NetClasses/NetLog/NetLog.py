# pylint: disable=unused-variable
__author__ = 'Jean-Michel Cuvelier'

import sys

import NetLib
from NetLib.NetClasses.NetClassParatemter.NetClassParameter import NetClassParameterUnique,NetClassParameterContains
from NetLib.NetClasses.NetException.NetException import NetException
from NetLib.NetClasses.NetConfig.NetConfigFile.NetConfigFile import NetTypeConfigFile,NetTypeExcpetionConfigFile,NetExceptionConfigFile,NetConfigFile

import logging
from logging.config import dictConfig
import os
import json

class NetTypeLog(NetTypeConfigFile):
    def __new__(self,*param_no_named,**param_named):
        return super(NetTypeLog,self).__new__(self,*param_no_named,**param_named)

class NetTypeExceptionLog(NetTypeExcpetionConfigFile):
    def __new__( self,*param_no_named,**param_named):
        return super(NetTypeExceptionLog,self).__new__(self,*param_no_named,**param_named)

class NetExceptionLog(NetExceptionConfigFile,metaclass=NetTypeExceptionLog):
    __metaclass__=NetTypeExceptionLog
    
    def __init__(self,*param_no_named,**param_named):       
        super(NetExceptionLog,self).__init__(*param_no_named,**param_named)
        self._config['exception']['content']['class_name']='NetLog'

    def __str__(self):
        return super(NetExceptionLog,self).__str__()
     
class NetLog(NetConfigFile,metaclass=NetTypeLog):
    __metaclass__=NetTypeLog
    
    __DEFAULT_CONFIG={
        "version": 1,
        "disable_existing_loggers": True,
        "filters": {
            "message_regex": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Message_Regex",
                "regex": "."
            },
            "message_regex_reverse": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Message_Regex_Reverse",
                "regex": "^NetException"
            },
            "name_regex": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Name_Regex",
                "regex": "."
            },
            "name_regex_reverse": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Name_Regex_Reverse",
                "regex": "."
            },
            "function_regex": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Function_Regex",
                "regex": "."
            },
            "function_regex_reverse": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Function_Regex_Reverse",
                "regex": "."
            },
            "thread_regex": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Thread_Regex",
                "regex": "."
            },
            "thread_regex_reverse": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Thread_Regex_Reverse",
                "regex": "."
            },
            "process_regex": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Process_Regex",
                "regex": "."
            },
            "process_regex_reverse": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Process_Regex_Reverse",
                "regex": "."
            },
            "filename_regex": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_FileName_Regex",
                "regex": "."
            },
            "filename_regex_reverse": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_FileName_Regex_Reverse",
                "regex": "."
            },
            "pathname_regex": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_PathName_Regex",
                "regex": "."
            },
            "pathname_regex_reverse": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_PathName_Regex_Reverse",
                "regex": "."
            },
            "line_number_regex": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Line_Number_Regex",
                "regex": "."
            },
            "line_number_regex_reverse": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Line_Number_Regex_Reverse",
                "regex": "."
            },
            "lvl_debug_only": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Lvl_Debug_Only"
            },
            "lvl_debug_skip": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Lvl_Debug_Skip"
            },
            "lvl_informal_only": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Lvl_Informal_Only"
            },
            "lvl_informal_skip": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Lvl_Informal_Skip"
            },
            "lvl_warning_only": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Lvl_Warning_Only"
            },
            "lvl_warning_skip": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Lvl_Warning_Skip"
            },
            "lvl_error_only": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Lvl_Error_Only"
            },
            "lvl_error_skip": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Lvl_Error_Skip"
            },
            "lvl_critical_only": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Lvl_Critical_Only"
            },
            "lvl_critical_skip": {
                "()": "NetLib.NetClasses.NetLog.NetLogFilter.NetFilter_Lvl_Critical_Skip"
            }
        },
        "formatters": {
            "colored_lossless_multi_threads": {
                "format": "%(asctime)s - %(levelname)s - <LOGGER %(name)s> - <PID %(process)d:%(processName)s> - <TID %(thread)d:%(threadName)s> - %(pathname)s => %(funcName)s():%(lineno)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S",
                "()": "coloredlogs.ColoredFormatter",
                "level_styles": {
                    "debug": {
                    "color": "yellow",
                    "faint": True
                    },
                    "info": {
                    "color": "cyan"
                    },
                    "warning": {
                    "color": "yellow"
                    },
                    "error": {
                    "color": "red"
                    },
                    "critical": {
                    "color": "red",
                    "bold": True
                    }
                },
                "field_styles": {
                    "process": {
                    "color": "red",
                    "bold": True
                    },
                    "processName": {
                    "color": "red",
                    "bold": True
                    },
                    "thread": {
                    "color": "red"
                    },
                    "threadName": {
                    "color": "red"
                    },
                    "pathname": {
                    "color": "magenta"
                    },
                    "funcName": {
                    "color": "magenta",
                    "bold": True
                    },
                    "lineno": {
                    "color": "magenta",
                    "bold": True
                    },
                    "asctime": {
                    "color": "green"
                    },
                    "hostname": {
                    "color": "magenta"
                    },
                    "levelname": {
                    "color": "black",
                    "bold": True
                    },
                    "name": {
                    "color": "blue"
                    },
                    "programname": {
                    "color": "cyan"
                    },
                    "username": {
                    "color": "yellow"
                    }
                }
            },
            "colored_lossless_multi_process": {
                "format": "%(asctime)s - %(levelname)s - <LOGGER %(name)s> - <PID %(process)d:%(processName)s> - %(pathname)s => %(funcName)s():%(lineno)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S",
                "()": "coloredlogs.ColoredFormatter",
                "level_styles": {
                    "debug": {
                    "color": "yellow",
                    "faint": True
                    },
                    "info": {
                    "color": "cyan"
                    },
                    "warning": {
                    "color": "yellow"
                    },
                    "error": {
                    "color": "red"
                    },
                    "critical": {
                    "color": "red",
                    "bold": True
                    }
                },
                "field_styles": {
                    "process": {
                    "color": "red",
                    "bold": True
                    },
                    "processName": {
                    "color": "red",
                    "bold": True
                    },
                    "thread": {
                    "color": "red"
                    },
                    "threadName": {
                    "color": "red"
                    },
                    "pathname": {
                    "color": "magenta"
                    },
                    "funcName": {
                    "color": "magenta",
                    "bold": True
                    },
                    "lineno": {
                    "color": "magenta",
                    "bold": True
                    },
                    "asctime": {
                    "color": "green"
                    },
                    "hostname": {
                    "color": "magenta"
                    },
                    "levelname": {
                    "color": "black",
                    "bold": True
                    },
                    "name": {
                    "color": "blue"
                    },
                    "programname": {
                    "color": "cyan"
                    },
                    "username": {
                    "color": "yellow"
                    }
                }
            },
            "colored_lossless_single_process": {
                "format": "%(asctime)s - %(levelname)s - <LOGGER %(name)s> - %(pathname)s => %(funcName)s():%(lineno)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S",
                "()": "coloredlogs.ColoredFormatter",
                "level_styles": {
                    "debug": {
                    "color": "yellow",
                    "faint": True
                    },
                    "info": {
                    "color": "cyan"
                    },
                    "warning": {
                    "color": "yellow"
                    },
                    "error": {
                    "color": "red"
                    },
                    "critical": {
                    "color": "red",
                    "bold": True
                    }
                },
                "field_styles": {
                    "process": {
                    "color": "red",
                    "bold": True
                    },
                    "processName": {
                    "color": "red",
                    "bold": True
                    },
                    "thread": {
                    "color": "red"
                    },
                    "threadName": {
                    "color": "red"
                    },
                    "pathname": {
                    "color": "magenta"
                    },
                    "funcName": {
                    "color": "magenta",
                    "bold": True
                    },
                    "lineno": {
                    "color": "magenta",
                    "bold": True
                    },
                    "asctime": {
                    "color": "green"
                    },
                    "hostname": {
                    "color": "magenta"
                    },
                    "levelname": {
                    "color": "black",
                    "bold": True
                    },
                    "name": {
                    "color": "blue"
                    },
                    "programname": {
                    "color": "cyan"
                    },
                    "username": {
                    "color": "yellow"
                    }
                }
            },
            "colored_loss_more_multi_threads": {
                "format": "%(asctime)s - %(levelname)s - <PID %(process)d:%(processName)s> - <TID %(thread)d:%(threadName)s> - %(pathname)s => %(funcName)s():%(lineno)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S",
                "()": "coloredlogs.ColoredFormatter",
                "level_styles": {
                    "debug": {
                    "color": "yellow",
                    "faint": True
                    },
                    "info": {
                    "color": "cyan"
                    },
                    "warning": {
                    "color": "yellow"
                    },
                    "error": {
                    "color": "red"
                    },
                    "critical": {
                    "color": "red",
                    "bold": True
                    }
                },
                "field_styles": {
                    "process": {
                    "color": "red",
                    "bold": True
                    },
                    "processName": {
                    "color": "red",
                    "bold": True
                    },
                    "thread": {
                    "color": "red"
                    },
                    "threadName": {
                    "color": "red"
                    },
                    "pathname": {
                    "color": "magenta"
                    },
                    "funcName": {
                    "color": "magenta",
                    "bold": True
                    },
                    "lineno": {
                    "color": "magenta",
                    "bold": True
                    },
                    "asctime": {
                    "color": "green"
                    },
                    "hostname": {
                    "color": "magenta"
                    },
                    "levelname": {
                    "color": "black",
                    "bold": True
                    },
                    "name": {
                    "color": "blue"
                    },
                    "programname": {
                    "color": "cyan"
                    },
                    "username": {
                    "color": "yellow"
                    }
                }
            },
            "colored_loss_more_multi_process": {
                "format": "%(asctime)s - %(levelname)s - <PID %(process)d:%(processName)s> - %(pathname)s => %(funcName)s():%(lineno)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S",
                "()": "coloredlogs.ColoredFormatter",
                "level_styles": {
                    "debug": {
                    "color": "yellow",
                    "faint": True
                    },
                    "info": {
                    "color": "cyan"
                    },
                    "warning": {
                    "color": "yellow"
                    },
                    "error": {
                    "color": "red"
                    },
                    "critical": {
                    "color": "red",
                    "bold": True
                    }
                },
                "field_styles": {
                    "process": {
                    "color": "red",
                    "bold": True
                    },
                    "processName": {
                    "color": "red",
                    "bold": True
                    },
                    "thread": {
                    "color": "red"
                    },
                    "threadName": {
                    "color": "red"
                    },
                    "pathname": {
                    "color": "magenta"
                    },
                    "funcName": {
                    "color": "magenta",
                    "bold": True
                    },
                    "lineno": {
                    "color": "magenta",
                    "bold": True
                    },
                    "asctime": {
                    "color": "green"
                    },
                    "hostname": {
                    "color": "magenta"
                    },
                    "levelname": {
                    "color": "black",
                    "bold": True
                    },
                    "name": {
                    "color": "blue"
                    },
                    "programname": {
                    "color": "cyan"
                    },
                    "username": {
                    "color": "yellow"
                    }
                }
            },
            "colored_loss_more_single_process": {
                "format": "%(asctime)s - %(levelname)s - %(pathname)s => %(funcName)s():%(lineno)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S",
                "()": "coloredlogs.ColoredFormatter",
                "level_styles": {
                    "debug": {
                    "color": "yellow",
                    "faint": True
                    },
                    "info": {
                    "color": "cyan"
                    },
                    "warning": {
                    "color": "yellow"
                    },
                    "error": {
                    "color": "red"
                    },
                    "critical": {
                    "color": "red",
                    "bold": True
                    }
                },
                "field_styles": {
                    "process": {
                    "color": "red",
                    "bold": True
                    },
                    "processName": {
                    "color": "red",
                    "bold": True
                    },
                    "thread": {
                    "color": "red"
                    },
                    "threadName": {
                    "color": "red"
                    },
                    "pathname": {
                    "color": "magenta"
                    },
                    "funcName": {
                    "color": "magenta",
                    "bold": True
                    },
                    "lineno": {
                    "color": "magenta",
                    "bold": True
                    },
                    "asctime": {
                    "color": "green"
                    },
                    "hostname": {
                    "color": "magenta"
                    },
                    "levelname": {
                    "color": "black",
                    "bold": True
                    },
                    "name": {
                    "color": "blue"
                    },
                    "programname": {
                    "color": "cyan"
                    },
                    "username": {
                    "color": "yellow"
                    }
                }
            },
            "colored_loss_fully_multi_threads": {
                "format": "%(asctime)s - %(levelname)s - <PID %(process)d:%(processName)s> - <TID %(thread)d:%(threadName)s> - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S",
                "()": "coloredlogs.ColoredFormatter",
                "level_styles": {
                    "debug": {
                    "color": "yellow",
                    "faint": True
                    },
                    "info": {
                    "color": "cyan"
                    },
                    "warning": {
                    "color": "yellow"
                    },
                    "error": {
                    "color": "red"
                    },
                    "critical": {
                    "color": "red",
                    "bold": True
                    }
                },
                "field_styles": {
                    "process": {
                    "color": "red",
                    "bold": True
                    },
                    "processName": {
                    "color": "red",
                    "bold": True
                    },
                    "thread": {
                    "color": "red"
                    },
                    "threadName": {
                    "color": "red"
                    },
                    "pathname": {
                    "color": "magenta"
                    },
                    "funcName": {
                    "color": "magenta",
                    "bold": True
                    },
                    "lineno": {
                    "color": "magenta",
                    "bold": True
                    },
                    "asctime": {
                    "color": "green"
                    },
                    "hostname": {
                    "color": "magenta"
                    },
                    "levelname": {
                    "color": "black",
                    "bold": True
                    },
                    "name": {
                    "color": "blue"
                    },
                    "programname": {
                    "color": "cyan"
                    },
                    "username": {
                    "color": "yellow"
                    }
                }
            },
            "colored_loss_fully_multi_process": {
                "format": "%(asctime)s - %(levelname)s - <PID %(process)d:%(processName)s> - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S",
                "()": "coloredlogs.ColoredFormatter",
                "level_styles": {
                    "debug": {
                    "color": "yellow",
                    "faint": True
                    },
                    "info": {
                    "color": "cyan"
                    },
                    "warning": {
                    "color": "yellow"
                    },
                    "error": {
                    "color": "red"
                    },
                    "critical": {
                    "color": "red",
                    "bold": True
                    }
                },
                "field_styles": {
                    "process": {
                    "color": "red",
                    "bold": True
                    },
                    "processName": {
                    "color": "red",
                    "bold": True
                    },
                    "thread": {
                    "color": "red"
                    },
                    "threadName": {
                    "color": "red"
                    },
                    "pathname": {
                    "color": "magenta"
                    },
                    "funcName": {
                    "color": "magenta",
                    "bold": True
                    },
                    "lineno": {
                    "color": "magenta",
                    "bold": True
                    },
                    "asctime": {
                    "color": "green"
                    },
                    "hostname": {
                    "color": "magenta"
                    },
                    "levelname": {
                    "color": "black",
                    "bold": True
                    },
                    "name": {
                    "color": "blue"
                    },
                    "programname": {
                    "color": "cyan"
                    },
                    "username": {
                    "color": "yellow"
                    }
                }
            },
            "colored_loss_fully_single_process": {
                "format": "%(asctime)s - %(levelname)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S",
                "()": "coloredlogs.ColoredFormatter",
                "level_styles": {
                    "debug": {
                    "color": "yellow",
                    "faint": True
                    },
                    "info": {
                    "color": "cyan"
                    },
                    "warning": {
                    "color": "yellow"
                    },
                    "error": {
                    "color": "red"
                    },
                    "critical": {
                    "color": "red",
                    "bold": True
                    }
                },
                "field_styles": {
                    "process": {
                    "color": "red",
                    "bold": True
                    },
                    "processName": {
                    "color": "red",
                    "bold": True
                    },
                    "thread": {
                    "color": "red"
                    },
                    "threadName": {
                    "color": "red"
                    },
                    "pathname": {
                    "color": "magenta"
                    },
                    "funcName": {
                    "color": "magenta",
                    "bold": True
                    },
                    "lineno": {
                    "color": "magenta",
                    "bold": True
                    },
                    "asctime": {
                    "color": "green"
                    },
                    "hostname": {
                    "color": "magenta"
                    },
                    "levelname": {
                    "color": "black",
                    "bold": True
                    },
                    "name": {
                    "color": "blue"
                    },
                    "programname": {
                    "color": "cyan"
                    },
                    "username": {
                    "color": "yellow"
                    }
                }
            },
            "colored_date_message": {
                "format": "%(asctime)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S",
                "()": "coloredlogs.ColoredFormatter",
                "level_styles": {
                    "debug": {
                    "color": "yellow",
                    "faint": True
                    },
                    "info": {
                    "color": "cyan"
                    },
                    "warning": {
                    "color": "yellow"
                    },
                    "error": {
                    "color": "red"
                    },
                    "critical": {
                    "color": "red",
                    "bold": True
                    }
                },
                "field_styles": {
                    "process": {
                    "color": "red",
                    "bold": True
                    },
                    "processName": {
                    "color": "red",
                    "bold": True
                    },
                    "thread": {
                    "color": "red"
                    },
                    "threadName": {
                    "color": "red"
                    },
                    "pathname": {
                    "color": "magenta"
                    },
                    "funcName": {
                    "color": "magenta",
                    "bold": True
                    },
                    "lineno": {
                    "color": "magenta",
                    "bold": True
                    },
                    "asctime": {
                    "color": "green"
                    },
                    "hostname": {
                    "color": "magenta"
                    },
                    "levelname": {
                    "color": "black",
                    "bold": True
                    },
                    "name": {
                    "color": "blue"
                    },
                    "programname": {
                    "color": "cyan"
                    },
                    "username": {
                    "color": "yellow"
                    }
                }
            },
            "colored_single_message": {
                "format": "%(message)s",
                "()": "coloredlogs.ColoredFormatter",
                "level_styles": {
                    "debug": {
                    "color": "yellow",
                    "faint": True
                    },
                    "info": {
                    "color": "cyan"
                    },
                    "warning": {
                    "color": "yellow"
                    },
                    "error": {
                    "color": "red"
                    },
                    "critical": {
                    "color": "red",
                    "bold": True
                    }
                },
                "field_styles": {
                    "process": {
                    "color": "red",
                    "bold": True
                    },
                    "processName": {
                    "color": "red",
                    "bold": True
                    },
                    "thread": {
                    "color": "red"
                    },
                    "threadName": {
                    "color": "red"
                    },
                    "pathname": {
                    "color": "magenta"
                    },
                    "funcName": {
                    "color": "magenta",
                    "bold": True
                    },
                    "lineno": {
                    "color": "magenta",
                    "bold": True
                    },
                    "asctime": {
                    "color": "green"
                    },
                    "hostname": {
                    "color": "magenta"
                    },
                    "levelname": {
                    "color": "black",
                    "bold": True
                    },
                    "name": {
                    "color": "blue"
                    },
                    "programname": {
                    "color": "cyan"
                    },
                    "username": {
                    "color": "yellow"
                    }
                }
            },
            "lossless_multi_threads": {
                "format": "%(asctime)s - %(levelname)s - <LOGGER %(name)s> - <PID %(process)d:%(processName)s> - <TID %(thread)d:%(threadName)s> - %(pathname)s => %(funcName)s():%(lineno)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S"
            },
            "lossless_multi_process": {
                "format": "%(asctime)s - %(levelname)s - <LOGGER %(name)s> - <PID %(process)d:%(processName)s> - %(pathname)s => %(funcName)s():%(lineno)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S"
            },
            "lossless_single_process": {
                "format": "%(asctime)s - %(levelname)s - <LOGGER %(name)s> - %(pathname)s => %(funcName)s():%(lineno)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S"
            },
            "loss_more_multi_threads": {
                "format": "%(asctime)s - %(levelname)s - <PID %(process)d:%(processName)s> - <TID %(thread)d:%(threadName)s> - %(pathname)s => %(funcName)s():%(lineno)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S"
            },
            "loss_more_multi_process": {
                "format": "%(asctime)s - %(levelname)s - <PID %(process)d:%(processName)s> - %(pathname)s => %(funcName)s():%(lineno)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S"
            },
            "loss_more_single_process": {
                "format": "%(asctime)s - %(levelname)s - %(pathname)s => %(funcName)s():%(lineno)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S"
            },
            "loss_fully_multi_threads": {
                "format": "%(asctime)s - %(levelname)s - <PID %(process)d:%(processName)s> - <TID %(thread)d:%(threadName)s> - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S"
            },
            "loss_fully_multi_process": {
                "format": "%(asctime)s - %(levelname)s - <PID %(process)d:%(processName)s> - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S"
            },
            "loss_fully_single_process": {
                "format": "%(asctime)s - %(levelname)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S"
            },
            "date_message": {
                "format": "%(asctime)s - %(message)s",
                "datefmt": "%Y/%m/%d %H:%M:%S"
            },
            "single_message": {
                "format": "%(message)s"
            }
        },
        "handlers": {
            "prompt": {
                "class": "logging.StreamHandler",
                "level": 10,
                "filters": [
                    "lvl_informal_only",
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex",
                    "line_number_regex"
                ],
                "formatter": "colored_single_message",
                "stream": "ext://sys.stdout"
            },
            "console": {
                "class": "logging.StreamHandler",
                "level": 10,
                "filters": [
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex"
                ],
                "formatter": "colored_loss_fully_single_process",
                "stream": "ext://sys.stdout"
            },
            "syslog_hf01": {
                "class": "logging.handlers.SysLogHandler",
                "level": 20,
                "filters": [
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex"
                ],
                "formatter": "loss_more_single_process",
                "address": "('HOST', 1511 )"
            },
            "debug_file_handler": {
                "class": "logging.FileHandler",
                "level": 10,
                "filters": [
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex",
                    "lvl_debug_only"
                ],
                "formatter": "loss_more_single_process",
                "filename": ".//debug.log",
                "mode":"w",
                "encoding": "utf8"
            },
            "info_file_handler": {
                "class": "logging.FileHandler",
                "level": "INFO",
                "filters": [
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex",
                    "lvl_informal_only"
                ],
                "formatter": "loss_more_single_process",
                "filename": "info.log",
                "mode":"w",
                "encoding": "utf8"
            },
            "warn_file_handler": {
                "class": "logging.FileHandler",
                "level": 30,
                "filters": [
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex",
                    "lvl_warning_only"
                ],
                "formatter": "loss_more_single_process",
                "filename": ".//warn.log",
                "mode":"w",
                "encoding": "utf8"
            },
            "error_file_handler": {
                "class": "logging.FileHandler",
                "level": 40,
                "filters": [
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex",
                    "lvl_error_only"
                ],
                "formatter": "loss_more_single_process",
                "filename": ".//errors.log",
                "mode":"w",
                "encoding": "utf8"
            },
            "critical_file_handler": {
                "class": "logging.FileHandler",
                "level": 50,
                "filters": [
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex",
                    "lvl_critical_only"
                ],
                "formatter": "loss_more_single_process",
                "filename": ".//critical.log",
                "mode":"w",
                "encoding": "utf8"
            },
            "debug_rotating_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": 10,
                "filters": [
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex",
                    "lvl_debug_only"
                ],
                "formatter": "loss_more_single_process",
                "filename": ".//debug.log",
                "maxBytes": 10485760,
                "mode":"a",
                "backupCount": 20,
                "encoding": "utf8"
            },
            "info_rotating_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "filters": [
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex",
                    "lvl_informal_only"
                ],
                "formatter": "loss_more_single_process",
                "filename": "info.log",
                "maxBytes": 10485760,
                "mode":"a",
                "backupCount": 20,
                "encoding": "utf8"
            },
            "warn_rotating_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": 30,
                "filters": [
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex",
                    "lvl_warning_only"
                ],
                "formatter": "loss_more_single_process",
                "filename": ".//warn.log",
                "maxBytes": 10485760,
                "mode":"a",
                "backupCount": 20,
                "encoding": "utf8"
            },
            "error_rotating_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": 40,
                "filters": [
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex",
                    "lvl_error_only"
                ],
                "formatter": "loss_more_single_process",
                "filename": ".//errors.log",
                "maxBytes": 10485760,
                "mode":"a",
                "backupCount": 20,
                "encoding": "utf8"
            },
            "critical_rotating_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": 50,
                "filters": [
                    "message_regex",
                    "name_regex",
                    "function_regex",
                    "thread_regex",
                    "process_regex",
                    "filename_regex",
                    "pathname_regex",
                    "lvl_critical_only"
                ],
                "formatter": "loss_more_single_process",
                "filename": ".//critical.log",
                "maxBytes": 10485760,
                "mode":"a",
                "backupCount": 20,
                "encoding": "utf8"
            }
        },
        "root": {
            "level": "NOTSET",
            "propogate": True
        },
        "loggers": {
            "console": {
                "level": "DEBUG",
                "handlers": [
                    "console"
                ],
                "propogate": False
            },
            "prompt": {
                "level": "DEBUG",
                "handlers": [
                    "prompt"
                ],
                "propogate": False
            },
            "file": {
                "level": "DEBUG",
                "handlers": [
                    "info_file_handler",
                    "error_file_handler",
                    "critical_file_handler",
                    "debug_file_handler",
                    "warn_file_handler"
                ],
                "propogate": False
            },                   
            "rotating_file": {
                "level": "DEBUG",
                "handlers": [
                    "info_rotating_file_handler",
                    "error_rotating_file_handler",
                    "critical_rotating_file_handler",
                    "debug_rotating_file_handler",
                    "warn_rotating_file_handler"
                ],
                "propogate": False
            }
        }
    }
    __DEFAULT_TYPE={
        "version": 1,
        "disable_existing_loggers": True,
        "formatters":{
        },
        "handlers":{
        },
        "root": {
        },
        "loggers": {
        }
    }
    __DEFAULT_REGEX={
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
                self._logger.debug('NetLog@'+ self._id +' ::_update_config -> '+'new_config => '+str(new_config)) 

            dictConfig(new_config)

            if self.__current_logger_name != None and self.__current_logger_name in self._config['loggers'].keys():
                self.logger_name=self.__current_logger_name
            else:
                if 'loggers' in self._config.keys():
                    self.logger_name=list(self._config['loggers'].keys())[0]
                
            if self._logger != None:
                self._logger.info('NetLog@'+ self._id +' ::_update_config -> '+'Success')
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionLog(self._logger,exception) 

    def generate_default_config(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            if self._logger != None:
                self._logger.debug('NetLog@'+ self._id +' ::generate_default_config -> '+'default_config => '+str(NetLog.__DEFAULT_CONFIG))   

            self.config=NetLog.__DEFAULT_CONFIG

            return
                        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionLog(self._logger,exception) 

    @NetClassParameterUnique(load=dict)     
    def _dict_load(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            super(NetLog,self)._dict_load(*list_param_no_named,**dict_param_named)
            
            load=dict_param_named['load']
            
            attributes=[
                'logger_name'
            ]
            
            if self._logger != None:
                self._logger.debug('NetLog@'+ self._id +' ::_dict_load -> '+'attributes => '+str(attributes))                
            
            for attribut in attributes:
                if attribut not in dict_param_named.keys():
                    exception={
                        'keys':'['+attribut+']',
                        'error':'missing key',
                        'message':'['+attribut+']'+' not in '+str(list(dict_param_named.keys()))
                        }
                
                    if self._logger != None:
                        self._logger.error('NetLog@'+ self._id +' ::_dict_load -> '+'exception => '+str(exception))                    
                        
                    raise NetExceptionLog(self._logger,**exception)

            self.logger_name=load['logger_name']
            
            return
                        
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionLog(self._logger,exception)  
    def _dict_save(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)            
            
            retour=super(NetLog,self)._dict_save(*list_param_no_named,**dict_param_named)
            
            retour['logger_name']=self.__current_logger_name

            if self._logger != None:
                self._logger.debug('NetLog@'+ self._id +' ::__dict_save -> '+'atributes => '+str(retour.keys()))
                
            return retour
            
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionLog(self._logger,exception)  

    def __init__(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)

            self.__current_logger_name='N/A'
            self.__current_logger=None

            super(NetLog,self).__init__(*param_no_named,**param_named)

            self.config_type=NetLog.__DEFAULT_TYPE  
            self.config_regex=NetLog.__DEFAULT_REGEX        

            if self._logger != None:
                self._logger.debug('NetLog@'+ self._id +' ::__init__ -> Creating object')

            if 'generate_default_config' in dict_param_named.keys() and type(dict_param_named['generate_default_config']) is bool and dict_param_named['generate_default_config'] is True:
                self.generate_default_config(*param_no_named,**param_named)
            
            if 'logger_name' in dict_param_named.keys() and type(dict_param_named['logger_name'] is str):
                self.logger_name=dict_param_named['logger_name'] 
                
            if self._logger != None:
                self._logger.info('NetLog@'+ self._id +' :: '+'object created -> '+'id => ' + self._id +' || '+'logger_name => '+str(self.__current_logger_name))
                                       
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionLog(self._logger,exception) 
    def __str__(self,*param_no_named,**param_named):
        try:
            if self._logger != None:
                self._logger.debug('NetLog@'+ self._id +' ::__str__ -> Getting str')              
            
            return 'logger => '+str(self.__current_logger)+' || '+'logger_name => '+str(self.__current_logger_name)
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionLog(self._logger,exception)

    @NetClassParameterUnique(str)
    def __set_current_logger_name(self,*param_no_named,**param_named):
        try:
            list_param_no_named=list(param_no_named)
            dict_param_named=dict(param_named)
            
            i=0
            while type(list_param_no_named[i]) is not str:
                i=i+1
            logger_name=list_param_no_named[i]
            
            if self._logger != None:
                self._logger.debug('NetLog@'+ self._id +' ::__set_current_logger_name -> '+'logger_name => '+str(logger_name))            
            
            if logger_name in self._config['loggers'].keys():
                self.__current_logger_name=logger_name
                self.__current_logger=logging.getLogger(logger_name)
            else:
                exception={
                    'logger':logger_name,
                    'error':'wrong logger',
                    'message':logger_name+' not in '+str(list(self._config['loggers'].keys()))
                    }
                    
                if self._logger != None:
                    self._logger.error('NetLog@'+ self._id +' ::__set_current_logger_name -> '+'exception => '+str(exception))                  
                    
                raise NetExceptionLog(self._logger,**exception)               
            return 
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionLog(self._logger,exception)
    def __get_current_logger_name(self,*param_no_named,**param_named):
        try:
            if self._logger != None:
                self._logger.debug('NetLog@'+ self._id +' ::__get_current_logger_name -> '+'logger_name => '+str(self.__current_logger_name))            
            
            return self.__current_logger_name
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionLog(self._logger,exception)
    logger_name=property(__get_current_logger_name,__set_current_logger_name)

    def __set_current_logger(self,*param_no_named,**param_named):
        try:
            
            if self._logger != None:
                self._logger.debug('NetLog@'+ self._id +' ::__set_current_logger -> logger_log is read only property')            
            
            exception={
                'property':'logger_log',
                'error':'read only property',
                'message':'logger_log is only reachable as read only property'
                }
 
            if self._logger != None:
                self._logger.error('NetLog@'+ self._id +' ::__set_current_logger -> logger_log is read only property')
                            
            raise NetExceptionLog(self._logger,**exception)
     
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionLog(self._logger,exception)   
    def __get_current_logger(self,*param_no_named,**param_named):
        try:   
            if self._logger != None:
                self._logger.debug('NetLog@'+ self._id +' ::__get_current_logger -> '+'logger => '+str(self.__current_logger))              
            
            return self.__current_logger
        except Exception as exception:
            if issubclass(type(exception),NetException):
                exception.logger=self._logger
                raise exception
            else:            
                raise NetExceptionLog(self._logger,exception)
    logger=property(__get_current_logger,__set_current_logger)    


