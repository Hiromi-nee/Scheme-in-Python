import Image
import numpy as np
from scipy.io.wavfile import write

im = Image.open("allen.png")
matrix = []

imm = im.load()

for i in range(1000):
    line = []
    for j in range(1000):
        line.append(imm[i, j])
    matrix.append(line)

data = np.array(matrix)
write('test.wav', 44100, data)
