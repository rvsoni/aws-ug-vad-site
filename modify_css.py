import re

with open('style.css', 'r') as f:
    content = f.read()

# Replace max-width: \d+px; with max-width: 100%;
# but exclude media queries
def replacer(match):
    # If the match is a media query, return it unchanged
    if '@media' in match.group(0):
        return match.group(0)
    # Otherwise replace max-width: \d+px
    return re.sub(r'max-width:\s*\d+px;', 'max-width: 100%;', match.group(0))

# We can just split by @media and process the non-media parts
parts = re.split(r'(@media\s*\([^)]+\)\s*\{)', content)
new_content = ""
for i, part in enumerate(parts):
    if i % 2 == 0:
        # non-media part
        part = re.sub(r'max-width:\s*\d+px;', 'max-width: 100%;', part)
    new_content += part

with open('style.css', 'w') as f:
    f.write(new_content)
