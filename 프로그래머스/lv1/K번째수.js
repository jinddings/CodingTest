function solution(array, commands) {
  var answer = [];
  for (let a = 0; a < commands.length; a++) {
    let [i, j, k] = commands[a];
    answer.push(
      array
        .slice(i - 1, j)
        .sort((a, b) => a - b)
        .at(k - 1)
    );
  }
  return answer;
}
