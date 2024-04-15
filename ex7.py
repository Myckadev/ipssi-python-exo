def count_pair_and_impair_digit(digits):

    pair_count = 0
    impair_count = 0

    for n in digits:
        if int(n) % 2 == 0:
            pair_count += 1
        else:
            impair_count += 1

    return pair_count, impair_count


letters, digits = count_pair_and_impair_digit([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("paire", letters)
print("imapir", digits)
