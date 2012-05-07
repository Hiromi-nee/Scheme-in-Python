# pcpu - simple memory and processor emulator
# memory is addressed from 0x00 to 0xFF

class PCPU:
    # Initialise the available memory as 0x00 - 0xFF
    memory = [0 for i in range(0x00, 0xFF + 1)]
    
    # Allow for 2 registers (register a and b)
    ra = 0
    rb = 0
    
    # Allow for pointers (instruction, stack, base)
    ip = 0
    sp = 0xFF # Set the base of the stack at 0xFF
    bp = 0xFF

    # Allow for flags (zero)
    zf = 0 

    # Instructions are fixed width two bytes long
    # <operand> <parameter>
    inst_set = {
        "PUSH": 0x00,
        "POP": 0x01,
        "ADD": 0x02,
        "SUB": 0x03,
        "XOR": 0x04,
        "MOV": 0x05,
        "IEQ": 0x06
        }

def main():
    pcpu = PCPU()

if __name__ == "__main__":
    main()
