import re
with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update wire-window height
content = content.replace("height: 700px;\n    background: #fff;", "min-height: 700px; height: auto;\n    background: #fff;")

# 2. Reformat the reward items to grid mode
# Container start: <div style="flex: 1; display: flex; flex-direction: column; gap: 8px;">
old_container = '<div style="flex: 1; display: flex; flex-direction: column; gap: 8px;">'
new_container = '<div style="flex: 1; display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px 10px;">'
content = content.replace(old_container, new_container)

# Now regex replace each item:
# From:
# <div style="display: flex; align-items: center; gap: 15px; padding: 10px; border: 1px solid #e2e8f0; border-radius: 6px; background: #f7fafc;">
#         <div style="width: 60px; height: 60px; background: #edf2f7; border-radius: 6px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 10px; color: #a0aec0; font-weight: 700; border: 1px dashed #cbd5e0;">IMAGE</div>
#         <div style="font-weight: 900; font-size: 15px; color: #2d3748;">Name</div>
#       </div>
# To:
# <div style="display: flex; flex-direction: column; align-items: center; gap: 8px;">
#         <div style="width: 80px; height: 80px; background: #edf2f7; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 12px; color: #a0aec0; font-weight: 800; border: 2px dashed #cbd5e0;">IMAGE</div>
#         <div style="font-weight: 900; font-size: 13px; color: #2d3748; text-align: center; word-break: break-word; line-height: 1.2;">Name</div>
#       </div>

def replace_item(match):
    name = match.group(1).strip()
    return f"""<div style="display: flex; flex-direction: column; align-items: center; gap: 8px;">
        <div style="width: 80px; height: 80px; background: #edf2f7; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 12px; color: #a0aec0; font-weight: 800; border: 2px dashed #cbd5e0;">IMAGE</div>
        <div style="font-weight: 900; font-size: 13px; color: #2d3748; text-align: center; word-break: break-word; line-height: 1.2;">{name}</div>
      </div>"""

pattern = r'<div style="display: flex; align-items: center; gap: 15px; padding: 10px; border: 1px solid #e2e8f0; border-radius: 6px; background: #f7fafc;">\s*<div style="width: 60px; height: 60px; background: #edf2f7; border-radius: 6px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 10px; color: #a0aec0; font-weight: 700; border: 1px dashed #cbd5e0;">IMAGE</div>\s*<div style="font-weight: 900; font-size: 15px; color: #2d3748;">(.*?)</div>\s*</div>'

content = re.sub(pattern, replace_item, content)

# Write back
with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)
