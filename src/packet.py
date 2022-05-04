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
        self.address_family: int = address_family  # IP is 2
        self.ip = ip                               # can by any of the following
        # host address
        # subnet number
        # network number
        # 0, indicating a default route
        self.metric = metric


class Packet:
    """ Represents a single RIP protocol packet """

    def __init__(self, command: Type[Command], version: str, packet_body: List[Type[PacketBodyEntry]]) -> None:
        self.command = command
        self.version = version
        if len(packet_body) >= 25:
            raise Exception("Cannot have more than 25 elements in a packet body")
        self.packet_body = packet_body
