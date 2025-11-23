def fac(x):
    '''initiating doc string here, the recursive function to find factorial of an integer'''
    if x ==0 or x==1:
        return 1
    else:
        return x*fac(x-1)
print(fac.__doc__)
print("factorial of 1 is:", fac(1))
print("factorial of 2 is:", fac(2))
print("factorial of 3 is:", fac(3))
print("factorial of 4 is:", fac(4))
print("factorial of 5 is:", fac(5))