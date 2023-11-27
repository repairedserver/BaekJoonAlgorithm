# [level 4] 도둑질 - 42897 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42897) 

### 성능 요약

메모리: 88.4 MB, 시간: 566.16 ms

### 구분

코딩테스트 연습 > 동적계획법（Dynamic Programming）

### 채점결과

정확성: 50.0<br/>효율성: 50.0<br/>합계: 100.0 / 100.0

### 제출 일자

2023년 11월 1일 19:11:51

### 문제 설명

<p>도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다. </p>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/ybm/e7dd4f51c3/a228c73d-1cbe-4d59-bb5d-833fd18d3382.png" title="" alt="image.png"></p>

<p>각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.</p>

<p>각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.</p>

<h5>제한사항</h5>

<ul>
<li>이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.</li>
<li>money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>money</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 1]</td>
<td>4</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges