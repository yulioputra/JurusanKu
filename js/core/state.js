const ROOT=document.body.dataset.root||'';
const S={fav:store.get('fav',[]),cmp:store.get('cmp',[]),res:store.get('res',null)};
const cnt={};Q.forEach(q=>cnt[q[1]]=(cnt[q[1]]||0)+1);
const prof=a=>{const s={};Object.keys(TR).forEach(k=>s[k]=0);a.forEach((v,i)=>s[Q[i][1]]+=v);Object.keys(s).forEach(k=>s[k]=s[k]/(2*cnt[k]));return s};
const rank=(p,lv)=>J.filter(j=>j.lv===lv).map(j=>{let s=0,w=0;for(const k in j.w){s+=j.w[k]*p[k];w+=j.w[k]}return{id:j.id,p:Math.round(Math.min(.99,s/w)*100)}}).sort((a,b)=>b.p-a.p);
const jb=id=>J.find(j=>j.id===+id);
const href=j=>`${ROOT}jurusan/${j.slug}.html`;
