function initWordDict(dict, s) {
  let words = ['A', 'E', 'I', 'O', 'U'];
  if (s.length > 5) return;

  dict.push(s);
  for (let i = 0; i < words.length; i++) {
    initWordDict(dict, s + words[i]);
  }
}

function solution(word) {
  var answer = 0;
  let dict = [];
  initWordDict(dict, '');
  dict.shift();
  return dict.indexOf(word) + 1;
}
