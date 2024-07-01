function solution(my_string) {
  return my_string
    .match(/\d/g)
    .map((item) => Number(item))
    .reduce((acc, val) => acc + val);
}
