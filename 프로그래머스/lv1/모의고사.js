function solution(answers) {
  let max_score_p = [];
  let answer = [0, 0, 0];
  let answer1 = [1, 2, 3, 4, 5];
  let answer2 = [2, 1, 2, 3, 2, 4, 2, 5];
  let answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  while (true) {
    if (
      answer1.length < answers.length ||
      answer2.length < answers.length ||
      answer3.length < answers.length
    ) {
      answer1.push(...answer1);
      answer2.push(...answer2);
      answer3.push(...answer3);
    } else {
      answer1 = answer1.slice(0, answers.length);
      answer2 = answer2.slice(0, answers.length);
      answer3 = answer3.slice(0, answers.length);
      break;
    }
  }

  answer[0] = answers.filter((a, i) => answer1[i] === a).length;
  answer[1] = answers.filter((a, i) => answer2[i] === a).length;
  answer[2] = answers.filter((a, i) => answer3[i] === a).length;

  let max_cnt = Math.max(...answer);
  for (let i = 0; i < answer.length; i++) {
    if (answer[i] == max_cnt) max_score_p.push(i + 1);
  }
  return max_score_p;
}
