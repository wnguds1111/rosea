import re

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# find q4RewardsModal and remove it
match = re.search(r'<!-- Q4 REWARDS MODAL -->[\s\S]*?<!-- PROMO MODAL -->', content)
if match:
    content = content.replace(match.group(0), '<!-- PROMO MODAL -->')

with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)
