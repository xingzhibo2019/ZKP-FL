#!/bin/bash

#compile
time ./zokrates compile -i cnn/cnn_back2/cnn_back2.zok -o cnn/cnn_back2/out
#setup
time ./zokrates setup -i cnn/cnn_back2/out -p cnn/cnn_back2/proving.key -v cnn/cnn_back2/verification.key
#compute witness
time ./zokrates compute-witness --stdin --abi --abi-spec abi.json -i cnn/cnn_back2/out -o cnn/cnn_back2/witness < cnn/cnn_back2/in.json
#generate proof
time ./zokrates generate-proof -i cnn/cnn_back2/out -j cnn/cnn_back2/proof.json -p cnn/cnn_back2/proving.key -w cnn/cnn_back2/witness
#verify
time ./zokrates verify -j cnn/cnn_back2/proof.json -v cnn/cnn_back2/verification.key
