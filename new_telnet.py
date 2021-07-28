import time
import telnetlib
from strip_ansi import strip_ansi

class aruba_os_telnet:
    def __init__(self,ip_address_aruba_telnet,port_aruba_telnet):
        self.ip_address_aruba_telnet = ip_address_aruba_telnet
        self.port_aruba_telnet = port_aruba_telnet
    def send_telnet_commands(self,command):
        '''
        Send Telnet Command
        Input = "String" Datatype
        Output = "NoneType" Datatype
        '''
        command_sent = telnet_socket.write(command.encode('utf-8') + b"\n")
    def read_telnet_commands(self):
        '''
        Read Telnet Output
        Output = "string" Datatype
        '''
        readoutput = telnet_socket.read_all().decode('ascii')
        pretty_readouput = strip_ansi(readoutput)
        return pretty_readouput
    def close_telnet_connection(self):
        '''
        Closes Telnet connection
        '''
        telnet_socket.close()
    def connect_telnet(self):
        '''
        Create Socket
        Output = "Object" Datatype
        '''
        global telnet_socket
        telnet_socket = telnetlib.Telnet(self.ip_address_aruba_telnet,self.port_aruba_telnet)

test = aruba_os_telnet("10.210.210.117",2004)
test.connect_telnet()
test.send_telnet_commands("sh version")
result = test.read_telnet_commands()
print(result)
test.close_telnet_connection()

