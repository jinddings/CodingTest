function solution(array, n) {
  let answer = 0;
  var diff = Math.abs(n - Math.min(...array));
  array.forEach((item) => {
    if (Math.abs(n - item) < diff) {
      diff = Math.abs(n - item);
    }
  });

  return array
    .filter((item) => Math.abs(n - item) === diff)
    .sort((a, b) => a - b)[0];
}
