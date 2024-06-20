function solution(food) {
  var answer = '';
  let arr = [];

  for (let i = 1; i < food.length; i++) {
    answer += `${i}`.repeat(Math.floor(food[i] / 2));
  }

  return answer + '0' + answer.split('').reverse().join('');
}
