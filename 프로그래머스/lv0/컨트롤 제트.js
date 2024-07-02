function solution(s) {
  let arr = s.split(' ').map((item) => (isNaN(item) ? item : Number(item)));
  return arr.reduce((acc, val, idx) => {
    if (val === 'Z') return acc - arr[idx - 1];
    return acc + val;
  });
}
