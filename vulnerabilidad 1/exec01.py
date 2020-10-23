def exc01(packet):
    if packet["FTP"]["request.command"] == "USER":
        packet["TCP"]["payload"] = b'USER admin\r\n'
        packet["FTP"]["request.arg"] = "Maldito"
        return packet

