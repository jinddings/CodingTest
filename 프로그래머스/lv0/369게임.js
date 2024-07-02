function solution(order) {
  return String(order)
    .split('')
    .filter((item) => item % 3 === 0 && item !== '0').length;
}
