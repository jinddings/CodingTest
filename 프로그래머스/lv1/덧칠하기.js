function solution(n, m, section) {
  var answer = 0;
  let s = new Set();
  for (let i = 1; i <= n; i++) s.add(i);
  section.forEach((val) => {
    if (s.has(val)) {
      for (let i = 0; i < m; i++) s.delete(val + i);
      answer += 1;
    }
  });

  return answer;
}
