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

## Chapter3. 탐욕법

- 매 순간마다 최선의 경우만 골라간다
- 다른 경우는 고려하지 않으며 다음 또한 고려하지 않는다
- 시간초과 발생을 고려하여 문제 풀이 필요
- 반례 상화이 없는지 신중하게 고려

## Chapter4. DFS, BFS, 백트래킹

### 그래프

- 방향성 그래프
- 무방향성, 양방향 그래프
- 순환 그래프
- 비순환 그래프

### 방향성 비순환 그래프

- DAG
- Directed Acyclic Graph
- VSC 버전 관리 시스템 - Git 등

### 트리

- 순환성 없는 무방향 그래프
- 특정하지 않으면 어떤 노드이든지 루트가 될 수 있다
- 가장 바깥쪽 노드는 리프노드이다
- node A 에서 node B 로 가는 경로는 반드시 존재하며 유일하다
- 노드 개수 = 간선 개수 + 1

- 전산학에서의 트리는 방향 그래프이고 루트는 하나이다

### 코드로 나타내는 방법

1. 인접 행렬(2차원 배열)
2. 인접 리스트(딕셔너리 + 리스트)

#### 비교하기

인접 행렬은 N2 의 공간 복잡도를 가져가고 중복 데이터가 생긴다.
인접 리스트는 반면에 해당 노드 존재 유무를 판단하는데 N 이라는 시간 복잡도를 가진다

### DFS

- 깊이 우선 탐색
- stack, recursion 을 활용하여 구현한다

```python
def dfs(now):
    for nxt in range(13):
        if adj[now][nxt]:
            dfs(nxt)
```

### BFS

- 너비 우선 탐색
- 큐를 사용해서 구현

```python
from collections import deque


def bfs():
    q = deque()
    q.append(0)
    while q:
        now = q.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                q.append(nxt)
```

### DFS && BFS

#### 인접 행렬 vs 인접 리스트

- 인접 행렬 : O(v^2)
- 인접 리스트: O(V+E)

## 방향값

```python
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
```

### 백트래킹

- 가지치기를 통해 탐색 경우의 수를 줄이는 방법이다

## Chapter5. 이진 탐색

- 탐색 전 정렬이 필요하다
- 절반씩 줄여가면서 답을 찾는다
- 정렬 O(nlogn) + 이진 탐색 O(logn) 이므로 결과적으로 O(nlogn)
- 이미 정렬되어 들어오면 이진 탐색만 하므로 O(logn) 이다

```python
from bisect import bisect_left, bisect_right
```

### Parametric Search 파라메트릭 서치, 매개변수 탐색

- 최적화 문제를 결정 문제로 바꿔서 이진 탐색으로 해결하는 방법이다
- 최적화 문제 Optimization Problem
    - 문제 상황을 만족하는 변수의 최소값, 최대값을 구하는 문제
- 결정 문제 Decision Problem
- 매개변수가 주어지면 true, false 가 결정되어야 한다
- 가능한 해의 영역이 연속적이어야 한다
- 범위를 절반으로 줄이면서 가운데 값이 true, false 인지 구한다
- 이진 탐색과 같은 원리이다

## Chapter6. 동적 계획법, Dynamic Programming

- 문제를 작게 나누어 작은 문제의 답을 구하고, 더 큰 문제의 답을 구한다

### DP 두가지 구현 방법

#### Top-Down

- 구현 : 재귀
- 저장 방식 : 메모이제이션 Memoization

#### Bottom-Up

- 구현 : 반복문
- 저장 방식 : 타뷸레이션 Tabulation

### Memoiztion, Top-Down

- 부분 문제들의 답을 한 번 구하면 다시 구하지 않도록 캐시에 저장하여 사용하는 방법
- 필요한 부분의 문제들만 구한다 - Lazy Evaluation

### Tabulation, Buttom-Up

- 부분 문제들의 답을 미리 다 구한다 
- 테이블을 채워나가는 방식 - 타뷸레이션 

## DP 구현 2가지 장단점

### Top-Down

- 구현 : 재귀
- 저장 방식 : 메모이제이션
- 장점 : 직관적이라 코드 가독성이 좋음
- 단덤 : 재귀함수 호출을 많이 해서 느릴 수 있다 

### Bottom-Up

- 구현 : 반복문 
- 저장 박식 : 타뷸레이션
- 장점 : 시간과 메모리를 조금 절약할 수 있음
- 단점 : DP 테이블을 채워나가는 순서를 알아야 함