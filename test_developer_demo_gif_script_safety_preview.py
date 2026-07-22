import subprocess, sys, tempfile, pathlib, json
p=pathlib.Path(tempfile.mkdtemp())/'demo.sh'
p.write_text('export API_KEY=abc\ncat .env\npython app.py --demo\n',encoding='utf-8')
r=subprocess.run([sys.executable,'developer_demo_gif_script_safety_preview.py','--json',str(p)],text=True,capture_output=True)
assert r.returncode==2
j=json.loads(r.stdout); assert not j['safe_to_record'] and len(j['storyboard'])==3
redacted=subprocess.run([sys.executable,'developer_demo_gif_script_safety_preview.py','--json','--redacted-storyboard',str(p)],text=True,capture_output=True)
assert redacted.returncode==2
rj=json.loads(redacted.stdout)
assert rj['storyboard'][0]['command']=='export API_KEY=<redacted>'
assert rj['findings'][0]['command']=='export API_KEY=abc'
print('ok developer-demo-gif-script-safety-preview blocked unsafe script and emitted redacted storyboard')
