import random
x = 2; print(x)
for i in range(20):
    if x == 1:
        x = random.randint(1, 2)
    elif x == 2:
        x = random.randint(1, 3)
    else:
        x = random.randint(2,3)
    print(x)