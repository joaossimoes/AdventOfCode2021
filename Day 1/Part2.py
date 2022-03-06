from os import read


f = open("inputP1", 'r').readlines()


result = sum((int(b)>int(a)) for a,b in zip(f,f[3:]))
# count = zip(f,f[3:])

# for a,b in count:
#     if int(b) > int(a):
#         print(a,b)
#         result += 1

    
print(result)