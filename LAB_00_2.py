import time

start = time.time()
def calc_fib(n):
    if (n <= 1):
        return n
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return b
with open ('input.txt', 'r') as f:
    n = int(f.readline())


with open('output.txt', 'w') as p:
    p.write(str(calc_fib(n)))
    print(calc_fib(n))

end = time.time()
print(end - start)