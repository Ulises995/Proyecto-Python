"""matrix transpose
Here’s an example of the input and output values of this problem:

Input: [[1,2,3],[4,5,6],[7,8,9]] | Output: [[1,4,7],[2,5,8],[3,6,9]]
"""
def transpose(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

a = [[1,2,3],[4,5,6],[7,8,9]]
#print(a)
for i in range(len(a)):
    print(a[i])

b = transpose(a)
for i in range(len(b)):
    print(b[i])