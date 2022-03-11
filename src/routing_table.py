from typing import List

class RoutingTableEntry:
    """ A single entry in a routing table, describes routes to a destination """

    def __init__(self, dest_name: str, dest_ip: str, metric: int,
                 next_gw_ip: str, rc_flag: bool, timers: int) -> None:
        self.dest_name = dest_name
        self.dest_ip = dest_ip
        self.metric = metric
        self.next_gw_ip = next_gw_ip
        self.rc_flag = rc_flag
        self.timers = timers


class RoutingTable:
    """ RIP routing table """

    def __init__(self) -> None:
        self.entry_list: List[Type[RoutingTableEntry]] = []

    def add_entry(self, entry: Type[RoutingTableEntry]) -> None:
        self.entry_list.append(entry)

    def remove_entry(self):
        return
