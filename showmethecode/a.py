import sys
input = sys.stdin.readline

def get_sum(left, right):
    return abs(left - right)

def calculate_left_right(element, left, right):
    if element == 1:
        left += 1
    elif element == 2:
        right += 1
    elif element == -1:
        left -= 1
    elif element == -2:
        right -= 2
    return (left,right)
    

def slide_window(table, window_size):
    table_length = len(table)
    start = 0
    end = start + window_size - 1
    left = 0
    right = 0

    for i in range(window_size):
        left, right = calculate_left_right(table[i], left, right)
    
    sol = get_sum(left, right)

    for i in range(window_size, table_length):
        left, right = calculate_left_right(table[i], left, right)
        left, right = calculate_left_right(-(table[i-window_size]), left, right)
        sol = max(sol, get_sum(left,right))

    return sol 

n = int(input())
table = list(map(int, input().split()))
sol = slide_window(table, 1)
for window_size in range(1, n + 1):
    sol = max(sol, slide_window(table, window_size))
print(sol)