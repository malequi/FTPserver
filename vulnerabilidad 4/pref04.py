def prefTEST1(packet):
    try:
        if packet["FTP"]["request.command"] == "STOR":
            return packet
    except:
        return None
~                     
