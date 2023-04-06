// 1. while문을 이용한 random값 생성
function usingWhile() {
  let answer = '';
  while (answer.length < 3) {
    const randomNum = Math.floor(Math.random() * 10);
    if(!answer.includes(randomNum)) answer += randomNum;
  }
  console.log(answer);
}

// 2. set 객체를 이용한 random값 생성
function usingSet() {
  let randomNum = new Set();
  while (randomNum.size < 3) randomNum.add(Math.floor(Math.random() * 10));
  const answer = [...randomNum];
  console.log(answer);
}

// 3. 배열 메서드를 이용한 random값 생성
function usingArray() {
  let answer = '';
  let num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  while (answer.length < 3) {
    const randomNum = Math.floor(Math.random() * num.length);
    answer += num.splice(randomNum, 1)[0];
  }
  console.log(answer);
}