def diagonalDifference(arr):
    # Write your code here
    pri_diag = 0
    sec_diag = 0
    n = len(arr)
    for i in range(n):
        pri_diag += arr[i][i]
        sec_diag += arr[i][n - 1 - i]
    return abs(pri_diag - sec_diag)
n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)