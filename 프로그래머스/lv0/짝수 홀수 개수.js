function solution(num_list) {
  return [
    num_list.filter((val) => val % 2 === 0).length,
    num_list.filter((val) => val % 2 === 1).length,
  ];
}
