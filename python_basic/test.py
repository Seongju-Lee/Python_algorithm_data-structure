# print('hello world', 12)

# float_num = float(input())

# print(round(float_num,2))

# num = input()

# print(num,end=" ")
# print(num,end=" ")
# print(num,end=" ")


# # 포맷형식 지정
# a,b = input().split(":")

# s = '{0}:{1}'.format(a,b)
# print(s)


# # strptime: 문자열을 날짜/시간으로 변환: %Y: 4자리 연도, %m: 월, %d: 일
# # strftime: 포맷 지정
# # from datetime import datetime
# # a = input()
# # date = datetime.strptime(a.replace('.',''), '%Y%m%d').strftime('%Y.%m.%d')
# # print(date)

# a,b,c = input().split('.')

# if len(a)==4 and len(b)==1 and len(c) ==2:
#     print("{0}.0{1}.{2}".format(a,b,c))
# if len(a)==4 and len(b)==2 and len(c) ==1:
#     print("{0}.{1}.0{2}".format(a,b,c))
# if len(a)==4 and len(b)==1 and len(c) ==1:
#     print("{0}.0{1}.0{2}".format(a,b,c))
# if len(a)==3 and len(b)==1 and len(c) ==2:
#     print("0{0}.0{1}.{2}".format(a,b,c))
# if len(a)==3 and len(b)==2 and len(c) ==1:
#     print("0{0}.{1}.0{2}".format(a,b,c))
# if len(a)==3 and len(b)==1 and len(c) ==1:
#     print("0{0}.0{1}.0{2}".format(a,b,c))
# if len(a)==2 and len(b)==1 and len(c) ==2:
#     print("00{0}.0{1}.{2}".format(a,b,c))
# if len(a)==2 and len(b)==2 and len(c) ==1:
#     print("00{0}.{1}.0{2}".format(a,b,c))
# if len(a)==2 and len(b)==1 and len(c) ==1:
#     print("00{0}.0{1}.0{2}".format(a,b,c))
# if len(a)==1 and len(b)==1 and len(c) ==2:
#     print("000{0}.0{1}.{2}".format(a,b,c))
# if len(a)==1 and len(b)==2 and len(c) ==1:
#     print("000{0}.{1}.0{2}".format(a,b,c))
# if len(a)==1 and len(b)==1 and len(c) ==1:
#     print("000{0}.0{1}.0{2}".format(a,b,c))
# if len(a) == 3 and len(b)==2 and len(c) ==2:
#     print("0{0}.{1}.{2}".format(a,b,c))
# if len(a) == 2 and len(b)==2 and len(c) ==2:
#     print("00{0}.{1}.{2}".format(a,b,c))
# if len(a) == 4 and len(b)==2 and len(c) ==2:
#     print("{0}.{1}.{2}".format(a,b,c)) # 문자열 포맷 방식

# ######################################################

# a,b,c=input().split('.')

# print('%04d' % int(a), end='.') # 정수를 4칸 맞추어 채우는데 앞의 빈칸은 0으로 채워짐
# print('%02d' % int(b), end='.')
# print('%02d' % int(c))

# rrn = input()
# rrn = rrn.replace("-","")

# print(rrn)

f = float(input())

a = round((f - int(f)),7)
a = str(a)
c,d = a.split(".")
print(int(f))
print(int(d))

################

i,x = input().split(".")
print(int(i))
print(int(x))

list_ = input()
result = [i for i in range(len(list_))]

for i in range(len(list_)):
    result[i] = str(list_[i])
    print("'" + str(result[i]) + "'")
