function solution(strings, n) {
  let m = new Map();

  m = strings.sort((a, b) => {
    if (a[n] == b[n]) {
      return a > b ? 1 : -1;
    } else if (a[n] > b[n]) {
      return 1;
    } else {
      return -1;
    }
  });
  return m;
}
