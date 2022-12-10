import os

input_hex = ""

hex_bin_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

class Packet:
    def __init__(self, version, id):
        self.version = version
        self.id = id
        self.subpackets = []
        if id == 4:
            self.literal = None
        else:
            self.type = None
            self.counter = None
            self.operator = None

    def version_sum(self):
        return self.version + sum([p.version_sum() for p in self.subpackets])

    def __str__(self):
        if self.id == 4:
            return "Packet(v{},#{}, Literal {})".format(self.version, self.id, self.literal)
        else:
            return "Packet(v{},#{}, Operator ({}), ({} subpackets:{})".format(self.version, self.id, self.operator, len(self.subpackets), [str(p) for p in self.subpackets])

with open(os.getcwd() + "\\2021\\day_16\\day_16-input.txt", 'r') as file:
    phase = 0
    line = file.readline()
    while line:
        line = line.strip()
        input_hex = line
        line = file.readline()

# Test_cases
# ---------
#input_hex = "D2FE28" # Version 6, Literal (4), 2021
#input_hex = "38006F4529120" # Version 1, Operator (type 0), 27 sub-packet length
#input_hex = "EE00D40C823060" # Version 7, Operator (type 1) 3 sub-packets
#input_hex = "8A004A801A8002F478" # Version sum 16
#input_hex = "620080001611562C8802118E34" # Version sum 12
#input_hex = "C0015000016115A2E0802F182340" # Version sum 23
#input_hex = "A0016C880162017C3686B18A3D4780" # Version sum 31
# ---------

# sequence
sequence = []
for hex in input_hex:
    for bit in hex_bin_map[hex]:
        sequence.append(bit)

def sequence_pop(sequence, count=1):
    if len(sequence) < count:
        bin = ""
        for b in sequence:
            bin += b
        return bin
    else:
        bin = ""
        for i in range(count):
            bin += sequence.pop(0)
        return bin

def read_sequence(sequence, count=-1):
    subpackets = []
    step = 0
    while len(sequence) > 0 and int("".join(sequence), 2) != 0 and (count == -1 or step < count):
        version = int(sequence_pop(sequence, 3), 2)
        id = int(sequence_pop(sequence, 3), 2)
        packet = Packet(version, id)
        if id == 4:
            bin_str = ""
            while True:
                leading = int(sequence_pop(sequence), 2)
                bin_str += sequence_pop(sequence, 4)
                if leading == 0:
                    break
            packet.literal = int(bin_str, 2)
        else:
            length_type_id = int(sequence_pop(sequence), 2)
            if length_type_id == 0:
                # 15 bits represent Total length of subpackets
                subpacket_len = int(sequence_pop(sequence, 15), 2)
                subsequence = []
                for i in range(subpacket_len):
                    subsequence.append(sequence.pop(0))
                packet.subpackets = read_sequence(subsequence)
            else:
                # 11 represent number of immediate subpackets
                subpacket_count = int(sequence_pop(sequence, 11), 2)
                packet.subpackets = read_sequence(sequence, count=subpacket_count)
        subpackets.append(packet)
        step += 1
    return subpackets

packet = read_sequence(sequence)[0]
print(packet)
print(packet.version_sum())
