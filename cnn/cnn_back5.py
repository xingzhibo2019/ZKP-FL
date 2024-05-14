import json

FILTER_NUM = 2
CONV_NUM = 26
POOL_NUM = 13
NODE_NUM = 10
INPUT_LEN = 13*13*FILTER_NUM

in_path = "in.json"
back1_path = "cnn_back/proof.json" #dl_dt
back2_path = "cnn_back2/proof.json"#dl_dinput
for_path = "conv_for/proof.json"#conv_out, pool_out
out_path = "cnn_back5/in.json"
out_json = []

with open(in_path, "r") as for_data:
    in_json = json.load(for_data)
    out_json.append(in_json[0])
    #out_json.append(in_json[1])

with open(back1_path, "r") as for_data:
    back1_json = json.load(for_data)
    data = back1_json["inputs"]
    dl_dt = []
    for i in range(NODE_NUM):
        dl_dt.append(data[i])
    out_json.append(dl_dt)


with open(back2_path, "r") as for_data:
    back2_json = json.load(for_data)
    data = back2_json["inputs"]
    idx = 0
    dl_dinput = []
    for i in range(13):
        div2 = []
        for j in range(13):
            div3 = []
            for k in range(FILTER_NUM):
                div3.append(data[idx])
                idx += 1
            div2.append(div3)
        dl_dinput.append(div2)
    out_json.append(dl_dinput)

with open(for_path, "r") as for_data:
    for_json = json.load(for_data)
    data = for_json["inputs"]
    idx = 0
    conv_out = []
    for i in range(CONV_NUM):
        div2 = []
        for j in range(CONV_NUM):
            div3 = []
            for k in range(FILTER_NUM):
                div3.append(data[idx])
                idx += 1
            div2.append(div3)
        conv_out.append(div2)
    out_json.append(conv_out)

    pool_out = []
    for i in range(POOL_NUM):
        div2 = []
        for j in range(POOL_NUM):
            div3 = []
            for k in range(FILTER_NUM):
                div3.append(data[idx])
                idx += 1
            div2.append(div3)
        pool_out.append(div2)
    out_json.append(pool_out)


with open(out_path, "w") as write_data:
    json.dump(out_json, write_data, indent=2)