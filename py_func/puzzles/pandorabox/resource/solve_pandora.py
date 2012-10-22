import sys, md5
from socket import *

HOST = "localhost"
PORT = 1337

def stage1():
    data = grab_copy()

    # xor with 0x42, this is repeating for overlong inputs at the end
    pbox_data = []
    for i in data:
        pbox_data.append(i^0x42)

    print "Please analyse the following (look for patterns):"
    print "".join(chr(i) for i in pbox_data)

def stage2(s):
    data = grab_copy()
    pbox = list(ord(i) for i in s)
    
    pre_ans = []
    # xor with the pbox
    for i in range(len(data)):
        pre_ans.append(data[i]^pbox[i%len(pbox)])

    # strip 0x42s
    pre_ans.reverse()
    ans = []
    for i in pre_ans:
        if i == 0x42:
            continue
        ans.append(i)
    ans.reverse()
        
    answer = "".join(chr(i) for i in ans)
    dig = md5.md5(answer).hexdigest()
    sys.stdout.write("Contents: \n******\n%s******\n" % answer)
    print "Digest: %s" % dig

    

def grab_copy():
    # magic numbers
    # b1 = 0xfd 0b11111101
    # b2 = 0xfc 0b11111100
    mb = "\xfd\xfc"

    # grab a copy
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect((HOST, PORT))
    s.sendall(mb * 499)
    data = s.recv(1000)

    # since, the first seven bytes will be equivalent and will be the random salt added to the pbox
    salt = ord(data[0])
    
    # xor with salt
    salted_data = []
    for i in data:
        salted_data.append(ord(i)^salt)

    return salted_data

def main():
    if len(sys.argv) < 2:
        print "./solve_pandora.py <stage> [params]"
        return

    if sys.argv[1] == "1":
        stage1()
    elif sys.argv[1] == "2":
        stage2(sys.argv[2])

if __name__ == "__main__":
    main()
