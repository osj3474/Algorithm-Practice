pseudo_header = [0b1001100100010010, 0b0000100001101001, 0b1010101100000010, 0b0000111000001010, 0b0000000000010001, 0b0000000000001111]
header = [0b0000010000111111, 0b0000000000001101, 0b0000000000001111, 0b0000000000000000]
data = [0b0101010001000101, 0b0101001101010100, 0b0100100101001110, 0b0100011100000000]

entire_lst = pseudo_header+header+data
SUM = 0
for item in entire_lst:
    SUM += item
SUM = str(bin(SUM))

carry = bin(int(SUM[2:-16],2))
SUM = bin(int(SUM[-16:],2))

answer = bin((int(SUM,2)+int(carry,2))^ 0b1111111111111111)

print("SUM : {}".format(SUM[2:]))
print("carry: {}".format(carry[2:]))
print("checksum: {:0>16}".format(answer[2:]))



