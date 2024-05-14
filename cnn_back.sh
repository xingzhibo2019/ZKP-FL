#!/bin/bash

#compile
time ./zokrates compile --curve bls12_381 -i cnn/cnn_back/cnn_back.zok -o cnn/cnn_back/out
#setup
time ./zokrates setup --proving-scheme g16 -i cnn/cnn_back/out -p cnn/cnn_back/proving.key -v cnn/cnn_back/verification.key
#compute witness
time ./zokrates compute-witness --stdin --abi --abi-spec abi.json -i cnn/cnn_back/out -o cnn/cnn_back/witness < cnn/cnn_back/in.json
#generate proof
time ./zokrates generate-proof --proving-scheme g16 -i cnn/cnn_back/out -j cnn/cnn_back/proof.json -p cnn/cnn_back/proving.key -w cnn/cnn_back/witness
#verify
time ./zokrates verify -j cnn/cnn_back/proof.json -v cnn/cnn_back/verification.key
