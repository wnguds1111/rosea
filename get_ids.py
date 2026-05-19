import re

content = open('wireframe.html', encoding='utf-8').read()
q3_idx = content.find('Quest 3')
q3 = content[q3_idx:q3_idx + 4000]
print("Q3 IDs:", re.findall(r'id="([^"]+)"', q3))

q4_idx = content.find('Quest 4')
q4 = content[q4_idx:q4_idx + 4000]
print("Q4 IDs:", re.findall(r'id="([^"]+)"', q4))

