def beautifulDays(i, j, k):
    # Write your code here
    b_date = 0
    for date in range(i,j+1):
        reverse_date = str(date)
        reverse_date = int(reverse_date[::-1])
        day = abs(date - reverse_date)
        if day % k == 0:
            b_date += 1
    return b_date

first_multiple_input = input().rstrip().split()  # input format: "i j k" where i, j, k are integers

i = int(first_multiple_input[0])

j = int(first_multiple_input[1])

k = int(first_multiple_input[2])

result = beautifulDays(i, j, k)
print(f"Beautiful day/s in the given day range is {result}")