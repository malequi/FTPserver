def execTEST(packet):
    import random
    if packet["FTP"]["request.arg"] != "admin":
        PASS = ("dainm","naidm","maind","iandm","12345","admin","holap","chaop","98765","lolol","ayuda","porfa","vorxd","uwuwu")
        correct_PASS = "admin"
        while True:
            position = random.randrange(len(PASS))
            packet["FTP"]["request.arg"] = PASS[position]
            print(packet["FTP"]["request.arg"])
            if PASS[position] == correct_PASS:
                break
        return packet

