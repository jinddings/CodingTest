function solution(N, stages) {
  var answer = [];
  let people = stages.length;
  let m = new Map();

  for (let i = 1; i <= N + 1; i++) {
    m.set(i, stages.filter((stage) => stage == i).length / people);
    people -= stages.filter((stage) => stage == i).length;
  }

  return [...m]
    .slice(0, N)
    .sort((a, b) => b[1] - a[1] || a[0] - b[0])
    .map((item) => item[0]);
}
