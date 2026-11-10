'use strict';
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
 try{await navigator.clipboard.writeText(target.textContent.trim());status.textContent='Prompt copied';}catch{status.textContent='Select and copy the prompt text above';}
});
const checks=[...document.querySelectorAll('.checklist input')];
function updateChecks(){const n=checks.filter(x=>x.checked).length;const el=document.querySelector('#check-summary');if(el)el.textContent=`${n} of ${checks.length} reminders marked. Use the full guides to gather release evidence.`;}
checks.forEach(x=>x.addEventListener('change',updateChecks));
document.querySelector('#reset-checks')?.addEventListener('click',()=>{checks.forEach(x=>x.checked=false);updateChecks()});
// Keep the scheduled companion discoverable without publishing a broken article link.
const article=document.querySelector('[data-publication]');
if(article&&Date.now()>=Date.parse(article.dataset.publication)){const a=document.createElement('a');a.href=article.dataset.href;a.textContent='Read the design article';article.replaceChildren(a);}
