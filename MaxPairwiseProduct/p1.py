n = input()
arr = input()
l = list(map(int,arr.split(' ')))

num1 = -1
for i in range(len(l)):
    if l[i] > num1:
        num1 = l[i]
        k = i

num2 = -1
for j in range(len(l)):
    if j!=k and l[j] > num2:
        num2 = l[j]

# print(num1, num2)
print(num1 * num2)