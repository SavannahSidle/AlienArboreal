---
layout: page
title: Family Tree
eyebrow: Visual lineage
description: Parent and offspring relationships across Alien Arboreal.
permalink: /family-tree/
---
<p>Follow parentage through generations. Every relationship is generated from the animal profiles’ <code>parents</code> field.</p>
<style>
.genealogy{display:grid;gap:2rem;margin-top:1.5rem}
.family-branch{min-width:0}
.family-unit{padding:1rem;background:var(--panel);border:1px solid var(--line);border-radius:6px;overflow-x:auto}
.family-parents{display:flex;justify-content:center;align-items:flex-start;gap:.75rem;min-width:max-content}
.tree-animal{display:block;width:144px;padding:.55rem;text-align:center;border:1px solid var(--line);border-radius:5px;background:rgba(0,0,0,.12);color:var(--ink);text-decoration:none}
.tree-animal:hover{border-color:var(--moss);color:var(--acid)}
.tree-photo{width:100%;height:88px;margin-bottom:.45rem;display:grid;place-items:center;overflow:hidden;border:1px dashed var(--line);border-radius:3px;background:rgba(255,255,255,.025);color:var(--muted);font:400 .62rem "Space Mono",monospace;text-transform:uppercase;letter-spacing:.04em}
.tree-photo img{display:block;width:100%;height:100%;object-fit:cover}
.tree-name{display:block;font-weight:700}
.tree-meta{display:block;margin-top:.18rem;color:var(--muted);font:400 .62rem "Space Mono",monospace}
.pair-mark{align-self:center;color:var(--acid);font:700 1.25rem "Space Mono",monospace}
.family-stem{width:2px;height:22px;margin:0 auto;background:var(--moss)}
.family-branch{width:min(72%,420px);height:14px;margin:0 auto;border-top:2px solid var(--moss);border-left:2px solid var(--moss);border-right:2px solid var(--moss);border-radius:7px 7px 0 0}
.tree-generation{display:flex;justify-content:center;align-items:flex-start;gap:1.2rem;margin:0;padding:0;list-style:none}
.tree-generation>li{position:relative;display:flex;flex-direction:column;align-items:center;min-width:150px;padding:0 .15rem}
.tree-generation>li:before{position:absolute;top:-14px;left:50%;height:14px;border-left:2px solid var(--moss);content:""}
.descendant-groups{display:grid;gap:1rem;width:max-content;max-width:min(100%,560px);margin:1rem 0 0;padding:1rem 0 0;border-top:1px solid var(--line)}
.descendant-groups .family-unit{padding:.7rem}
.unlinked-note{color:var(--muted);font:400 .68rem "Space Mono",monospace}
@media(max-width:700px){.family-unit{padding:.7rem}.family-parents{gap:.4rem}.tree-animal{width:125px}.tree-photo{height:76px}.tree-generation{gap:.55rem}.tree-generation>li{min-width:130px}.descendant-groups{max-width:calc(100vw - 4rem)}}
</style>

