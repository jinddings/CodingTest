function solution(my_string) {
  let answer = '';
  let dict = {};

  my_string = my_string.split('').forEach((item) => {
    if (!dict.hasOwnProperty(item)) {
      dict[item] = true;
      answer += item;
    }
  });

  return answer;
}
