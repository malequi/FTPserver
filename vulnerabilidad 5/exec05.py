def typeExec(packet):
    if packet["FTP"]["request.arg"] == "I":
        packet["FTP"]["request.arg"] = "A"
        print("Cambiado a:"+str(packet["FTP"]["request.arg"]))
        return packet
    if packet["FTP"]["request.arg"] == "A":
        packet["FTP"]["request.arg"] = "I"
        print("CAMBIADO A:"+str(packet["FTP"]["request.arg"]))
        return packet
~                                                                               
~                            
