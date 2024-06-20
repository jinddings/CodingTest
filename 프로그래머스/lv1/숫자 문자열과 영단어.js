function solution(s) {
  var answer = s;
  let numbers = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
  ];

  for (let i = 0; i < numbers.length; i++) {
    let tmp = answer.split(numbers[i]);
    answer = tmp.join(i);
  }

  return Number(answer);
}
