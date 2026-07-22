import argparse,json,re,shlex
from pathlib import Path
SECRET=re.compile(r'(?i)(api[_-]?key|token|secret|password|authorization:|sk-[A-Za-z0-9_-]{8,})')
DANGER=re.compile(r'(?i)\b(rm\s+-rf|del\s+/|format\b|curl\b.*\|\s*(bash|sh)|wget\b.*\|\s*(bash|sh)|gh auth token|cat .*\.env|printenv|env\b)')
def analyze(text):
    out=[]
    for i,line in enumerate(text.splitlines(),1):
        s=line.strip()
        if not s or s.startswith('#'): continue
        sev=None; typ=None; detail=None
        if SECRET.search(s): sev='high'; typ='secret-looking-text'; detail=SECRET.search(s).group(0)
        if DANGER.search(s): sev='high'; typ='dangerous-demo-command'; detail=DANGER.search(s).group(0)
        if len(s)>100: out.append({'line':i,'severity':'low','type':'long-command-hard-to-read-in-gif','detail':str(len(s)),'command':s[:180]})
        if sev: out.append({'line':i,'severity':sev,'type':typ,'detail':detail,'command':s[:180]})
    return out
def storyboard(text):
    safe=[]
    for line in text.splitlines():
        s=line.strip()
        if s and not s.startswith('#'): safe.append({'command':s,'caption':'Run: '+shlex.split(s)[0] if shlex.split(s) else 'Run command'})
    return safe[:20]
def main(argv=None):
    ap=argparse.ArgumentParser(description='Preview terminal demo scripts before recording GIFs, flagging secrets and destructive commands.')
    ap.add_argument('script'); ap.add_argument('--json',action='store_true')
    args=ap.parse_args(argv); text=Path(args.script).read_text(encoding='utf-8')
    findings=analyze(text); report={'findings':findings,'storyboard':storyboard(text),'safe_to_record':not any(f['severity']=='high' for f in findings)}
    print(json.dumps(report,indent=2,ensure_ascii=False) if args.json else f"safe_to_record={report['safe_to_record']} findings={len(findings)} storyboard_steps={len(report['storyboard'])}")
    return 2 if not report['safe_to_record'] else 0
if __name__=='__main__': raise SystemExit(main())
