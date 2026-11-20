function reveal(){const io=new IntersectionObserver(e=>e.forEach(x=>{if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}}),{threshold:.1});$$('.rv:not(.in)').forEach(e=>io.observe(e))}
function growBars(){setTimeout(()=>$$('[data-w]').forEach(e=>e.style.width=e.dataset.w+'%'),150)}
function afterRender(){reveal();growBars();$$('[data-act=fav]').forEach(x=>{const on=S.fav.includes(+x.dataset.id);x.textContent=x.textContent.replace(/^(❤️|🤍)/,on?'❤️':'🤍')});$$('[data-act=cmp]').forEach(x=>x.textContent=S.cmp.includes(+x.dataset.id)?'✓ Dibanding':'+ Banding')}
(function(){const sp=$('#splash');if(sp){let seen=false;try{seen=sessionStorage.getItem('jk_seen')}catch(e){}
if(seen)sp.remove();else setTimeout(()=>{sp.classList.add('hide');try{sessionStorage.setItem('jk_seen','1')}catch(e){}},2000)}
$$('[data-n]').forEach(e=>{const n=+e.dataset.n;let i=0;const t=setInterval(()=>{e.textContent=++i;if(i>=n)clearInterval(t)},70)});
const b=$('#lastres');if(b&&S.res){const r=S.res.top[0],j=jb(r.id);b.innerHTML=`<div class="card rv"><b>Hasil terakhirmu:</b> ${esc(j.n)} (${r.p}% cocok) <a href="${ROOT}hasil.html">Lihat hasil</a></div>`}
afterRender()})();
