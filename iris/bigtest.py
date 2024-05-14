from fractions import Fraction
import py_ecc
import json
import sys


class Input:
    pass
class Output:
    pass


input = Input()
output = Output() 
# those input and output are processed from raw data, which can throw into the model directely, which accuracy is 96.00%
input.d_in = [[4090909, 7352941, 2028986, 3235294],[3636364, 5882353, 2028986, 3235294],[3181818, 6470588, 1884058, 3235294],[2954545, 6176471, 2173913, 3235294],[3863636, 7647059, 2028986, 3235294],[4772727, 8529412, 2463768, 3823529],[2954545, 7058824, 2028986, 3529412],[3863636, 7058824, 2173913, 3235294],[2500000, 5588235, 2028986, 3235294],[3636364, 6176471, 2173913, 2941176],[4772727, 7941176, 2173913, 3235294],[3409091, 7058824, 2318841, 3235294],[3409091, 5882353, 2028986, 2941176],[2272727, 5882353, 1594203, 2941176],[5681818, 8823529, 1739130, 3235294],[5454545, 10000000, 2173913, 3823529],[4772727, 8529412, 1884058, 3823529],[4090909, 7352941, 2028986, 3529412],[5454545, 8235294, 2463768, 3529412],[4090909, 8235294, 2173913, 3529412],[4772727, 7058824, 2463768, 3235294],[4090909, 7941176, 2173913, 3823529],[2954545, 7647059, 1449275, 3235294],[4090909, 6764706, 2463768, 4117647],[3409091, 7058824, 2753623, 3235294],[8409091, 6470588, 6811594, 6764706],[7045455, 6470588, 6521739, 7058824],[8181818, 6176471, 7101449, 7058824],[5000000, 3823529, 5797101, 6470588],[7272727, 5294118, 6666667, 7058824],[5454545, 5294118, 6521739, 6470588],[6818182, 6764706, 6811594, 7352941],[3636364, 4117647, 4782609, 5588235],[7500000, 5588235, 6666667, 6470588],[4318182, 5000000, 5652174, 6764706],[3863636, 2941176, 5072464, 5588235],[5909091, 5882353, 6086957, 7058824],[6136364, 3529412, 5797101, 5588235],[6363636, 5588235, 6811594, 6764706],[5227273, 5588235, 5217391, 6470588],[7727273, 6176471, 6376812, 6764706],[5227273, 5882353, 6521739, 7058824],[5681818, 5000000, 5942029, 5588235],[6590909, 3529412, 6521739, 7058824],[5227273, 4411765, 5652174, 5882353],[5909091, 6470588, 6956522, 7941176],[6363636, 5294118, 5797101, 6470588],[6818182, 4411765, 7101449, 7058824],[6363636, 5294118, 6811594, 6176471],[7045455, 5588235, 6231884, 6470588],[6818182, 6764706, 8695652, 10000000],[5681818, 5000000, 7391304, 8235294],[8636364, 5882353, 8550725, 8823529],[6818182, 5588235, 8115942, 7941176],[7272727, 5882353, 8405797, 9117647],[9772727, 5882353, 9565217, 8823529],[3636364, 4411765, 6521739, 7647059],[9090909, 5588235, 9130435, 7941176],[7727273, 4411765, 8405797, 7941176],[8863636, 7647059, 8840580, 10000000],[7272727, 6470588, 7391304, 8529412],[7045455, 5000000, 7681159, 8235294],[7954545, 5882353, 7971014, 8823529],[5454545, 4411765, 7246377, 8529412],[5681818, 5294118, 7391304, 9705882],[7045455, 6470588, 7681159, 9411765],[7272727, 5882353, 7971014, 7941176],[10000000, 8235294, 9710145, 9117647],[10000000, 4705882, 10000000, 9411765],[6136364, 3529412, 7246377, 7058824],[8181818, 6470588, 8260870, 9411765],[5227273, 5294118, 7101449, 8529412],[10000000, 5294118, 9710145, 8529412],[6818182, 5000000, 7101449, 7941176],[7727273, 6764706, 8260870, 8823529]]
input.w = [[1, 1, -10000000, 1],[-10000000, 1, -10000000, -10000000],[1, 1, -10000000, 1],[-10000000, -10000000, 1, 1],[1, 1, 1, 1],[1, 1, -10000000, 1],[1, 1, -10000000, 1],[1, 1, -10000000, 1],[-10000000, -10000000, 1, 1],[-10000000, -10000000, 1, -10000000]]
input.v = [[-10000000, -10000000, 1, 1, -10000000, 1, -10000000, 1, 1, 1],[1, 1, 1, -10000000, -10000000, -10000000, -10000000, -10000000, -10000000, -10000000],[-10000000, -10000000, 1, 1, -10000000, 1, -10000000, 1, 1, 1]]
input.dw = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
input.dv = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
output.d_out = [[10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000],[5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000],[5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 5000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000]]
output.o = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
output.OutputData = [1, 1, 1]
bigest = 1
test = []

