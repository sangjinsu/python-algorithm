# 컴공선배 알고리즘 캠프

## Chapter1. 자료구조

### 배열, 벡터(동적 배열)

- 삽입/삭제 : O(N)
    - 삽입시 데이터 이동이 필요하며 첫번재 인덱스에 값 추가시 최대 데이터 N 개를 이동해야 한다
    - 삭제시 최대 N개의 데이터를 앞으로 이동해야 한다
- 탐색: O(1)
    - 인덱스를 통한 임의 접근 가능

### 연결 리스트

- 삽입/삭제 : O(1)
    - 연결 관계를 변경하면서 삽입, 삭제가 빠르다
- 탐색: O(N)
    - 첫 노드부터 찾는 값을 가진 노드로 이동하면서 탐색한다

### 스택

- FILO, Fist In Last Out
- 삽입/삭제 : O(1)
- 탐색: O(N)

### 큐

- FIFO, First In First Out
- 삽입/삭제 : O(1)
- 탐색: O(N)

```python
from collections import deque
```

### 우선순위 큐

- 삽입/삭제 : O(logN)

```python
import heapq  # min-heap
from queue import PriorityQueue  # thread-safe 느린 속도
```

### 맵, 딕셔너리

- key, value
- key 는 중복되어서는 안된다
- 삽입/삭제 : python, golang Hash Table 사용 O(1)

### 집합

- 중복 불가
- 삽입/삭제 : O(1)

## Chapter2. 완전 탐색

장점: 반드시 답을 찾을 수 있다
단점: 시간과 리소스가 많이 사용된다

### Brute-Force 무차별 대입

### Permutation 순열

- 모든 경우의 수를 순서대로 살펴볼 때 용이하다

```python
from itertools import permutations
```

### Combination 조합

```python
from itertools import combinations
```

