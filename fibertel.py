with open('fibertel.txt', 'w') as fibertel:
    st = ['014','004']
    for i in range(0, len(st)):
        for x in range(2000000,5000000):
            fibertel.write(f'{st[i]}{x}\n')
