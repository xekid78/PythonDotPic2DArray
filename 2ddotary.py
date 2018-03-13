letterA =  [[0,0,1,1,0,0],
            [0,1,0,0,1,0],
            [1,0,0,0,0,1],
            [1,1,1,1,1,1],
            [1,0,0,0,0,1],
            [1,0,0,0,0,1]]

for line in letterA:
    for char in line:
        if char == 1:
            print("@", end="")
        else:
            print(" ", end="")
    print()
