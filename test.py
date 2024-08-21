a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for row in a:
    print(row)

def transpose(matrix):
    res = []
    for i in range(len(matrix[1])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        res.append(row)
    return res

print()

for row in b:
    print(row)