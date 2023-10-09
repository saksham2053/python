def hash(func):
    def wrapper():
        print('#'*10)
        func()
        print('#'*10)
    return wrapper
def star(func):
    def wrap():
        print('*'*10)
        func()
        print('*'*10)
    return wrap
def per(func):
    def wrapp():
        print('%'*10)
        func()
        print('%'*10)
    return wrapp

def hello():
    print('hello')
def world():
    print('world')
hello = hash(star(per(hello)))
hello()  

