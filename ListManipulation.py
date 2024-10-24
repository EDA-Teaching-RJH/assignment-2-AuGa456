ham = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
ham.extend([7, 8])
ham.sort()
ham = [num for num in ham if num != 1]
print(ham)
