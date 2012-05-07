import socket

def main():
    
    service_dict = ["thelength", 
                    "kayla",
                    "upper",
                    "lower",
                    "reverse",
                    "wollsmoth",
                    "swapcase",
                    ]

    print "Welcome to the Trapform Text Translation Service!"
    print "                   by amon\n"
    print "Here are the services available for you to use: "

    for i in range(0, len(service_dict)):
        print "%d. %s" % (i, service_dict[i])

    service = ""
    while True:
        if not service.isdigit():
            service = raw_input("\nPlease enter the number " +
                                "of the service you wish to use: ")
        else:
            break

    usertext = raw_input("Please enter the text you wish to transform: ")
    
    tosend = "<%s>%s" % (service_dict[int(service)], usertext)
    tosend = "%d:%s," % (len(tosend), tosend)

    host = raw_input("Please enter the host: ")
    port = raw_input("Please enter the port: ")
    print("Stand by. Getting your transformed text...")
    
    sock = socket.socket()
    sock.connect((host, int(port)))
    sock.sendall(tosend)
    
    total_received = ""
    
    while True:
        received = sock.recv(1024)
        if received == "":
            break
        else:
            total_received += received

    print "Here is your transformed text: \n"
    print total_received.split(":", 1)[1][:-1]
    print ""

if __name__ == "__main__":
    main()
