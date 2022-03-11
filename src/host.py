from routing_table import RoutingTable

class Host():
    """ Represents a host in the network """

    def __init__(self) -> None:
        self.table: Type[RoutingTable] = RoutingTable()
        self.directly_connected_hosts = None # TODO: 
    
    def propagate_table(self) -> None:
        return
