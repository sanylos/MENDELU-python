mat = [[1 if y == x else 0 for y in range(10)] for x in range(10)]
for x in range(10):
    for y in range(10):
        print(mat[x][y])
