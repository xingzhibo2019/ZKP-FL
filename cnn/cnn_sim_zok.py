import numpy as np
import json
import ast
import time
"""
必要说明：
1.两个扩大后的数相乘后，需要除以EXTD，数据在计算后都只保留整数部分


"""
IMAGE_SIZE = 28
EXAM_NUM = 500
EXTD = np.asarray([1000000], dtype="uint64")
EXTD_OUT = 1000000
FILTER_NUM = 2
NODE_NUM = 10
INPUT_LEN = 13*13*FILTER_NUM
KER_SIZE = 3
POOL_SIZE = 2
LR = 10000
epochs = 20
minus = 9223372036854775807
max64 = 18446744073709551616
data_path = "./examples.json"

#=====保存数据=========
per = np.random.permutation(EXAM_NUM)
with open(data_path, "r") as data:
    proof_json = json.load(data)
    images = np.zeros((EXAM_NUM, 28, 28))
    labels = np.zeros(EXAM_NUM)

    for i in range(EXAM_NUM):
        for j in range(28):
            for k in range(28):
                #print(proof_json[0][i][j][k])
                images[i][j][k] = ast.literal_eval(proof_json[0][i][j][k])
    images = np.asarray(images, "uint64")
    images = images[per]
    for i in range(len(labels)):
        labels[i] = ast.literal_eval(proof_json[1][i])
    labels = np.asarray(labels, "uint64")
    labels = labels[per]


#images = ast.literal_eval(images)
print("images.shape", images.shape)
print("labels.shape", labels.shape)
#print("label=", labels)


