function solution(dartResult) {
  var answer = 0;
  let nums = [];
  let score = 0;

  for (let i = 0; i < dartResult.length; i++) {
    // 숫자인 경우
    if (!isNaN(dartResult[i])) {
      score =
        Number(dartResult[i]) === 0 && Number(dartResult[i - 1]) === 1
          ? 10
          : Number(dartResult[i]);
    } else if (dartResult[i] === 'S') {
      nums.push(score);
    } else if (dartResult[i] === 'D') {
      nums.push(Math.pow(score, 2));
    } else if (dartResult[i] === 'T') {
      nums.push(Math.pow(score, 3));
    } else if (dartResult[i] === '*') {
      nums[nums.length - 1] = nums[nums.length - 1] * 2;
      nums[nums.length - 2] = nums[nums.length - 2] * 2;
    } else if (dartResult[i] === '#') {
      nums[nums.length - 1] = nums[nums.length - 1] * -1;
    }
  }
  console.log(nums);
  return nums.reduce((a, b) => a + b);
}
