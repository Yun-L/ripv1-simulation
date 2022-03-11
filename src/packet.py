class Packet:
    """ Represents a single RIP protocol packet """

    def __init__(self, command, version, address_family, ip, metric) -> None:
        self.command = command
        self.version = version
        self.address_family = address_family
        self.ip = ip
        self.metric = metric
        
        
