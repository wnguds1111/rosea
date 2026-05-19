import re

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Extract the 17 reward items (Grid layout)
match = re.search(r'<div style="flex: 1; display: grid; grid-template-columns: repeat\(4, 1fr\); gap: 20px 10px;">(.*?)</div>\s*</div>\s*</div>\s*<div style="text-align: center; margin-top: 10px; margin-bottom: -5px;">', content, re.DOTALL)

if not match:
    print("Could not find the reward grid!")
    # Just grab whatever is between <div style="flex: 1; display: grid... and the end of the right panel
    match2 = re.search(r'<div style="flex: 1; display: grid; grid-template-columns: repeat\(4, 1fr\); gap: 20px 10px;">(.*?)</div>\s*<!-- QUEST 4 DEMO', content, re.DOTALL)
    if match2:
        items_html = match2.group(1)
        print("Found items using fallback regex.")
    else:
        # Extreme fallback
        idx1 = content.find('<div style="flex: 1; display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px 10px;">')
        if idx1 > 0:
            idx2 = content.find('<!-- QUEST 4 DEMO (Moved out of window) -->', idx1)
            items_html = content[idx1 + len('<div style="flex: 1; display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px 10px;">'):idx2]
            items_html = items_html.rsplit('</div>', 4)[0] # remove wrapping divs
            print("Found items using extreme fallback.")
        else:
            items_html = "<!-- ITEMS NOT FOUND -->"
else:
    items_html = match.group(1)

# Ensure items_html is clean
items_html = items_html.strip()

# New Q4 Layout
new_q4_html = """
            <div style="display: flex; gap: 20px; position: relative; margin-top: 15px; background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #cbd5e0;">
              
              <!-- Login Overlay -->
              <div id="q4LoginOverlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(255,255,255,0.9); z-index: 10; display: flex; flex-direction: column; align-items: center; justify-content: center; border-radius: 8px; backdrop-filter: blur(2px);">
                <div style="font-weight: 800; font-size: 16px; margin-bottom: 15px; color: #2d3748; text-align: center;">You can proceed after logging in.</div>
                <div style="display: flex; gap: 10px;">
                  <button onclick="document.getElementById('fakeLoginPopup').style.display='flex'" style="padding: 12px 24px; background: #e53e3e; color: #fff; border: none; border-radius: 4px; font-weight: 800; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#c53030'" onmouseout="this.style.background='#e53e3e'">GNJOY LOGIN</button>
                  <button style="padding: 12px 24px; background: #fff; color: #000; border: 1px solid #000; border-radius: 4px; font-weight: 800; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#f7fafc'" onmouseout="this.style.background='#fff'">SIGN UP</button>
                </div>
              </div>

              <!-- LEFT: Gacha Machine (Wider) -->
              <div style="flex: 1.5; background: #fff; border-radius: 16px; border: 4px solid #4a5568; padding: 15px; display: flex; flex-direction: column;">
                
                <!-- Machine Header -->
                <div style="background: #f7fafc; border-radius: 8px; padding: 15px; text-align: center; border: 2px solid #a0aec0;">
                  <div style="color: #2d3748; font-weight: 900; font-size: 16px; letter-spacing: 1px;">PONPON MACHINE</div>
                </div>

                <!-- Capsule Window (Tall) -->
                <div style="flex: 1; min-height: 480px; background: #edf2f7; border-radius: 16px; border: 2px dashed #a0aec0; margin: 15px 0; display: flex; align-items: center; justify-content: center;">
                   <div style="font-size: 20px; font-weight: 900; color: #a0aec0;">GIF AREA</div>
                </div>

                <!-- Control Panel -->
                <div style="background: #f7fafc; border-radius: 8px; padding: 10px 15px; display: flex; justify-content: space-between; align-items: center; border: 2px solid #a0aec0;">
                  <div>
                    <div style="color: #4a5568; font-size: 12px; font-weight: 800;">AVAILABLE ATTEMPTS</div>
                    <div style="color: #2d3748; font-size: 24px; font-weight: 900;" id="q4TicketCount">0</div>
                  </div>
                  <button id="q4StartBtn" style="background: #e2e8f0; color: #4a5568; border: 2px solid #cbd5e0; border-radius: 50px; padding: 10px 25px; font-weight: 900; font-size: 18px; cursor: pointer; transition: 0.1s;" disabled>START</button>
                </div>

                <!-- Action Buttons -->
                <div style="display: flex; gap: 10px; margin-top: 15px;">
                  <button onclick="document.getElementById('q4RewardsModal').style.display='flex'" style="flex: 1; padding: 12px; background: #3182ce; color: #fff; border: none; border-radius: 8px; font-weight: 800; font-size: 13px; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#2b6cb0'" onmouseout="this.style.background='#3182ce'">REWARD LIST</button>
                  <button onclick="document.getElementById('q4HistoryModal').style.display='flex'" style="flex: 1; padding: 12px; background: #4a5568; color: #fff; border: none; border-radius: 8px; font-weight: 800; font-size: 13px; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#2d3748'" onmouseout="this.style.background='#4a5568'">OBTAINED HISTORY</button>
                </div>
              </div>

              <!-- RIGHT: Ticket Rules (Single Column) -->
              <div style="flex: 1; display: flex; flex-direction: column;">
                <div style="font-weight: 900; font-size: 15px; color: #2d3748; margin-bottom: 15px; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">TICKET ACQUISITION RULES</div>
                
                <div style="display: flex; flex-direction: column; gap: 12px; flex: 1;">
                  <!-- Rule 1 -->
                  <div style="display: flex; flex-direction: column; padding: 12px; background: #f7fafc; border-radius: 8px; border: 1px solid #e2e8f0;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                      <div style="font-size: 14px; font-weight: 800; color: #2d3748;">Pre-registration</div>
                      <div style="font-size: 13px; font-weight: 900; color: #3182ce;">+3 Tickets</div>
                    </div>
                    <button style="padding: 8px; background: #3182ce; color: #fff; border: none; border-radius: 6px; font-weight: 800; cursor: pointer; font-size: 12px; width: 100%;">GO</button>
                  </div>

                  <!-- Rule 2 -->
                  <div style="display: flex; flex-direction: column; padding: 12px; background: #f7fafc; border-radius: 8px; border: 1px solid #e2e8f0;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                      <div style="font-size: 14px; font-weight: 800; color: #2d3748;">Invite a Friend</div>
                      <div style="font-size: 13px; font-weight: 900; color: #3182ce;">+3 Tickets</div>
                    </div>
                    <div style="font-size: 11px; color: #718096; font-weight: 600; margin-bottom: 8px;">Max 5 successful invites per day</div>
                    <button style="padding: 8px; background: #3182ce; color: #fff; border: none; border-radius: 6px; font-weight: 800; cursor: pointer; font-size: 12px; width: 100%;">INVITE</button>
                  </div>

                  <!-- Rule 3 -->
                  <div style="display: flex; flex-direction: column; padding: 12px; background: #f7fafc; border-radius: 8px; border: 1px solid #e2e8f0;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                      <div style="font-size: 14px; font-weight: 800; color: #2d3748;">Daily Login (24h)</div>
                      <div style="font-size: 13px; font-weight: 900; color: #48bb78;">+1~2 Tickets</div>
                    </div>
                    <div style="font-size: 11px; color: #718096; font-weight: 600; margin-bottom: 8px;">Random drop each day</div>
                    <button style="padding: 8px; background: #48bb78; color: #fff; border: none; border-radius: 6px; font-weight: 800; cursor: pointer; font-size: 12px; width: 100%;">CLAIM</button>
                  </div>
                </div>

                <div style="text-align: center; margin-top: 15px;">
                  <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Daily Roulette Precautions')">Daily Roulette Event precautions</span>
                </div>
              </div>
            </div>
"""

