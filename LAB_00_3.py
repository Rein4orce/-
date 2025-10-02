import time

def fib(n):
    n = n % 60
    if n <= 1:
        print(n)
        return n
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, (a + b) % 10
    return b

start = time.time()

with open ('input.txt', 'r') as f:
    n = int(f.read())

with open('output.txt', 'w') as p:
    p.write(str(fib(n)))

print(time.time() - start)
