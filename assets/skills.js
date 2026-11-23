'use strict';
// The HTML includes every skill so reading and downloads also work without JavaScript.
const skillsRoot=document.querySelector('[data-skills]');
if(skillsRoot){
 const panels=[...skillsRoot.querySelectorAll('[data-skill-panel]')];
 const links=[...skillsRoot.querySelectorAll('[data-skill-link]')];
 const search=skillsRoot.querySelector('#skill-search');
 const browser=skillsRoot.querySelector('#skill-browser');
 const nav=browser.querySelector('nav');
 const narrow=matchMedia('(max-width: 800px)');
 const browseLinks=skillsRoot.querySelectorAll('.skill-browse-return');

 function syncBrowserLayout(){
  browser.open=!narrow.matches;
  nav.tabIndex=narrow.matches?-1:0;
  for(const link of browseLinks)link.hidden=!narrow.matches;
 }
 narrow.addEventListener('change',syncBrowserLayout);
 syncBrowserLayout();

 for(const link of browseLinks)link.addEventListener('click',event=>{
  if(event.button!==0||event.ctrlKey||event.metaKey||event.shiftKey||event.altKey)return;
  event.preventDefault();
  browser.open=true;
  search.focus();
 });

 function revealCurrentSkill(){
  const active=nav.querySelector('[aria-current]');
  if(!active||active.closest('li').hidden||!browser.open||narrow.matches)return;
  const row=active.getBoundingClientRect();
  const list=nav.getBoundingClientRect();
  if(row.top<list.top+4)nav.scrollTop+=row.top-list.top-4;
  else if(row.bottom>list.bottom-4)nav.scrollTop+=row.bottom-list.bottom+4;
 }
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
  revealCurrentSkill();
  // Clear stale copy messages when changing the displayed skill.
  for(const status of skillsRoot.querySelectorAll('.skill-status'))status.textContent='';
  if(focus)panel.querySelector('.skill-title').focus({preventScroll:true});
 }
 skillsRoot.classList.add('skills-enhanced');
 skillsRoot.querySelector('.skill-filter').hidden=false;
 showSkill(panelForHash()||panels[0]);
 for(const link of links)link.addEventListener('click',event=>{
  if(event.button!==0||event.ctrlKey||event.metaKey||event.shiftKey||event.altKey)return;
  event.preventDefault();
  const panel=document.getElementById(link.dataset.skillLink);
  if(narrow.matches)browser.open=false;
  showSkill(panel,true);
  if(location.hash!==link.hash)history.pushState(null,'',link.hash);
  const top=panel.getBoundingClientRect().top;
  if(narrow.matches||top<0||top>innerHeight/2)panel.scrollIntoView({block:'start'});
 });
 addEventListener('hashchange',()=>showSkill(panelForHash()||panels[0],true));
 function filterSkills(){
  const query=search.value.trim().toLocaleLowerCase();let count=0;
  for(const link of links){
   const show=!query||(link.dataset.skillSearch||link.textContent).toLocaleLowerCase().includes(query);
   link.closest('li').hidden=!show;
   if(show)count++;
  }
  skillsRoot.querySelector('#skill-count').textContent=`${count} of ${links.length} skills`;
  skillsRoot.querySelector('.skill-empty').hidden=count!==0;
  nav.scrollTop=0;
  revealCurrentSkill();
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
