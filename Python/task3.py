from typing import Collection
str1 = str()
ss = "Балабол"
for a in range(len(ss)):
    str1 = str1 + ss[-a-1]
print(str1)

str2 = str()
flag = int()
ss = "'Лучший в деле за работой', - сказал Отец ,- 'Приехали...'"
for a in range(len(ss)):
  if(flag == 1):
    if(ss[a] != "'"):
      str2 += ss[a]
  if(ss[a] == "'"):
    if(flag == 0):
      flag = 1
    else:
      flag = 0
      str2 += "  "
print(str2)

k = input()
k = int(k)
k *= 2
print(k)

k = input()
print(k[k.find(" ")+1:],k[:k.find(" ")])

k = "SDJGjknnsdgnsdj.fsdjgdsf.jgfjdgjo@gmail.com"
a = int(0)
while k[a] != "@":
  print(k[a], end = "", sep = "")
  a += 1

k = "+7 (921) 97-86-888"
print("26")
for a in range(len(k)):
  if(int(k[a] == "-") | int(k[a] == " ") | int(k[a] == "(") | int(k[a] == ")")):
    continue
  print(k[a], end = "", sep = "")

Pal = "abcghgcba"
flag = bool(1)
for a in range(len(Pal)//2):
  if(Pal[a] != Pal[-a-1]):
    flag = 0

if(flag):
  print("\nAll OK")

for a in range(124):
  if str(a).count("9") > 0:
    continue
  print(a, sep =",", end = " ")

print("\n")

for a in range(100, 999):
  if int(str(a)[0])**3 + int(str(a)[1])**3 + int(str(a)[2])**3 == int(a):
    print(a)

print("\n")
last = str("")
str4 = str("")
for a in range(100):
  last = str(a**2)[len(str(a**2)) - len(str(a)):]
  if last  == str(a):
    print(a)
  last = ""

print("\n")
for a in range(20):
  for b in range(18):
    for c in range(17):
      if 15*a + 17*b + 21*c == 185:
        print(a,b,c)