# given n * n 2D matrix, rotate the matrix by 90 degrees.
# rotate the image in place

input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

def rotateimage():
    for r in range(len(input)):
        for c in range(r):
            print(input[r][c])  # (1,0) (2,0) (2,1)
            rc = input[r][c]
            input[r][c] = input[c][r]
            input[c][r] = rc


    print(input)

    for r in input:
        r.reverse()

    print(input)

