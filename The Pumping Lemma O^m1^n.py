"""Definition of the Language L = {0^m 1^n | m<n} given as a take home example for homework.  This program explores the
use of the pumping lemma as it applies to this language.
Author: Timothy Capille"""


# Returns true if m < n and prints the corresponding string, otherwise returns false and states that its not
# in the language
def L(m, n):
    if (m < n):
        zeros = '0' * m
        ones = '1' * n
        return True, zeros + ones
    return False, "Not in language"

# Uses pumping lemma and the definition of L to decide if the pumped string is in L.
def pumping_lemma():
    # Assume L is regular, choose an string in L with pumping length k, such that
    # |s| >= k.  s  in this case will be 0^k 1^k+1. |s| = 2k + 1
    # by the pumping lemma s = uvw s.t. uv^iw is in L for all i >=0.
    # Since |v| > 0 and |uv| <= k

    # Result is a list instead of string to store 0's and 1's to make use of pythons count function
    result = []
    # O^1 1^2 is in our given s
    zeros = '0'
    ones = '11'

    # pumping zeros => uv = 0^i, this example produces a contradiction at i = 2

    for _ in range(2):
        result.append(zeros)
    result.append(ones)

    return (L(result.count('0'), result.count(('1'))))

#By proof of contradiction this language is proven to be
#non-regular using the pumping lemma

print(pumping_lemma())
