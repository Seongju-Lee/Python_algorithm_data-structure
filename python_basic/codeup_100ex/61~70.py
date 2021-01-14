# 61번 문제

# a,b = map(int, input().split())
# print(a|b)


# 62번 문제

# a,b = map(int, input().split())
# print(a^b)

# 63번 문제 (삼항 연산자 이용하기)

# a,b = map(int, input().split())

# print(a if a>b else b)

# 64번 문제

# a,b,c = map(int, input().split())

# first = a if a < b else b
# print(first if first < c else c)

# 65번 문제

# a,b,c = map(int, input().split())

# if a % 2 == 0:
#     print(a)
# if b % 2 == 0:
#     print(b)
# if c % 2 == 0:
#     print(c)


# 65번 문제

# a,b,c = map(int, input().split())

# if a % 2 == 0:
#     print('even')
# else:
#     print('odd')
# if b % 2 == 0:
#     print('even')
# else:
#     print('odd')
# if c % 2 == 0:
#     print('even')
# else:
#     print('odd')

# 66번 문제

# a = int(input())

# if a > 0:
#     print('plus')
# else:
#     print('minus')

# if a % 2 == 0:
#     print('even')
# else:
#     print('odd')


# 67번 문제

# a = int(input())

# if 90 <= a <= 100:
#     print('A')
# elif 70 <= a < 89:
#     print('B')
# elif 40 <= a < 69:
#     print('C')
# elif a >= 0:
#     print('D')

# 69번 문제

a = input()

if a == 'A':
    print('best!!!')
elif a == 'B':
    print('good!!')
elif a == 'C':
    print('run!')
elif a == 'D':
    print('slowly~')
else:
    print('what?')