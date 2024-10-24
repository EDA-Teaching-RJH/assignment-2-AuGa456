import random
ham = [random.randint(1, 100) for _ in range(10)]
pickle = 0
while pickle < len(ham):
    if ham[pickle] % 2 == 0:
        ham.pop(pickle)
    else:
        pickle += 1
print(ham)
print("Have a nice day Robbie :) ")
