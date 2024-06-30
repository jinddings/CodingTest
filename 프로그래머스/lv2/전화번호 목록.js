let dict = {};

function solution(phone_book) {
  var answer = true;
  phone_book.forEach((phoneNumber) => (dict[phoneNumber] = true));

  for (let number of phone_book) {
    for (let i = 0; i < number.length; i++) {
      let prefix = number.substring(0, i);
      if (dict[prefix]) return false;
    }
  }
  return true;
}
