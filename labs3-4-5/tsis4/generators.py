# ex1 
def squares_generator(N):
    for i in range(N):
        yield i ** 2
N = 5
squares = squares_generator(N)
for square in squares:
    print(square)


# ex2
def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
n = int(input("Enter a number: "))
even_nums = even_numbers_generator(n)
print(','.join(map(str, even_nums)))



# ex3
def divisible_by_3_and_4(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
start = 0
end = 20
result = divisible_by_3_and_4(start, end)
for num in result:
    print(num)


# ex4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = 3
b = 7
for square in squares(a, b):
    print(square)



# ex5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = 5
for num in countdown(n):
    print(num)