function factorial(n) {
  if (n == 1 || n == 0) return 1;
  return n * factorial(n - 1);
}
function solution(balls, share) {
  return Math.round(
    factorial(balls) / (factorial(balls - share) * factorial(share))
  );
}
