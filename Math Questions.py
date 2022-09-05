# Math questions


# 1. Write a function that takes two integers (x and y) and returns a list of numbers between x and y that are divisible
# by 5 but not by 7

def func1(x,y):
    if x < -1 and x < -1:
        print ('choose postive values')
    else:
        list = []
        for i in range(x+1,y):
            if i % 5 == 0 and i % 7 != 0:
                list.append(i)
        print(list)


