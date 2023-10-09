person = [
    {'name':'saksham', 'age':12, 'gender':'male', 'Language':['python','java']},
    {'name':'shyam', 'age':12, 'gender':'male', 'Language':['python','java']},
    {'name':'Ram', 'age':12, 'gender':'male', 'Language':['python','java']}
]

print(f'''
My name is {person[0]['name']}
and age is {person[0]['age']}
and gender is {person[0]['gender']}
and I know different languages like
  1. {person[0]['Language'][0]}
  2. {person[0]['Language'][1][1:4]}
My name is {person[1]['name']}
and age is {person[1]['age']}
and gender is {person[1]['gender']}
and I know different languages like
  1. {person[1]['Language'][0]}
  2. {person[1]['Language'][1:4]}
My name is {person[2]['name']}
and age is {person[2]['age']}
and gender is {person[2]['gender']}
and I know different languages like
  1. {person[2]['Language'][0]}
  2. {person[2]['Language'][:4]}
''')
