"""Headless UI smoke checks for the YönetAI static preview. Requires Playwright and Chromium."""
import asyncio,re
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).parent.parent

def preview():
 html=(ROOT/'index.html').read_text(encoding='utf-8')
 html=html.replace('<link rel="stylesheet" href="/style.css">', '<style>'+ (ROOT/'style.css').read_text(encoding='utf-8')+'</style>')
 html=html.replace('<script src="/app.js" defer></script>', '<script>'+ (ROOT/'app.js').read_text(encoding='utf-8')+'</script>')
 return re.sub(r'<link[^>]+href="https://fonts\.(googleapis|gstatic)\.com[^>]+>', '', html)
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-web-security'])
  page=await browser.new_page(viewport={'width':1440,'height':900},device_scale_factor=1)
  page.set_default_timeout(3000)
  errs=[]
  page.on('pageerror',lambda e:errs.append(str(e)))
  await page.route('**/*',lambda route:route.abort())
  await page.set_content(preview(),wait_until='domcontentloaded',timeout=15000)
  await page.wait_for_timeout(320)
  assert await page.locator('h1').first.text_content()=='Yönetim Özeti'
  pages=['overview','units','dues','finance','bank','meters','tickets','visitors','moves','bookings','news','polls','documents','services','settings']
  for i in pages:
   await page.locator(f'.sidebar .nav-link[data-go="{i}"]').click()
   assert await page.locator('h1').count()==1,f'No heading for {i}'
  # primary CTA from overview should open actionable choices, not an info-only modal
  await page.locator('.sidebar [data-go="overview"]').click()
  await page.locator('[data-action="newOperation"]').click()
  assert await page.locator('.quick-modal-btn').count()==6
  await page.keyboard.press('Escape')
  assert await page.locator('.modal').count()==0
  # Bank matching is local and updates matching unit status
  await page.locator('.sidebar [data-go="bank"]').click()
  assert await page.locator('button[data-action="matchBank"]').count()>=1
  await page.locator('button[data-action="matchBank"]').first.click()
  assert await page.get_by_text('Eşleştirildi').count()>=1
  # Search result navigates to right app workflow
  await page.locator('#global-search').fill('asansör')
  await page.locator('#global-search').press('Enter')
  assert await page.locator('.search-results .result-row').count()>=1
  await page.locator('.search-results [data-go="tickets"]').first.click()
  assert await page.locator('h1').text_content()=='Arıza & İş Emirleri'
  # Create booking and prevent duplicate slot
  await page.locator('.sidebar [data-go="bookings"]').click()
  await page.locator('button[data-action="newBooking"]').first.click()
  await page.locator('#form-booking [name="resource"]').select_option('Spor Salonu')
  await page.locator('#form-booking [name="date"]').fill('2026-12-13')
  await page.locator('#form-booking [name="time"]').select_option('12:00')
  await page.locator('button[form="form-booking"]').click()
  count=await page.locator('.record-row').count()
  assert count>=3
  await page.locator('button[data-action="newBooking"]').first.click()
  await page.locator('#form-booking [name="resource"]').select_option('Spor Salonu')
  await page.locator('#form-booking [name="date"]').fill('2026-12-13')
  await page.locator('#form-booking [name="time"]').select_option('12:00')
  await page.locator('button[form="form-booking"]').click()
  assert await page.locator('.record-row').count()==0 or await page.locator('.modal').count()==1
  assert 'zaten var' in (await page.locator('#toast').text_content())
  await page.keyboard.press('Escape')
  # Booking approvals
  await page.locator('button[data-action="approveBooking"]').first.click()
  assert await page.get_by_text('Onaylandı').count()>=1
  # Move notification
  await page.locator('.sidebar [data-go="moves"]').click()
  await page.locator('[data-action="newMove"]').first.click()
  await page.locator('#form-move [name="date"]').fill('2026-12-18')
  await page.locator('button[form="form-move"]').click()
  assert await page.locator('.record-row').count()>=2
  # Document record
  await page.locator('.sidebar [data-go="documents"]').click()
  await page.locator('[data-action="newDocument"]').click()
  await page.locator('#form-document [name="title"]').fill('Bakım özeti')
  await page.locator('#form-document [name="body"]').fill('Talep incelendi ve bakım planlandı.')
  await page.locator('button[form="form-document"]').click()
  assert await page.get_by_text('Bakım özeti').count()>=1
  # Resident polls
  await page.locator('#role-select').select_option('resident')
  await page.locator('.sidebar [data-go="polls"]').click()
  await page.locator('[data-vote]').first.click()
  assert await page.get_by_text('Katıldınız').count()>=1
  assert await page.locator('[data-vote]').count()==0
  # mobile QA including menu navigation, viewport overflow, photo banner
  for width in [320,375,390,430,768,1024,1440]:
   await page.set_viewport_size({'width':width,'height':844})
   await page.wait_for_timeout(275)
   overflow=await page.evaluate('document.documentElement.scrollWidth > window.innerWidth')
   assert not overflow,f'horizontal overflow at width {width}'
  await page.set_viewport_size({'width':390,'height':844})
  await page.wait_for_timeout(350)
  await page.locator('.mobile-nav [data-action="navToggle"]').click()
  await page.wait_for_timeout(260)
  assert await page.locator('.sidebar.open').count()==1
  await page.locator('.sidebar [data-go="bookings"]').click()
  await page.wait_for_timeout(300)
  assert await page.locator('.sidebar.open').count()==0
  assert 'Rezervasyon' in (await page.locator('h1').text_content())
  await page.screenshot(path=str(ROOT/'mobile-reservations.png'),full_page=True)
  await page.locator('.mobile-nav [data-action="navToggle"]').click()
  await page.wait_for_timeout(200)
  await page.locator('.sidebar [data-go="resident"]').click()
  await page.wait_for_timeout(300)
  await page.screenshot(path=str(ROOT/'mobile-resident.png'),full_page=True)
  await page.set_viewport_size({'width':1440,'height':900})
  await page.locator('#role-select').select_option('admin')
  await page.wait_for_timeout(350)
  await page.screenshot(path=str(ROOT/'desktop-dashboard.png'),full_page=True)
  assert not errs,f'JS errors: {errs}'
  print('PASS: 15 admin views, action menu, bank matching, search, booking + duplicate check + approval, move, documents, poll, 7 responsive viewports, mobile sidebar, JS console.')
  await browser.close()
if __name__=='__main__':asyncio.run(main())
