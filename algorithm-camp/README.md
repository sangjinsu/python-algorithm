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





