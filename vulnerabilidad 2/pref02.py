def prefTEST(packet):
    try:
        if packet["FTP"]["request.command"] == "PASS":
            return packet
    except:
        return None

