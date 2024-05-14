#!/bin/bash

#compile
time ./zokrates compile -i cnn/cnn_back3/cnn_back3.zok -o cnn/cnn_back3/out
#setup
time ./zokrates setup -i cnn/cnn_back3/out -p cnn/cnn_back3/proving.key -v cnn/cnn_back3/verification.key
#compute witness
time ./zokrates compute-witness --stdin --abi --abi-spec abi.json -i cnn/cnn_back3/out -o cnn/cnn_back3/witness < cnn/cnn_back3/in.json
#generate proof
time ./zokrates generate-proof -i cnn/cnn_back3/out -j cnn/cnn_back3/proof.json -p cnn/cnn_back3/proving.key -w cnn/cnn_back3/witness
#verify
time ./zokrates verify -j cnn/cnn_back3/proof.json -v cnn/cnn_back3/verification.key
