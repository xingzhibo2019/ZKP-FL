import json
import secrets
import sys
from Cryptodome.Hash import SHA3_256
from py_ecc import bn128
from py_ecc import fields

choice = 1
path1 = "output.point"
path2 = "input.point"
path3 = "sigmaproof.json"
if len(sys.argv) > 2:
    choice = int(sys.argv[1])
    path1 = sys.argv[2]
    if choice == 1:
        path2 = sys.argv[3]
        path3 = sys.argv[4]


def prove():
    w1 = open(path1, "r")
    jw1 = json.load(w1)
    w1.close()

    w2 = open(path2, "r")
    jw2 = json.load(w2)
    w2.close()

    proof = {}
    # proof['A1'] = []
    # proof['A2'] = []
    proof['g1'] = []
    proof['g2'] = []
    proof['a1'] = []
    proof['a2'] = []
    proof['C1'] = []
    proof['C2'] = []
    proof['e'] = []
    proof['z'] = []

    # proof['A1'] = jw1['A']
    # proof['A2'] = jw2['A']

    for i in range (0, 3):
        g1 = (fields.bn128_FQ(int(jw1['g'][i][0], 16)), fields.bn128_FQ(int(jw1['g'][i][1], 16)))
        C1 = (fields.bn128_FQ(int(jw1['gx'][i][0], 16)), fields.bn128_FQ(int(jw1['gx'][i][1], 16)))
        g2 = (fields.bn128_FQ(int(jw2['g'][i][0], 16)), fields.bn128_FQ(int(jw2['g'][i][1], 16)))
        C2 = (fields.bn128_FQ(int(jw2['gx'][i][0], 16)), fields.bn128_FQ(int(jw2['gx'][i][1], 16)))
        x = jw1['x'][i]
        r = secrets.randbelow(fields.field_properties['bn128']['field_modulus'])
        a1 = bn128.multiply(g1, r)
        a2 = bn128.multiply(g2, r)

        b = bytes(str(g1)+str(g2)+\
            str(C1)+str(C2)+\
            str(a1)+str(a2), encoding = "utf8")

        e = int(SHA3_256.new().update(b).hexdigest(), 16)

        z = r + e * x

        pointa1 = ['{:#066x}'.format(int(a1[0])), '{:#066x}'.format(int(a1[1]))]
        pointa2 = ['{:#066x}'.format(int(a2[0])), '{:#066x}'.format(int(a2[1]))]
        pointg1 = ['{:#066x}'.format(int(g1[0])), '{:#066x}'.format(int(g1[1]))]
        pointg2 = ['{:#066x}'.format(int(g2[0])), '{:#066x}'.format(int(g2[1]))]
        pointC1 = ['{:#066x}'.format(int(C1[0])), '{:#066x}'.format(int(C1[1]))]
        pointC2 = ['{:#066x}'.format(int(C2[0])), '{:#066x}'.format(int(C2[1]))]

        proof['a1'].append(pointa1)
        proof['a2'].append(pointa2)
        proof['g1'].append(pointg1)
        proof['g2'].append(pointg2)
        proof['C1'].append(pointC1)
        proof['C2'].append(pointC2)
        proof['e'].append(e)
        proof['z'].append(z)
    
    fn = open(path3, "w")
    json.dump(proof, fn, indent=2)
    fn.close()


def verify():
    fn = open(path1, "r")
    proof = json.load(fn)
    fn.close()
    for i in range(0, 3):
        # A1 = (fields.bn128_FQ(int(proof['A1'][i][0], 16)), fields.bn128_FQ(int(proof['A1'][i][1], 16)))
        # A2 = (fields.bn128_FQ(int(proof['A2'][i][0], 16)), fields.bn128_FQ(int(proof['A2'][i][1], 16)))
        a1 = (fields.bn128_FQ(int(proof['a1'][i][0], 16)), fields.bn128_FQ(int(proof['a1'][i][1], 16)))
        a2 = (fields.bn128_FQ(int(proof['a2'][i][0], 16)), fields.bn128_FQ(int(proof['a2'][i][1], 16)))
        g1 = (fields.bn128_FQ(int(proof['g1'][i][0], 16)), fields.bn128_FQ(int(proof['g1'][i][1], 16)))
        g2 = (fields.bn128_FQ(int(proof['g2'][i][0], 16)), fields.bn128_FQ(int(proof['g2'][i][1], 16)))
        C1 = (fields.bn128_FQ(int(proof['C1'][i][0], 16)), fields.bn128_FQ(int(proof['C1'][i][1], 16)))
        C2 = (fields.bn128_FQ(int(proof['C2'][i][0], 16)), fields.bn128_FQ(int(proof['C2'][i][1], 16)))
        e = proof['e'][i]
        z = proof['z'][i]
        try:
            pair12 = bn128.add(a1, bn128.multiply(C1, e))
            if C1[0] == 0 and C1[1] == 0:
                pair12 = a1
            pair22 = bn128.add(a2, bn128.multiply(C2, e))
            if C2[0] == 0 and C2[1] == 0:
                pair22 = a2
            # A1 = bn128.multiply(A1, e)
            # A2 = bn128.multiply(A2, e)
            # assert(bn128.eq(bn128.add(bn128.multiply(g1, z), A1), pair12))
            # assert(bn128.eq(bn128.add(bn128.multiply(g2, z), A1), pair22))
            assert(bn128.eq(bn128.multiply(g1, z), pair12))
            assert(bn128.eq(bn128.multiply(g2, z), pair22))
        except AssertionError:
            print(str(i) + " VERIFY FAIL")
            print(C1, C2)
    print("VERIFY DONE")

def main():
	if choice == 1:
		print("generating sigma_proof...")
		prove()
	elif choice == 2:
		print("verifying sigma_proof...")
		verify()
	else:
		print("wrong args")

main()