# python-algorithm

파이썬 알고리즘 문제풀이

## 백준 알고리즘

| Date       | Name        | Site               |                   Type           | Solved                                                       | visualize |
| ---------- | ----------- | --------------------|---------------------------- | ------------------------------------------------------------ | ---- |
| 2021.07.21 | 제로 | [10773](https://www.acmicpc.net/problem/10773) | stack | [solved](https://github.com/jinsuSang/python-algorithm/blob/main/boj/stack/boj_10773.py) | [show](http://pythontutor.com/visualize.html#code=k%20%3D%20int%28input%28%29.strip%28%29%29%0A%0Astack%20%3D%20list%28%29%0A%0Afor%20i%20in%20range%28k%29%3A%0A%20%20%20%20item%20%3D%20int%28input%28%29.strip%28%29%29%0A%0A%20%20%20%20if%20item%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20stack.pop%28%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20stack.append%28item%29%0A%0Atotal%20%3D%200%0Afor%20i%20in%20stack%3A%0A%20%20%20%20total%20%2B%3D%20i%0A%0Aprint%28total%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%224%22,%224%22,%220%22,%223%22,%220%22%5D&textReferences=false) |
| 2021.07.21 | 단어순서 뒤집기 | [12605](https://www.acmicpc.net/problem/12605) | stack | [solved](https://github.com/jinsuSang/python-algorithm/blob/main/boj/stack/boj_12605.py) | [show](http://pythontutor.com/visualize.html#code=n%20%3D%20int%28input%28%29.strip%28%29%29%0A%0Afor%20i%20in%20range%28n%29%3A%0A%20%20%20%20stack%20%3D%20input%28%29.strip%28%29.split%28%29%0A%0A%20%20%20%20answer%20%3D%20f'Case%20%23%7Bi%20%2B%201%7D%3A'%0A%20%20%20%20while%20len%28stack%29%20%3E%200%3A%0A%20%20%20%20%20%20%20%20word%20%3D%20stack.pop%28%29%0A%20%20%20%20%20%20%20%20answer%20%2B%3D%20'%20'%20%2B%20word%0A%0A%20%20%20%20print%28answer%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) |
| 2021.07.21 | 막대기 | [17068](https://www.acmicpc.net/problem/17608) | stack | [solved](https://github.com/jinsuSang/python-algorithm/blob/main/boj/stack/boj_17608.py) | [show](http://pythontutor.com/visualize.html#code=%0An%20%3D%20int%28input%28%29.strip%28%29%29%0A%0Asticks%20%3D%20list%28%29%0A%0Afor%20i%20in%20range%28n%29%3A%0A%20%20%20%20stick%20%3D%20int%28input%28%29.strip%28%29%29%0A%20%20%20%20sticks.append%28stick%29%0A%0Ahighest%20%3D%200%0Acount%20%3D%200%0Afor%20i%20in%20range%28n%29%3A%0A%20%20%20%20stick%20%3D%20sticks.pop%28%29%0A%20%20%20%20if%20highest%20%3C%20stick%3A%0A%20%20%20%20%20%20%20%20count%20%2B%3D%201%0A%20%20%20%20%20%20%20%20highest%20%3D%20stick%0A%0Aprint%28count%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) |
| 2021.07.20 | 요세푸스 문제 | [1158](https://www.acmicpc.net/problem/1158)|  queue| [solved](https://github.com/jinsuSang/python-algorithm/blob/main/boj/queue/boj_1158.py) :heavy_check_mark: | [show](http://pythontutor.com/visualize.html#code=n,%20k%20%3D%20map%28int,%20input%28%29.split%28%29%29%0A%0Aqueue%20%3D%20list%28range%281,%20n%20%2B%201%29%29%0Aresult%20%3D%20list%28%29%0A%0Ai%20%3D%20k%20-%201%0Awhile%20len%28queue%29%3A%0A%20%20%20%20item%20%3D%20queue.pop%28i%29%0A%20%20%20%20result.append%28item%29%0A%20%20%20%20if%20len%28queue%29%20%3E%200%3A%0A%20%20%20%20%20%20%20%20i%20%3D%20%28i%20%2B%20k%20-%201%29%20%25%20%28len%28queue%29%29%0A%0Aprint%28'%3C%7B%7D%3E'.format%28',%20'.join%28map%28str,%20result%29%29%29%29%0A&cumulative=false&curInstr=1&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%227%203%22%5D&textReferences=false) |
| 2021.07.20 | 에디터 | [1406](https://www.acmicpc.net/problem/1406)| stack| [solved](https://github.com/jinsuSang/python-algorithm/blob/main/boj/stack/boj_1406.py) | |
| 2021.07.19 | 스택 수열 | [1874](https://www.acmicpc.net/problem/1874)| stack| [solved](https://github.com/jinsuSang/python-algorithm/blob/main/boj/stack/boj_1874.py) | |
| 2021.07.18 | 단어 뒤집기 | [9093](https://www.acmicpc.net/problem/9093)| stack | [solved](https://github.com/jinsuSang/python-algorithm/blob/main/boj/stack/boj_9093.py) | |
| 2021.07.18 | 괄호        | [9012](https://www.acmicpc.net/problem/9012)|stack| [solved](https://github.com/jinsuSang/python-algorithm/blob/main/boj/stack/boj_9012.py) | |

## 프로그래머스

| Date       | Name        | Type                                             | Solved                                                       |
| ---------- | ----------- | ------------------------------------------------ | ------------------------------------------------------------ |
| 2021.07.19 | 포켓몬 | [찾아라 프로그래밍 마스터](https://programmers.co.kr/learn/courses/30/lessons/1845) | [solved](https://github.com/jinsuSang/python-algorithm/blob/main/programmers/level1/%ED%8F%AC%EC%BC%93%EB%AA%AC.py) |
| 2021.07.19 | 완주하지 못한 선수 | [해시](https://programmers.co.kr/learn/courses/30/lessons/42576) | [solved](https://github.com/jinsuSang/python-algorithm/blob/main/programmers/level1/%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80%EB%AA%BB%ED%95%9C%EC%84%A0%EC%88%98.py) |
| 2021.07.19 | 모의고사 | [완전탐색](https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3) | [solved](https://github.com/jinsuSang/python-algorithm/blob/main/programmers/level1/%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC.py) |

## SW EXPERT ACADEMY

| Date       | Name        | Site                                 | Type     | level      | Solved                                                       |
| ---------- | ----------- | --------------------------------------|---------- | ----|-------------------------------------------------------- |
| 2021.07.20 | 초심자의 회문 검사 | [1989](https://swexpertacademy.com/main/code/problem/problemDetail.do)| | d2 | [solved](https://github.com/jinsuSang/python-algorithm/blob/main/swexpert/d2/sw_1989.py) |
| 2021.07.20 | 수도 요금 경쟁 | [1284](https://swexpertacademy.com/main/code/problem/problemDetail.do)| | d2 |[solved](https://github.com/jinsuSang/python-algorithm/blob/main/swexpert/d2/sw_1284.py) |
| 2021.07.20 | 새로운 불면증 치료법 | [1288](https://swexpertacademy.com/main/code/problem/problemDetail.do)| | d2 |[solved](https://github.com/jinsuSang/python-algorithm/blob/main/swexpert/d2/sw_1288.py) |
