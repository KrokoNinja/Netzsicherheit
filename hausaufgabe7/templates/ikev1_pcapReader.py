def openPCAPFile(path: str) -> scapy.plist.PacketList:
    #TODO Read a pcap or pcapng file and return a packet list
    raise NotImplementedError('Reading packets not implemented.')

def getISAKMPPackets(packets: scapy.plist.PacketList) -> []:
    #TODO returns a list containing only the ISAKMP Layers of the packets in packetList 
    raise NotImplementedError('Getting ISAKMP Layer from PacketList not implemented.')
