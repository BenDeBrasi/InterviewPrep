import math
"Rotate matrix 90 degrees"
"Can be done in place by flipping from first and last row start to finish till the counters pass each other or are on the same row"
"Draw it out in the interview. "
def RotateMatrix(M):
    for layer in range(math.floor(len(M)/2)):
        first = layer
        end = len(M) - layer - 1

        for i in range(first,end):
            offset = i - first
            tmp = M[first][first + offset]
            M[first][first + offset] = M[end - offset][first]
            M[end - offset][first] = M[end][end - offset]
            M[end][end - offset] = M[first + offset][end]
            M[first + offset][end] = tmp
    return M

M = [[0,1,2,3,4] for i in range(5)]
print(M)
print(RotateMatrix(M))
