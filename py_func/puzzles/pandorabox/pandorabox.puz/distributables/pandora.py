import struct, random
from socket import *

SECRET_FILE = "secret_file"
HOST = ""
PORT = 1337

def main():
    secret_bytes = file(SECRET_FILE).read()

    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    while True:
        data, addr = s.recvfrom(999)
        print "Received {} bytes from {}:{}.".format(len(data), *addr)
        s.sendto(proc(data, secret_bytes), addr)
    return

def proc(r_input, secret_bytes):
    if len(r_input) % 2:
        return ""

    if len(r_input) > len(secret_bytes):
        secret_bytes += (len(r_input) - len(secret_bytes)) * "\x42"

    tr = random.randint(0x0, 0xff)
    pandora = "".join(chr(ord(i)^tr) for i in secret_bytes[:7])

    p_input= ""
    for i in range(0, len(r_input), 2):
        r1 = (ord(r_input[i]) & 0xfc) + ((~ord(r_input[i+1]) & 0xff) & 0x03)
        r2 = ((ord(r_input[i]) & 0x01) << 6) + (~((ord(r_input[i+1]) & 0xfc) >> 2) & 0xff) & 0x80
        p_input += struct.pack("<BB", ~r1 & 0xff, r2)

    f_out =[]
    for i in range(len(p_input)):
        f_out.append(ord(p_input[i]) ^ ord(secret_bytes[i]) ^ ord(pandora[i%len(pandora)]))

    return "".join(chr(i) for i in f_out)
    
    
if __name__ == "__main__":
    main()
