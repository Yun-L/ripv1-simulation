from typing import List

class RoutingTableEntry:
    """ A single entry in a routing table, describes routes to a destination """

    def __init__(self, dest_name: str, dest_ip: str, metric: int,
                 next_gw_ip: str, rc_flag: bool, timers: int) -> None:
        self.dest_name: str = dest_name
        self.dest_ip: str = dest_ip
        self.metric: int = metric  # hop count
        self.next_gw_ip: str = next_gw_ip
        self.rc_flag: bool = rc_flag
        self.timers: int = timers


class RoutingTable:
    """ RIP routing table """

    def __init__(self) -> None:
        self.entry_table: Dict[str, Type[RoutingTableEntry]] = {}

    def add_entry(self, entry: Type[RoutingTableEntry]) -> None:
        if entry.dest_ip in self.entry_table:
            if entry.metric == self.entry_table[entry.dest_ip].metric:
                # if hops are same than add both
                print("hops are the same")
        self.entry_table[entry.dest_ip] = entry
        return

    def remove_entry(self):
        return
