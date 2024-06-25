function solution(babbling) {
  var answer = 0;
  let able = ['aya', 'ye', 'woo', 'ma'];
  babbling.forEach((item) => {
    able.forEach((a) => {
      if (!item.includes(a.repeat(2))) {
        item = item.replace(new RegExp(`${a}`, 'g'), ' ');
      }
    });
    if (item.replace(/ /g, '').length == 0) answer += 1;
  });
  return answer;
}
