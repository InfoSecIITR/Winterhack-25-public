from z3 import *

s = Solver()

key = [BitVec(f'key{i}', 8) for i in range(52)]

for i in range(52):
    s.add(Or(And(key[i] >= 48, key[i] <= 57), And(key[i] >= 65, key[i] <= 90), And(key[i] >= 97, key[i] <= 122), key[i] == 95))

eqns =  '''key[0] + (key[1] ^ key[3])=110
key[2] + (key[1] ^ key[5])=139
(key[7] ^ key[4]) + key[3]=119
key[8] + key[3] + key[6]=322
key[8] + (key[3] ^ key[5])=221
key[11] + (key[9] ^ key[8])=188
key[10] ^ key[9] ^ key[7]=56
(key[12] ^ key[10]) + key[5]=62
(key[3] ^ key[13]) + key[14]=160
(key[13] ^ key[15]) + key[14]=160
(key[15] ^ key[12]) + key[0]=95
(key[0] | key[16]) + key[19]=178
(key[14] ^ key[16]) + key[12]=207
key[16] ^ key[17] ^ key[19]=110
key[19] + (key[17] ^ key[12])=122
key[20] + (key[7] ^ key[20])=140
key[6] - (key[21] ^ key[20])=7
(key[3] ^ key[8]) + key[21]=98
(key[22] ^ key[21]) + key[21]=141
(key[23] | key[29]) + key[17]=167
(key[6] ^ key[13]) + key[24]=113
key[23] + key[12] + key[24]=279
key[21] + (key[17] ^ key[24])=49
key[29] ^ key[16] ^ key[17]=106
(key[17] & key[16]) ^ key[1]=72
(key[25] & key[14]) ^ key[8]=94
key[0] + (key[1] ^ key[26])=150
key[26] + key[1] + key[29]=214
(key[49] ^ key[50]) + key[51]=200
(key[49] ^ key[29]) + key[17]=139
(key[3] ^ key[4]) + key[30]=148
key[25] ^ key[14] ^ key[38]=116
key[27] ^ key[14] ^ key[28]=111
key[23] + key[28] + key[26]=277
key[27] + key[29] + key[32]=211
key[30] + (key[28] ^ key[32])=101
key[41] ^ key[29] ^ key[31]=114
(key[18] ^ key[33]) + key[31]=125
key[34] + key[33] - key[29]=107
(key[36] ^ key[34]) + key[34]=199
(key[36] | key[34]) - key[35]=32
(key[36] & key[29]) + key[37]=159
key[32] + key[39] + key[35]=294
key[32] + (key[30] | key[35])=199
key[38] - key[37] + key[31]=2
key[43] ^ key[19] ^ key[42]=52
key[22] | key[29] | key[51]=127
(key[23] ^ key[25]) + key[48]=97
key[14] + (key[24] ^ key[42])=56
key[43] ^ key[27] ^ key[42]=51
(key[41] ^ key[44]) + key[45]=188
(key[42] ^ key[43]) + key[44]=60
key[44] + key[45] - key[42]=119
(key[25] ^ key[39]) + key[46]=159
(key[44] | key[37]) + key[48]=220
key[40] ^ (key[41] & key[42])=5
(key[22] ^ key[40]) + key[40]=145
(key[16] | key[47]) ^ key[47]=76
(key[47] | key[46]) + key[47]=166
key[49] + key[50] - key[51]=48'''

for eqn in eqns.split('\n'):
    eqn = eqn.replace('=', '==')
    exec(f's.add({eqn})')
    eqn = eqn.replace('==', ')==')
    print(f'(({eqn});')

if s.check() == sat:
    m = s.model()
    print(''.join([chr(m[key[i]].as_long()) for i in range(52)]))
