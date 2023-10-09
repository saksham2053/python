# def hello_world():
#     print('hello world')
#     hello_world()
# hello_world()
# def sum(a,b):
#     return a+b
# number = sum(1,2)
# print(number)
# def number(start=0):
#     print(start)
#     if start==10:
#         return
#     number(start+1)
# number()
def sum_numbers_in_range(start, end):
    if start == end:
        return start
    else:
        return start + sum_numbers_in_range(start + 1, end)

# Example usage:
start = 1  # Start of the range
end = 5    # End of the range
result = sum_numbers_in_range(start, end)
print(f"The sum of numbers from {start} to {end} is: {result}")

    

    