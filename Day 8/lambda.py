# sum=lambda a:a+10
# print(sum(19))
def myfunc(n):
    return lambda a:a*n
doubler =myfunc(3)
print(doubler(10))