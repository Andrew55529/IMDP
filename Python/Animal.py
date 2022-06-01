file = open("input.txt")
Animals = list();
for Animal in file:
    Animals.append(Animal)

AnimalCan = list()

for a in range(7):
    for b in range(a, 7):
        if (Animals[a].split()[1] == Animals[b].split()[1] and Animals[a].split()[2] != Animals[b].split()[
            2] and AnimalCan.count(Animals[a].split()[1]) == 0):
            AnimalCan.append(Animals[a].split()[1])

count = dict()
for a in range(8):
    if (Animals[a].split()[1] not in count.keys()):
        count[Animals[a].split()[1]] = 1
    else:
        count[Animals[a].split()[1]] += 1

CountSorted = sorted(count.items(), key=lambda x: x[1], reverse=1)

AnimalSort = sorted(AnimalCan, key=len)
print(AnimalSort)
print(CountSorted)

file.close()