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

    def process_input(self, packet: Type[Packet]):
        if packet.command == Command.REQUEST:
            if len(packet.packet_body) == 0:
                # no response if no packet_body
                return
            if len(packet.packet_body) == 1:
                [entry] = packet.packet_body
                if entry.address_family == 0 and entry.metric == 16:
                    # special case to send whole routing table
                    return
            for entry in packet.packet_body:
                # for every entry, look up dest in host routing table, if there is a route then put the metric in the metric field, if no route put INF (16), then set command to RESPONSE and send back the datagram

        if packet.command == Command.RESPONSE:
            if 
        # if RESPONSE
        # check if source ip is from directly connected hosts
        # source ip shouldnt be from own ip
        
        # process entries in datagram one by one,
        # if metric > INF, ignore
        # log erroneous metrics/data
        # look at dest addr,
        # check fam ID, must be 2 for IP, ignore otherwise
        # check for inappropriate addresses
        # if version == 1, unused octets in packet must be checked
        # update metric by adding cost of network on the message metric, if result is greate than 16, use 16 -> metric = MIN (metric + cost, 16)
        # check addr to see if it already exists in routing table
        # if true, update, if not, add
        # if metric is INF, don't add, still update
        # to update means -> set dest + metric, set GW to be host datagram came from, initiliaze timeout for that route, stop garbage collection timer for that route, set route change flag, signal output process to trigger update

        # if exists, compare GWs, if same GW as existing, reinit timout
        # cmp metrics, if datagrams are same and metrics diff, then
        #     use new route + metric + gw
        #     init timeout
        #     set route change flag, signall output process to trigger update
        #     if new metric is 16 (INF), start delete process

        # if new metric is 16, route no longer used for routing pcakets, deletion timer is started
        # if metric already 16, new deletion is not started (one should already exist)

        # if new metric is same as old, then do nothing

        # everything else ignored
        return

    def process_output(self):
        # general process for sending parts of routing tables, happens when:
        # 1. input process sees request
        # 2. regular routing update, every 30 seconds whole routing tabel is sent to neighbor
        #     
        # 3. triggered update, if metric of route is change, update is triggered
        #     random timer should be set between 1 and 5 before the update
        #     do not need to include entire routing table, will possible omit routes that have not changed, source ip must be hosts address
        return

    def handle_arb_packet(self):
        return

    def tick(self):
        return
