#!/bin/bash

#please edit $max and iter cond

zero=0
one=1
imax=1
jmax=1

# compile (once only
./zokrates compile -i iris/func1/main.zok -o iris/func1/out -s iris/func1/abi.json

# perform the setup phase (once only
time ./zokrates setup -i iris/func1/out -p iris/func1/proving.key -v iris/func1/verification.key

# execute the program

mkdir iris/e0s0
cd iris
python genorigininput.py
cd ..

for i in {0..1}
do
    for j in {0..1}
    do
        ./zokrates compute-witness --stdin --abi --abi-spec iris/func1/abi.json -i iris/func1/out -o iris/e${i}s${j}/witness < iris/e${i}s${j}/zok-in.json
        time ./zokrates generate-proof -i iris/func1/out -j iris/e${i}s${j}/proof.json -p iris/func1/proving.key -w iris/e${i}s${j}/witness

	    # here is eisj & eisj-1 or eis0 & ei-1sjmax or e0s0 & jump
        cd iris
        if [[ ${i} == $zero ]] && [[ ${j} == $zero ]]
        then
            python edit.py e${i}s${j}/proof.json func1/verification.key e${i}s${j}/newproof.json e${i}s${j}/newverification.key e${i}s${j}/output.point e${i}s${j}/input.point 0
        elif [[ ${j} == $zero ]]
        then
            python edit.py e${i}s${j}/proof.json func1/verification.key e${i}s${j}/newproof.json e${i}s${j}/newverification.key e${i}s${j}/output.point e${i}s${j}/input.point e$((${i}-$one))s${jmax}/output.point
            python sigma.py 1 e$((${i}-$one))s${jmax}/output.point e${i}s${j}/input.point e${i}s${j}/sigmaproof.json
            python sigma.py 2 e${i}s${j}/sigmaproof.json
        else
            python edit.py e${i}s${j}/proof.json func1/verification.key e${i}s${j}/newproof.json e${i}s${j}/newverification.key e${i}s${j}/output.point e${i}s${j}/input.point e${i}s$((${j}-$one))/output.point
            python sigma.py 1 e${i}s$((${j}-$one))/output.point e${i}s${j}/input.point e${i}s${j}/sigmaproof.json
            python sigma.py 2 e${i}s${j}/sigmaproof.json
        fi
        cd ..
        time ./zokrates verify -j iris/e${i}s${j}/newproof.json -v iris/e${i}s${j}/newverification.key

        if [ $j == $jmax ]
        then
            mkdir iris/e$((${i}+$one))s0
            cd iris
            python getnextinput.py e${i}s${j} e$((${i}+$one))s0 0 1
            cd ..
        else
            mkdir iris/e${i}s$((${j}+$one))
            cd iris
            python getnextinput.py e${i}s${j} e${i}s$((${j}+$one)) $((${j}+$one)) 0
            cd ..
        fi

    done
done



#check with python

# cd iris
# python bigtest.py $imax $jmax

# generate a proof of computation



# edit vk & proof
# python edit.py ${path}/ ${choice}

# verify the edited one
# ./zokrates verify -j ${path}/new_proof.json -v ${path}/new_verification.key

