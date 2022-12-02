from scapy.all import *
def openPCAPFile(path: str): #-> scapy.plist.PacketList:
    #TODO Read a pcap or pcapng file and return a packet list
    return rdpcap(path)

def getISAKMPPackets(packets: scapy.plist.PacketList): #-> []
    #TODO returns a list containing only the ISAKMP Layers of the packets in packetList
    isakmppackets = []
    for packet in packets:
        if packet.haslayer("ISAKMP"):
            isakmppackets.append(packet)
    return isakmppackets
