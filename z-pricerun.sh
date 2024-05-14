#!/bin/bash

zero=0
one=1

# compile (once only
./zokrates compile -i price/func1/main.zok -o price/func1/out -s price/func1/abi.json

# perform the setup phase (once only
time ./zokrates setup -i price/func1/out -p price/func1/proving.key -v price/func1/verification.key

# execute the program

for i in {0..9}
do
    mkdir price/e${i}
    cd price
    python getnextinput.py ${i}
    cd ..

    ./zokrates compute-witness --stdin --abi --abi-spec price/func1/abi.json -i price/func1/out -o price/e${i}/witness < price/e${i}/zok-in.json
    time ./zokrates generate-proof -i price/func1/out -j price/e${i}/proof.json -p price/func1/proving.key -w price/e${i}/witness

    cd price
	if [[ ${i} == $zero ]]
	then
    	 python edit.py e${i}/proof.json func1/verification.key e${i}/newproof.json e${i}/newverification.key e${i}/output.point e${i}/input.point 0
	else
		echo "number1"
		python edit.py e${i}/proof.json func1/verification.key e${i}/newproof.json e${i}/newverification.key e${i}/output.point e${i}/input.point e$((${i}-$one))/output.point
	fi
    if [[ ${i} > $zero ]]
    then
	echo "number2"
        python sigma.py 1 e$((${i}-$one))/output.point e${i}/input.point e${i}/sigmaproof.json	
	echo "number3"        
	python sigma.py 2 e${i}/sigmaproof.json
    fi
    cd ..
    time ./zokrates verify -j price/e${i}/proof.json -v price/func1/verification.key

done


