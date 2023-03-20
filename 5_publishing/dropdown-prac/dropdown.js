
// * 기존 jQuery 코드
/*
$('.dropbtn').on('click', function (evt) {
  const ulElement = $('ul');
  
  // 단순 보이기 구현
  // ulElement.show();

  // 토글 기능 구현
  ulElement.toggle();
});

// Click Outside : 버튼 외부 요소 클릭시 드롭다운이 다시 닫히도록 할 경우 사용합니다.
$(document).on('click', function (evt) {
  if ($(evt.target).parents('.dropdown').length === 0) {
    $('ul').hide();
  }
});
*/

// ! 바닐라JS로 코드 변경해보기
// * 토글 기능
// 버튼 클릭 시 ul에 open 클래스 부여하고,
// css에서 ul의 class가 open일 경우 기존의 display:none에서 block으로 보이도록 함
document.querySelector('.dropbtn').addEventListener('click', () => {
  document.querySelector('ul').classList.toggle('open');
});

// * 버튼 외부 요소 클릭 시 드롭다운 닫기 기능
// document 클릭 시의 event를 추적하고
// ul의 클래스에 open이 부여되어있으면서 && event.target.children의 length가 0이 아닐 경우
// open 속성을 지워 기존의 display:none이 되도록 함
document.addEventListener('click', event => {
  if(
    document.querySelector('ul').classList.contains('open')
    && event.target.children.length !== 0
  ) {
    document.querySelector('ul').classList.remove('open');
  }
});

