read line0 < ./init0.txt
read line1 < ./init1.txt
# update the client’s weight
cargo contract instantiate --constructor new --args $line0, $line1 --suri //Alice --salt $(date +%s) -x

