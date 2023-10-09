# a= 10
# def numb():
#     global a
#     a = 11
#     print(a)
# numb()
# print(a)
x=10 
def outer():
    x=11
    def imner():
        global x
        x= 12
        return x
    print(x)
    print(imner())
print(x)
outer()