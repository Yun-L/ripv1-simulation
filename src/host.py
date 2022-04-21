from routing_table import RoutingTable
from packet import Packet, PacketBodyEntry, Command

class Host():
    """ Represents a host in the network """
    def __init__(self, directly_connected_hosts: Dict[str, Type[Host]]) -> None:
        self.table: Type[RoutingTable] = RoutingTable()
        self.directly_connected_hosts = None # TODO: 
    
    def send_request(self, dest_host: str):
        if dest_host not in self.directly_connect_hosts:
            raise Exception(f"Could not send request to '{dest_host}', does not exist");
        packet_body = []
        req = Packet(Command.REQUEST, "placeholder_version", packet_body)
        self.directly_connected_hosts.get(dest_host).handle_packet();
        return

    def send_response(self, dest_host: str):
        if dest_host not in self.directly_connect_hosts:
            raise Exception(f"Could not send response to '{dest_host}', does not exist");
        return

    def send_arb_packet(self, dest_host: str):
        return

    def handle_rip_packet(self, packet: Type[Packet]):
        return

    def handle_arb_packet(self):
        return

    def tick(self):
        return
