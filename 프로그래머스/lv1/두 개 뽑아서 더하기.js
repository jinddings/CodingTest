function solution(numbers) {
  let s = new Set();

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      s.add(numbers[i] + numbers[j]);
    }
  }
  return [...s].sort((a, b) => a - b);
}
