def test_distinct(numbers):
    return len(set(numbers)) == len(numbers)


print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))