#!/bin/bash

#compile
time ./zokrates compile -i cnn/conv_for/conv_for.zok -o cnn/conv_for/out
#setup
time ./zokrates setup -i cnn/conv_for/out -p cnn/conv_for/proving.key -v cnn/conv_for/verification.key
#compute witness
time ./zokrates compute-witness --stdin --abi --abi-spec abi.json -i cnn/conv_for/out -o cnn/conv_for/witness < cnn/in.json
#generate proof
time ./zokrates generate-proof -i cnn/conv_for/out -j cnn/conv_for/proof.json -p cnn/conv_for/proving.key -w cnn/conv_for/witness
#verify
time ./zokrates verify -j cnn/conv_for/proof.json -v cnn/conv_for/verification.key
