function solution(k, score) {
  let arr = [];
  var answer = [];
  for (let item of score) {
    arr.push(item);
    arr = arr.sort((a, b) => b - a).slice(0, k);
    answer.push(Math.min(...arr));
  }
  return answer;
}
