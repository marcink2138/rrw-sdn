from mininet.topo import Topo


class RrTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        datacenter_dict = {}
        switch_dict = {}
        for i in range(1, 7):
            datacenter_key = 'D' + str(i)
            switch_key = 'S' + str(i)
            datacenter_dict[datacenter_key] = self.addHost(datacenter_key)
            switch_dict[switch_key] = self.addSwitch(switch_key)

        self.addLink(switch_dict["S1"], switch_dict["S2"])

        self.addLink(switch_dict["S5"], switch_dict["S1"])

        self.addLink(switch_dict["S6"], switch_dict["S1"])
	self.addLink(datacenter_dict["D1"], switch_dict["S1"])
        # Datacenters
        self.addLink(switch_dict["S6"], datacenter_dict["D3"])
        self.addLink(switch_dict["S6"], datacenter_dict["D4"])


topos = {'rr_topo': (lambda: RrTopo())}
