'use strict';
// Preserve links to sections that now have their own supplemental pages.
const movedSections={'#tools':'guides/helpful-githubs.html','#ai-agent-instructions':'guides/ai-agent.html#ai-agent-instructions','#what':'guides/about.html','#start':'guides/start.html','#before-sharing':'guides/before-sharing.html'};
if(document.querySelector('.hero')&&movedSections[location.hash])location.replace(movedSections[location.hash]);
const search=document.querySelector('#resource-search');
const category=document.querySelector('#resource-category');
const entries=[...document.querySelectorAll('[data-resource]')];
function filterResources(){
 if(!search||!category)return;
 const query=search.value.trim().toLocaleLowerCase();
 let count=0;
 for(const entry of entries){const show=(!query||entry.textContent.toLocaleLowerCase().includes(query))&&(category.value==='all'||entry.dataset.category===category.value);entry.hidden=!show;if(show)count++;}
 document.querySelector('#result-count').textContent=`${count} of ${entries.length} resources`;
 document.querySelector('#no-results').hidden=count!==0;
}
search?.addEventListener('input',filterResources);category?.addEventListener('change',filterResources);
document.querySelector('#clear-search')?.addEventListener('click',()=>{search.value='';category.value='all';filterResources();search.focus()});
for(const btn of document.querySelectorAll('[data-copy]'))btn.addEventListener('click',async()=>{
 const target=document.getElementById(btn.dataset.copy);const status=btn.parentElement.querySelector('[role=status]');
 try{await navigator.clipboard.writeText(target.textContent.trim());status.textContent=`${btn.dataset.copyLabel||'Prompt'} copied`;}catch{const range=document.createRange();range.selectNodeContents(target);const selection=window.getSelection();selection.removeAllRanges();selection.addRange(range);status.textContent='Text selected. Use your device’s copy command.';}
});
const checks=[...document.querySelectorAll('.checklist input')];
function updateChecks(){const n=checks.filter(x=>x.checked).length;const el=document.querySelector('#check-summary');if(el)el.textContent=`${n} of ${checks.length} reminders marked. Use the full guides to gather release evidence.`;}
checks.forEach(x=>x.addEventListener('change',updateChecks));
document.querySelector('#reset-checks')?.addEventListener('click',()=>{checks.forEach(x=>x.checked=false);updateChecks()});
const supplemental=document.querySelector('.supplement-nav');
document.addEventListener('keydown',event=>{
 if(event.key==='Escape'&&supplemental?.open){supplemental.open=false;supplemental.querySelector('summary').focus();}
});
document.addEventListener('click',event=>{
 if(supplemental?.open&&(!supplemental.contains(event.target)||event.target.closest('a')))supplemental.open=false;
});
