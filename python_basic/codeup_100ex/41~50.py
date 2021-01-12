# 41번 문제

# a = input()

# asc = ord(a)
# result = chr(asc + 1)

# print(result)

# 42번 문제
# a,b = map(int, input().split(' '))
# print(a//b) # 파이썬 몫 연산자: //

# 43번 문제

# a,b = map(int, input().split(' '))
# print(a%b) # 파이썬 나머지 연산자: %

# 44번 문제

# a = int(input())
# print(a+1)

# 45번 문제

# a,b = map(int, input().split(' '))
# print(a+b) # 합
# print(a-b) # 차
# print(a*b) # 곱
# print(a//b) # 몫
# print(a%b) # 나머지
# print('%.2f' %round(a/b,2)) # 나눗셈: 셋째 자리에서 반올림, 둘째 자리까지 출력

# 46번 문제

# data = list(map(int, input().split(' ')))
# result = 0

# for i in range(len(data)):
#     result += data[i]    
# print(result)
# print('%.1f' %(round(result/len(data), 2)))

# 47번 문제

# a = int(input())
# print(a*2)

# 48번 문제

# a,b = map(int, input().split())
# print(a*(2**b))

# 49번 문제
# a,b = map(int, input().split())
# print(1 if a > b else 0) # 삼항 연산자


# 50번 문제

a,b = map(int, input().split())
if a == b:
    print(1)
else:
    print(0)