import json

FILTER_NUM = 2
CONV_NUM = 26
POOL_NUM = 13
NODE_NUM = 10
INPUT_LEN = 13*13*FILTER_NUM

in_path = "in.json"
back5_path = "cnn_back5/proof.json"#dpool
out_path = "conv_back/in.json"
out_json = []

with open(in_path, "r") as for_data:
    in_json = json.load(for_data)
    out_json.append(in_json[0])
    #out_json.append(in_json[1])

with open(back5_path, "r") as for_data:
    back5_json = json.load(for_data)
    data = back5_json["inputs"]
    dpool = []
    idx = 0
    for i in range(26):
        div2 = []
        for j in range(26):
            div3 = []
            for k in range(FILTER_NUM):
                div3.append(data[idx])
                idx += 1
            div2.append(div3)
        dpool.append(div2)

    out_json.append(dpool)

with open(out_path, "w") as write_data:
    json.dump(out_json, write_data, indent=2)
