function solution(rsp) {
  let win = { 2: 0, 0: 5, 5: 2 };
  return rsp.split('').reduce((prev, curr) => (prev += win[curr]), '');
}
