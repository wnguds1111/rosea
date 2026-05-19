import re

with open('wireframe.html', encoding='utf-8') as f:
    content = f.read()
    
idx = content.find('id="q4RewardsModal"')
if idx != -1:
    end = content.find('id="promoModal"', idx)
    with open('rewards.txt', 'w', encoding='utf-8') as out:
        out.write(content[idx:end])
