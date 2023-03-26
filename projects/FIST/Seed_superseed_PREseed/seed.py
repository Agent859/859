seeds=[]
seed=input("SEED: ")
seeds.append(int(seed))

while True:
    seeding=str(int(seeds[-1])**2)
    x=(len(seeding)-len(seed))//2
    seeded=seeding[x:x+len(seed)]
    if (seeded in seeds)==True:
        break
    else:
        seeds.append(seeded)
        print(seeds[-1],end="")