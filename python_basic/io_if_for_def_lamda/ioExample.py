import sys
# 기본 입출력

# input() : 한 줄의 문자열을 입력 받는 함수
# map(): 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

#데이터 개수 입력
#n = int(input())

# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split())) # 공백을 기준으로 나누고, 정수형을 바꿔준뒤 리스트로 만들어줌

# 입력받을 데이터가 공백 기준으로 몇개인지 정해져 있는 경우, 변수명을 직접 입력해서 정해진 양 입력 받기 가능.
a,b,c = map(int, input().split()) 

#print(n)
print(data)

print(a,b,c)

# 입력을 최대한 빠르게 받아야 하는 경우

# sys 라이브러리에 정의 되어 있는 sys.stdin.readline() 메소드 사용ㅇ
# 단, 입력 후 엔터가 줄 바꿈 기호로 입력 되므로, rstrip() 함께 사용

# 입력의 개수가 많은 경우 -> 사용

data = sys.stdin.readline().rstrip()
print(data)

#####################
### 표준 출력
#####################

# print는 기본적으로 줄 바꿈을 수행 -> end 속성 변경 가능

a = 1
b = 2

print(a,b)
print(7, end=" ")
print(8, end=" ")
print("정답은 " + str(b) + "입니다.") # 정수와 문자열 연산이 안되기 때문에 str형 변환

# f-string 위 방식 처럼 안해도 문자열 앞에 접두어로 f 사용하면 {}안에 정수형 문자로 인식
print(f"정답은 {b}입니다.")
