import re

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the floating demo bar
content = re.sub(r'<!-- UNIFIED DEMO CONTROLS \(FLOATING\) -->.*?</div>\s*</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<!-- UNIFIED DEMO CONTROLS \(FLOATING\) -->.*</body>', '</body>', content, flags=re.DOTALL)

# 2. Add individual demo controls back to each section.
# We will find the closing tag of the `.wire-window` for each section and insert the demo bar right after it, before the section's closing tag.

q1_demo = """
      <!-- QUEST 1 DEMO CONTROLS -->
      <div style="width: 100%; max-width: 1100px; display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 10px; padding-right: 10px;">
        <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 1 DEMO</span>
        <button onclick="setDemoState(0)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[1] Not Logged In</button>
        <button onclick="setDemoState(1)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[2] Logged In</button>
        <button onclick="setDemoState(2)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[3] Success</button>
      </div>"""

q3_demo = """
      <!-- QUEST 3 DEMO CONTROLS -->
      <div style="width: 100%; max-width: 1100px; display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 10px; padding-right: 10px;">
        <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 3 DEMO</span>
        <button onclick="setQuest3DemoState(0)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[1] Not Logged In</button>
        <button onclick="setQuest3DemoState(1)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[2] Logged In</button>
        <button onclick="setQuest3DemoState(2)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[3] Success</button>
      </div>"""

q4_demo = """
      <!-- QUEST 4 DEMO CONTROLS -->
      <div style="width: 100%; max-width: 1100px; display: flex; align-items: center; justify-content: flex-end; gap: 8px; margin-top: 10px; padding-right: 10px;">
        <span style="font-size: 11px; font-weight: 800; color: #a0aec0; margin-right: 5px;">QUEST 4 DEMO</span>
        <button onclick="setQuest4DemoState(0)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[1] Not Logged In</button>
        <button onclick="setQuest4DemoState(1)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[2] Logged In</button>
      </div>"""

# For PRD1
content = re.sub(
    r'(<div id="prd1" class="section"[^>]*>.*?<div class="wire-window">.*?</div>\s*</div>\s*</div>\s*</div>)(\s*</div>\s*</div>)',
    r'\1' + q1_demo + r'\n    </div>\n  </div>',
    content, flags=re.DOTALL
)

# For PRD4
content = re.sub(
    r'(<div id="prd4" class="section"[^>]*>.*?<div class="wire-window">.*?</div>\s*</div>\s*</div>\s*</div>)(\s*</div>\s*</div>)',
    r'\1' + q3_demo + r'\n    </div>\n  </div>',
    content, flags=re.DOTALL
)

# For PRD5
content = re.sub(
    r'(<div id="prd5" class="section"[^>]*>.*?<div class="wire-window">.*?</div>\s*</div>\s*</div>\s*</div>)(\s*</div>\s*</div>)',
    r'\1' + q4_demo + r'\n    </div>\n  </div>',
    content, flags=re.DOTALL
)

with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)