# Replace old Q4 content
# Old Q4 content starts at: <!-- Top Layout: Rules & History -->
# And ends at: <div style="text-align: center; margin-top: 10px; margin-bottom: -5px;">...</div>... </div> </div> </div> <!-- QUEST 4 DEMO
# I will use a regex to replace everything between <!-- Top Layout: Rules & History --> and <!-- QUEST 4 DEMO
pattern_replace = r'<!-- Top Layout: Rules & History -->.*?<!-- QUEST 4 DEMO'
content = re.sub(pattern_replace, new_q4_html + '\n      <!-- QUEST 4 DEMO', content, flags=re.DOTALL)


# Create Modals (Rewards & History)
modals_html = f"""
<!-- Q4 REWARDS MODAL -->
<div id="q4RewardsModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 9999; align-items: center; justify-content: center; backdrop-filter: blur(2px);">
  <div style="background: #fff; width: 500px; padding: 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); position: relative; max-height: 80vh; display: flex; flex-direction: column;">
    <button onclick="document.getElementById('q4RewardsModal').style.display='none'" style="position: absolute; top: 15px; right: 15px; background: none; border: none; font-size: 24px; cursor: pointer; color: #a0aec0;">&times;</button>
    <div style="font-size: 18px; font-weight: 900; color: #2d3748; margin-bottom: 20px; text-align: center;">AVAILABLE REWARD LIST</div>
    
    <div style="overflow-y: auto; flex: 1; display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px 10px; padding-right: 5px;">
      {items_html}
    </div>
  </div>
</div>

<!-- Q4 HISTORY MODAL -->
<div id="q4HistoryModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 9999; align-items: center; justify-content: center; backdrop-filter: blur(2px);">
  <div style="background: #fff; width: 400px; padding: 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); position: relative; max-height: 80vh; display: flex; flex-direction: column;">
    <button onclick="document.getElementById('q4HistoryModal').style.display='none'" style="position: absolute; top: 15px; right: 15px; background: none; border: none; font-size: 24px; cursor: pointer; color: #a0aec0;">&times;</button>
    <div style="font-size: 18px; font-weight: 900; color: #2d3748; margin-bottom: 20px; text-align: center;">OBTAINED HISTORY</div>
    
    <div style="overflow-y: auto; flex: 1; min-height: 200px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: #f7fafc; border: 1px dashed #cbd5e0; border-radius: 8px;">
      <span style="font-size: 14px; color: #a0aec0; font-weight: 600;">No history yet.</span>
    </div>
  </div>
</div>
"""

# Append modals before </body>
content = content.replace("</body>", modals_html + "\n</body>")

# Fix setQuest4DemoState
new_demo_script = """window.setQuest4DemoState = function(state) {
  var overlay = document.getElementById('q4LoginOverlay');
  if (state === 0) {
    if(overlay) overlay.style.display = "flex";
  } else if (state === 1) {
    if(overlay) overlay.style.display = "none";
  }
};"""

old_demo_script_pattern = r'window\.setQuest4DemoState = function\(state\) \{.*?\} \};'
# Actually just replace using regex
content = re.sub(r'window\.setQuest4DemoState = function\(state\) \{[\s\S]*?\n\};', new_demo_script, content)

with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Q4 Restructured!")
