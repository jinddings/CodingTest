function solution(numbers) {
  let nums = [
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
  nums.forEach(
    (item) => (numbers = numbers.replaceAll(item, `${nums.indexOf(item)}`))
  );

  return Number(numbers);
}
