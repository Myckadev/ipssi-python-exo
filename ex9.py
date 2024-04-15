for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print('fizzbuzz')
    elif fizzbuzz % 3 != 0 and fizzbuzz % 5 == 0:
        print('buzz')
    elif fizzbuzz % 3 == 0 and fizzbuzz % 5 != 0:
        print('fizz')
    else:
        print(fizzbuzz)