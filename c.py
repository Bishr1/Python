import numpy as np

a = 1
b = 1

for n in range(100):
    a = complex(1, 1)**a
    b = np.exp(complex(0, 5 * np.pi / 2) * b)

    print(a, b)
