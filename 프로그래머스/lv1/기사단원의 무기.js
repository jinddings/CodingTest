function solution(number, limit, power) {
  let knights = [];

  for (let i = 1; i <= number; i++) {
    let cnt = 0;
    for (let j = 1; j <= Math.sqrt(i); j++) {
      if (i % j == 0) {
        if (j * j == i) {
          cnt++;
        } else {
          cnt += 2;
        }
      }
    }
    if (cnt > limit) knights.push(power);
    else knights.push(cnt);
  }
  console.log(knights);

  return knights.reduce((a, b) => a + b);
}
