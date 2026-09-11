import os
import re

EMOJI = "emoji"
BLANK = "https://xcancel.com/tenderlove/status/1032299379707863040"
GROUPS = [
    ("utility", "Utility Reactions"),
    ("memes", "Meme Classics"),
    ("party", "Party Dance"),
    ("parrots", "Party Parrot"),
    ("ai", "AI"),
    ("old-man", "Old Man Yells At"),
    ("numbers", "Numbers"),
]

def key(name):
    m = re.match(r"-?\d+", name)
    if m:
        return (0, int(m.group()), name)
    return (1, 0, name)

rows = []
for folder, title in GROUPS:
    files = {f.split(".")[0]: f for f in os.listdir(f"{EMOJI}/{folder}")}
    names = sorted(files, key=key)
    if folder == "parrots":
        names.remove("party_parrot")
        names.insert(0, "party_parrot")
    rows.append(f"## {title}\n")
    rows.append("| Emoji | Name |")
    rows.append("| :---: | --- |")
    for name in names:
        label = f"`:{name}:`"
        if name == "blank":
            label = f"[{label}]({BLANK})"
        rows.append(f'| <img src="{EMOJI}/{folder}/{files[name]}" width="40" alt="{name}"> | {label} |')
    rows.append("")

header = """# Slack Emoji

To add one to Slack: **Settings & administration -> Customize workspace -> Add Custom Emoji**, upload the file, and give it the name shown beside it.

"""

open("README.md", "w").write(header + "\n".join(rows) + "\n")
