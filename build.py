import json, re

with open('syllable_dict.json') as f:
    raw = f.read()

with open('annotate.html') as f:
    html = f.read()

injection = f'<script>window.SYLDICT={raw};</script>'
out = html.replace('</head>', injection + '\n</head>', 1)

with open('annotate_bundle.html', 'w') as f:
    f.write(out)

d = json.loads(raw)
print(f'Bundled {len(d)} syllable entries into annotate_bundle.html ({len(out)//1024}KB)')
