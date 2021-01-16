
# 71번 문제

# a = list(map(int, input().split()))

# for i in range(len(a)):
#     if a[i] == 0:
#         break
#     else:
#         print(a[i])


# 72번 문제

# max_num = int(input())

# a = list(map(int, input().split()))

# for i in range(max_num):
#     print(a[i])

# 73번 문제




# # 74번 문제

# a = int(input())

# while a != 0:
#     print(a)
#     a -= 1


# 75번 문제

# a = int(input())

# while a != 0:
#     a -= 1
#     print(a)


# 76번 문제

# print(ord('a'))
# a = input()

# ascii_num = ord(a)
# tmp = ascii_num - 97

# for i in range(tmp + 1):
#     print(chr(97 + i), end=' ')


# 77번 문제

# a = int(input())

# for i in range(a + 1):
#     print(i)


# 78번 문제

# a = int(input())
# temp = 0
# for i in range(a + 1):
#     if i % 2 == 0:
#         temp += i
    
# print(temp)



# 79번 문제

# a = list(input().split())

# for i in range(len(a)):
#     print(a[i])
#     if a[i] == 'q':
#         break


# 80번 문제

a = int(input())
tmp = 0
s = 0

while tmp < a:
    s += 1
    tmp += s

print(s)