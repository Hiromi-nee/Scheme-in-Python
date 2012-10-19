encode = "http://www.youtube.com/watch?v=Ik-RsDGPI5Y"
bit_list = []

for i in encode:
    bits = []
    for j in bin(ord(i))[2:]:
        bits.append(int(j, 2))
    bit_list.append(bits)

char_list = ["/", "\\"]
for i in bit_list:
    print "".join(char_list[j] for j in i)
    
