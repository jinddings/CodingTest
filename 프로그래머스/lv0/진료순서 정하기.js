function solution(emergency) {
  let newArr = emergency.slice().sort((a, b) => b - a);
  return emergency.map((item) => newArr.indexOf(item) + 1);
}
