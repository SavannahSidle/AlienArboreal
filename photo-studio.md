---
layout: page
title: Photo Studio
permalink: /photo-studio/
description: Prepare up to ten gecko photos, crop each image, and arrange the main photo.
---
<style>
.ps{max-width:980px;margin:auto}.ps-toolbar{display:flex;gap:.75rem;flex-wrap:wrap;align-items:center;margin:1rem 0}.ps button,.ps label.ps-upload{display:inline-flex;align-items:center;justify-content:center;padding:.65rem 1rem;border:1px solid var(--moss);border-radius:6px;background:var(--panel);color:var(--ink);font:inherit;cursor:pointer}.ps button:disabled{opacity:.4;cursor:default}.ps-upload input{position:absolute;opacity:0;width:1px;height:1px}.ps-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:.8rem}.ps-item{border:1px solid var(--line);padding:.5rem;border-radius:8px;background:var(--panel)}.ps-item.active{border-color:var(--acid)}.ps-item img{width:100%;height:125px;object-fit:contain;background:#050b07;border-radius:5px}.ps-item .ps-actions{display:flex;justify-content:space-between;gap:.25rem;margin-top:.5rem}.ps-item button{padding:.2rem .5rem}.ps-preview{display:grid;grid-template-columns:minmax(0,1fr) minmax(220px,300px);gap:1rem;margin:1.5rem 0}.ps-preview canvas{width:100%;max-height:500px;object-fit:contain;background:#07100a;border:1px solid var(--line)}.ps-controls{display:grid;gap:.7rem;align-content:start}.ps-controls label{display:grid;gap:.25rem}.ps-controls select,.ps-controls input[type=range]{width:100%}.ps-note{color:var(--muted);font-size:.85rem}.ps-item[draggable=true]{cursor:grab}@media(max-width:680px){.ps-preview{grid-template-columns:1fr}}
</style>
<div class="ps">
<p>Prepare up to 10 photos at once. Select a thumbnail to edit its shape and crop. Drag thumbnails to reorder, or use the arrow buttons on mobile. The first photo is the main photo.</p>
<p class="ps-note"><strong>Safe workspace:</strong> Your original photos are never modified. This tool works in your browser and does not edit gecko records or lineage. Export the prepared images, then upload them in order using Pages CMS.</p>
<div class="ps-toolbar"><label class="ps-upload">Add photos (up to 10)<input id="ps-files" type="file" accept="image/*" multiple></label><button id="ps-export" disabled>Download prepared photos</button><button id="ps-clear">Clear workspace</button><span id="ps-count" aria-live="polite">0 / 10</span></div>
<div id="ps-grid" class="ps-grid" aria-label="Photo order"></div>
<div id="ps-editor" class="ps-preview" hidden>
<canvas id="ps-canvas" width="600" height="450" aria-label="Edited photo preview"></canvas>
<div class="ps-controls">
<strong id="ps-title">Edit photo</strong>
<label>Frame shape<select id="ps-shape"><option value="original">Original proportions</option><option value="square">Square</option><option value="landscape">Horizontal rectangle</option><option value="portrait">Vertical rectangle</option><option value="circle">Circle</option></select></label>
<label>Photo sizing<select id="ps-fit"><option value="contain">Fit whole photo</option><option value="cover">Crop to fill frame</option></select></label>
<label>Zoom <input id="ps-zoom" type="range" min="1" max="3" step=".01" value="1"></label>
<label>Horizontal position <input id="ps-x" type="range" min="-1" max="1" step=".01" value="0"></label>
<label>Vertical position <input id="ps-y" type="range" min="-1" max="1" step=".01" value="0"></label>
<p class="ps-note">Each photo has its own settings. Circle exports as a transparent PNG; other shapes export as JPEG.</p>
</div></div>
<p id="ps-message" class="ps-note" role="status"></p>
<p><a href="https://app.pagescms.org/">Open Pages CMS to upload the prepared images</a></p>
</div>
<script>
(()=>{'use strict';
const $=id=>document.getElementById(id),grid=$('ps-grid'),canvas=$('ps-canvas'),ctx=canvas.getContext('2d'),files=$('ps-files');
let items=[],selected=-1,dragged=-1;
function message(s){$('ps-message').textContent=s}
function current(){return items[selected]}
function dimensions(item){let w=item.image.naturalWidth,h=item.image.naturalHeight;switch(item.shape){case 'square':case 'circle':return [800,800];case 'landscape':return [1000,750];case 'portrait':return [750,1000];default:{const scale=Math.min(1,1400/Math.max(w,h));return [Math.round(w*scale),Math.round(h*scale)]}}}
function draw(item,target){const [w,h]=dimensions(item);target.width=w;target.height=h;const c=target.getContext('2d');c.clearRect(0,0,w,h);c.save();if(item.shape==='circle'){c.beginPath();c.arc(w/2,h/2,w/2,0,Math.PI*2);c.clip()}else{c.fillStyle='#101c16';c.fillRect(0,0,w,h)}
const iw=item.image.naturalWidth,ih=item.image.naturalHeight,base=item.fit==='cover'?Math.max(w/iw,h/ih):Math.min(w/iw,h/ih),scale=base*item.zoom,dw=iw*scale,dh=ih*scale;
const roomX=Math.abs(w-dw)/2,roomY=Math.abs(h-dh)/2;
c.drawImage(item.image,(w-dw)/2+item.x*roomX,(h-dh)/2+item.y*roomY,dw,dh);c.restore()}
function preview(){const item=current();$('ps-editor').hidden=!item;if(!item)return;$('ps-title').textContent=item.name;$('ps-shape').value=item.shape;$('ps-fit').value=item.fit;$('ps-zoom').value=item.zoom;$('ps-x').value=item.x;$('ps-y').value=item.y;draw(item,canvas)}
function move(from,to){if(from<0||to<0||to>=items.length||from===to)return;const [item]=items.splice(from,1);items.splice(to,0,item);selected=items.indexOf(item);render()}
function render(){grid.replaceChildren();items.forEach((item,i)=>{const card=document.createElement('div');card.className='ps-item'+(i===selected?' active':'');card.draggable=true;card.addEventListener('dragstart',()=>{dragged=i});card.addEventListener('dragover',e=>e.preventDefault());card.addEventListener('drop',e=>{e.preventDefault();move(dragged,i)});const img=document.createElement('img');img.src=item.url;img.alt=item.name;img.addEventListener('click',()=>{selected=i;render()});const title=document.createElement('small');title.textContent=(i===0?'Main · ':'')+item.name;const actions=document.createElement('div');actions.className='ps-actions';const select=document.createElement('button');select.textContent='Edit';select.onclick=()=>{selected=i;render()};const left=document.createElement('button');left.textContent='←';left.setAttribute('aria-label','Move photo earlier');left.disabled=i===0;left.onclick=()=>move(i,i-1);const right=document.createElement('button');right.textContent='→';right.setAttribute('aria-label','Move photo later');right.disabled=i===items.length-1;right.onclick=()=>move(i,i+1);const remove=document.createElement('button');remove.textContent='×';remove.setAttribute('aria-label','Remove photo');remove.onclick=()=>{URL.revokeObjectURL(item.url);items.splice(i,1);selected=items.length?Math.min(i,items.length-1):-1;render()};actions.append(select,left,right,remove);card.append(img,title,actions);grid.append(card)});$('ps-count').textContent=items.length+' / 10';$('ps-export').disabled=!items.length;preview()}
files.addEventListener('change',async()=>{const chosen=[...files.files].slice(0,10-items.length);if(files.files.length>chosen.length)message('Only 10 photos can be added. Extra files were skipped.');for(const file of chosen){if(!file.type.startsWith('image/'))continue;const url=URL.createObjectURL(file),img=new Image();try{await new Promise((resolve,reject)=>{img.onload=resolve;img.onerror=reject;img.src=url});items.push({name:file.name,image:img,url,shape:'original',fit:'contain',zoom:1,x:0,y:0})}catch(e){URL.revokeObjectURL(url);message('Could not read '+file.name)}}files.value='';if(selected<0&&items.length)selected=0;render()});
for(const [id,key] of [['ps-shape','shape'],['ps-fit','fit'],['ps-zoom','zoom'],['ps-x','x'],['ps-y','y']])$(id).addEventListener('input',()=>{const item=current();if(!item)return;item[key]=['zoom','x','y'].includes(key)?Number($(id).value):$(id).value;draw(item,canvas)});
$('ps-clear').onclick=()=>{items.forEach(i=>URL.revokeObjectURL(i.url));items=[];selected=-1;message('Workspace cleared.');render()};
$('ps-export').onclick=async()=>{message('Preparing images…');for(let i=0;i<items.length;i++){const item=items[i],out=document.createElement('canvas');draw(item,out);const png=item.shape==='circle',mime=png?'image/png':'image/jpeg';const blob=await new Promise(resolve=>out.toBlob(resolve,mime,.92));if(!blob){message('Could not export '+item.name);return}const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=String(i+1).padStart(2,'0')+'-'+item.name.replace(/\.[^.]+$/,'').replace(/[^a-z0-9_-]+/gi,'-')+(png?'.png':'.jpg');document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),60000);await new Promise(resolve=>setTimeout(resolve,220))}message('Export complete. Upload images in numbered order in Pages CMS. Your originals remain unchanged.')};
render();
})();
</script>
