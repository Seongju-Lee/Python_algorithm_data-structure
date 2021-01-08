######## 조건문 양식

a = 10
b = 20

if a < b:
    print('if문 양식 테스트')

# 파이썬 조건문 논리는 and랑 or이라고 적음

if a < 20 and b > 10:
    print("True")

if 10 <= a < 20: # 파이썬에서는 부등식이 가능하다.
    print("True")
if a >5:
    pass  # pass 키워드: 아무것도 처리하지 않을 때

# 조건부 표현식
score = 85
result = "Success" if score >=80 else "Fail"

print(result)

# in, not in
# 리스트, 튜플, 딕셔너리, 문자열에서 안에 데이터가 포함되어 있나, 없나 확인할 때 사용