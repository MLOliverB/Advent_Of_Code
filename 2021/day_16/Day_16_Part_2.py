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

    def evaluate(self):
        subpacket_results = []
        for sub in self.subpackets:
            subpacket_results.append(sub.evaluate())
        results_len = len(subpacket_results)
        if results_len > 0:
            if self.id == 0:
                # packet.operator = "+"
                return sum(subpacket_results)
            elif self.id == 1:
                # packet.operator = "*"
                if results_len == 1:
                    return subpacket_results[0]
                else:
                    prod = 1
                    for p in subpacket_results:
                        prod *= p
                    return prod
            elif self.id == 2:
                # packet.operator = "min"
                min = subpacket_results[0]
                for i in range(1, results_len):
                    if subpacket_results[i] < min:
                        min = subpacket_results[i]
                return min
            elif self.id == 3:
                # packet.operator = "max"
                max = subpacket_results[0]
                for i in range(1, results_len):
                    if subpacket_results[i] > max:
                        max = subpacket_results[i]
                return max
            elif self.id == 5:
                # packet.operator = ">"
                greater_progression = True
                for i in range(results_len-1):
                    if subpacket_results[i] > subpacket_results[i+1]:
                        continue
                    else:
                        greater_progression = False
                if greater_progression:
                    return 1
                else:
                    return 0
            elif self.id == 6:
                # packet.operator = "<"
                smaller_progression = True
                for i in range(results_len-1):
                    if subpacket_results[i] < subpacket_results[i+1]:
                        continue
                    else:
                        smaller_progression = False
                if smaller_progression:
                    return 1
                else:
                    return 0
            elif self.id == 7:
                # packet.operator = "=="
                equals_progression = True
                for i in range(results_len-1):
                    if subpacket_results[i] == subpacket_results[i+1]:
                        continue
                    else:
                        equals_progression = False
                if equals_progression:
                    return 1
                else:
                    return 0
        else:
            return self.literal

    def __str__(self):
        if self.id == 4:
            return "{}".format(self.literal)
        else:
            return "({};{})".format(self.operator, ",".join([str(p) for p in self.subpackets]))
            #return "Packet(v{},#{}, Operator ({}), ({} subpackets:{})".format(self.version, self.id, self.operator, len(self.subpackets), [str(p) for p in self.subpackets])

with open(os.getcwd() + "\\2021\\day_16\\day_16-input.txt", 'r') as file:
    phase = 0
    line = file.readline()
    while line:
        line = line.strip()
        input_hex = line
        line = file.readline()

# Test_cases
# ---------
#input_hex = "C200B40A82" # 1 + 2 = 3
#input_hex = "04005AC33890" # 6 * 9 = 54
#input_hex = "880086C3E88112" # min(7, 8, 9) = 7
#input_hex = "CE00C43D881120" # max(7, 8, 9) = 9
#input_hex = "D8005AC2A8F0" # 5 < 5 = 1
#input_hex = "F600BC2D8F" # 5 > 15 = 0
#input_hex = "9C005AC2F8F0" # 5 == 15 = 0
#input_hex = "9C0141080250320F1802104A08" # 1+3 == 2*2 = 1
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
            if id == 0:
                packet.operator = "+"
            elif id == 1:
                packet.operator = "*"
            elif id == 2:
                packet.operator = "min"
            elif id == 3:
                packet.operator = "max"
            elif id == 5:
                packet.operator = ">"
            elif id == 6:
                packet.operator = "<"
            elif id == 7:
                packet.operator = "=="
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
print(packet.evaluate())
