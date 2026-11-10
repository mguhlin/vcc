const { chromium }=require(process.env.VCC_PLAYWRIGHT||'@playwright/test');
const assert=require('node:assert/strict');
(async()=>{
const browser=await chromium.launch({headless:true,executablePath:process.env.VCC_CHROME||undefined,args:['--no-sandbox']});
const context=await browser.newContext({viewport:{width:1440,height:1000},permissions:['clipboard-read','clipboard-write']});
const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
const base=process.env.VCC_URL||'http://127.0.0.1:4186/';
await page.goto(base,{waitUntil:'networkidle'});
if(process.env.VCC_SCREENSHOTS==='1')await page.screenshot({path:'/tmp/vcc-desktop.png',fullPage:true});
assert.equal(await page.locator('.foundation-art img').count(),3);
for(const route of ['design','security','education']){await page.locator('.foundation-art[href="guides/'+route+'.html"]').click();assert.ok(page.url().endsWith('/guides/'+route+'.html'));assert.ok(await page.locator('.guide-explainer').isVisible());await page.goto(base);}
assert.equal(await page.locator('[data-resource]:visible').count(),6);
await page.locator('#resource-search').fill('privacy');assert.ok(await page.locator('[data-resource]:visible').count()>0);
await page.locator('#resource-search').fill('zzzznomatch');assert.ok(await page.locator('#no-results').isVisible());
await page.locator('#clear-search').click();await page.locator('#resource-category').selectOption('security');assert.equal(await page.locator('[data-resource]:visible').count(),1);
await page.locator('#clear-search').click();assert.equal(await page.locator('[data-resource]:visible').count(),6);
await page.locator('[data-copy]').click();await page.waitForFunction(()=>document.querySelector('.copy-status').textContent.length>0);assert.equal(await page.locator('.copy-status').textContent(),'Prompt copied');
assert.ok((await page.evaluate(()=>navigator.clipboard.readText())).includes('PROJECT_BRIEF.md'));
await page.locator('.checklist input').first().check();assert.ok((await page.locator('#check-summary').textContent()).startsWith('1 of 6'));
await page.locator('#reset-checks').click();assert.equal(await page.locator('.checklist input:checked').count(),0);
await page.reload();assert.equal(await page.locator('.checklist input:checked').count(),0);
await page.keyboard.press('Tab');assert.equal(await page.locator(':focus').textContent(),'Skip to content');await page.keyboard.press('Enter');assert.equal(await page.evaluate(()=>location.hash),'#main');
await page.evaluate(require('node:fs').readFileSync(process.env.VCC_AXE||require.resolve('axe-core/axe.min.js'),'utf8')); 
let axe=await page.evaluate(()=>axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa','wcag22aa']}}));
console.log('Home axe violations',JSON.stringify(axe.violations.map(x=>({id:x.id,impact:x.impact,nodes:x.nodes.map(n=>n.target)}))));assert.equal(axe.violations.length,0);
for(const route of ['design','security','education','project-brief','launch','prompts','resource-vetting']){
 const response=await page.goto(base+'guides/'+route+'.html');assert.equal(response.status(),200);assert.equal(await page.locator('h1').count(),1);
 await page.evaluate(require('node:fs').readFileSync(process.env.VCC_AXE||require.resolve('axe-core/axe.min.js'),'utf8')); 
 axe=await page.evaluate(()=>axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa','wcag22aa']}}));
 console.log(route+' axe violations',JSON.stringify(axe.violations.map(x=>({id:x.id,nodes:x.nodes.map(n=>n.target)}))));assert.equal(axe.violations.length,0);
}
await page.setViewportSize({width:390,height:844});await page.goto(base);if(process.env.VCC_SCREENSHOTS==='1')await page.screenshot({path:'/tmp/vcc-mobile.png',fullPage:true});
assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
await page.locator('#resource-category').selectOption('design');assert.equal(await page.locator('[data-resource]:visible').count(),1);
for(const route of ['', 'guides/security.html','guides/education.html','guides/resource-vetting.html']){
 await page.goto(base+route);await page.setViewportSize({width:320,height:800});await page.waitForFunction(()=>innerWidth===320);await page.evaluate(()=>new Promise(requestAnimationFrame));assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),route+' reflow');
}
await page.setViewportSize({width:1280,height:900});await page.goto(base);await page.evaluate(()=>document.body.style.fontSize='34px');assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
await page.emulateMedia({reducedMotion:'reduce'});assert.equal(await page.evaluate(()=>matchMedia('(prefers-reduced-motion: reduce)').matches),true);
const download=await context.request.get(base+'downloads/vcc-complete.zip');assert.equal(download.status(),200);assert.ok((await download.body()).length>1000000);
assert.deepEqual(errors,[]);console.log('PASS: search, filters, empty/reset, copy, reminders, keyboard skip, 8-page axe scan, mobile, 320px reflow, text resizing, reduced-motion context, ZIP, no runtime errors');
await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
