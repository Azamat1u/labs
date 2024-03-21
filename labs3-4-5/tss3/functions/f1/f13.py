def solve(numheads, numlegs):
    for c in range(numheads + 1):
        r = numheads - c
        if 2 * c + 4 * r == numlegs:
            return c, r

    return None

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)

if result:
    chickens, rabbits = result
    print(f"Number of chickens: {chickens}\nNumber of rabbits: {rabbits}")
else:
    print("There is no solution.")
