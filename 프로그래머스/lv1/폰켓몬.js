function solution(nums) {
  let ponketmon_map = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (!ponketmon_map.get(nums[i])) {
      ponketmon_map.set(nums[i], 1);
    } else {
      ponketmon_map.set(nums[i], ponketmon_map.get(nums[i]) + 1);
    }
  }
  return nums.length / 2 > [...ponketmon_map].length
    ? [...ponketmon_map].length
    : nums.length / 2;
}
