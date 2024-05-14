import json
import secrets
import sys
from py_ecc import bn128
from py_ecc import fields


proof_path = "e0s0/proof.json"
vk_path = "verification1.key"
newproof_path = "newproof.json"
newvk_path = "newverification.key"
outputpoint_path = "output.point"
inputpoint_path = "input.point"
old_outputpoint_path = "oldoutput.point"
if len(sys.argv) > 1:
	proof_path = sys.argv[1]
	vk_path = sys.argv[2]
	newproof_path = sys.argv[3]
	newvk_path = sys.argv[4]
	outputpoint_path = sys.argv[5]
	inputpoint_path = sys.argv[6]
	old_outputpoint_path = sys.argv[7]

times = 0

proof = open(proof_path, "r")
jproof = json.load(proof)
proof.close()
vk = open(vk_path, "r")
jvk = json.load(vk)
vk.close()
if old_outputpoint_path != "0":
	oldout = open(old_outputpoint_path, "r")
	joldout = json.load(oldout)
	oldout.close()

rand_list = []
p0 = (fields.bn128_FQ(int(jvk['gamma_abc'][0][0], 16)), fields.bn128_FQ(int(jvk['gamma_abc'][0][1], 16)))

def process(i, new):
	global p0
	global rand_list

	if new == 1:
		r = secrets.randbelow(fields.field_properties['bn128']['field_modulus'])
		rand_list.append(r)
	elif old_outputpoint_path == "0":
		r = r = secrets.randbelow(fields.field_properties['bn128']['field_modulus'])
	else:
		r = int(joldout['rand_list'][i])
	p = (fields.bn128_FQ(int(jvk['gamma_abc'][i+1][0], 16)), fields.bn128_FQ(int(jvk['gamma_abc'][i+1][1], 16)))
	x = int(jproof['inputs'][i], 16) + r
	if x == 0:
		_p = (0, 0)
	else:
		_p = bn128.multiply(p, x)
	pr = bn128.multiply(p, r)
	p0 = bn128.add(p0, bn128.neg(pr))
	
	pointp = ['{:#066x}'.format(int(p[0])), '{:#066x}'.format(int(p[1]))]
	point_p = ['{:#066x}'.format(int(_p[0])), '{:#066x}'.format(int(_p[1]))]

	jpoint = {}
	jpoint['g'] = pointp
	jpoint['gx'] = point_p
	jpoint['x'] = x

	jproof['inputs'][i] = '{:#066x}'.format(1)
	jvk['gamma_abc'][i+1] = point_p
	return jpoint


def main():
	joutputpoint = {}
	joutputpoint['g'] = []
	joutputpoint['gx'] = []
	joutputpoint['x'] = []
	for i in range(153, 306):
		jpoint = process(i, 1)
		joutputpoint['g'].append(jpoint['g'])
		joutputpoint['gx'].append(jpoint['gx'])
		joutputpoint['x'].append(jpoint['x'])
	joutputpoint['rand_list'] = rand_list
	fn = open(outputpoint_path, "w")
	json.dump(joutputpoint, fn, indent=2)
	fn.close()

	jinputpoint = {}
	jinputpoint['g'] = []
	jinputpoint['gx'] = []
	jinputpoint['x'] = []
	for i in range(0, 153):
		jpoint = process(i, 0)
		jinputpoint['g'].append(jpoint['g'])
		jinputpoint['gx'].append(jpoint['gx'])
		jinputpoint['x'].append(jpoint['x'])
	fn = open(inputpoint_path, "w")
	json.dump(jinputpoint, fn, indent=2)
	fn.close()

	pointp0 = ['{:#066x}'.format(int(p0[0])), '{:#066x}'.format(int(p0[1]))]
	jvk['gamma_abc'][0] = pointp0

	new_proof = open(newproof_path, "w")
	json.dump(jproof, new_proof, indent=2)
	new_proof.close()
	print("written proof to " + newproof_path)
	new_vk = open(newvk_path, "w")
	json.dump(jvk, new_vk, indent=2)
	new_vk.close()
	print("written vk to " + newvk_path)


main()
