def plusMinus(arr):
    # Write your code here
    posit, negat, zero = 0, 0, 0
    for num in range(n):
        if num > 0:
            posit += 1
        elif num < 0:
            negat += 1
        elif num == 0:
            zero += 1
    print(f"{posit/n:.6f}")
    print(f"{negat/n:.6f}")
    print(f"{zero/n:.6f}")
        
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
plusMinus(arr)