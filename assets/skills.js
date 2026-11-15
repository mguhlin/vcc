'use strict';
// The HTML includes every skill so reading and downloads also work without JavaScript.
const skillsRoot=document.querySelector('[data-skills]');
if(skillsRoot){
 const panels=[...skillsRoot.querySelectorAll('[data-skill-panel]')];
 const links=[...skillsRoot.querySelectorAll('[data-skill-link]')];
 const search=skillsRoot.querySelector('#skill-search');
 function panelForHash(){
  let id;try{id=decodeURIComponent(location.hash.slice(1));}catch{return null;}
  const target=document.getElementById(id);
  return target?.closest('[data-skill-panel]')||null;
 }
 function showSkill(panel,focus=false){
  for(const item of panels)item.hidden=item!==panel;
  for(const link of links){
   if(link.dataset.skillLink===panel.id)link.setAttribute('aria-current','true');
   else link.removeAttribute('aria-current');
  }
  const nav=skillsRoot.querySelector('.skills-sidebar nav');
  const list=nav.scrollHeight>nav.clientHeight?nav:skillsRoot.querySelector('.skills-sidebar-inner');
  const active=links.find(link=>link.dataset.skillLink===panel.id);
  if(list.scrollHeight>list.clientHeight)list.scrollTop+=active.getBoundingClientRect().top-list.getBoundingClientRect().top-(list.clientHeight-active.offsetHeight)/2;
  // Clear stale copy messages when changing the displayed skill.
  for(const status of skillsRoot.querySelectorAll('.skill-status'))status.textContent='';
  if(focus)panel.querySelector('.skill-title').focus({preventScroll:true});
 }
 skillsRoot.classList.add('skills-enhanced');
 showSkill(panelForHash()||panels[0]);
 skillsRoot.querySelector('.skill-filter').hidden=false;
 for(const link of links)link.addEventListener('click',event=>{
  if(event.button!==0||event.ctrlKey||event.metaKey||event.shiftKey||event.altKey)return;
  event.preventDefault();
  const panel=document.getElementById(link.dataset.skillLink);
  showSkill(panel,true);
  if(location.hash!==link.hash)location.hash=link.hash;
  else panel.scrollIntoView({block:'start'});
 });
 addEventListener('hashchange',()=>showSkill(panelForHash()||panels[0],true));
 function filterSkills(){
  const query=search.value.trim().toLocaleLowerCase();let count=0;
  for(const link of links){
   const show=!query||link.textContent.toLocaleLowerCase().includes(query);
   link.closest('li').hidden=!show;
   if(show)count++;
  }
  skillsRoot.querySelector('#skill-count').textContent=`${count} of ${links.length} skills`;
  skillsRoot.querySelector('.skill-empty').hidden=count!==0;
  for(const heading of skillsRoot.querySelectorAll('[data-skill-group-heading]')){
   heading.hidden=!links.some(link=>{
    const entry=link.closest('li');
    return entry.dataset.skillGroup===heading.dataset.skillGroupHeading&&!entry.hidden;
   });
  }
 }
 search.addEventListener('input',filterSkills);
 skillsRoot.querySelector('.skill-clear').addEventListener('click',()=>{search.value='';filterSkills();search.focus();});
 for(const button of skillsRoot.querySelectorAll('[data-skill-copy]'))button.addEventListener('click',async()=>{
  const target=document.getElementById(button.dataset.skillCopy);
  const status=button.parentElement.querySelector('[role=status]');
  try{
   await navigator.clipboard.writeText(target.value);
   status.textContent=`${button.dataset.copyLabel} copied`;
  }catch{
   target.focus();target.select();
   status.textContent='Text selected. Use your device’s copy command.';
  }
 });
}
