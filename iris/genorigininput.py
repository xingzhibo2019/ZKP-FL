import json

class Input:
    pass
class Output:
    pass
input = Input()
output = Output()

input.w = [["9806218", "5446931", "0xffffffffff3916a6", "0xffffffffff762166"], ["0xffffffffffca61fd", "0xfffffffffff2bd37", "0xffffffffffa8c8db", "0xffffffffff813572"], ["1284529", "0xffffffffffa69114", "3703291", "11129511"], ["0xffffffffff3a2407", "0xffffffffff67d890", "0xffffffffffdb05f6", "0xffffffffffe3eb5b"], ["0xffffffffffc5042f", "0xffffffffffb4ad4c", "0xffffffffffa542e1", "0xffffffffff8cf36d"], ["0xffffffffffb5302b", "12087752", "0xfffffffffe3c3882", "0xfffffffffef2e9a0"], ["2148455", "964252", "0xffffffffff3bc21c", "0xffffffffffc49836"], ["0xffffffffffb5302b", "12087752", "0xfffffffffe3c3882", "0xfffffffffef2e9a0"], ["0xffffffffff3a2407", "0xffffffffff67d890", "0xffffffffffdb05f6", "0xffffffffffe3eb5b"], ["0xffffffffff226b44", "0xffffffffffa71205", "0xffffffffff6c3db6", "0xfffffffffeec49d5"]]

input.v = [["0xfffffffffff71d3d", "3489567", "6876553", "0xffffffffffe6e223", "0xffffffffffa370fd", "9246780", "578612", "9246780", "0xffffffffffe6e223", "5251732"], ["28458211", "8042554", "0xffffffffff375129", "5632139", "14709860", "0xfffffffffeba9e38", "10100404", "0xfffffffffeba9e38", "5632139", "0xffffffffff5f8e5e"], ["0xffffffffff34fd58", "0xffffffffff1b88f0", "27421729", "1277007", "0xffffffffff9f157e", "14929907", "0xffffffffff0aea7b", "14929907", "1277007", "2903503"]]

input.dw = [["5683", "4890", "6059", "6504"], ["2541", "2190", "2710", "2907"], ["0xffffffffffffe996", "0xffffffffffffecaa", "0xffffffffffffe818", "0xffffffffffffe65b"], ["181", "152", "192", "207"], ["1551", "1329", "1653", "1776"], ["0xfffffffffffffd2b", "0xfffffffffffffd92", "0xfffffffffffffcfb", "0xfffffffffffffcc2"], ["3421", "2949", "3649", "3915"], ["0xfffffffffffffd2b", "0xfffffffffffffd92", "0xfffffffffffffcfb", "0xfffffffffffffcc2"], ["181", "152", "192", "207"], ["0xffffffffffffff48", "0xffffffffffffff65", "0xffffffffffffff3d", "0xffffffffffffff2e"]]

input.dv = [["676", "374", "1534", "246", "303", "67", "497", "67", "246", "51"], ["2974", "1675", "6694", "1126", "1374", "309", "2211", "309", "1126", "240"], ["0xffffffffffffed98", "0xfffffffffffff5b5", "0xffffffffffffd673", "0xfffffffffffff925", "0xfffffffffffff799", "0xfffffffffffffe1d", "0xfffffffffffff261", "0xfffffffffffffe1d", "0xfffffffffffff925", "0xfffffffffffffe8d"]]

output.o = ["3217097", "1780139", "7294643", "1170297", "1444860", "323034", "2364503", "323034", "1170297", "244537"]

output.OutputData = ["5052602", "5197282", "9665258"]

f = open("e0s0/zok-in.json", "w")

d = open("d_in_d_out.json", "r")
jd = json.load(d)
d.close()

d_in = jd['d_in'][0]
d_out = [jd['d_out'][0][0], jd['d_out'][1][0], jd['d_out'][2][0]]
input_dict = {}
input_dict['w'] = input.w
input_dict['v'] = input.v
input_dict['dw'] = input.dw
input_dict['dv'] = input.dv
output_dict = {}
output_dict['o'] = output.o
output_dict['OutputData'] = output.OutputData
stru = [d_in, d_out, input_dict, output_dict]
json.dump(stru, f,indent=4)
