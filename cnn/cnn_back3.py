import json

FILTER_NUM = 2
CONV_NUM = 26
POOL_NUM = 13
NODE_NUM = 10
INPUT_LEN = 13*13*FILTER_NUM

in_path = "conv_for/proof.json"
input_path = "in.json"
out_path = "cnn_back3/in.json"
back1_path = "cnn_back/proof.json"
out_json = []

dl_dt = []
with open(back1_path, "r") as for_data:
    back1_json = json.load(for_data)
    data = back1_json["inputs"]

    for i in range(NODE_NUM):
        dl_dt.append(data[i])
        #idx += 1
    out_json.append(dl_dt)


with open(in_path, "r") as for_data:
    proof_json = json.load(for_data)
#
    data = proof_json["inputs"]
    print("data_len=",len(data))
    idx = 26*26*2+13*13*2


    idx += NODE_NUM

    input_flat = []
    for i in range(INPUT_LEN):
        input_flat.append(data[idx])
        idx += 1
    out_json.append(input_flat)

with open(out_path, "w") as write_data:
    json.dump(out_json, write_data, indent=2)
