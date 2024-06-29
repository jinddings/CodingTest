function solution(num_list, n) {
  var answer = [];

  for (let row = 0; row < num_list.length / n; row++) {
    answer.push(num_list.slice(row * n, row * n + n));
  }
  return answer;
}
