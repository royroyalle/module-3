def cube(num):
    return num*num*num
def three(num):
    if num %3 == 0:
        return cube(num)
    else:
        return ("false")
print(three(9))
print(three(4))