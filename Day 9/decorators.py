def hash(func):
    def wrapper():
        print('*'*10)
        print('%'*10)
        print('#'*10)
        func()
        print('*'*10)
        print('%'*10)
        print('#'*10)
    return wrapper

@hash
def hello():
    print('hello')
def world():
    print('world')
hello()
