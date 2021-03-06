import socket


class ProtocolScanner(object):
    def __init__ (self, protocolName, portNumber, IPAddress, MACaddress):
        self.protocolName = protocolName
        self.portNumber = portNumber
        self.IPAddress = IPAddress
        self.MACaddress = MACaddress

    def getProtocolName(self):
        return self.protocolName

    def getPortNumber(self):
        return self.portNumber

    def getIPAddress(self):
        return self.IPAddress

    def getMACaddress(self):
        return self.MACaddress



    def isPortOpen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(8)
        result = sock.connect_ex((str(self.IPAddress), self.portNumber))

        try:
            sock.shutdown(2)
        except: # anything really
            pass
        return result


class ProtocolExploiter(ProtocolScanner):
    def __init__ (self, protocolName, portNumber, IPAddress, MACaddress):
        self.protocolName = protocolName
        self.portNumber = portNumber
        self.IPAddress = IPAddress
        self.MACaddress = MACaddress

    def getProtocolName(self):
        return self.protocolName

    def getPortNumber(self):
        return self.portNumber

    def getIPAddress(self):
        return self.IPAddress

    def getMACaddress(self):
        return self.MACaddress



    def isPortOpen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(8)
        result = sock.connect_ex((str(self.IPAddress), self.portNumber))

        try:
            sock.shutdown(2)
        except: # anything really
            pass
        return result
