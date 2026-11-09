#!/usr/bin/env python3
"""Read-only policy tests; outputs stay alongside this script. No dependencies."""
from pathlib import Path
import subprocess, re, json, hashlib, html, sys
BASE=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
DRAFT=OUT.parent
BASELINE_COMMIT="cf351655899bf53b64d256f4e4e6952a8050a327"
errors=[]
def ck(ok,message):
    if not ok: errors.append(message)
def head(path): return subprocess.check_output(['git','show',BASELINE_COMMIT+':'+path],cwd=BASE).decode()
def urls(text): return re.findall(r'https?://[^\s<>\])]+',text)
files=sorted(BASE.glob('privacy*.md'))
ck(len(files)==34,'expected 34 privacy pages')
translations=sorted((DRAFT/'translations').glob('*.md'))
ck(len(translations)==33,'expected 33 translation deltas')
routes={}
previews=[]
results=[]
for p in files:
    locale='en' if p.name=='privacy.md' else p.stem.removeprefix('privacy-')
    delta=(DRAFT/('source.md' if locale=='en' else 'translations/'+locale+'.md')).read_text().strip()
    current=p.read_text(); original=head(p.name)
    ck(bool(delta) and '\n\n' not in delta and '\n' not in delta,f'{p.name}: delta is not one paragraph')
    ck(current.count(delta)==1,f'{p.name}: exact source delta does not occur once')
    ck(current.count('2026-11-09')==1 and '2026-11-05' not in current,f'{p.name}: date stamp invalid')
    ck(original.count('2026-11-05')==1,f'{p.name}: original date assumption invalid')
    reconstructed=current.replace(delta+'\n\n','',1).replace('2026-11-09','2026-11-05')
    ck(reconstructed==original,f'{p.name}: baseline not preserved byte-for-byte')
    ck(re.search(re.escape(delta)+r'\n\n### 3\.3\b',current) is not None,f'{p.name}: delta not before 3.3')
    fm=current.split('---',2)[1]; original_fm=original.split('---',2)[1]
    ck(fm==original_fm,f'{p.name}: frontmatter changed')
    route=re.search(r'^permalink: (.+)$',fm,re.M).group(1)
    ck(route==('/privacy/' if locale=='en' else '/privacy/'+locale+'/'),f'{p.name}: unexpected route')
    ck(route not in routes,f'{p.name}: duplicate route'); routes[route]=locale
    ck(urls(current)==urls(original),f'{p.name}: URLs changed')
    ck(current.count('<div dir="rtl" markdown="1">')==original.count('<div dir="rtl" markdown="1">'),f'{p.name}: RTL opening changed')
    if locale in ('ar','he'): ck('<div dir="rtl" markdown="1">' in current and current.count('</div>')==original.count('</div>'),f'{p.name}: RTL wrapper invalid')
    ck(not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f\ufffd]',delta),f'{p.name}: control/replacement character')
    ck(all(x in delta for x in ['RevenueCat','PostHog','Ranked']),f'{p.name}: processor/product marker missing')
    ck(not re.search(r'\b(?:TODO|TBD|PLACEHOLDER)\b|```|\{\{|\}\}',delta),f'{p.name}: malformed draft marker')
    ck(not any(x in delta for x in ['<','>','[',']','*','`']),f'{p.name}: unexpected markdown delimiters in plain paragraph')
    ck(delta.count('§3.3')==1,f'{p.name}: section reference missing/repeated')
    previews.append({'locale':locale,'dir':'rtl' if locale in ('ar','he') else 'ltr','markdown':delta+'\n\n'+re.search(r'^### 3\.3.*$',current,re.M).group(0)})
    results.append({'file':p.name,'locale':locale,'route':route,'baseline_reconstructed':reconstructed==original,'paragraph_characters':len(delta),'frontmatter_preserved':fm==original_fm,'sha256':hashlib.sha256(current.encode()).hexdigest()})
# Verify all selector destinations exist and no translations are unreachable.
selector=re.findall(r'\]\(([^)]+/)\)',(BASE/'privacy.md').read_text().split('\n')[5])
ck(len(selector)==33 and set('/privacy/'+x for x in selector)==set(routes)-{'/privacy/'},'English selector must resolve to all 33 translations')
# The supported locale inventory is a dated ASC evidence file, not a new ASC fetch.
mapfile=Path('/Users/dylan/ranked-analytics-consent/docs/analytics/ab006-paywall-2026-10-11/preparation-2026-10-15/locale-map.json')
mapping=json.loads(mapfile.read_text())
regional=[]
for store,app in mapping['mapping'].items():
    code=app.replace('_','-'); lang=code.split('-')[0]; legal='no' if lang=='nb' else lang
    if lang=='zh': legal='zh-Hant' if 'Hant' in code or code.endswith(('-TW','-HK')) else 'zh-Hans'
    route='/privacy/' if legal=='en' else '/privacy/'+legal+'/'
    ck(route in routes,f'{store}->{app}: route missing {route}')
    regional.append({'store':store,'app':app,'route':route})
ck(len(regional)==37,'expected 37 dated supported regional entries')
# Support may only replace cancellation and refund content; all other bytes stay intact.
support=(BASE/'support.md').read_text(); oldsupport=head('support.md')
pattern=r'(?<=### How do I cancel?\n)' # explicit indexes avoid regex ? ambiguity
start=support.index('### How do I cancel?'); end=support.index('### Delete my training data')
oldstart=oldsupport.index('### How do I cancel?'); oldend=oldsupport.index('### Delete my training data')
ck(support[:start]==oldsupport[:oldstart] and support[end:]==oldsupport[oldend:],'support changed outside cancellation/refunds')
settings=Path('/Users/dylan/ranked-analytics-consent/Sources/Features/Profile/SettingsView.swift').read_text()
ck('Label("Manage Subscription", systemImage: "apple.logo")' in settings,'app fallback label changed')
ck('**Manage Subscription** link with the Apple logo' in support,'support fallback label does not match current UI')
ck('reportaproblem.apple.com' in support and 'does not mean it has been approved' in support,'support refund boundaries missing')
ck(urls(support)==urls(oldsupport),'support URL inventory changed')
previews.append({'locale':'support','dir':'ltr','markdown':support[start:end]})
# Render only changed paragraphs + next heading / changed support sections with bundled RDoc.
(OUT/'preview-input.json').write_text(json.dumps(previews,ensure_ascii=False,indent=2))
report={'baseline_commit':BASELINE_COMMIT,'checks':{'privacy_pages':len(files),'translation_deltas':len(translations),'source_deltas':1,'selector_destinations':len(selector),'regional_entries_from_2026_10_15_evidence':len(regional),'rtl_pages':2,'support_pages':1},'pages':results,'regional_mapping':regional,'errors':errors,'not_verified':['Real Jekyll/GitHub Pages rendering: Jekyll/kramdown/theme unavailable locally.','Current ASC inventory not re-fetched; regional coverage grounded in dated 2026-10-15 evidence.','Translation legal/linguistic accuracy and app/provider runtime behavior outside this text/layout delta test.']}
(OUT/'delta-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('BASELINE:',BASELINE_COMMIT)
print(json.dumps(report['checks']))
print('ERRORS:',len(errors))
for e in errors: print(e)
sys.exit(bool(errors))
