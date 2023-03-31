document.addEventListener('DOMContentLoaded', () => {
  show_bucket();
})

function show_bucket() {
  fetch('/bucket')
  .then(res => res.json())
  .then(data => {
    const rows = data['buckets'];
    rows.forEach(element => {
      const num = element['num'];
      const bucket = element['bucket'];
      const done = element['done'];
      let temp_html = ``;

      if(done === 0) {
        temp_html = `
          <li>
            ✨&nbsp;<h2>${bucket}</h2>
            <button onclick="done_bucket(${num})" type="button" class="btn btn-primary">완료</button>
          </li>
        `;
      } else {
        temp_html = `
          <li>
            ✨&nbsp;<h2>${bucket} 완료!!</h2>
          </li>
        `;
      }

      document.querySelector('#bucket-list').insertAdjacentHTML('beforeend', temp_html)
    })
  })
  .catch(err => {
    console.log(err)
  });
}

function save_bucket() {
  let formData = new FormData();
  formData.append('bucket_give', document.querySelector('#bucket').value);
  fetch('/bucket', { method: 'POST', body: formData, })
  .then(res => res.json())
  .then(data => {
    alert(data['msg']);
    window.location.reload();
  })
  .catch(err => {
    console.log(err)
  });
}

function done_bucket(num) {
  let formData = new FormData();
  formData.append('num_give', num);
  fetch('/bucket/done', { method: 'POST', body: formData, })
  .then((response) => response.json())
  .then((data) => {
    alert(data['msg']);
    window.location.reload();
  })
  .catch(err => {
    console.log(err)
  });
}