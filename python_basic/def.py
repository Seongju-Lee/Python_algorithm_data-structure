# python 함수 양식

def testPrint():    # basic definition
    print('this is test with definition')


testPrint()

def ParmeterTest(a, b, c):  # parameter definition
    print(a+round(b)+c)
    print('this is print test {} 또는 {}'.format(a,c))  # print 출력 시 문자열.format 이용 예제


ParmeterTest(1,5.9,2)

def returnTest(a, b):   # return definition
    return a +b

print(returnTest(1,23.2)) 
print(returnTest(1,23.1))


# 함수에서 전역변수 사용하려면, global 키워드 사용

# 파이썬에서는 여러 개의 반환 값 가질 수 있음

# map(함수, 입력들)
# 람다는 이름 없는 함수라고 생각


print("Hello\nwo")
# 람다 표현식: 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 것이 특징( 이름없는 함수)
# 어떠한 함수 자체를 입력으로 받는 또 다른 함수를 사용할 때 유용, 또는 매우 간단하거나, 한번만 사용할 때

def add(a,b):
    return a+b
print(add(3,7))

print((lambda a,b: a+b)(3,7)) # 람다식

# 내장 함수에서 자주 사용되는 람다 함쉬:sorted
array = [('홍길동',50), ('이순신', 32), ('아무개',74)]

def my_key(x):
    return x[1]
print(sorted(array,key=my_key))

print(sorted(array, key=lambda x: x[1])) 


# 여러 개의 리스트
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = list(map(lambda a,b: a+b, list1, list2)) #람다식: a,b가 있으 때 두개를 더한다. a와b는 list1과 list2

print(result)


# 람다와 map을 이용한 구구단
result_ = list(map(lambda x:str((x//10))+'*'+str((x%10))+' = ' + str((x//10)*(x%10)), range(10,100)))

print(result_)