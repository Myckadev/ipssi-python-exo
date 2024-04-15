def score_of_string(s):
    score = 0
    for i in range(1, len(s)):
        score += abs(ord(s[i]) - ord(s[i - 1]))
    return score


s1 = "hello"
print("Score de", s1, ":", score_of_string(s1))

s2 = "zaz"
print("Score de", s2, ":", score_of_string(s2))
