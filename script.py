from time import sleep # Just in case I want to add a delay between each number
addorsub = 2
denom = 3
answer = 4
addend = 0
printout = 0
while True:
addend = 4.0/denom
denom = denom + 2
if addorsub == 2:
answer = answer - addend
addorsub = 1
elif addorsub == 1:
answer = answer + addend
addorsub = 2
print(answer)
