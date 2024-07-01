function factorial(num) {
  if (num === 1 || num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
function solution(n) {
  for (let i = 1; i < 11; i++) {
    if (factorial(i) > n) {
      return i - 1;
    }
  }
}
