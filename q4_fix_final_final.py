import re

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update GNB scroll logic
# Add event listener for .right-panel scroll
scroll_script = """
<script>
document.addEventListener('DOMContentLoaded', function() {
  var rightPanel = document.querySelector('.right-panel');
  var header = document.querySelector('.global-header');
  if(rightPanel && header) {
    rightPanel.addEventListener('scroll', function(e) {
      if (e.target.scrollTop > 10) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }
});
</script>
</body>
"""
content = content.replace('</body>', scroll_script)

# 2. Add individual demo controls to Q1, Q3, Q4 and reduce padding-bottom by 5px

# Q1 Precautions replacement:
q1_old = """<div style="text-align: center; margin-top: 30px;">
        <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Quest 1 Precautions')">Quest 1 precautions</span>
      </div>"""
q1_new = """<div style="text-align: center; margin-top: 30px; margin-bottom: -5px;">
        <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Quest 1 Precautions')">Quest 1 precautions</span>
      </div>
      <!-- QUEST 1 DEMO CONTROLS -->
      <div style="display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 20px;">
        <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 1 DEMO</span>
        <button onclick="setDemoState(0)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568; transition: 0.2s;" onmouseover="this.style.background='rgba(0,0,0,0.1)'" onmouseout="this.style.background='rgba(0,0,0,0.05)'">[1] Not Logged In</button>
        <button onclick="setDemoState(1)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568; transition: 0.2s;" onmouseover="this.style.background='rgba(0,0,0,0.1)'" onmouseout="this.style.background='rgba(0,0,0,0.05)'">[2] Logged In</button>
        <button onclick="setDemoState(2)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568; transition: 0.2s;" onmouseover="this.style.background='rgba(0,0,0,0.1)'" onmouseout="this.style.background='rgba(0,0,0,0.05)'">[3] Success</button>
      </div>"""
content = content.replace(q1_old, q1_new)

# Q3 Precautions replacement:
q3_old = """<div style="text-align: center; margin-top: 10px; padding-bottom: 20px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Veteran Rewards Precautions')">Veteran Rewards precautions</span>
            </div>"""
q3_new = """<div style="text-align: center; margin-top: 10px; padding-bottom: 15px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Veteran Rewards Precautions')">Veteran Rewards precautions</span>
            </div>
            <!-- QUEST 3 DEMO CONTROLS -->
            <div style="display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 10px;">
              <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 3 DEMO</span>
              <button onclick="setQuest3DemoState(0)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568; transition: 0.2s;" onmouseover="this.style.background='rgba(0,0,0,0.1)'" onmouseout="this.style.background='rgba(0,0,0,0.05)'">[1] Not Logged In</button>
              <button onclick="setQuest3DemoState(1)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568; transition: 0.2s;" onmouseover="this.style.background='rgba(0,0,0,0.1)'" onmouseout="this.style.background='rgba(0,0,0,0.05)'">[2] Logged In</button>
              <button onclick="setQuest3DemoState(2)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568; transition: 0.2s;" onmouseover="this.style.background='rgba(0,0,0,0.1)'" onmouseout="this.style.background='rgba(0,0,0,0.05)'">[3] Success</button>
            </div>"""
content = content.replace(q3_old, q3_new)

# Q4 Precautions replacement:
q4_old = """<div style="text-align: center; margin-top: 10px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Daily Roulette Precautions')">Daily Roulette Event precautions</span>
            </div>"""
q4_new = """<div style="text-align: center; margin-top: 10px; margin-bottom: -5px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Daily Roulette Precautions')">Daily Roulette Event precautions</span>
            </div>
            <!-- QUEST 4 DEMO CONTROLS -->
            <div style="display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 15px;">
              <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 4 DEMO</span>
              <button onclick="setQuest4DemoState(0)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568; transition: 0.2s;" onmouseover="this.style.background='rgba(0,0,0,0.1)'" onmouseout="this.style.background='rgba(0,0,0,0.05)'">[1] Not Logged In</button>
              <button onclick="setQuest4DemoState(1)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568; transition: 0.2s;" onmouseover="this.style.background='rgba(0,0,0,0.1)'" onmouseout="this.style.background='rgba(0,0,0,0.05)'">[2] Logged In</button>
            </div>"""
content = content.replace(q4_old, q4_new)


# 3. Replace the 17 items safely
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

# Safely target the list div inside q4RewardsModal
start_modal = '<div style="padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px;">'
end_modal = '    </div>\n  </div>\n</div>\n\n<script>'

parts = content.split(start_modal)
if len(parts) > 1:
    second_part = parts[1].split(end_modal, 1)
    if len(second_part) > 1:
        content = parts[0] + start_modal + '\n' + items_html + '\n' + end_modal + second_part[1]


# 4. Remove floating demo controls block
floating_start = '<!-- UNIFIED DEMO CONTROLS (FLOATING) -->'
floating_end = '</div>\n</body>'

# We know the block is directly before </body> if we look at the file. Actually it's:
# <!-- UNIFIED DEMO CONTROLS (FLOATING) --> ... </div>\n</body>
# Let's just use regex to remove it safely.
content = re.sub(r'<!-- UNIFIED DEMO CONTROLS \(FLOATING\) -->[\s\S]*?(?=</body>)', '', content)


with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)

