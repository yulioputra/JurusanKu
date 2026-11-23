/* Service worker: simpan halaman yang pernah dibuka supaya bisa dipakai offline. */
const V='jk-v25';
self.addEventListener('install',e=>{self.skipWaiting();e.waitUntil(caches.open(V).then(c=>c.addAll(['index.html','tes.html','info.html','cari-jalurku.html','persiapan-smp.html','tes-jurusan.html','hasil.html','riwayat.html','profil.html','jalur-masuk.html','glosarium.html','jurusan/index.html','404.html'])).catch(()=>{}))});
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==V).map(x=>caches.delete(x)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET'||!e.request.url.startsWith(self.location.origin))return;
e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(V).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request).then(r=>r||caches.match('index.html'))))});
