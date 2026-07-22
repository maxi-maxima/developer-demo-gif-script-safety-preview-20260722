# Developer Demo GIF Script Safety Preview

## Pain it solves
Open source launches need short terminal GIFs, but demo scripts often accidentally reveal tokens, .env files, or destructive commands before recording.

## Why now
AI/devtool projects compete on quick visual demos; safer scripted recordings reduce leaks while keeping launch velocity high.

## Install and run
No third-party dependencies are required.

```bash
python developer_demo_gif_script_safety_preview.py --help
python developer_demo_gif_script_safety_preview.py --json examples/demo.sh
```

## Example
```bash
python developer_demo_gif_script_safety_preview.py examples/demo.sh
# safe_to_record=False findings=2 storyboard_steps=3
```

## Self-check
```bash
python test_developer_demo_gif_script_safety_preview.py
```

## Roadmap
- Emit asciinema chapter files
- Add terminal-width readability scoring
- Auto-redact safe preview scripts

## License
MIT
