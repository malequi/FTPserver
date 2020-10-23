def pref01(packet):
    try:
        if packet["FTP"]["request.command"] == "USER":
            return packet
    except:
        return None

