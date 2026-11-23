'use strict';
const assert=require('node:assert/strict');
module.exports=async function({page,context,base}){
 const response=await context.request.get(base+'agent-skills.json');assert.equal(response.status(),200);
 const catalog=await (await context.request.get(base+'skills/catalog.json')).json();
 const manifest=await response.json();assert.equal(manifest.skills.length,catalog.length+4);assert.equal(new Set(manifest.skills.map(s=>s.name)).size,catalog.length+4);
 const index=await context.request.get(base+'llms.txt');assert.equal(index.status(),200);const indexText=await index.text();
 for(const skill of manifest.skills){
  const relativeGuide=new URL(skill.guide_url).pathname.replace('/vcc/','')+new URL(skill.guide_url).hash;
  await page.goto(base+relativeGuide);
  const block=page.locator('.agent-instructions:visible');assert.equal(await block.count(),1);
  const details=block.locator('details');await details.locator('summary').focus();await page.keyboard.press('Enter');assert.ok(await details.evaluate(el=>el.open));
  for(const [label,statusText,suffix] of [['Copy skill setup prompt','Setup prompt copied','setup'],['Copy skill use prompt','Use prompt copied','use']]){
   const button=block.getByRole('button',{name:label,exact:true});await button.focus();await page.keyboard.press('Enter');
   await page.waitForFunction(text=>[...document.querySelectorAll('.agent-copy [role=status]')].some(el=>el.textContent===text),statusText);
   const expected=(await block.locator('#agent-'+skill.name+'-'+suffix).textContent()).trim();assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),expected);assert.ok(expected.includes(skill.skill_url));
  }
  const payload=await context.request.get(base+new URL(skill.skill_url).pathname.replace('/vcc/',''));assert.equal(payload.status(),200);
  const text=await payload.text();assert.ok(text.startsWith('---\nname: '+skill.name+'\n'));assert.ok(text.includes('## VCC source and reuse'));assert.ok(indexText.includes(skill.skill_url));
  for(const file of skill.support_files||[]){
   const path=new URL(file,skill.skill_url).pathname.replace('/vcc/','');const support=await context.request.get(base+path);assert.equal(support.status(),200,skill.name+' agent reference '+file);
   const source=await context.request.get(base+'skills/'+skill.name+'/'+file);assert.equal(await support.text(),await source.text(),'agent reference content stays complete');
   assert.ok((await block.locator('#agent-'+skill.name+'-setup').textContent()).includes(file),'setup prompt preserves supporting paths');
  }
  await page.setViewportSize({width:320,height:844});assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),skill.name+' open agent prompts reflow');await page.setViewportSize({width:1440,height:1000});
 }
 await page.goto(base+'guides/rescue.html#ai-agent-instructions');const block=page.locator('.agent-instructions');await block.locator('summary').click();
 await page.evaluate(()=>Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async()=>{throw Error('Denied')}}}));
 await block.getByRole('button',{name:'Copy skill setup prompt',exact:true}).click();assert.equal(await block.locator('.agent-copy [role=status]').first().textContent(),'Text selected. Use your device’s copy command.');assert.ok((await page.evaluate(()=>window.getSelection().toString())).includes('vibe-code-rescue'));
 await page.goto(base);await page.locator('.supplement-nav summary').click();await page.locator('.supplement-links').getByRole('link',{name:'Give VCC to your AI agent',exact:true}).click();await page.locator('#ai-agent-instructions summary').click();await page.getByRole('button',{name:'Copy VCC agent prompt',exact:true}).click();await page.waitForFunction(()=>document.querySelector('#ai-agent-instructions [role=status]').textContent==='VCC agent prompt copied');assert.ok((await page.evaluate(()=>navigator.clipboard.readText())).includes('agent-skills.json'));
 const bundle=await context.request.get(base+'downloads/vcc-agent-skills.zip');assert.equal(bundle.status(),200);assert.ok((await bundle.body()).length>10000);
 const nojs=await context.browser().newContext({javaScriptEnabled:false});const plain=await nojs.newPage();await plain.goto(base+'guides/skills.html');assert.equal(await plain.locator('.agent-instructions').count(),catalog.length);await plain.goto(base+'guides/rescue.html');await plain.locator('.agent-instructions summary').click();assert.ok(await plain.getByRole('link',{name:'Download agent-ready SKILL.md',exact:true}).isVisible());await nojs.close();
 console.log(`PASS: ${manifest.skills.length} agent exports and page directions, keyboard disclosures, ${manifest.skills.length*2} exact clipboard prompts, fallback selection, plain-text discovery, homepage entry, open-prompt mobile reflow, no-JS directions, all-skills ZIP`);
};
