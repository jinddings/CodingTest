function solution(n) {
  var answer = [];

  let i = 2;
  while (n !== 1 || i < n) {
    if (n % i === 0) {
      answer.push(i);
      n = Math.floor(n / i);
    } else {
      i++;
    }
  }

  return [...new Set(answer)];
}
