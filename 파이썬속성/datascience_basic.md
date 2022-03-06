
# 파이썬 속성 강좌


### 출처

- "Data Science from scratch" - 저자 Joel Grus 


### 1. 기본기 다지기

파이썬에는 설계 원칙에 대한 일종의 교리인 'The Zen of Python'이 있다.
여기서 가장 중요한 것은 "어떤 일에든 명확한-바람직하고 유일한 방법이 존재한다"라는 말이다.
명확한 방식으로 쓰여진 코드를 일반적으로 '파이썬스럽다(Pythonic)'이라고 한다. 이제부터 파이썬에 대해 알아보자.
<br/><br/>
"아름다움이 추함보다 좋다. 명시가 암시보다 좋다. 단순함이 복잡함보다 좋다."


### 2. 파이썬 설치

- python.org 또는 아나콘다(Anaconda) 배포판


### 3. 가상환경

matplotlib 라이브러리 사용하여 데이터 시각화를 해야하는데,
matplotlib은 파이썬에서 기본적으로 제공하는 라이브러리가 아니기 때문에 직접 설치해야한다.
독립적인 파이썬 및 라이브러리 환경을 제공하는 가상 환경(virtual environment)은 버전 충돌 문제를 해결해줄 수 있다.
아나콘다에서 가상환경을 생성해보자. 가상환경이 활성화되어 있는 동안 설치한 모든 라이브러리는 dsfs 가상 환경에만 설치된다.

```shell
# dsfs라는 파이썬 3.6 가상 환경 생성
conda create -n dsfs python=3.9

# 가상 환경 활성화
source activate dsfs

# 가상 환경 비활성화
source deactivate
```

여기에 더해 파이썬 셸인 IPython을 설치하면 좋을 것이다.
```shell
python -m pip install ipython
```

### 4. 들여쓰기
다른 언어와는 다르게 파이썬에서는 들여쓰기를 통해 단락을 구분한다. 
들여쓰기를 잘못하면 오류가 발생할 수 있기 때문에 주의해야 한다.



### 5. 모듈
모듈을 사용할 때는 import를 사용해 불러온다.
matplotlib 라이브러리로 데이터를 시각화할 때는 다음과 같은 별칭을 관습적으로 사용한다.
```python
import matplotlib.pyplot as plt

plt.plot(...)
```

특정기능만 필요하다면 전체 모듈을 부르지 않고 해당 기능만 명시해서 불러올 수도 있다.
```python
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()
```
가장 좋지 않은 방법은 모듈의 기능을 통째로 불러와서 기존의 변수를 덮어쓰는 것이다.
```python
match = 10
from re import *   # re 라이브러리에 match라는 함수가 있기 때문에 변수를 덮어쓴다.
print(match)       # <function match at ~~~~~~>
```

### 6. 함수

일반함수
```python
def double(num):
    return num * 2
```

람다함수
```python
double = lambda x: x*2  # 좋은 방법은 아니다.
```

### 7. 문자열
작은 따옴표 혹은 큰 따옴표로 묶어 나타낸다.
특수문자를 인코딩할 때는 \(역슬래쉬)를 붙여준다.
문자열을 합치는 방법은 아래와 같다. ('+' 사용하기 or .format 사용하기)
```python
first_name = "Joel"
last_name = "Grus"
full_name1 = first_name + " " + last_name
full_name1 = "{0} {1}".format(first_name, last_name)
```

### 8. 예외처리
예외처리를 위해 사용하는 것은 try & except 문이다.
```python
try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
```

### 9. 리스트 
파이썬의 가장 기본적인 데이터 구조이다. 리스트는 순서가 있는 자료의 집합이다.
슬라이싱을 통해 원하는 자료를 분리하여 가져오는 것도 가능하다. (문자열도 슬라이싱이 가능하다!!)
#### 리스트 안에서 항목의 존재 여부 확인
```python
1 in [1, 2, 3]   #True
0 in [1, 2, 3]   #False
```

#### 리스트에 다른 리스트의 내용 추가하기
```python
x = [1, 2, 3]
x.extend([4, 5, 6]) # x는 [1, 2, 3, 4, 5, 6]이 된다.

# x의 내용을 바꾸고 싶지 않아 다른 변수를 선언할 때.
x = [1, 2, 3]
y = x + [4, 5, 6]
```

### 10. 튜플
변경할 수 없는 리스트이다. 대괄호 대신 소괄호를 사용한다. 함수에서 여러 개의 값을 반환할 때 튜플을 사용하면 편리하다.
#### 리스트와 튜플은 다중할당 지원
```python
x, y = 1, 2
x, y = y, x
```

### 11. 딕셔너리
기본적인 데이터 구조로 특정 값(value)과 연관된 키(key)를 연결해 값을 빠르게 검색할 수 있다.
#### 대괄호를 통해 키의 값 불러오기
```python
grades = {"Joel": 80, "Tim": 95}
joels_grade = grades["Joel"]  # 80이 저장됨.
```
딕셔너리에 존재하지 않는 키를 입력하면 KeyError가 발생하니 주의하자.
<br/>
#### in을 이용해 키의 존재 여부를 확인
```python
exist1 = "Joel" in grades   #True
exist2 = "Kate" in grades   #False
```
#### 대괄호를 사용해 키와 값을 수정하거나 넣어주기
```python
grades["Tim"] = 99   # 기존의 값을 수정
grades["Kate"] = 100   # Kate키를 가진 새로운 값 추가
```

#### 딕셔너리의 모든 값을 살펴보기
```python
grades_keys = grades.keys()  # 키에 대한 리스트
grades_values = grades.values()  # 값에 대한 리스트
grades_items = grades.items()  # (key, value) 튜플에 대한 리스트

"Kate" in grades_keys  # True. 그러나 리스트에서 사용하는 in은 속도가 느리다. O(n)
"Kate" in grades       # True. O(1) 훨씬 빠르다.
```
리스트보다 딕셔너리에서 in을 사용하는 것이 훨씬 빠르니 알아두자.

### 11-1. defalutdict