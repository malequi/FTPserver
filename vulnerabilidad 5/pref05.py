def type(packet):
    try:
        if packet["FTP"]["request.command"] == "TYPE":
            return packet
    except:
        return None

