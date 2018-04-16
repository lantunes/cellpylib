import numpy as np

import cellpylib as cpl


def entropy(m):
    timestep = []
    tbien = []
    ktbien = []
    shannon_entropies = []
    apentropies = []
    for i, row in enumerate(m):
        timestep.append(i)
        bit_string = ''.join([str(x) for x in row])
        tbien.append(cpl.tbien(bit_string))
        ktbien.append(cpl.ktbien(bit_string))
        shannon_entropies.append(cpl.shannon_entropy(bit_string))
        apentropies.append(cpl.apen(bit_string))

    print("mean TBiEn: %s" % np.mean(tbien))
    print("mean KTBiEn: %s" % np.mean(ktbien))
    print("mean Shannon: %s" % np.mean(shannon_entropies))
    print("mean ApEn: %s" % np.mean(apentropies))

matrix = np.random.randint(2, size=(100,100), dtype=np.int)
cpl.plot(matrix)
entropy(matrix)

print("--------")

r = [1]*50 + [0]*50
matrix = [r]*100
cpl.plot(matrix)
entropy(matrix)
