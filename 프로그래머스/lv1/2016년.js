function solution(a, b) {
  let days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
  let months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  let day = 0;
  day = a < 2 ? b : months.slice(0, a - 1).reduce((a, b) => a + b) + b;
  return days[(day + 4) % 7];
}
