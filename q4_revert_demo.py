import re

with open('rewards.txt', 'r', encoding='utf-8') as f:
    rewards_content = f.read()

# Extract just the list items
match = re.search(r'<div style="padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px;">([\s\S]*?)</div>\s*</div>\s*</div>', rewards_content)
if match:
    items_html = match.group(1).strip()
else:
    items_html = "ERROR NOT FOUND"
    print("FAILED TO FIND ITEMS")
    exit(1)

new_q4_html = """            <!-- Top Layout: Rules & History -->
            <div style="background: #fff; border: 1px solid #cbd5e0; border-radius: 8px; padding: 15px; margin-top: 15px; position: relative;">
              
              <!-- Login Overlay -->
              <div id="q4LoginOverlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(255,255,255,0.9); z-index: 10; display: flex; flex-direction: column; align-items: center; justify-content: center; border-radius: 8px; backdrop-filter: blur(2px);">
                <div style="font-weight: 800; font-size: 16px; margin-bottom: 15px; color: #2d3748; text-align: center;">You can proceed after logging in.</div>
                <div style="display: flex; gap: 10px;">
                  <button onclick="document.getElementById('fakeLoginPopup').style.display='flex'" style="padding: 12px 24px; background: #e53e3e; color: #fff; border: none; border-radius: 4px; font-weight: 800; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#c53030'" onmouseout="this.style.background='#e53e3e'">GNJOY LOGIN</button>
                  <button style="padding: 12px 24px; background: #fff; color: #000; border: 1px solid #000; border-radius: 4px; font-weight: 800; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#f7fafc'" onmouseout="this.style.background='#fff'">SIGN UP</button>
                </div>
              </div>

              <div style="display: flex; gap: 20px;">
                
                <!-- Rules -->
                <div style="flex: 2;">
                  <div style="font-weight: 900; font-size: 14px; color: #2d3748; margin-bottom: 10px;">TICKET ACQUISITION RULES</div>
                  <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: #f7fafc; border-radius: 4px; border: 1px solid #e2e8f0;">
                      <div>
                        <div style="font-size: 13px; font-weight: 700; color: #4a5568;">Pre-registration Participation</div>
                        <div style="font-size: 12px; font-weight: 800; color: #3182ce;">+3 Tickets</div>
                      </div>
                      <button style="padding: 6px 16px; background: #3182ce; color: #fff; border: none; border-radius: 4px; font-weight: 800; cursor: pointer; font-size: 11px;">GO</button>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: #f7fafc; border-radius: 4px; border: 1px solid #e2e8f0;">
                      <div>
                        <div style="font-size: 13px; font-weight: 700; color: #4a5568;">Invite a Friend (Max 5/day)</div>
                        <div style="font-size: 12px; font-weight: 800; color: #3182ce;">+3 Tickets per successful invite</div>
                      </div>
                      <button style="padding: 6px 16px; background: #3182ce; color: #fff; border: none; border-radius: 4px; font-weight: 800; cursor: pointer; font-size: 11px;">INVITE</button>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: #f7fafc; border-radius: 4px; border: 1px solid #e2e8f0;">
                      <div>
                        <div style="font-size: 13px; font-weight: 700; color: #4a5568;">Daily Login (24h)</div>
                        <div style="font-size: 12px; font-weight: 800; color: #3182ce;">+1~2 Tickets randomly</div>
                      </div>
                      <button style="padding: 6px 16px; background: #48bb78; color: #fff; border: none; border-radius: 4px; font-weight: 800; cursor: pointer; font-size: 11px;">CLAIM</button>
                    </div>
                  </div>
                </div>

                <!-- Obtained History -->
                <div style="flex: 1;">
                  <div style="font-weight: 900; font-size: 14px; color: #2d3748; margin-bottom: 10px;">OBTAINED HISTORY</div>
                  <div style="height: 165px; display: flex; align-items: center; justify-content: center; background: #f7fafc; border: 1px dashed #cbd5e0; border-radius: 4px;">
                    <span style="font-size: 12px; color: #a0aec0; font-weight: 600;">No history yet.</span>
                  </div>
                </div>

              </div>
            </div>

            <!-- Bottom Layout Container -->
            <div style="display: flex; gap: 20px; margin-top: 20px;">
              
              <!-- LEFT: Gacha Machine -->
              <div style="flex: 1; max-width: 400px; background: #fff; border-radius: 16px; border: 4px solid #4a5568; padding: 15px; display: flex; flex-direction: column;">
                
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
              </div>

              <!-- RIGHT: Reward List inline -->
              <div style="flex: 1; background: #fff; border: 1px solid #cbd5e0; border-radius: 16px; padding: 20px; display: flex; flex-direction: column;">
                <div style="font-size: 16px; font-weight: 900; color: #2d3748; margin-bottom: 15px; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">AVAILABLE REWARD LIST</div>
                
                <div style="overflow-y: auto; flex: 1; display: flex; flex-direction: column; gap: 8px; max-height: 600px; padding-right: 5px;">
""" + items_html + """
                </div>
              </div>
            </div>"""

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- Left/Right Layout Container -->'
end_marker = '<!-- Reward List Button -->'
end_div = '</div>\n            </div>'

start_idx = content.find(start_marker)
# Find the exact end of the old block
end_idx = content.find('<!-- Reward List Button -->', start_idx)
if end_idx != -1:
    # also skip the button itself
    end_idx = content.find('</button>', end_idx) + 9
    end_idx = content.find('</div>', end_idx) + 6
    end_idx = content.find('</div>', end_idx) + 6
else:
    print("END MARKER NOT FOUND")
    exit(1)

# Now we also need to change the setQuest4DemoState logic since we changed from "0 / 15" to "0"
new_content = content[:start_idx] + new_q4_html + content[end_idx:]

new_content = new_content.replace("ticketCount.innerText = '0 / 15';", "ticketCount.innerText = '0';")
new_content = new_content.replace("ticketCount.innerText = '3 / 15';", "ticketCount.innerText = '3';")
new_content = new_content.replace("ticketCount.innerText = '2 / 15';", "ticketCount.innerText = '2';")

with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
