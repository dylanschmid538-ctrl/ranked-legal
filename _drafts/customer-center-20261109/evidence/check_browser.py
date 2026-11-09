from pathlib import Path
import subprocess,json,re,html,shutil
out=Path(__file__).resolve().parent
chrome='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
allmetrics=[]
findings=[]
for i in range(1,11):
    profile=out/'chrome-profile'
    cmd=[chrome,'--headless','--disable-gpu','--no-first-run','--no-default-browser-check','--disable-background-networking','--hide-scrollbars','--user-data-dir='+str(profile),'--window-size=1280,'+('2200' if i==10 else '1400'),'--screenshot='+str(out/f'preview-{i}.png'),'--dump-dom',(out/f'preview-{i}.html').as_uri()]
    p=subprocess.run(cmd,capture_output=True,text=True,timeout=45)
    (out/f'chrome-{i}.log').write_text(p.stderr)
    (out/f'preview-{i}.dom.html').write_text(p.stdout)
    assert p.returncode==0,(i,p.returncode,p.stderr[-1000:])
    raw=re.search(r'<pre id="metrics">(.*?)</pre>',p.stdout,re.S).group(1)
    metrics=json.loads(html.unescape(raw)); metrics['sheet']=i; metrics['exit_code']=p.returncode
    for c in metrics['cards']:

        if not (c['visible'] and c['outerWidth']==320 and c['scrollWidth']==c['width']): findings.append({'sheet':i,'locale':c['locale'],'font':metrics['font'],'issue':'horizontal overflow or invisible text','metrics':c})
        assert c['height']<= (2200 if i==10 else 1400),(i,'screenshot clipped',c)
    allmetrics.append(metrics)
    print(f"sheet {i}: {len(metrics['cards'])} visible sections; {sum(c['scrollWidth']>c['width'] for c in metrics['cards'])} horizontal overflows; screenshot captured; exit {p.returncode}",flush=True)
(out/'browser-check.json').write_text(json.dumps({'sheets':allmetrics,'findings':findings},ensure_ascii=False,indent=2)+'\n')
shutil.rmtree(profile)
print('35 standard sections at 320px; 4 large-text sections at 320px. Findings:',len(findings),'; preview only, not Jekyll.')
raise SystemExit(bool(findings))
