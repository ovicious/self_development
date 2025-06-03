def angryProfessor(k, a):
    # Write your code here
    on_time = int(0)
    for time in a:
        if time <= 0:
            on_time += 1
    if on_time >= int(k):
        return "NO"
    else:
        return "YES"

t = int(input().strip())
for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = angryProfessor(k, a)
    print(result)
