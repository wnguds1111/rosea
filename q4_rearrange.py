import re

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_q4_html = """
            <!-- Q4 Main Content -->
            <div style="position: relative; margin-top: 15px; background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #cbd5e0; display: flex; flex-direction: column; gap: 25px;">
              
              <!-- Login Overlay -->
              <div id="q4LoginOverlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(255,255,255,0.9); z-index: 10; display: flex; flex-direction: column; align-items: center; justify-content: center; border-radius: 8px; backdrop-filter: blur(2px);">
                <div style="font-weight: 800; font-size: 16px; margin-bottom: 15px; color: #2d3748; text-align: center;">You can proceed after logging in.</div>
                <div style="display: flex; gap: 10px;">
                  <button onclick="document.getElementById('fakeLoginPopup').style.display='flex'" style="padding: 12px 24px; background: #e53e3e; color: #fff; border: none; border-radius: 4px; font-weight: 800; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#c53030'" onmouseout="this.style.background='#e53e3e'">GNJOY LOGIN</button>
                  <button style="padding: 12px 24px; background: #fff; color: #000; border: 1px solid #000; border-radius: 4px; font-weight: 800; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#f7fafc'" onmouseout="this.style.background='#fff'">SIGN UP</button>
                </div>
              </div>

              <!-- TOP: Ticket Rules -->
              <div style="display: flex; flex-direction: column;">
                <div style="font-weight: 900; font-size: 15px; color: #2d3748; margin-bottom: 15px; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; display: flex; justify-content: space-between; align-items: center;">
                  <span>TICKET ACQUISITION RULES</span>
                  <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Daily Roulette Precautions')">Event precautions</span>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px;">
                  
                  <!-- Rule 1: Pre-registration -->
                  <div style="background: #f7fafc; border-radius: 8px; border: 1px solid #e2e8f0; padding: 15px; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                      <div style="font-size: 14px; font-weight: 800; color: #2d3748; margin-bottom: 5px;">Pre-registration</div>
                      <div style="font-size: 13px; font-weight: 900; color: #3182ce; margin-bottom: 15px;">+3 Tickets</div>
                    </div>
                    <button id="q4BtnPrereg" style="padding: 10px; background: #3182ce; color: #fff; border: none; border-radius: 6px; font-weight: 800; cursor: pointer; font-size: 12px; width: 100%;">Go to Pre-register</button>
                  </div>

                  <!-- Rule 2: Invite -->
                  <div style="background: #f7fafc; border-radius: 8px; border: 1px solid #e2e8f0; padding: 15px; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                      <div style="font-size: 14px; font-weight: 800; color: #2d3748; margin-bottom: 5px;">Invite a Friend</div>
                      <div style="font-size: 13px; font-weight: 900; color: #3182ce; margin-bottom: 5px;">+3 Tickets per invite</div>
                      <div style="font-size: 11px; color: #718096; font-weight: 600; margin-bottom: 10px;">Max 5 successful invites (Total)</div>
                      <div style="font-size: 12px; font-weight: 800; color: #4a5568; margin-bottom: 15px; text-align: right;">Invited: <span id="q4InviteCount" style="color: #3182ce;">0 / 5</span></div>
                    </div>
                    <button id="q4BtnInvite" style="padding: 10px; background: #3182ce; color: #fff; border: none; border-radius: 6px; font-weight: 800; cursor: pointer; font-size: 12px; width: 100%;">INVITE</button>
                  </div>

                  <!-- Rule 3: Daily Login -->
                  <div style="background: #f7fafc; border-radius: 8px; border: 1px solid #e2e8f0; padding: 15px; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                      <div style="font-size: 14px; font-weight: 800; color: #2d3748; margin-bottom: 5px;">Daily Login (24h)</div>
                      <div style="font-size: 13px; font-weight: 900; color: #48bb78; margin-bottom: 15px;">+1~2 Tickets (Random)</div>
                    </div>
                    <button id="q4BtnLogin" style="padding: 10px; background: #48bb78; color: #fff; border: none; border-radius: 6px; font-weight: 800; cursor: pointer; font-size: 12px; width: 100%;">CHECK IN</button>
                  </div>

                </div>
              </div>

              <!-- BOTTOM: Machine -->
              <div style="display: flex; justify-content: center;">
                <div style="width: 100%; max-width: 650px; background: #fff; border-radius: 16px; border: 4px solid #4a5568; padding: 15px; display: flex; flex-direction: column;">
                  
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
                    <button id="q4StartBtn" style="background: #e2e8f0; color: #4a5568; border: 2px solid #cbd5e0; border-radius: 50px; padding: 10px 30px; font-weight: 900; font-size: 18px; cursor: pointer; transition: 0.1s;" disabled>START</button>
                  </div>

                  <!-- Action Buttons -->
                  <div style="display: flex; gap: 10px; margin-top: 15px;">
                    <button onclick="document.getElementById('q4RewardsModal').style.display='flex'" style="flex: 1; padding: 12px; background: #3182ce; color: #fff; border: none; border-radius: 8px; font-weight: 800; font-size: 13px; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#2b6cb0'" onmouseout="this.style.background='#3182ce'">REWARD LIST</button>
                    <button onclick="document.getElementById('q4HistoryModal').style.display='flex'" style="flex: 1; padding: 12px; background: #4a5568; color: #fff; border: none; border-radius: 8px; font-weight: 800; font-size: 13px; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#2d3748'" onmouseout="this.style.background='#4a5568'">OBTAINED HISTORY</button>
                  </div>
                </div>
              </div>

            </div>
"""

