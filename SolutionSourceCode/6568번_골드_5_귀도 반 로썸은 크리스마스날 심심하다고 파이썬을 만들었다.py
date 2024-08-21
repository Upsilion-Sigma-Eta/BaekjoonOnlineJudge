import sys

memory = {}
instruction_mask = 0b11100000
address_mask = 0b00011111
pc_mask = 0b00011111
pc = 0
adder_result_mask = 0b11111111
adder_value = 0

def STA(addr, val):
    global memory

    memory[addr] = bin(val)[2:].zfill(8)

def LDA(addr, val):
    return int(memory[addr], 2)

def BEQ(addr, val):
    global adder_value
    global pc

    if adder_value == 0:
        pc = val
        pc &= pc_mask

def NOP(addr):
    return

def DEC(addr):
    global adder_value

    adder_value -= 1
    adder_value &= adder_result_mask

def INC(addr):
    global adder_value

    adder_value += 1
    adder_value &= adder_result_mask

def JMP(addr, val):
    global pc

    pc = val
    pc &= pc_mask

def HLT(addr):
    return True

def Solution():
    global pc
    global adder_value
    global memory
    global pc_mask
    global address_mask
    global instruction_mask
    global pc
    global adder_result_mask

    while True:
        adder_value = 0
        pc = 0
        memory.clear()
        memory["-1"] = adder_value

        for i in range(32):
            instruct = sys.stdin.readline().strip()
            if not instruct:
                return
            memory[bin(i)[2:].zfill(5)] = instruct

        while True:
            instruct = memory[bin(pc)[2:].zfill(5)]

            pc += 1
            pc &= pc_mask

            if (instruct[:3] == "000"):
                STA(instruct[3:], adder_value)
            elif (instruct[:3] == "001"):
                adder_value = LDA(instruct[3:], 0)
            elif (instruct[:3] == "010"):
                BEQ(instruct[3:], int(instruct[3:], 2))
            elif instruct[:3] == "011":
                NOP("-1")
            elif instruct[:3] == "100":
                DEC("-1")
            elif instruct[:3] == "101":
                INC("-1")
            elif instruct[:3] == "110":
                JMP(instruct[3:], int(instruct[3:], 2))
            elif instruct[:3] == "111":
                if HLT("-1"):
                    break

        sys.stdout.write(bin(adder_value)[2:].zfill(8) + "\n")



if __name__ == "__main__":
    Solution()