
# 파이썬 속성 강좌


### 출처

- "Data Science from scratch" - 저자 Joel Grus


### 1. 기본기 다지기

<hr/>

파이썬에는 설계 원칙에 대한 일종의 교리인 'The Zen of Python'이 있다.
여기서 가장 중요한 것은 "어떤 일에든 명확한-바람직하고 유일한 방법이 존재한다"라는 말이다.
명확한 방식으로 쓰여진 코드를 일반적으로 '파이썬스럽다(Pythonic)'이라고 한다. 이제부터 파이썬에 대해 알아보자.
<br/><br/>
"아름다움이 추함보다 좋다. 명시가 암시보다 좋다. 단순함이 복잡함보다 좋다."

<br/>

### 2. 파이썬 설치

<hr/>

- python.org 또는 아나콘다(Anaconda) 배포판

<br/>

### 3. 가상환경

<hr/>

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

<br/>

### 4. 들여쓰기

<hr/>

다른 언어와는 다르게 파이썬에서는 들여쓰기를 통해 단락을 구분한다. 
들여쓰기를 잘못하면 오류가 발생할 수 있기 때문에 주의해야 한다.



### 5. 모듈

<hr/>

모듈을 사용할 때는 import를 사용해 불러온다.
matplotlib 라이브러리로 데이터를 시각화할 때는 다음과 같은 별칭을 관습적으로 사용한다.
```python
import matplotlib.pyplot as plt

plt.plot(...)
```

<br/>

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

<hr/>

일반함수
```python
def double(num):
    return num * 2
```

람다함수
```python
double = lambda x: x*2  # 좋은 방법은 아니다.
```

<br/>

### 7. 문자열

<hr/>

작은 따옴표 혹은 큰 따옴표로 묶어 나타낸다.
특수문자를 인코딩할 때는 \(역슬래쉬)를 붙여준다.
문자열을 합치는 방법은 아래와 같다. ('+' 사용하기 or .format 사용하기)
```python
first_name = "Joel"
last_name = "Grus"
full_name1 = first_name + " " + last_name
full_name1 = "{0} {1}".format(first_name, last_name)
```

<br/>

### 8. 예외처리

<hr/>

예외처리를 위해 사용하는 것은 try & except 문이다.
```python
try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
```

<br/>

### 9. 리스트

<hr/>

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

<br/>

### 10. 튜플

<hr/>

변경할 수 없는 리스트이다. 대괄호 대신 소괄호를 사용한다. 함수에서 여러 개의 값을 반환할 때 튜플을 사용하면 편리하다.
#### 리스트와 튜플은 다중할당 지원
```python
x, y = 1, 2
x, y = y, x
```

<br/>

### 11. 딕셔너리

<hr/>

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

<br/>

### 11-1. defalutdict

<hr/>
defaultdict와 평범한 딕셔너리의 차이점은 만약 존재하지 않는 키가 주어진다면 defaultdict는 이 키와 인자에서 주어진 값으로 dict에 새로운 항목을 추가해 준다는 것이다.
defaultdict를 사용하기 위해서는 collections 모듈에서 defaultdict를 가져와야한다.

```python
from collections import defaultdict

word_counts = defaultdict(int)  #int()는  0을 생성
for word in document:
    word_counts[word] += 1
```

리스트, 딕션너리 혹은 직접 만든 함수를 인자에 넣어줄 수도 있다.
```python
dd_list = defaultdict(list)         # list()는 빈 리스트를 생성
dd_list[2].append(1)                # 이제 dd_list는 {2: [1]}을 포함

dd_dict = defaultdict(dict)         # dict()는 빈 딕셔너리를 생성
dd_dict["Joel"]["City"] = "Seattle" # {"Joel": {"City": "Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                   # dd_pair는 {2: [0,1]}을 포함
```

<br/>

### 12. Counter
Counter는 연속된 값을 defalutdict(int)와 유사한 객체로 변환해주면, 키와 값의 빈도를 연결시켜준다.

```python
from collections import Counter
c = Counter([0, 1, 2, 0])  # c는 {0: 2, 1: 1, 2: 1} 이 된다.
```

특정 문서에서 단어의 개수를 셀 때도 유용하다.
```python
# document는 단어의 리스트
word_counts = Counter(document)
```

Counter 객체에는 most_common 메소드가 있는데, 빈도에 관련된 함수이다.
```python
# 가장 자주 나오는 단어 10개와 이 단어들의 빈도수를 출력
for word, count in word_counts.most_common(10):
    print(word, count)
```

### 13. Set

<hr/>
집합(Set)은 파이썬의 데이터 구조 중 유일한 항목의 집합을 나타내는 구조다. 집합은 중괄호를 사용해서 정의한다.

```python
mySet = {2, 3, 5, 7}
```

{}는 비어있는 딕셔너리를 의미하기 때문에 set()을 사용해서 비어있는 set을 생성할 수도 있다.

```python
s = set()
s.add(1)
s.add(2)
s.add(2)    # 중복을 허용하지 않기 때문에 {1, 2} 그대로이다.
x = len(s)  # 출력값: 2
y = 2 in s  # True
z = 3 in s  # False
```

Set에는 장점이 있다. 첫째로 in이 굉장히 빨리 작동한다는 점이다.
두 번째로 중복된 원소를 제거해준다는 점이 있다. 그러나 Set보다 리스트이 더 많이 사용된다.

<br/>


### 14. 흐름 제어

<hr/>
대부분의 프로그래밍 언어처럼 if를 통해 코드의 분기를 만들어 제어할 수 있다.
또한 삼항연산자를 통해 if-then-else문을 한 줄로 표현하기도 한다.

```python
parity = "even" if x % 2 == 0 else "odd"
```

파이썬에서는 while보다는 for in문이 더 많이 사용되는 편이다. 복잡한 논리체계가 필요하다면 continue와 break를 사용할 수도 있다.

<br/>

### 15. True와 False

<hr/>
파이썬의 boolean 타입은 대부분의 다른 언어와는 다르게 대문자로 시작한다. 
또한 존재하지 않는 값을 null이 아닌 None으로 표기한다.

```python
x = None
assert x == None, "this is the not the Pythonic way to check for None"
assert x is None, "this is the the Pythonic way to check for None"
```

파이썬에서는 다른 값으로도 boolean 타입을 표현할 수 있는데 다음은 모두 거짓을 의미한다.

- False
- None
- [] (빈 리스트)
- {} (빈 딕셔너리)
- ""
- set()
- 0
- 0.0

나머지 거의 모든 것이 참(True)을 의미한다. 이를 통해 리스트, 문자열, 딕셔너리 등이 비어 있는지 쉽게 확인할 수 있다.
하지만 이로 인해 예상치 못한 오류가 발생하기도 한다.

```python
s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""
```

위 코드는 아래와 같이 간략하게 표현할 수 있다.

```python
first_char = s and s[0]
```

.. 이어서


<br/>

### 16. 

<hr/>

<br/>

### 17. 

<hr/>

<br/>

### 18. 

<hr/>

<br/>

### 19. 

<hr/>

<br/>

### 20. 

<hr/>

<br/>

### 21. 

<hr/>

<br/>

### 22. 

<hr/>

<br/>

### 23. 

<hr/>

<br/>


### 24. 

<hr/>

<br/>

### 25. 

<hr/>

<br/>

### 26. 

<hr/>

<br/>