E9 = 10000000
epoch = 1199
sample = 74
path = "proof.json"
if len(sys.argv) > 1:
    epoch = int(sys.argv[1])
    sample = int(sys.argv[2])
    path = "e"+str(epoch)+"s"+str(sample)+"/"+"proof.json"

def conv(a):
    global bigest
    if a > bigest:
        bigest = a
    # print(a)
    return int(a)

def pow(a, b): # a is E9
    result = 1*E9 # result is E9
    for i in range(0, b):
        result = conv((result * a)/E9)
    return result
    

# the PROBLEM ACTIVATION FUNCTION!!!
def activation(x): # x is E9
    msum = (-1 * x) # msum is E9
    taylor = conv(1*E9 + msum) # taylor is E9
    n = 1*E9 # n is E9
    for m in range(2, 6):
        n *= m
        taylor = conv(taylor + conv((pow(msum, m) / n)*E9))
    return conv((1*E9 / conv(1*E9 + taylor))*E9) # return is E9

def computO(var):
    sum = 0
    for i in range(0,10):
        sum = 0
        for j in range(0,4):
            sum = conv(sum + conv((input.w[i][j] * input.d_in[var][j])/E9)) # sum is E9
            output.o[i] = activation(sum) # o is E9
    for i in range(0,3):
        sum = 0
        for j in range(0,10):
            sum = conv(sum + conv((input.v[i][j] * output.o[j])/E9)) # sum is E9
        output.OutputData[i] = sum # OutputData is E9
    
def BackUpdate(var):
    t = 0
    StudyRate_A = conv(0.02*E9) #).limit_denominator(10000)
    StudyRate_B = conv(0.04*E9) #).limit_denominator(10000)
    StudyRate_a = conv(0.02*E9) #).limit_denominator(10000)
    StudyRate_b = conv(0.03*E9) #).limit_denominator(10000)
    for i in range(0,10):
        t = 0
        for j in range(0,3):
            t = conv(t + conv((conv(output.OutputData[j] - output.d_out[j][var]) * input.v[j][i])/E9)) # t is E9
            input.dv[j][i] = conv(conv((StudyRate_A * input.dv[j][i])/E9) + conv((conv((StudyRate_B * conv(output.OutputData[j] - output.d_out[j][var]))/E9) * output.o[i])/E9)) # dv is E9
            input.v[j][i] = conv(input.v[j][i] - input.dv[j][i])
        for j in range(0,4):
            input.dw[i][j] = conv(conv((StudyRate_a * input.dw[i][j])/E9) + conv((conv((conv((conv((StudyRate_b * t)/E9) * output.o[i])/E9) * conv(1*E9 - output.o[i]))/E9) * input.d_in[var][j])/E9)) # dw is E9
            input.w[i][j] = conv(input.w[i][j] - input.dw[i][j])
    # return input

def main():
    global input
    global output
    for k in range(0, epoch + 1):
        for j in range(0, sample + 1): # sample size
            # if k == epoch and j == 67:
            #     return
            computO(j)
            BackUpdate(j)

