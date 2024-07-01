function solution(numbers) {
  let [max1, max2] = numbers
    .sort((a, b) => a - b)
    .splice(numbers.length - 2, 2);
  return max1 * max2;
}
