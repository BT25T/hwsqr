def count_digits(n):
    if n<10:
        return 1
    return 1 + count_digits(n//10)

def power(base, exponent):
    if exponent == 0:
        return 1
    return power(base, exponent-1) * base

def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

print(is_palindrome("raceca"))