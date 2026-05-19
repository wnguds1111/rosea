import os

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# For Quest 1
q1_old = """            <div style="text-align: center; margin-top: 30px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Quest 1 Precautions')">Quest 1 precautions</span>
            </div>
          </div>
        </div>
      </div>
    </div>
"""
q1_new = """            <div style="text-align: center; margin-top: 30px; margin-bottom: -5px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Quest 1 Precautions')">Quest 1 precautions</span>
            </div>
            <!-- QUEST 1 DEMO CONTROLS -->
            <div style="display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 15px;">
              <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 1 DEMO</span>
              <button onclick="setDemoState(0)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[1] Not Logged In</button>
              <button onclick="setDemoState(1)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[2] Logged In</button>
              <button onclick="setDemoState(2)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[3] Success</button>
            </div>
          </div>
        </div>
      </div>
    </div>
"""
if q1_old in content:
    content = content.replace(q1_old, q1_new)
else:
    print("Could not find Q1 target")


# For Quest 3
q3_old = """            <div style="text-align: center; margin-top: 10px; padding-bottom: 20px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Veteran Rewards Precautions')">Veteran Rewards precautions</span>
            </div>
          </div>
        </div>
      </div>
    </div>"""
q3_new = """            <div style="text-align: center; margin-top: 10px; padding-bottom: 15px; margin-bottom: -5px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Veteran Rewards Precautions')">Veteran Rewards precautions</span>
            </div>
            <!-- QUEST 3 DEMO CONTROLS -->
            <div style="display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 10px;">
              <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 3 DEMO</span>
              <button onclick="setQuest3DemoState(0)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[1] Not Logged In</button>
              <button onclick="setQuest3DemoState(1)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[2] Logged In</button>
              <button onclick="setQuest3DemoState(2)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[3] Success</button>
            </div>
          </div>
        </div>
      </div>
    </div>"""
if q3_old in content:
    content = content.replace(q3_old, q3_new)
else:
    print("Could not find Q3 target")

# For Quest 4
q4_old = """            <div style="text-align: center; margin-top: 10px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Daily Roulette Precautions')">Daily Roulette Event precautions</span>
            </div>
            
            

          </div>
        </div>
      </div>
    </div>"""
q4_new = """            <div style="text-align: center; margin-top: 10px; margin-bottom: -5px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Daily Roulette Precautions')">Daily Roulette Event precautions</span>
            </div>
            
            <!-- QUEST 4 DEMO CONTROLS -->
            <div style="display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 15px;">
              <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 4 DEMO</span>
              <button onclick="setQuest4DemoState(0)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[1] Not Logged In</button>
              <button onclick="setQuest4DemoState(1)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[2] Logged In</button>
            </div>

          </div>
        </div>
      </div>
    </div>"""
if q4_old in content:
    content = content.replace(q4_old, q4_new)
else:
    # try slightly different whitespace
    q4_old2 = """            <div style="text-align: center; margin-top: 10px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Daily Roulette Precautions')">Daily Roulette Event precautions</span>
            </div>
            
            

          </div>"""
    if q4_old2 in content:
        content = content.replace(q4_old2, q4_new.replace("        </div>\n      </div>\n    </div>", ""))
    else:
        # let's just do regex for q4
        import re
        content = re.sub(r'<div style="text-align: center; margin-top: 10px;">\s*<span[^>]*>Daily Roulette Event precautions</span>\s*</div>\s*</div>',
        """<div style="text-align: center; margin-top: 10px; margin-bottom: -5px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Daily Roulette Precautions')">Daily Roulette Event precautions</span>
            </div>
            <!-- QUEST 4 DEMO CONTROLS -->
            <div style="display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 15px;">
              <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 4 DEMO</span>
              <button onclick="setQuest4DemoState(0)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[1] Not Logged In</button>
              <button onclick="setQuest4DemoState(1)" style="padding: 4px 8px; background: rgba(0,0,0,0.05); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[2] Logged In</button>
            </div>
          </div>""", content)


# 17 Items update
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
    items_html += f"""      <div style="display: flex; align-items: center; gap: 15px; padding: 10px; border: 1px solid #e2e8f0; border-radius: 6px; background: #f7fafc;">
        <div style="width: 60px; height: 60px; background: #edf2f7; border-radius: 6px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 10px; color: #a0aec0; font-weight: 700; border: 1px dashed #cbd5e0;">IMAGE</div>
        <div style="font-weight: 900; font-size: 15px; color: #2d3748;">{item}</div>
      </div>\n"""

# We can replace the contents of q4RewardsModal using re
import re
content = re.sub(
    r'(<div style="padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px;">)[\s\S]*?(?=    </div>\n  </div>\n</div>\n\n<script>)',
    r'\1\n' + items_html,
    content
)

with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)

