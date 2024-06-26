function solution(my_string, letter) {
  return my_string
    .split('')
    .filter((s) => ![...letter].includes(s))
    .join('');
}
