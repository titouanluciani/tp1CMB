import re
file = open("separaters.txt", "r")
data = file.read()
print(data.split("(,|;|:)*"))
file.close()

a = []
b = []
a = [1,2,3]
b = [1,4,10]
print(a,b)
def vector_add(a,b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    print(result)
vector_add(a,b)