import re

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the floating demo bar
content = re.sub(r'<!-- UNIFIED DEMO CONTROLS \(FLOATING\) -->.*?</div>\s*</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<!-- UNIFIED DEMO CONTROLS \(FLOATING\) -->.*</body>', '</body>', content, flags=re.DOTALL)

# 2. Define the exact 17 items from the user's image
items = [
    "C_Khalitzburg_KN_Helm",
    "C_Ifrit's_Ear",
    "C_Magic_Circle_Rainbow",
    "Premium_Box_1d",
    "Comp_Battle_Manual",
    "Comp_Bubble_Gum",
    "C_Wing_Of_Fly_1Day_Para",
    "E_Regeneration_Potion",
    "E_Small_Life_Potion",
    "E_Med_Life_Potion",
    "Comp_Small_Mana_Potion",
    "White_Potion_B",
    "Yellow_Potion_B",
    "Orange_Potion_B",
    "Green_Potion_B",
    "E_Inc_Agi_10_Scroll",
    "E_Blessing_10_Scroll"
]

items_html = ""
for item in items:
    items_html += f"""
      <div style="display: flex; align-items: center; gap: 15px; padding: 10px; border: 1px solid #e2e8f0; border-radius: 6px; background: #f7fafc;">
        <div style="width: 60px; height: 60px; background: #edf2f7; border-radius: 6px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 10px; color: #a0aec0; font-weight: 700; border: 1px dashed #cbd5e0;">IMAGE</div>
        <div style="font-weight: 900; font-size: 15px; color: #2d3748;">{item}</div>
      </div>"""

# Replace the inner content of the Q4 rewards modal
modal_start = '<div style="padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px;">'
content = re.sub(
    r'<div style="padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px;">.*?</script>',
    modal_start + items_html + '\n    </div>\n  </div>\n</div>\n\n<script>',
    content, flags=re.DOTALL
)

# 3. Add individual demo controls back to each section just outside .wire-window
q1_demo = """
      <!-- QUEST 1 DEMO CONTROLS -->
      <div style="width: 100%; max-width: 1100px; display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 15px; margin-bottom: 20px; padding-right: 10px; margin-left: auto; margin-right: auto;">
        <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 1 DEMO</span>
        <button onclick="setDemoState(0)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[1] Not Logged In</button>
        <button onclick="setDemoState(1)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[2] Logged In</button>
        <button onclick="setDemoState(2)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[3] Success</button>
      </div>"""

q3_demo = """
      <!-- QUEST 3 DEMO CONTROLS -->
      <div style="width: 100%; max-width: 1100px; display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 15px; margin-bottom: 20px; padding-right: 10px; margin-left: auto; margin-right: auto;">
        <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 3 DEMO</span>
        <button onclick="setQuest3DemoState(0)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[1] Not Logged In</button>
        <button onclick="setQuest3DemoState(1)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[2] Logged In</button>
        <button onclick="setQuest3DemoState(2)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[3] Success</button>
      </div>"""

q4_demo = """
      <!-- QUEST 4 DEMO CONTROLS -->
      <div style="width: 100%; max-width: 1100px; display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 15px; margin-bottom: 20px; padding-right: 10px; margin-left: auto; margin-right: auto;">
        <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 4 DEMO</span>
        <button onclick="setQuest4DemoState(0)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[1] Not Logged In</button>
        <button onclick="setQuest4DemoState(1)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[2] Logged In</button>
      </div>"""

# Remove old demo if present
content = re.sub(r'<!-- QUEST 1 DEMO CONTROLS -->.*?</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<!-- QUEST 3 DEMO CONTROLS -->.*?</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<!-- QUEST 4 DEMO CONTROLS -->.*?</div>', '', content, flags=re.DOTALL)

# Insert after <div class="wire-window">...</div> inside each <div class="section">
# Because regex match of nested divs is risky, we inject right before `</div>\n</div> <!-- End Main Content -->`?
# No, let's inject by looking for `<div id="prdX" ...> ... </div><!-- END prdX -->` if we can.
# Instead, since we know there is `</div>` closing `wire-window` and another `</div>` closing `section`:
# PRD1 ends at line ~480. We can replace: `<div id="prd1"` ... `</div>`
# Better: Just replace the precise markers.

# PRD 1 insertion point: just before `<!-- SECTION 2: -->` or `<div id="prd2"`
content = content.replace('<div id="prd2" class="section"', q1_demo + '\n    <div id="prd2" class="section"')

# PRD 3 insertion point: just before `<div id="prd5" class="section"`
content = content.replace('<div id="prd5" class="section"', q3_demo + '\n    <div id="prd5" class="section"')

# PRD 4 insertion point: just before `  </div> <!-- End Right Panel -->`
content = content.replace('  </div> <!-- End Right Panel -->', q4_demo + '\n  </div> <!-- End Right Panel -->')


with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)

