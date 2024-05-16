read line0 < ./cli0.txt
read line1 < ./cli1.txt
# update the client’s weight
cargo contract call --contract ${1} --message up_data --args 0 $line0 --suri //Alice -x
cargo contract call --contract ${1} --message up_data --args 1 $line1 --suri //Alice -x
# aggregation
cargo contract call --contract ${1} --message cal --suri //Alice