def div(x, y)->int:
    if x<= minus and y <= minus:
        return int((x//y)%max64)
    elif x > minus and y <= minus:

        return int((max64-(max64-x)//y)%max64)

    elif x <= minus and y > minus:

        return int((max64-(x//(max64-y)))%max64)

    elif x > minus and y > minus:
        return int(((max64-x)//(max64-y))%max64)

"""
def mul(x, y):
    x = np.asarray([x], "uint64")
    y = np.asarray([y], "uint64")
    ret = np.asarray([0], "uint64")
    #print(x[0], y[0])
    if x[0] <= minus and y[0] <= minus:
        ret[0] = x[0]*y[0]
        return ret[0]
    elif x[0] > minus and y[0] <= minus:
        #print(x[0],y[0])
        ret[0] = max64-((max64-x[0])*y[0])
        return ret[0]
    elif x[0] <= minus and y[0] > minus:
        #print(x[0],y[0])
        ret[0] = int(max64-(x[0]*(max64-y[0])))%64
        #print(ret[0])
        return ret[0]
    elif x[0] > minus and y[0] > minus:
        ret[0] = (max64-x[0])*(max64-y[0])
        return ret[0]
"""
def mul(x, y)->int:
    if x<=minus and y<=minus:
        try:
            return int((x * y))
        except:
            print("x=", x, "y=", y)
            return x

    elif x<=minus and y>minus:
        return int((max64-x*(max64-y))%max64)
    elif x>=minus and y<minus:
        return int((max64-(max64-x)*y)%max64)
    elif x>=minus and y>=minus:
        return int(((max64-x)*(max64-y))%max64)

def add(x, y)->int:
    if x<=minus and y<=minus:
        return int((x+y)%max64)
    elif x<= minus and y>minus:
        if x>=max64-y:
            return int((x-(max64-y))%max64)
        else:
            return int((max64-((max64-y)-x))%max64)
    elif x>minus and y<=minus:
        if max64-x<=y:
            return int((y-(max64-x))%max64)
        else:
            return int((max64-((max64-x)-y))%max64)
    elif x>minus and y>minus:
        return int((max64-((max64-x)+(max64-y)))%max64)

def sub(x, y)->int:
    if x<=minus and y<=minus:
        if x>=y:
            return int((x-y)%max64)
        else:
            return int((max64-(y-x))%max64)
    elif x<=minus and y>minus:
        return int((x+(max64-y))%max64)
    elif x>minus and y<=minus:
        return int((max64-((max64-x)+y))%max64)
    elif x>minus and y>minus:
        if (max64-x)>=(max64-y):
            return int((max64-((max64-x)-(max64-y)))%max64)
        else:
            return int(((max64-y)-(max64-x))%max64)

#========卷积层========
#input:图片
def conv_forward(input, kernel):
    output = np.zeros((26, 26, FILTER_NUM), dtype="uint64")
    for i in range(26):
        for j in range(26):
            for f in range(FILTER_NUM):
                sum = 0
                for row in range(i, i+3):
                    for line in range(j, j+3):
                        #print("input[][]=",input[row][line])
                        sum = add(sum,input[row][line]*kernel[f][row-i][line-j])
                #print("sum=", sum)
                output[i][j][f] = div(sum, EXTD[0])
    #print("output=", output)
    return output
# print("conv.shape", conv_kernel.shape)
# #print(conv_kernel)

#print(conv_out.shape)
#TODO: def conv_backprop(dL_dout, kernel, input):
def conv_backprop(dL_dout, kernel, conv_input):
    dL_df = np.zeros((FILTER_NUM, 3, 3), dtype="uint64")
    out_kernel = np.zeros((FILTER_NUM, 3, 3), dtype="uint64")

    for i in range(26):
        for j in range(26):
            for f in range(FILTER_NUM):
                for i2 in range(3):
                    for j2 in range(3):
                        dL_df[f][i2][j2] = add(dL_df[f][i2][j2], div(mul(dL_dout[i][j][f], conv_input[i+i2][j+j2]),EXTD[0]))


    for i in range(FILTER_NUM):
        for j in range(3):
            for k in range(3):
                out_kernel[i][j][k] = sub(kernel[i][j][k], div(dL_df[i][j][k], LR))

    return out_kernel


#========降采样层===========

def comp_big(x, y):
    if x<=minus and y<=minus:
        return x if(x>=y) else y
    elif x>minus and y<=minus:
        return y
    elif x<=minus and y>minus:
        return x
    elif x>minus and y>minus:
        return x if x>=y else y


def pool_forward(input):
    output = np.zeros((13, 13, FILTER_NUM), dtype="uint64")
    for i in range(13):
        for j in range(13):
            for f in range(FILTER_NUM):
                max = 0
                for row in range(i * 2, i * 2 + 2):
                    for line in range(j * 2, j * 2 + 2):
                        max = comp_big(max, input[row][line][f])
                            #max = input[row][line][f]
                output[i][j][f] = max
    return output


#print("pool.shape=", pool_out.shape)

#TODO: pool_backprop
def pool_backprop(dL_dout, pool_input, pool_output):
    dL_dinput = np.zeros((26, 26, FILTER_NUM), dtype="uint64")
    #img_max = np.zeros(FILTER_NUM, dtype="uint64")
    for i in range(13):
        for j in range(13):
            img_max = pool_output[i][j]
            for i2 in range(2):
                for j2 in range(2):
                    for f2 in range(FILTER_NUM):
                        dL_dinput[i*2+i2][j*2+j2][f2]=\
                            dL_dout[i][j][f2] if img_max[f2]==pool_input[i*2+i2][j2+j2][f2] else 0
    return dL_dinput

#=========全连接==========
def relu(x):
    minus = 9223372036854775807
    if x>minus:
        return 0
    else:
        return x

#泰勒公式
def e(x):
    ex = add(EXTD[0], add(x, add(int(div(div(mul(x,x),EXTD[0]),2)), int(div(div(mul(div(mul(x,x),EXTD[0]),x),EXTD[0]),6)))))
    #print("aaa", x, int((x*x)/EXTD/2), int(((x*x)/EXTD)*x/EXTD/6))
    return ex
#输入在0-1
def log(x):
    #logx = x - int((x*x)/EXTD/2) + int(((x*x)/EXTD)*x/EXTD/3) - int((((x*x)/EXTD)*x/EXTD)*x/EXTD/4)
    logx = add(sub(sub(mul(3,x), int(div(11*EXTD[0],6))), int(div(div(mul(mul(3,x),x),EXTD[0]),2))), int(div(div(mul(div(mul(x,x),EXTD[0]),x),EXTD[0]),3)))
    #logx = x-EXTD - (x-EXTD)*(x-EXTD)/EXTD/2 + ((x-EXTD)*(x-EXTD)/EXTD)*(x-EXTD)/EXTD/3
    return logx

def full_forward(weights, biases, input):
    total = np.zeros(NODE_NUM, dtype="uint64")
    output = np.zeros(NODE_NUM, dtype="uint64")
    input_flat = np.zeros(INPUT_LEN, dtype="uint64")
    tmp = np.zeros(1, dtype="uint64")

    index = 0
    for i in range(13):
        for j in range(13):
            for k in range(FILTER_NUM):
                input_flat[index] = input[i][j][k]
                index = index + 1
    #print("weights=",weights)
    for i in range(NODE_NUM):
        for j in range(INPUT_LEN):

            #temp = np.zeros(1, "uint64")
            #print("flat=",input_flat[j], "weight=", weights[j][i])
            #temp[0] = mul(input_flat[j],weights[j][i])
            # print("temp1=",temp)
            # #temp[0]=max64
            # print("zzz=",temp[0])
            #temp[0] = div(temp[0], EXTD[0])
            # print("temp2=", temp)
            #print("total[i]=",total[i],"temp=",temp[0])
            #print("add=",add(total[i], temp[0]))
            #total[i] = add(total[i], temp[0])

            #print("div=",div(input_flat[j]*weights[j][i],EXTD))
            #tmp[0] = input_flat[j]*weights[j][i]

            total[i] = add(total[i], div(mul(input_flat[j],weights[j][i]),EXTD[0]))
        #print("total[i]=",total[i], "bias=",biases[i])
        total[i] = add(total[i], biases[i])
    #print("total=", total)
    sum = 0
    for i in range(NODE_NUM):
        #print("total[i", type(total[i]))
        sum = int(add(sum, e(total[i])))
    #print("sum0=", sum)
    #print(sum, type(sum))
    for i in range(NODE_NUM):
        output[i] = div(e(total[i]), div(sum, EXTD[0]))
    #print(output)
    return total, output, input_flat



def full_backprop(dL_dout, f_total, weights, biases, f_input_flat):
    output = np.zeros((13, 13, FILTER_NUM), dtype="uint64")
    dout_dt = np.zeros(NODE_NUM, dtype="uint64")
    total_exp = np.zeros(NODE_NUM, dtype="uint64")
    dL_dw = np.zeros((INPUT_LEN,NODE_NUM), dtype="uint64")
    out_weights = np.zeros((INPUT_LEN,NODE_NUM), dtype="uint64")
    out_bias = np.zeros(NODE_NUM, dtype="uint64")
    dL_dinput = np.zeros(INPUT_LEN, dtype="uint64")
    dL_dt= np.zeros(NODE_NUM, dtype="uint64")
    dt_db = 1
    grad_idx = 10
    #选出唯一一个不为0的grad
    for i in range(NODE_NUM):
        #grad = dL_dout[i] if(dL_dout[i]!=0) else grad
        grad_idx = i if(dL_dout[i]!=0) else grad_idx
    #链式法则

    #print("grad=", grad)

    total_sum = 0
    for i in range(NODE_NUM):
        total_exp[i] = e(f_total[i])
        total_sum = add(total_sum, total_exp[i])
        #print("fto=",f_total[i])

    #print("total_exp=", total_exp)
    for i in range(NODE_NUM):
        try:
            dout_dt[i] = int((max64-div(mul(div(total_exp[i], total_sum/EXTD[0]), total_exp[grad_idx]), total_sum))%max64)
            #dout_dt[i] = int((max64-div(mul(total_exp[i],total_exp[grad_idx]),total_sum/EXTD[0]*total_sum))%max64)
        except:
            dout_dt[i] = div(mul(div((total_sum - total_exp[grad_idx]), total_sum/EXTD[0]), total_exp[grad_idx]),total_sum)
            #print("aa=",div(mul(total_exp[i],total_exp[grad_idx]),total_sum/EXTD[0]*total_sum))

    dout_dt[grad_idx] = div(mul(div((total_sum - total_exp[grad_idx]), total_sum/EXTD[0]), total_exp[grad_idx]),total_sum)
    #print("dodt=", dout_dt)
    
    
    
    dt_dw = f_input_flat
    dt_dinput = weights
    #print("dtdw.type", type(dt_dw))

    #temp = dout_dt  #grad_idx是正数，其他是负数
    for i in range(NODE_NUM):
        #print("i=",i, "index=", grad_idx)
        #print("dL_dout=", max64-dL_dout[grad_idx], "dout_dt=", max64-dout_dt[i])
        #dL_dt[i] = div(mul((max64-dL_dout[grad_idx]),(max64-dout_dt[i])),EXTD[0]) if i!=grad_idx else div(mul((max64-dL_dout[grad_idx]),dout_dt[i]),EXTD[0])
        dL_dt[i] = div(mul(dL_dout[grad_idx], dout_dt[i]), EXTD[0])
        #dL_dt[i] = div(grad*dout_dt[i], EXTD)
    #print("dldt=",dL_dt)
    #print("dtdw=",dt_dw)
    #计算dL_dw
    for i in range(INPUT_LEN):
        for j in range(NODE_NUM):
            #print("dt_dw[i]*dL_dt[j]=",dt_dw[i]*dL_dt[j])
            dL_dw[i][j] = div(mul(dt_dw[i],dL_dt[j]),EXTD[0])

    #print("dldw=", dL_dw)
    #dL_db
    dL_db = dt_db * dL_dt
    #计算dL_dinput
    for i in range(INPUT_LEN):
        for j in range(NODE_NUM):
            dL_dinput[i] = add(dL_dinput[i], div(mul(dt_dinput[i][j],dL_dt[j]),EXTD[0]))
    #print("dldinput=",dL_dinput)
    #更新weights和biases
    for i in range(INPUT_LEN):
        for j in range(NODE_NUM):

            out_weights[i][j] = sub(weights[i][j], div(dL_dw[i][j],LR))
    #print("weight=",f_weights)
    for i in range(NODE_NUM):
        #print("bias=",biases[i],"div=",div(dL_db[i],LR), "sub=",sub(biases[i], div(dL_db[i],LR)))
        out_bias[i] = sub(biases[i], div(dL_db[i],LR))
    #reshape
    input_idx = 0
    for i in range(13):
        for j in range(13):
            for k in range(FILTER_NUM):
                output[i][j][k] = dL_dinput[input_idx]
                input_idx = input_idx + 1
    return output, out_weights, out_bias

#卷积核随机数初始化

conv_kernel = np.random.rand(FILTER_NUM, 3, 3)
conv_kernel = np.asarray(conv_kernel*EXTD[0], "uint64")
#print(conv_kernel.shape)
#print(conv_kernel)
weights = np.asarray(np.random.rand(INPUT_LEN, NODE_NUM)*EXTD[0]/INPUT_LEN, "uint64")
#print(weights)
biases = np.asarray(np.random.rand(NODE_NUM)*EXTD[0], "uint64")
#print("ori_weights=", weights, "bias=", biases)

#========开始训练===========
total_loss = 0
correct_num = 0
start_time = time.time()

for epoch in range(epochs):
    for exam_idx in range(EXAM_NUM):
        # print("===============now index", exam_idx)
        # exam_idx = 0
        conv_out = conv_forward(images[exam_idx], conv_kernel)

        pool_out = pool_forward(conv_out)
        # print("pool_out", pool_out)

        # full_out 范围(0,1)
        total, full_out, input_flat = full_forward(weights, biases, pool_out)

        # ====损失函数=====
        loss = np.asarray(np.array([0]), "uint64")
        # print("loss",log(full_out[labels[exam_idx]]))
        loss[0] = max64 - log(full_out[labels[exam_idx]])
        gradient = np.zeros(NODE_NUM, dtype="uint64")
        gradient[labels[exam_idx]] = max64 - div(EXTD[0] * EXTD[0], full_out[labels[exam_idx]])
        full_back_out, weights, biases = full_backprop(gradient, total, weights, biases, input_flat)
  
        pool_back_out = pool_backprop(full_back_out, conv_out, pool_out)

        argmax = 0
        out_idx = 0
        acc = 0
        for i in range(NODE_NUM):
            out_idx = i if full_out[i] > argmax else out_idx
            argmax = full_out[i] if full_out[i] > argmax else argmax
        acc = 1 if out_idx == labels[exam_idx] else 0
        total_loss = total_loss + loss[0]
        correct_num = correct_num + acc
        if (exam_idx % 100 == 99):
            end_time = time.time()
            print('[epoch=',epoch,'Step', exam_idx + 1, '] Past 100 steps: Average Loss ', total_loss, ' | Accuracy: ', correct_num,
                  "%")
            print("correct_num=", correct_num)
            print("运行时间：%.2fs" % (end_time - start_time))
            start_time = end_time
        total_loss = 0 if exam_idx % 100 == 99 else total_loss
        correct_num = 0 if exam_idx % 100 == 99 else correct_num







