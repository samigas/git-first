def cul_multi():
    for i in range(1, 10):
        for s in range(2, 6):
            print(f'{s} X {i} = {s * i}', end = '\t\t\t') 
        print()

    print()

    for i in range(1, 10):
        for s in range(6, 10):
            print(f'{s} X {i} = {s * i}', end = '\t\t\t')
        print()

cul_multi()
