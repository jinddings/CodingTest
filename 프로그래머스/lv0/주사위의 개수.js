function solution(box, n) {
  return box.reduce((acc, val) => (acc *= Math.floor(val / n)), 1);
}
