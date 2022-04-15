from enum import Enum, auto

class Command(Enum):
    REQUEST = auto()
    RESPONSE = auto()
    TRACEON = auto()            # obsolete
    TRACEOFF = auto()           # obsolete
    RESERVED = auto()           # unused, only for Sun Microsystems


class PacketBodyEntry:
    """ Represents the repeating portion of a RIP protocol packet """

    def __init__(self, address_family, ip, metric):
        self.address_family = address_family  # ip is 2
        self.ip = ip
        self.metric = metric


class Packet:
    """ Represents a single RIP protocol packet """

    def __init__(self, command: int, version: str, packet_body: List[Type[PacketBodyEntry]]) -> None:
        self.command = command
        self.version = version
        self.address_family = address_family
        self.ip = ip
        self.metric = metric
        
