def exec02(packet):
    if packet["FTP"]["request.command"] == "STOR":
        packet["FTP"]["request.command"] ="DELE"
        return packet
~                      
