function cal_gcd(a, b) {
  return a % b === 0 ? b : cal_gcd(b, a % b);
}
function solution(numer1, denom1, numer2, denom2) {
  let num = denom1 * numer2 + denom2 * numer1;
  let denom = denom1 * denom2;

  return [num / cal_gcd(num, denom), denom / cal_gcd(num, denom)];
}
