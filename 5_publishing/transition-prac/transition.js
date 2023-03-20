// * button use-javascript에 mouseover, mouseout 시 css 함수 사용
document.querySelector('.use-javascript').addEventListener('mouseover', event => {
  event.target.style.backgroundColor = '#e8344e';
  event.target.style.color = 'white';
});
document.querySelector('.use-javascript').addEventListener('mouseout', event => {
  event.target.style.backgroundColor = 'white';
  event.target.style.color = '#e8344e';
});

// * button use-class에 mouseenter, mouseleave 시 addClass, removeClass 함수 사용 css로 컨트롤
document.querySelector('.use-class').addEventListener('mouseenter', event => {
  event.target.classList.add('on');
});
document.querySelector('.use-class').addEventListener('mouseleave', event => {
  event.target.classList.remove('on');
});