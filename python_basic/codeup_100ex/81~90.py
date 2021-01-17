
# 81번 문제

# n, m = map(int, input().split())

# for i in range(n):
#     for j in range(m):
#         print(i + 1, j + 1)


# 82번 문제

# a = int(input(),16) # 정수형 출력: a
# b = hex(a)      # a를 16진수로 변환: b

# b = b.replace('0x','').upper()

# for i in range(15):
#     print(b + '*' + hex(i+1).replace('0x','').upper() + '=' + hex(a*(i+1)).replace('0x','').upper())


# 83번 문제

# a = int(input())

# for i in range(a):
#     if '3' in str(i + 1):
#         print('X', end = ' ')

#     elif '6' in str(i + 1):
#         print('X', end = ' ')
    
#     elif '9' in str(i + 1):
#         print('X', end = ' ')
    
#     else:
#         print(i + 1, end=' ')


# 84번 문제

# r, g, b= map(int, input().split())
# count = 0

# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i, j, k)
#             count += 1
# print(count)


# 85번 문제

# h, b, c, s = map(int, input().split())

# bit = h * b * c * s

# byte = bit / 8
# kbyte = byte / 1024
# mbyte = kbyte / 1024

# print('%.1f MB' %(round(mbyte,2)))


# 86번 문제

# w, h, b = map(int, input().split())

# bit = w * h * b

# byte = bit / 8
# kbyte = byte / 1024
# mbyte = kbyte / 1024

# print('%.2f MB' %(round(mbyte, 2)))


# 87번 문제

# a = int(input())
# tmp = 0
# result = 0

# while result < a:
#     tmp += 1
#     result += tmp

# print(result)


# 88번 문제

# a = int(input())

# for i in range(1,a+1):
#     if i%3 == 0:
#         continue
#     else:
#         print(i, end=' ')

# 89번 문제

# a, d, n = map(int, input().split())

# print(d*(n-1) + a)

# 90번 문제

a, r, n = map(int, input().split())

print(a*(r**(n-1)))

