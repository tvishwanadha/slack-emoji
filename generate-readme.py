import os

EMOJI = "emoji"
BLANK = "https://twitter.com/tenderlove/status/1032299379707863040"

files = {f.split(".")[0]: f for f in os.listdir(EMOJI)}

rows = []
for name in sorted(files):
    label = f"`:{name}:`"
    if name == "blank":
        label = f"[{label}]({BLANK})"
    rows.append(f'| <img src="{EMOJI}/{files[name]}" width="40" alt="{name}"> | {label} |')

header = """# Slack Emoji

To add one to Slack: **Settings & administration -> Customize workspace -> Add Custom Emoji**, upload the file, and give it the name shown beside it.

| Emoji | Name |
| :---: | --- |
"""

open("README.md", "w").write(header + "\n".join(rows) + "\n")
