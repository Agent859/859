seeds=[]
seed=input("SEED: ")
seeds.append(0)
seeds.append(int(seed))

while True:
    seeding=str(int(seeds[-1])**2)
    x=str(seeds[-2])
    y=int(x[0])%len(seed)
    seeded=seeding[y:y+len(seed)]
    if (seeded in seeds)==True:
        break
    else:
        seeds.append(seeded)
        print(seeds[-1],end="")