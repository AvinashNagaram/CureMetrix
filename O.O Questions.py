# O.O. Questions

# 1.
# Write a generator that takes a number N and returns all perfect squares less than N.
# Hint: use yield
# Example 1: N=30 then the generator will give 1, 4, 9, 16, 25 sequentially

import math
#
def squares(num):
    result=[]
    for each in range(1, num):
        if int(math.sqrt(each)) ** 2 == each:
            result.append(each)
    print(result)

squares(30)

