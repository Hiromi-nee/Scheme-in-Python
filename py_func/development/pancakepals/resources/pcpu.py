# pcpu - simple memory and processor emulator
# memory is addressed from 0x0000 to 0xFFFF

class PCPU:
    # Initialise the available memory as 0x0000 - 0xFFFF
    memory = [0 for i in range(0x0000, 0xFFFF + 1)]
    
    # Allow for 2 registers (register a and b)
    ra = 0
    rb = 0
    
    # Allow for pointers (instruction, stack, base)
    ip = 0
    sp = 0xFFFF # Set the base of the stack at 0xFFFF
    bp = 0xFFFF

    # Allow for flags (zero)
    zf = 0 

    # Instructions are variable width three bytes long
    # <operand> <parameter> <parameter> <parameter>
    inst_set = {
        "PUSH": 0x00,
        "POP": 0x01,
        "ADD": 0x02,
        "SUB": 0x03,
        "XOR": 0x04,
        "MOV": 0x05,
        "SHR": 0x06,
        "SHL": 0x07,
        }

    para_val = {
        "nul": 0x00,
        "ra": 0x01,
        "rb": 0x02,
        "ip": 0x03,
        "sp": 0x04,
        "bp": 0x05,
        
        }

def main():
    pcpu = PCPU()

if __name__ == "__main__":
    main()
