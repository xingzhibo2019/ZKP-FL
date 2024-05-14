import numpy
import gzip
import json

IMAGE_SIZE = 28
NUM_LABELS = 10
DATA_NUM = 2000

def extract_data(filename, num):
    with gzip.open(filename) as bytestream:
        bytestream.read(16)  # 跳过前16个字符
        buf = bytestream.read(IMAGE_SIZE * IMAGE_SIZE * num)
        data = numpy.frombuffer(buf, dtype=numpy.uint8).astype(numpy.float32)
        data = data / 255  # 划分到[0, 1]范围内
        data = data.reshape(num, IMAGE_SIZE, IMAGE_SIZE)
    return data

def extract_label(filename, num):

    with gzip.open(filename) as bytestream:
        bytestream.read(8)
        buf = bytestream.read(1 * num)
        labels = numpy.frombuffer(buf, dtype=numpy.uint8).astype(numpy.int64)
        num_labels_data = len(labels)
        lable = numpy.zeros(num_labels_data)
        for i, num in enumerate(labels):
            lable[i] = num
        one_hot_encoding = numpy.zeros((num_labels_data, NUM_LABELS))
        one_hot_encoding[numpy.arange(num_labels_data), labels] = 1
        one_hot_encoding = numpy.reshape(one_hot_encoding, [-1, NUM_LABELS])
        #print("lable=", lable)
        #print("one-hot", one_hot_encoding)
    return lable


data_path = "../实验/mnist/train-images-idx3-ubyte.gz"
label_path = "../实验/mnist/train-labels-idx1-ubyte.gz"
out_path = "examples.json"
print("Reading data...")
data = extract_data(data_path, DATA_NUM)
print("Reading labels...")
labels = extract_label(label_path,DATA_NUM)
print(labels)
#print(data)
res = {
    "examples": [],
    "labels": []
}

zok = []
exams = []
for i in range(DATA_NUM):
    example = numpy.around(data[i] * 10**6).astype("uint64").tolist()
    for j, line in enumerate(example):
        #print("line=", line, "i=", i)
        for k, val in enumerate(line):
            #print("val=", val)
            example[j][k] = str(val)

    # for j, val in enumerate(label):
    #     label[j] = str(val)
        #print(label[j])
    exams.append(example)


label = numpy.around(labels).astype("uint64").tolist()
print("lable=", label)
for i, val in enumerate(label):
    label[i] = str(label[i])
#label = str(label)
zok.append(exams)
zok.append(label)

with open(out_path, "w") as write_data:
    #json.dump(res, write_data, indent=2)
    json.dump(zok, write_data, indent=2)
