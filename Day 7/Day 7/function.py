# def hello(name):
#     print(f"hello!! {name} how are you?")
# hello("ram")
# hello("shyam")
# def person(name,age,gender,address,hobbies):
#     print(f"My name is {name} and i am {age} years old. I am {gender} and i live in {address}.")
#     for hobby in hobbies:
#         print(f"my hobby are {hobby}")
# person("Ram",12,"male","Kathmandu",["playing football","listing songs"])
# def person(*name):
#     for names in name:
#      print(names)
# person("saksham",'rasm','kk0',2.1,2.333)
def person(**person):
    print(f"My name is {person['name']} and i am {person['age']} years old. I am {person['gender']}.")
person(name='shyam',age=15,gender='male')