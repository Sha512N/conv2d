def conv2d (matrix, kernel, padding=0, strides=1):
  h = len(matrix)
  w = len(matrix[0])

  h_kernel = len(kernel)
  w_kernel = len(kernel[0])

  h_output = int((h - h_kernel + 2 * padding) / strides + 1)
  w_output = int((w - w_kernel + 2 * padding) / strides + 1)

  matrix_padded = []

  if padding == 0:
    matrix_padded = matrix
  else:
    for i in range(0, h + padding * 2):
      matrix_padded.append([])
      for j in range(0, w + padding * 2):
        if (i - padding >= 0 and i - padding < h and j - padding >= 0 and j - padding < w):
          matrix_padded[i].append(matrix[i - padding][j - padding])
        else:
          matrix_padded[i].append(0)

  output = [[0 for j in range(0, w_output)] for i in range(0, h_output)]

  i_stride = 0;
  j_stride = 0;

  for i in range(0, h + padding * 2, strides):
    if i_stride >= h_output:
      break
    for j in range(0, w + padding * 2, strides):
      if j_stride >= w_output:
        break
      sum = 0
      for i_i in range(0, h_kernel):
        for j_j in range(0, w_kernel):
          sum += kernel[i_i][j_j] * matrix_padded[i + i_i][j + j_j]
      output[i_stride][j_stride] += sum
      j_stride += 1
    i_stride += 1
    j_stride = 0
  return output
