function solution(age) {
  return age
    .toString()
    .split('')
    .map((c) => 'abcdefghij'[c])
    .join('');
}
