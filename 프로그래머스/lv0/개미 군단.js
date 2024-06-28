function solution(hp) {
  let ants = [5, 3, 1];
  var answer = 0;
  ants.forEach((ant) => {
    answer += ~~(hp / ant);
    hp = hp % ant;
  });
  return answer;
}
