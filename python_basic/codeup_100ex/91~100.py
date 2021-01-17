
# 91번 문제

# a, m, d, n = map(int, input().split())

# if n == 1:
#     print(a)
# else:
#     tmp = a*m + d
#     for _ in range(3, n+1):
#         tmp = tmp*m + d

#     print(tmp)

# a,m,d,n=input().split()

# A=int(a)
# M=int(m)
# D=int(d)
# N=int(n)

# for i in range(N-1) :
#     A = A*M+D

# print(A)


# 92번 문제

# a, b, c = map(int, input().split())
# day = 0

# while True:
#     day += 1

#     if day % a == 0 and day % b == 0 and day % c == 0:
#         break
#     else:
#         continue
# print(day)


# 93번 문제

# a = int(input())
# b = list(map(int, input().split()))
# c = []

# for i in range(1,24):
#     if b.count(i):
#         c.append(b.count(i))
#     else:
#         c.append(0)
#     print(c[i-1], end = ' ')


# 94번 문제

# a = int(input())
# b = list(map(int, input().split()))
# c = []

# for i in range(len(b)):
#     c.append(b[len(b) - (i+1)])

#     print(c[i], end=' ')


# 95번 문제

# a = input()
# b = list(map(int, input().split()))
# temp = b[0]

# for i in range(int(a)):
#     if b[i] < temp:
#         temp = b[i]
#     else:
#         continue

# print(temp)


# 96번 문제

# a = int(input())
# base = [[0]*19 for _ in range(19)]

# for i in range(a):
#     x,y = map(int, input().split())
#     base[x - 1][y - 1] = 1

# for i in range(19):
#     for j in range(19):
#         print(base[i][j], end = ' ')
#     print()



# 97번 문제

base = [[0]*19 for _ in range(19)]


for i in range(19):
    base[i] = list(map(int, input().split()))

print(base)
a = int(input())
for i in range(a):
    x, y = map(int, input().split())
    for j in range(19):
        if base[x-1][j] == 1:
            base[x-1][j] = 0
        else:
            base[x-1][j] = 1
    for j in range(19):
        if base[j][y-1] == 1:
            base[j][y-1] = 0
        else:
            base[j][y-1] = 1

for i in range(19):
    for j in range(19):
        print(base[i][j], end=' ')
    print()
         
