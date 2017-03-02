# m = qn + r
# m, n's gcd == n, r's gcd
def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)


assert gcd(12, 18) == 6
