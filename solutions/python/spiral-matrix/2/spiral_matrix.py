"""Python function for repeatable spiral matrix"""

def spiral_matrix(size):
  """ Size: total spiral estimation to know """
  # Agar size 0 ho to khali list return karein
  if size == 0:
    return []

  # 1. Aik khali (0 se bhara hua) grid banayein
  matrix = [[0] * size for _ in range(size)]

  # 2. Chaar deewarein (boundaries) set karein
  top = 0
  bottom = size - 1
  left = 0
  right = size - 1

  # Ginti shuru karne ke liye variable
  num = 1

  # 3. Jab tak deewarein aapas mein takra na jayein, loop chalayein
  while top <= bottom and left <= right:

    # Kaam 1: Left se Right jao (Top row bharo)
    for col in range(left, right + 1):
      matrix[top][col] = num
      num += 1
    top += 1  # Oopar wali line bhar gayi, ab isay 1 step neeche khiska dein

    # Kaam 2: Top se Bottom aao (Right column bharo)
    for row in range(top, bottom + 1):
      matrix[row][right] = num
      num += 1
    right -= 1  # Dayein line bhar gayi, ab isay 1 step andar (left) khiska dein

    # Kaam 3: Right se Left jao (Bottom row bharo)
    if top <= bottom:
      for col in range(right, left - 1, -1):
        matrix[bottom][col] = num
        num += 1
      bottom -= 1  # Neeche wali line bhar gayi, ab isay 1 step oopar khiska dein

    # Kaam 4: Bottom se Top jao (Left column bharo)
    if left <= right:
      for row in range(bottom, top - 1, -1):
        matrix[row][left] = num
        num += 1
      left += 1  # Bayein line bhar gayi, ab isay 1 step andar (right) khiska dein

  # 4. Mukammal matrix return karein
  return matrix
