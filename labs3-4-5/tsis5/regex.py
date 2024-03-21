# ex1
import re

pattern = r'ab*'
string = 'acbb'
if re.fullmatch(pattern, string):
    print("Match found")
else:
    print("No match")


# ex2
pattern = r'ab{2,3}'
string = 'abbb'
if re.fullmatch(pattern, string):
    print("Match found")
else:
    print("No match")



# ex3
pattern = r'[a-z]+_[a-z]+'
string = 'hello_world'
matches = re.findall(pattern, string)
print(matches)



# ex4
pattern = r'[A-Z][a-z]+'
string = 'HelloWorld'
matches = re.findall(pattern, string)
print(matches)


# ex5
pattern = r'a.*b$'
string = 'acb'
if re.fullmatch(pattern, string):
    print("Match found")
else:
    print("No match")



# ex6
pattern = r'[ ,.]'
string = 'Hello, world. How are you?'
replaced_string = re.sub(pattern, ':', string)
print(replaced_string)



# ex7
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake_string = 'hello_world_how_are_you'
camel_string = snake_to_camel(snake_string)
print(camel_string)




# ex8
pattern = r'[A-Z]'
string = 'HelloWorldHowAreYou'
split_string = re.findall(pattern + '[^A-Z]*', string)
print(split_string)



# ex9
pattern = r'(?<!^)(?=[A-Z])'
string = 'HelloWorldHowAreYou'
spaced_string = re.sub(pattern, ' ', string)
print(spaced_string)



# ex10
def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

camel_string = 'HelloWorldHowAreYou'
snake_string = camel_to_snake(camel_string)
print(snake_string)