(function(){const app=$('#app');function draw(){const l=S.fav.map(jb).filter(Boolean);
app.innerHTML=`<h1>Jurusan Favorit</h1>`+(l.length?`<div class="grid">${l.map(card).join('')}</div>`:`<div class="card">Belum ada favorit. Tekan 🤍 pada jurusan yang kamu suka di <a href="${ROOT}jurusan/index.html">daftar jurusan</a>.</div>`);afterRender()}
window.refresh=draw;draw()})();
