function solution(n, t, m, p) {
  var answer = '';
  str_nums = '';
  for (let i = 0; i <= m * t; i++) {
    str_nums += i.toString(n);
  }
  for (let i = 0; i < t; i++) {
    answer += str_nums[i * m + (p - 1)];
  }
  return answer.toUpperCase();
}
