function solution(lottos, win_nums) {
  let rank = { 6: 1, 5: 2, 4: 3, 3: 4, 2: 5 };

  let correct_cnt = win_nums.filter((win_num) =>
    lottos.includes(win_num)
  ).length;
  let best_cnt = correct_cnt + lottos.filter((num) => num === 0).length;
  let worst_cnt = correct_cnt;

  console.log([...Object.keys(rank)]);

  return [
    [...Object.keys(rank)].includes(String(best_cnt)) ? rank[best_cnt] : 6,
    [...Object.keys(rank)].includes(String(worst_cnt)) ? rank[worst_cnt] : 6,
  ];
}
