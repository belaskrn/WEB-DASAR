def fungsi_pangkat(x,y):
  if y > 1:
    return x * fungsi_pangkat (x, y - 1)
  return x

print(fungsi_pangkat(3,2))

