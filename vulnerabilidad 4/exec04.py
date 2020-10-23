def exceTEST1(packet):
    if packet["IP"]["addr"] == "172.17.0.2":
        packet["FTP"]["request.command"] = "STOU"
        packet["IP"]["addr"] = "172.17.0.5"
        print("IP DESTINO"+str(packet["IP"]["addr"]))
        return packet
~                          
