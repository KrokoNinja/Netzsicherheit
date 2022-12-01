from scapy.all import *
def getIniatorSAPacket(packets: []) -> scapy.layers.isakmp.ISAKMP:
    #TODO Get frist initiator SA ISAKMP layer
    pass

def getResponderSAPacket(packets: []) -> scapy.layers.isakmp.ISAKMP:
    #TODO Get first responder SA ISAKMP layer
    pass

def getPayloadFromISAKMP(packet: scapy.layers.isakmp.ISAKMP, name: str) -> bytes:
    # name == payload name
    # TODO Get the corresponding load from the selected (by name) layer
    pass

def getCookieFromISAKMP(respPacket: scapy.layers.isakmp.ISAKMP, responderCookie: bool) -> bytes:
    # TODO return corresponding cookie value
    # true -> responder cookie
    # false -> initiator cookie
    pass

def getSAPayloadFromInitPacket(packet: scapy.layers.isakmp.ISAKMP) -> bytes:
    # TODO Get the SA payload only from initiator packet
    pass

def getResponderIDFromRespPacket(packet: scapy.layers.isakmp.ISAKMP) -> bytes:
    # TODO Return responder ID from ISAKMP layer
    # Responder ID consist of  IDType||ProtoID||Port||load
    pass

def getRespHashfromPacket(packet: scapy.layers.isakmp.ISAKMP) -> bytes:
    # TODO Get the hash value to compare your computed value against
    pass
