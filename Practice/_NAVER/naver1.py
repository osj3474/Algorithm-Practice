import math

def udf_combination(n, r):
    return math.factorial(n) // (math.factorial(n-r)*math.factorial(r))

print(udf_combination(6, 4))