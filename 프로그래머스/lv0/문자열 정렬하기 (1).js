function solution(my_string) {
  return my_string
    .split('')
    .filter((item) => !isNaN(item))
    .map((item) => Number(item))
    .sort((a, b) => a - b);
}
