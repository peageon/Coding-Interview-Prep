def get_biggest_number(N, x, y):
    x_val = int(x)
    y_val = int(y)
    N_length = len(N)
    N_first_digit = int(N[0])

    if(N_length == 0):
        return ""

    if N_first_digit > y_val:
        return y * N_length
    elif N_first_digit == y_val:
        res = y + get_biggest_number(N[1:], x, y)
        if res[-1] == "t":
            return x + (y * (N_length - 1))
        else:
            return res
    elif N_first_digit > x_val:
        return x + (y * (N_length - 1))
    elif N_first_digit == x_val:
        return x + get_biggest_number(N[1:], x, y)
    elif N_first_digit < x_val:
        return "t"
    

T = int(input())
for test_case in range(1, T + 1):
    value_list = input().split()
    N = value_list[0]
    x = value_list[1]
    y = value_list[2]
    min_val = int(x)
    if min_val > int(N):
        print(f"#{test_case} -1")
    else:
        sol = get_biggest_number(N,x,y)
        if sol[-1] == "t":
            sol = y * (len(N)-1)
        if int(sol) == 0:
            sol = "-1"
        print(f"#{test_case} {int(sol)}")
