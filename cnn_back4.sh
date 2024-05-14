#!/bin/bash

#compile
time ./zokrates compile -i cnn/cnn_back4/cnn_back4.zok -o cnn/cnn_back4/out
#setup
time ./zokrates setup -i cnn/cnn_back4/out -p cnn/cnn_back4/proving.key -v cnn/cnn_back4/verification.key
#compute witness
time ./zokrates compute-witness --stdin --abi --abi-spec abi.json -i cnn/cnn_back4/out -o cnn/cnn_back4/witness < cnn/cnn_back4/in.json
#generate proof
time ./zokrates generate-proof -i cnn/cnn_back4/out -j cnn/cnn_back4/proof.json -p cnn/cnn_back4/proving.key -w cnn/cnn_back4/witness
#verify
time ./zokrates verify -j cnn/cnn_back4/proof.json -v cnn/cnn_back4/verification.key
