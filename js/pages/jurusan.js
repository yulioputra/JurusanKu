(function(){const app=$('#app');let flt=new URLSearchParams(location.search).get('lv')||'Semua',q='',so='nama';
app.innerHTML=`<div class="row" style="margin-bottom:12px"><div class="seg" id="sg"></div><input type="search" id="q" placeholder="Cari jurusan atau profesi…" aria-label="Cari"><select id="so" aria-label="Urutkan"><option value="nama">A–Z</option><option value="jenjang">Jenjang</option></select></div><div id="cmpbar"></div><div class="grid" id="jl"></div>`;
function list(){$('#sg').innerHTML=['Semua','SMK','Kuliah'].map(x=>`<button class="${flt===x?'on':''}" data-f="${x}">${x}</button>`).join('');
let a=J.filter(j=>(flt==='Semua'||j.lv===flt)&&(j.n+j.d+j.jobs).toLowerCase().includes(q.toLowerCase()));a=so==='nama'?a.sort((x,y)=>x.n.localeCompare(y.n)):a.sort((x,y)=>x.lv.localeCompare(y.lv));
$('#jl').innerHTML=a.map(card).join('')||'<p class="mut">Jurusan tidak ditemukan.</p>';
$('#cmpbar').innerHTML=S.cmp.length?`<div class="card">Dipilih: ${S.cmp.length}/3 <a class="btn sm" href="${ROOT}banding.html">Bandingkan</a></div>`:'';afterRender()}
window.refresh=()=>{$('#cmpbar').innerHTML=S.cmp.length?`<div class="card">Dipilih: ${S.cmp.length}/3 <a class="btn sm" href="${ROOT}banding.html">Bandingkan</a></div>`:''};
$('#q').oninput=e=>{q=e.target.value;list()};$('#so').onchange=e=>{so=e.target.value;list()};$('#sg').onclick=e=>{const b=e.target.closest('[data-f]');if(b){flt=b.dataset.f;list()}};list()})();
