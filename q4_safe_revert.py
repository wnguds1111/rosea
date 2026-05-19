import re

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the 17 Items inside q4RewardsModal
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

# Safely replace items in the modal. We find the start of the list area and replace up to just before the closing </div></div></div>
start_marker = '<div style="padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px;">'
end_marker = '    </div>\n  </div>\n</div>\n\n<script>'

# We can use split
parts = content.split(start_marker)
if len(parts) > 1:
    second_part = parts[1].split(end_marker, 1)
    if len(second_part) > 1:
        content = parts[0] + start_marker + '\n' + items_html + '\n' + end_marker + second_part[1]

# 2. Remove unified floating bar safely
unified_start = '<!-- UNIFIED DEMO CONTROLS (FLOATING) -->'
unified_end = '</body>'
u_parts = content.split(unified_start)
if len(u_parts) > 1:
    end_parts = u_parts[1].split(unified_end)
    content = u_parts[0] + unified_end + end_parts[1]


# 3. Add individual demo controls back inside each section.
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

# Insert just before the next section
content = content.replace('<!-- SECTION 2:', q1_demo + '\n\n<!-- SECTION 2:')
content = content.replace('<!-- SECTION 5:', q3_demo + '\n\n<!-- SECTION 5:')

# For Q4, we insert it just before '  </div> <!-- End Right Panel -->'
content = content.replace('  </div> <!-- End Right Panel -->', q4_demo + '\n  </div> <!-- End Right Panel -->')


with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)

