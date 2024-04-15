def fibonacci(rank):
    a, b = 0, 1

    if rank >= 0:
        print(a)
    while b <= rank:
        print(b)
        a, b = b, a + b

fibonacci(50);
