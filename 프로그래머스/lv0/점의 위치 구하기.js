const isWhere = (a, b) => {
  if (b > 0) {
    return a > 0 ? 1 : 2;
  } else {
    return a > 0 ? 4 : 3;
  }
};
function solution(dot) {
  return isWhere(dot[0], dot[1]);
}
