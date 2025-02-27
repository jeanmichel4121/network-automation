__author__ = 'Jean-Michel Cuvelier'

from Lib.Functions.LibControl.NetControlParameter import NetClassParameterUnique
from Lib.Classes.LibNotification.NetNotification import NetNotificationBase
import getpass
import types
import paramiko

class TypeNetSFTP(NetNotificationBase):
    def __new__ (obj,name,list_hierachy,dict_parameters):
        return super(TypeNetSFTP,obj).__new__(obj,name,list_hierachy,dict_parameters)

class NetSFTP():
    __metaclass__=TypeNetSFTP
    
    def __init__(self,*param_no_name,**param_name):
        try: 
            dict_param_name=dict(param_name)
            list_param_no_name=list(param_no_name)
            
            self.__user="usr"
            if "user" in dict_param_name.keys():               
                self.__user=dict_param_name["user"]
                
            self.__password=""
            if "password" in dict_param_name.keys():               
                self.__password=dict_param_name["password"]
                
            self.__password="22"
            if "password" in dict_param_name.keys():               
                self.__password=dict_param_name["password"]
                
        except BaseException as ex:
            raise ex
        return
    
def get_remote_file(self,hostname, port, username, password, remotepath, localpath):
    """Get remote file to local machine.

    Args:
        hostname(str):  Remote IP-address
        port(int):  Remote SSH port
        username(str):  Remote host username for authentication
        password(str):  Remote host password for authentication
        remotepath(str):  Remote file to download location path
        localpath(str):  Local path to save remote file

    Examples::

        get_remote_file(host, port, username, password, tar_remotepath, tar_localpath)

    """
    transport = paramiko.Transport((hostname, port))

    transport.connect(username=username, password=password)
    transport.load_server_moduli()
    sftp = paramiko.SFTPClient.from_transport(transport)
    try:
        sftp.get(remotepath=remotepath, localpath=localpath)
    except paramiko.AuthenticationException:
        print("SFTP Authentication failed when connecting to %s" % hostname)
    finally:
        sftp.close()
        transport.close() 