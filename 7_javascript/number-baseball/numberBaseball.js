setAnswer();

// 답안 생성
function setAnswer() {
  let answer = '';
  while (answer.length < 3) {
    const randomNum = Math.floor(Math.random() * 10);
    if(!answer.includes(randomNum)) answer += randomNum;
  }
  let count = 0;
  console.log(`컴퓨터가 숫자(${answer})를 생성하였습니다. 답을 맞춰보세요!`);
  getValue(answer, count);
}

// 사용자에게 입력값 받기
function checkValue() {
  let value = prompt(`정답을 입력하세요.`);
  if(value === null) {
    alert(`입력을 취소하셨습니다.\n새로고침을 눌러 다시 시도해주세요.`);
    return false;
  } else if(value.match(/\D/)) {
    // 숫자로만 이루어져있을 경우 null, 숫자가 아닌 수가 있을 경우 배열값 반환
    alert(`3자리 수의 숫자만 입력해야 합니다.\n다시 입력해주세요.`);
    // value = '';
    checkValue();
  } else if(value.length > 3) {
    alert(`입력한 값의 길이는 3을 넘을 수 없습니다.\n다시 입력해주세요.`);
    value = '';
    checkValue();
  }
  console.log(`if를 뚫고 나온 value : ${value}`);
  return value;
}

// 입력값과 답안 비교
function getValue(answer, count) {
  let value = prompt(`정답을 입력하세요.`);
  if(value === null) {
    alert(`입력을 취소하셨습니다.\n새로고침을 눌러 다시 시도해주세요.`);
    return;
  }
  count++;
  console.log(`${count}번째 시도 : ${value}`);

  let s = 0, b = 0;
  let str = '';
  value.split('').forEach((e, idx) => {
    if(answer.indexOf(e) === idx) s++;
    else if(answer.split('').includes(e)) b++;
  })

  if(s === 3) str = `${s}S`;
  else if(b === 3) str = `${b}B`;
  else str = `${b}B${s}S`;
  console.log(str);
  answer !== value ? getValue(answer, count) : console.log(`${count}번만에 맞히셨습니다.\n게임을 종료합니다.`);
}