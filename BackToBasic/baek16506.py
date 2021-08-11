my_dic = {'ADD':'0000', 'SUB':'0001', 'MOV':'0010',
          'AND':'0011', 'OR':'0100', 'NOT':'0101', 'MULT':'0110',
          'LSFTL':'0111', 'LSFTR':'1000', 'ASFTR':'1001',
          'RL':'1010', 'RR':'1011'}

n = int(input())

def fillZero(S, n):
    return '0'*(n-len(S))+S

for i in range(n):
    command = input().split()
    command = [command[0]]+list(map(lambda x: bin(int(x)), command[1:]))
    op = ''
    d, rA, BC = command[1][2:], command[2][2:], command[3][2:]
    isConstant = False
    if command[0][-1]=='C':
        op = my_dic[command[0][:-1]]+'1'
        isConstant = True
    else: op = my_dic[command[0]]+'0'
    d = fillZero(d, 3)
    rA = fillZero(rA, 3)
    if isConstant: BC = fillZero(BC, 4)
    else:
        BC = fillZero(BC, 3) + '0'
    answer = op+'0'+d+rA+BC
    print(answer)