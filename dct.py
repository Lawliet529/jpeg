import math

import matplotlib.pyplot as plt


def alpha(u):
    if u == 0:
        return 1.0 / math.sqrt(2.0)
    else:
        return 1.0


# Input: 8x8 matrix of integers
matrix = [[52, 55, 61, 66, 70, 61, 64, 73],
          [63, 59, 55, 90, 109, 85, 69, 72],
          [62, 59, 68, 113, 144, 104, 66, 73],
          [63, 58, 71, 122, 154, 106, 70, 69],
          [67, 61, 68, 104, 126, 88, 68, 70],
          [79, 65, 60, 70, 77, 68, 58, 75],
          [85, 71, 64, 59, 55, 61, 65, 83],
          [87, 79, 69, 68, 65, 76, 78, 94]]

# Print input matrix
print("Input:")
for row in matrix:
    for value in row:
        print("%3d" % value, end=" ")
    print()
print()

# Shift the values by 128
for i in range(8):
    for j in range(8):
        matrix[i][j] -= 128

# Print shifted matrix
print("Shifted:")
for row in matrix:
    for value in row:
        print("%3d" % value, end=" ")
    print()
print()

# Perform the DCT
dct = [[0.0 for i in range(8)] for j in range(8)]
for u in range(8):
    for v in range(8):
        sum = 0.0
        for x in range(8):
            for y in range(8):
                sum += matrix[x][y] * \
                       math.cos((2.0 * x + 1.0) * u * math.pi / 16.0) * \
                       math.cos((2.0 * y + 1.0) * v * math.pi / 16.0)
        sum *= 0.25 * alpha(u) * alpha(v)
        dct[u][v] = sum

# Print DCT coefficients
print("DCT coefficients:")
for row in dct:
    for value in row:
        print("%7.2f" % value, end=" ")
    print()
print()

# Quantize the DCT coefficients
quant = [[16, 11, 10, 16, 24, 40, 51, 61],
         [12, 12, 14, 19, 26, 58, 60, 55],
         [14, 13, 16, 24, 40, 57, 69, 56],
         [14, 17, 22, 29, 51, 87, 80, 62],
         [18, 22, 37, 56, 68, 109, 103, 77],
         [24, 35, 55, 64, 81, 104, 113, 92],
         [49, 64, 78, 87, 103, 121, 120, 101],
         [72, 92, 95, 98, 112, 100, 103, 99]]
for u in range(8):
    for v in range(8):
        dct[u][v] = round(dct[u][v] / quant[u][v])

# Print quantized DCT coefficients
print("Quantized DCT coefficients:")
for row in dct:
    for value in row:
        print("%3d" % value, end=" ")
    print()
print()

# Multiply the quantized DCT coefficients by the quantization matrix
for u in range(8):
    for v in range(8):
        dct[u][v] *= quant[u][v]

# Print the quantized DCT coefficients multiplied by the quantization matrix
print("Quantized DCT coefficients multiplied by the quantization matrix:")
for row in dct:
    for value in row:
        print("%4d" % value, end=" ")
    print()
print()

# Perform the inverse DCT
idct = [[0.0 for i in range(8)] for j in range(8)]
for x in range(8):
    for y in range(8):
        sum = 0.0
        for u in range(8):
            for v in range(8):
                sum += alpha(u) * alpha(v) * dct[u][v] * \
                       math.cos((2.0 * x + 1.0) * u * math.pi / 16.0) * \
                       math.cos((2.0 * y + 1.0) * v * math.pi / 16.0)
        sum *= 0.25
        idct[x][y] = round(sum)

# Print the inverse DCT
print("Inverse DCT:")
for row in idct:
    for value in row:
        print("%3d" % value, end=" ")
    print()
print()

# Shift the values back by 128
for i in range(8):
    for j in range(8):
        idct[i][j] += 128

# Print the shifted inverse DCT
print("Shifted inverse DCT:")
for row in idct:
    for value in row:
        print("%3d" % value, end=" ")
    print()
print()

# Shift the values back by 128
for i in range(8):
    for j in range(8):
        matrix[i][j] += 128

# Compare the input matrix with the inverse DCT
print("Errors:")
for i in range(8):
    for j in range(8):
        print("%3d" % (matrix[i][j] - idct[i][j]), end=" ")
    print()
print()

# Find average absolute error
sum = 0.0
for i in range(8):
    for j in range(8):
        sum += abs(matrix[i][j] - idct[i][j])
print("Average absolute error: %f" % (sum / 64.0))

# Display the original image and the reconstructed image
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(matrix, cmap='gray', vmin=0, vmax=255)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title('Original image')
ax2.imshow(idct, cmap='gray', vmin=0, vmax=255)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_title('Reconstructed image')
plt.show()
