def sum_all(*args):
    total = 1
    for num in args:
        total += num
    return total

result = sum_all(2, 3, 5) 
print("Sum:", result)
