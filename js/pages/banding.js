(function(){const app=$('#app');function draw(){const l=S.cmp.map(jb).filter(Boolean);
if(l.length<2){app.innerHTML=`<h1>Bandingkan Jurusan</h1><div class="card">Pilih minimal 2 jurusan lewat tombol “+ Banding” di <a href="${ROOT}jurusan/index.html">daftar jurusan</a>.</div>`;return}
const row=(t,f)=>`<tr><th>${t}</th>${l.map(j=>`<td>${f(j)}</td>`).join('')}</tr>`;
app.innerHTML=`<h1>Bandingkan Jurusan</h1><div class="card tw"><table><tr><th></th>${l.map(j=>`<th>${j.ic} <a href="${href(j)}">${esc(j.n)}</a></th>`).join('')}</tr>${row('Jenjang',j=>j.lv)}${row('Gambaran',j=>esc(j.d))}${row('Dipelajari',j=>esc(j.mp))}${row('Prospek',j=>esc(j.jobs))}${row('Minat utama',j=>Object.keys(j.w).map(k=>TR[k][0]+' '+TR[k][1]).join(', '))}</table></div><button class="btn g" id="clr">Kosongkan</button>`;
$('#clr').onclick=()=>{S.cmp=[];store.set('cmp',[]);draw()};afterRender()}draw()})();
