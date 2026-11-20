(function(){let lv='SMK',ans=[],on=false;const app=$('#app');
function draw(){if(!on){app.innerHTML=`<h1>Tes Minat Jurusan</h1><div class="card qc" style="text-align:center"><h2 style="margin-top:0">Cari jurusan untuk jenjang apa?</h2><div class="seg"><button class="${lv==='SMK'?'on':''}" data-t="lv" data-v="SMK">SMK</button><button class="${lv==='Kuliah'?'on':''}" data-t="lv" data-v="Kuliah">Kuliah</button></div><p><button class="btn" data-t="start">Mulai ➜</button></p></div>`}
else{const i=ans.length,q=Q[i];app.innerHTML=`<p class="mut">Pertanyaan ${i+1} dari ${Q.length}</p><div class="bar"><i data-w="${i/Q.length*100}" style="width:${i/Q.length*100}%"></i></div><div class="card qc"><h2 style="margin-top:0">${esc(q[0])}</h2>${O.map(o=>`<button class="opt" data-t="ans" data-v="${o[1]}">${o[0]}</button>`).join('')}${i?'<button class="btn g sm" data-t="back">← Kembali</button>':''}</div>`}afterRender()}
app.addEventListener('click',e=>{const b=e.target.closest('[data-t]');if(!b)return;const t=b.dataset.t,v=b.dataset.v;
if(t==='lv'){lv=v;draw()}else if(t==='start'){on=true;ans=[];draw()}else if(t==='back'){ans.pop();draw()}
else if(t==='ans'){ans.push(+v);if(ans.length>=Q.length){const p=prof(ans);store.set('res',{p,top:rank(p,lv),lv});location.href=ROOT+'hasil.html'}else draw()}});
draw()})();
