# Напишіть програму, для конкатенации N рядків
N = int(input("How many strings?: "))
arr = []
for i in range(N):
    arr.append(input())
print("".join(arr))
