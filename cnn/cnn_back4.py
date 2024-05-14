import json

FILTER_NUM = 2
CONV_NUM = 26
POOL_NUM = 13
NODE_NUM = 10
INPUT_LEN = 13*13*FILTER_NUM

in_path = "conv_for/proof.json"
input_path = "in.json"
out_path = "cnn_back4/in.json"
back3_path = "cnn_back3/proof.json"
out_json = []

dl_dw = []
with open(back3_path, "r") as for_data:
    back3_json = json.load(for_data)
    data = back3_json["inputs"]

    idx = 0
    for i in range(INPUT_LEN):
        node_list = []
        for j in range(NODE_NUM):
            node_list.append(data[idx])
        idx += 1
        dl_dw.append(node_list)
    out_json.append(dl_dw)

with open(out_path, "w") as write_data:
    json.dump(out_json, write_data, indent=2)
