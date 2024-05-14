import json
import sys
from py_ecc import bn128
from py_ecc import fields


in_path = "proof.json"
out_path = "zok-in.json"
para_path = "d_in_d_out.json"
next_epoch = 0
if len(sys.argv) > 1:
    in_path = sys.argv[1] + "/proof.json"
    out_path = sys.argv[2] + "/zok-in.json"
    next_epoch = int(sys.argv[3])
    max_epoch = int(sys.argv[4])

proof = open(in_path, "r")
jproof = json.load(proof)
proof.close()

start = 679 - 679 + 153
w = []
for i in range(0, 10):
    temp = []
    for j in range(0, 4):
        temp.append(jproof['inputs'][start + i*4 + j])
    w.append(temp)
# print(w)
start = 719 - 679 + 153
v = []
for i in range(0, 3):
    temp = []
    for j in range(0, 10):
        temp.append(jproof['inputs'][start + i*10 + j])
    v.append(temp)
# print(v)
start = 749 - 679 + 153
dw = []
for i in range(0, 10):
    temp = []
    for j in range(0, 4):
        temp.append(jproof['inputs'][start + i*4 + j])
    dw.append(temp)
# print(dw)
start = 789 - 679 + 153
dv = []
for i in range(0, 3):
    temp = []
    for j in range(0, 10):
        temp.append(jproof['inputs'][start + i*10 + j])
    dv.append(temp)
# print(dv)
start = 819 - 679 + 153
o = []
for i in range(0, 10):
    o.append(jproof['inputs'][start + i])
# print(o)
start = 829 - 679 + 153
OutputData = []
for i in range(0, 3):
    OutputData.append(jproof['inputs'][start + i])
# print(OutputData)
j = next_epoch
if max_epoch == 1:
    j = 0
# print(j)

f = open(out_path, "w")

d = open("d_in_d_out.json", "r")
jd = json.load(d)
d.close()

d_in = jd['d_in'][j]
d_out = [jd['d_out'][0][j], jd['d_out'][1][j], jd['d_out'][2][j]]

input_dict = {}
input_dict['w'] = w
input_dict['v'] = v
input_dict['dw'] = dw
input_dict['dv'] = dv
output_dict = {}
output_dict['o'] = o
output_dict['OutputData'] = OutputData
stru = [d_in, d_out, input_dict, output_dict]
json.dump(stru, f, indent=4)