def tshow1(array, m, n):
    global test
    print("{", end="")
    for i in range (0, m):
        print("{", end="")
        for j in range(0, n):
            print("{:.9f}".format(array[i][j]/E9), end="")
            if j != n-1:
                print(",", end=" ")
        print("}", end="")
        if i != m-1:
            print(",", end=" ")
    print("};")

def tshow2(array, m):
    global test
    print("{", end="")
    for i in range (0, m):
        print("{:.9f}".format(array[i]/E9), end="")
        if i != m-1:
            print(",", end=" ")
    print("};")

def tinyshow1(array, m, n):
    global test
    print("[", end="")
    for i in range (0, m):
        print("[", end="")
        for j in range(0, n):
            if array[i][j] < 0:
                print("\"0x{:x}\"".format(array[i][j]&0xffffffffffffffff), end="")
            else:
                print("\"{:d}\"".format(array[i][j]), end="")
            test.append(array[i][j])
            if j != n-1:
                print(",", end=" ")
        print("]", end="")
        if i != m-1:
            print(",", end=" ")
    print("]")

def tinyshow2(array, m):
    global test
    print("[", end="")
    for i in range (0, m):
        if array[i] < 0:
            print("\"0x{:x}\"".format(array[i]&0xffffffffffffffff), end="")
        else:
            print("\"{:d}\"".format(array[i]), end="")
        test.append(array[i])
        if i != m-1:
            print(",", end=" ")
    print("]")

def show():
    print("\ninput.w = ", end="")
    tinyshow1(input.w, 10, 4)
    print("\ninput.v = ", end="")
    tinyshow1(input.v, 3, 10)
    print("\ninput.dw = ", end="")
    tinyshow1(input.dw, 10, 4)
    print("\ninput.dv = ", end="")
    tinyshow1(input.dv, 3, 10)
    print("\noutput.o = ", end="")
    tinyshow2(output.o, 10)
    print("\noutput.OutputData = ", end="")
    tinyshow2(output.OutputData, 3)

    # print("\ndouble w_[Neuron][In] = ", end="")
    # tshow1(input.w, 10, 4)
    # print("\ndouble v_[Out][Neuron] = ", end="")
    # tshow1(input.v, 3, 10)
    # print("\ndouble dw_[Neuron][In] = ", end="")
    # tshow1(input.dw, 10, 4)
    # print("\ndouble dv_[Out][Neuron] = ", end="")
    # tshow1(input.dv, 3, 10)
    # print("\ndouble o_[Neuron] = ", end="")
    # tshow2(output.o, 10)
    # print("\ndouble OutputData_[Out] = ", end="")
    # tshow2(output.OutputData, 3)

def check():
    a = []
    proof = open(path, "r")
    jproof = json.load(proof)
    proof.close()
    start = 679 - 679 + 153
    for i in range(0, 10):
        for j in range(0, 4):
            a.append(jproof['inputs'][start + i*4 + j])
    start = 719 - 679 + 153
    for i in range(0, 3):
        for j in range(0, 10):
            a.append(jproof['inputs'][start + i*10 + j])
    start = 749 - 679 + 153
    for i in range(0, 10):
        for j in range(0, 4):
            a.append(jproof['inputs'][start + i*4 + j])
    start = 789 - 679 + 153
    for i in range(0, 3):
        for j in range(0, 10):
            a.append(jproof['inputs'][start + i*10 + j])
    start = 819 - 679 + 153
    for i in range(0, 10):
        a.append(jproof['inputs'][start + i])
    start = 829 - 679 + 153
    for i in range(0, 3):
        a.append(jproof['inputs'][start + i])
    i = 0
    flag = 0
    for item in a:
        num = int(item, base=16)
        if num > int("0x7fffffffffffffff", base=16):
            num -= int("0xffffffffffffffff", base=16)+1
        if num != test[i]:
            print(i, num, test[i])
            flag = 1
        i += 1
    if flag == 0:
        print("good zok!")


main()
show()
check()
print("bigest =", bigest)