{% assign geckos = site.geckos | sort: "name" %}
<script type="application/json" id="family-tree-data">[
{% for gecko in geckos %}
  {% assign tree_photo = gecko.image %}
  {% if tree_photo == nil and gecko.photos and gecko.photos.size > 0 %}{% assign tree_photo = gecko.photos[0] %}{% endif %}
  {"name":{{ gecko.name | jsonify }},"url":{{ gecko.url | relative_url | jsonify }},"parents":{{ gecko.parents | default: "" | jsonify }},"sex":{{ gecko.sex | default: "" | jsonify }},"status":{{ gecko.status | default: "" | jsonify }},"hatch_date":{{ gecko.hatch_date | default: "" | jsonify }},"morph":{{ gecko.morph | default: "" | jsonify }},"photo":{% if tree_photo %}{{ tree_photo | relative_url | jsonify }}{% else %}null{% endif %}}{% unless forloop.last %},{% endunless %}
{% endfor %}
]</script>
<div id="genealogy-tree" class="genealogy" aria-live="polite"></div>
<noscript><p>Enable JavaScript to view the connected family tree.</p></noscript>
<script>
(function(){
  const source=document.getElementById('family-tree-data');
  const host=document.getElementById('genealogy-tree');
  if(!source||!host)return;
  const animals=JSON.parse(source.textContent);
  const normalize=s=>(s||'').trim().replace(/\s+/g,' ').toLocaleLowerCase();
  const byName=new Map(animals.map(a=>[normalize(a.name),a]));
  const groups=new Map();
  animals.filter(a=>a.parents).forEach(child=>{
    const names=child.parents.split(/\s*[×]\s*|\s+[xX]\s+|\s*,\s*/).map(s=>s.trim()).filter(Boolean);
    if(!names.length)return;
    const key=names.map(normalize).sort().join('||');
    if(!groups.has(key))groups.set(key,{key,names,children:[]});
    groups.get(key).children.push(child);
  });
  const allGroups=[...groups.values()];
  const childrenSet=new Set(allGroups.flatMap(g=>g.children.map(c=>normalize(c.name))));
  const descendants=new Map();
  allGroups.forEach(g=>g.names.forEach(name=>{
    const key=normalize(name);
    if(!descendants.has(key))descendants.set(key,[]);
    descendants.get(key).push(g);
  }));
  let roots=allGroups.filter(g=>!g.names.some(n=>childrenSet.has(normalize(n))));
  if(!roots.length)roots=allGroups;
  const makeAnimal=(animal,name)=>{
    const el=animal&&animal.url?document.createElement('a'):document.createElement('div');
    el.className='tree-animal'+(!animal?' unlinked-note':'');
    if(animal&&animal.url)el.href=animal.url;
    const photo=document.createElement('div');photo.className='tree-photo';
    if(animal&&animal.photo){const img=document.createElement('img');img.src=animal.photo;img.alt='';img.loading='lazy';photo.appendChild(img)}
    else photo.textContent='Photo placeholder';
    el.appendChild(photo);
    const title=document.createElement('span');title.className='tree-name';title.textContent=animal?animal.name:name;el.appendChild(title);
    if(animal){[animal.sex,animal.hatch_date,animal.morph,animal.status==='placed'?'Placed':null].filter(Boolean).forEach(value=>{const meta=document.createElement('small');meta.className='tree-meta';meta.textContent=value;el.appendChild(meta)})}
    return el;
  };
  const renderGroup=(group,path)=>{
    const branch=document.createElement('div');branch.className='family-branch';
    const unit=document.createElement('section');unit.className='family-unit';unit.setAttribute('aria-label','Family pairing');
    const parents=document.createElement('div');parents.className='family-parents';
    group.names.forEach((name,index)=>{if(index){const mark=document.createElement('span');mark.className='pair-mark';mark.textContent='×';parents.appendChild(mark)}parents.appendChild(makeAnimal(byName.get(normalize(name)),name))});
    unit.appendChild(parents);
    const stem=document.createElement('div');stem.className='family-stem';unit.appendChild(stem);
    const rail=document.createElement('div');rail.className='family-branch';unit.appendChild(rail);
    const generation=document.createElement('ul');generation.className='tree-generation';
    group.children.forEach(child=>{
      const li=document.createElement('li');li.appendChild(makeAnimal(child,child.name));
      const next=(descendants.get(normalize(child.name))||[]).filter(g=>!path.has(g.key));
      if(next.length){const nested=document.createElement('div');nested.className='descendant-groups';next.forEach(g=>{const newPath=new Set(path);newPath.add(g.key);nested.appendChild(renderGroup(g,newPath))});li.appendChild(nested)}
      generation.appendChild(li);
    });
    unit.appendChild(generation);branch.appendChild(unit);return branch;
  };
  roots.forEach(g=>host.appendChild(renderGroup(g,new Set([g.key]))));
})();
</script>
