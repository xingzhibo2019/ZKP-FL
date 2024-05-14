#!/bin/bash

#compile
time ./zokrates compile -i cnn/cnn_back5/cnn_back5.zok -o cnn/cnn_back5/out
#setup
time ./zokrates setup -i cnn/cnn_back5/out -p cnn/cnn_back5/proving.key -v cnn/cnn_back5/verification.key
#compute witness
time ./zokrates compute-witness --stdin --abi --abi-spec abi.json -i cnn/cnn_back5/out -o cnn/cnn_back5/witness < cnn/cnn_back5/in.json
#generate proof
time ./zokrates generate-proof -i cnn/cnn_back5/out -j cnn/cnn_back5/proof.json -p cnn/cnn_back5/proving.key -w cnn/cnn_back5/witness
#verify
time ./zokrates verify -j cnn/cnn_back5/proof.json -v cnn/cnn_back5/verification.key
