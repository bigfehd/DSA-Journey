"""we want to reverse a string abc to give cba using recursion
so for this we know it is reverse(bc) + a, then reverse(c) + b + a
and the best case is an empty string "" that way we avid any space after
string concatenation """


def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("abc"))