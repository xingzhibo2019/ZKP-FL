#!/bin/bash

./conv_for.sh

python for2back.py
./cnn_back.sh

python cnn_back2.py
./cnn_back2.sh

python cnn_back3.py
./cnn_back3.sh

python cnn_back4.py
./cnn_back4.sh

python cnn_back5.py
./cnn_back5.sh
