function isLowerCase(s) {
  return s === s.toLowerCase(s);
}
function solution(my_string) {
  return my_string
    .split('')
    .map((item) =>
      isLowerCase(item) ? item.toUpperCase() : item.toLowerCase()
    )
    .join('');
}
