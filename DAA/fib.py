def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def non_recursive_fibonacci(n):
    first = 0
    second = 1
    print(first)
    print(second)
    for _ in range(n-2):
        third = first + second
        first = second
        second = third
        print(third)

n = 10
for i in range(n):
    print(recursive_fibonacci(i))
print()
non_recursive_fibonacci(n)