# Replace old Q4 content
# From <div style="display: flex; gap: 20px; position: relative; margin-top: 15px; background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #cbd5e0;">
# up to <!-- QUEST 4 DEMO
pattern_replace = r'<div style="display: flex; gap: 20px; position: relative; margin-top: 15px; background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #cbd5e0;">.*?<!-- QUEST 4 DEMO'
content = re.sub(pattern_replace, new_q4_html.strip() + '\n\n      <!-- QUEST 4 DEMO', content, flags=re.DOTALL)

# Add [3] Completed button to DEMO
demo_btns = """        <button onclick="setQuest4DemoState(0)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[1] Not Logged In</button>
        <button onclick="setQuest4DemoState(1)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[2] Logged In</button>
        <button onclick="setQuest4DemoState(2)" style="padding: 4px 8px; background: rgba(255,255,255,0.7); border: 1px solid #cbd5e0; border-radius: 4px; font-weight: 800; font-size: 11px; cursor: pointer; color: #4a5568;">[3] Completed</button>"""
content = re.sub(r'<button onclick="setQuest4DemoState\(0\).*?</button>\s*<button onclick="setQuest4DemoState\(1\).*?</button>', demo_btns, content, flags=re.DOTALL)

# Update setQuest4DemoState script
new_demo_script = """window.setQuest4DemoState = function(state) {
  var overlay = document.getElementById('q4LoginOverlay');
  
  var btnPrereg = document.getElementById('q4BtnPrereg');
  var btnInvite = document.getElementById('q4BtnInvite');
  var btnLogin = document.getElementById('q4BtnLogin');
  var inviteCount = document.getElementById('q4InviteCount');
  var startBtn = document.getElementById('q4StartBtn');
  var ticketCount = document.getElementById('q4TicketCount');
  
  if (state === 0) {
    if(overlay) overlay.style.display = "flex";
    if(ticketCount) ticketCount.innerText = "0";
    if(startBtn) { startBtn.disabled = true; startBtn.style.background = "#e2e8f0"; startBtn.style.color = "#4a5568"; }
  } else if (state === 1) {
    if(overlay) overlay.style.display = "none";
    if(btnPrereg) { btnPrereg.innerText = "Go to Pre-register"; btnPrereg.style.background = "#3182ce"; btnPrereg.disabled = false; }
    if(inviteCount) { inviteCount.innerText = "0 / 5"; }
    if(btnInvite) { btnInvite.style.background = "#3182ce"; btnInvite.disabled = false; }
    if(btnLogin) { btnLogin.innerText = "CHECK IN"; btnLogin.style.background = "#48bb78"; btnLogin.disabled = false; }
    if(ticketCount) ticketCount.innerText = "0";
    if(startBtn) { startBtn.disabled = true; startBtn.style.background = "#e2e8f0"; startBtn.style.color = "#4a5568"; }
  } else if (state === 2) {
    if(overlay) overlay.style.display = "none";
    if(btnPrereg) { btnPrereg.innerText = "Pre-registration Completed"; btnPrereg.style.background = "#a0aec0"; btnPrereg.disabled = true; }
    if(inviteCount) { inviteCount.innerText = "5 / 5"; }
    if(btnInvite) { btnInvite.style.background = "#a0aec0"; btnInvite.disabled = true; }
    if(btnLogin) { btnLogin.innerText = "CHECKED IN"; btnLogin.style.background = "#a0aec0"; btnLogin.disabled = true; }
    if(ticketCount) ticketCount.innerText = "3";
    if(startBtn) { startBtn.disabled = false; startBtn.style.background = "#3182ce"; startBtn.style.color = "#fff"; }
  }
};"""
content = re.sub(r'window\.setQuest4DemoState = function\(state\) \{[\s\S]*?\n\};', new_demo_script, content)

with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)
