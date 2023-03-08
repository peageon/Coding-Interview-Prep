equation = input()

sol = 0
minus = False
num = ""
for c in equation:
    if c == "+" or c == "-":
        if minus:
            sol -= int(num)
        else:
            sol += int(num)
        num = ""
    else:
        num += c
    if c == "-":
        minus = True
if minus:
    sol -= int(num)
else:
    sol += int(num)
print(sol)
    
    
    