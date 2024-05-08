import sys
N,M = map(int,input().split())

pokemons_dict = {}
for i in range(1,N+1):
    name = input()
    pokemons_dict[i] = name

pokemons_dict_rev = {v: k for k,v in pokemons_dict.items()}

for i in range(M):
    input_m = sys.stdin.readline().rstrip()

    if input_m.isdecimal():
        print(pokemons_dict[int(input_m)])
    else:
        print(pokemons_dict_rev[str(input_m).replace('\n','')])

