function solution(n) {
  var answer = 1;
  let s = new Set();
  for (let i = 1; i <= n; i += 2) s.add(i);
  s.delete(1);
  s.add(2);

  for (let i = 3; i <= n; i++) {
    if (s.has(i)) {
      for (let j = 2 * i; j <= n; j += i) {
        s.delete(j);
      }
    }
  }
  return s.size;
}
