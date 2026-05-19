import re

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Invite a Friend Rule
# Replace the INVITE button with the Invited text block
invite_rule_old = r'<div style="font-size: 12px; font-weight: 800; color: #4a5568; margin-bottom: 15px; text-align: right;">Invited: <span id="q4InviteCount" style="color: #3182ce;">0 / 5</span></div>\s*</div>\s*<button id="q4BtnInvite".*?</button>'

invite_rule_new = """<div style="font-size: 12px; font-weight: 800; color: #4a5568; margin-bottom: 15px; text-align: right; display: none;">Invited: <span id="q4InviteCount" style="color: #3182ce;">0 / 5</span></div>
                    </div>
                    <div id="q4InviteCountBox" style="background: #e2e8f0; border-radius: 6px; padding: 10px; text-align: center; font-weight: 900; color: #4a5568; font-size: 13px;">
                      Invited: <span id="q4InviteCountNum" style="color: #3182ce; font-size: 15px; margin-left: 5px;">0 / 5</span>
                    </div>"""
content = re.sub(invite_rule_old, invite_rule_new, content, flags=re.DOTALL)

# 2. Update Daily Login Rule (Add UTC note)
daily_login_title = r'<div style="font-size: 13px; font-weight: 900; color: #48bb78; margin-bottom: 15px;">\+1~2 Tickets \(Random\)</div>'
daily_login_title_new = """<div style="font-size: 13px; font-weight: 900; color: #48bb78; margin-bottom: 5px;">+1~2 Tickets (Random)</div>
                      <div style="font-size: 11px; color: #a0aec0; font-weight: 600; margin-bottom: 10px;">* Resets at 00:00 (UTC+8)</div>"""
content = re.sub(daily_login_title, daily_login_title_new, content)

# 3. Reduce Machine Size and Change Title
content = content.replace('max-width: 650px;', 'max-width: 450px;')
content = content.replace('PONPON MACHINE', 'Daily Machine')

# 4. Change Machine Buttons
old_action_buttons = r'<!-- Action Buttons -->\s*<div style="display: flex; gap: 10px; margin-top: 15px;">.*?</div>'
new_action_buttons = """<!-- Action Buttons -->
                  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 15px;">
                    <button onclick="document.getElementById('q4RewardsModal').style.display='flex'" style="grid-column: span 2; padding: 14px; background: #3182ce; color: #fff; border: none; border-radius: 8px; font-weight: 900; font-size: 15px; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#2b6cb0'" onmouseout="this.style.background='#3182ce'">REWARD LIST</button>
                    <button onclick="document.getElementById('q4RewardHistoryModal').style.display='flex'" style="padding: 12px 10px; background: #4a5568; color: #fff; border: none; border-radius: 8px; font-weight: 800; font-size: 12px; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#2d3748'" onmouseout="this.style.background='#4a5568'">REWARD HISTORY</button>
                    <button onclick="document.getElementById('q4TicketHistoryModal').style.display='flex'" style="padding: 12px 10px; background: #4a5568; color: #fff; border: none; border-radius: 8px; font-weight: 800; font-size: 12px; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#2d3748'" onmouseout="this.style.background='#4a5568'">TICKET HISTORY</button>
                  </div>"""
content = re.sub(old_action_buttons, new_action_buttons, content, flags=re.DOTALL)

# 5. Modify Modals
# We need to change q4HistoryModal to q4RewardHistoryModal and add Mockup Data
# and create q4TicketHistoryModal
old_history_modal = r'<!-- Q4 HISTORY MODAL -->.*?</div>\s*</div>'
new_modals = """<!-- Q4 REWARD HISTORY MODAL -->
<div id="q4RewardHistoryModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 9999; align-items: center; justify-content: center; backdrop-filter: blur(2px);">
  <div style="background: #fff; width: 450px; padding: 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); position: relative; max-height: 80vh; display: flex; flex-direction: column;">
    <button onclick="document.getElementById('q4RewardHistoryModal').style.display='none'" style="position: absolute; top: 15px; right: 15px; background: none; border: none; font-size: 24px; cursor: pointer; color: #a0aec0;">&times;</button>
    <div style="font-size: 18px; font-weight: 900; color: #2d3748; margin-bottom: 20px; text-align: center;">REWARD HISTORY</div>
    
    <div id="q4RewardHistoryEmpty" style="display: flex; flex: 1; min-height: 200px; flex-direction: column; align-items: center; justify-content: center; background: #f7fafc; border: 1px dashed #cbd5e0; border-radius: 8px;">
      <span style="font-size: 14px; color: #a0aec0; font-weight: 600;">No history yet.</span>
    </div>
    
    <div id="q4RewardHistoryList" style="display: none; overflow-y: auto; flex: 1; min-height: 200px; flex-direction: column; gap: 10px; padding-right: 5px;">
       <div style="display: flex; justify-content: space-between; align-items: center; padding: 12px; background: #f7fafc; border: 1px solid #e2e8f0; border-radius: 8px;">
          <div style="display: flex; align-items: center; gap: 12px;">
             <div style="width: 40px; height: 40px; background: #edf2f7; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 9px; font-weight: 700; color: #a0aec0; border: 1px dashed #cbd5e0;">IMAGE</div>
             <div style="font-weight: 900; font-size: 14px; color: #2d3748;">E_Blessing_10_Scroll</div>
          </div>
          <div style="font-size: 12px; font-weight: 600; color: #a0aec0;">2026-05-19 14:30</div>
       </div>
       <div style="display: flex; justify-content: space-between; align-items: center; padding: 12px; background: #f7fafc; border: 1px solid #e2e8f0; border-radius: 8px;">
          <div style="display: flex; align-items: center; gap: 12px;">
             <div style="width: 40px; height: 40px; background: #edf2f7; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 9px; font-weight: 700; color: #a0aec0; border: 1px dashed #cbd5e0;">IMAGE</div>
             <div style="font-weight: 900; font-size: 14px; color: #2d3748;">White_Potion_B</div>
          </div>
          <div style="font-size: 12px; font-weight: 600; color: #a0aec0;">2026-05-18 09:12</div>
       </div>
    </div>
  </div>
</div>

<!-- Q4 TICKET HISTORY MODAL -->
<div id="q4TicketHistoryModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 9999; align-items: center; justify-content: center; backdrop-filter: blur(2px);">
  <div style="background: #fff; width: 450px; padding: 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); position: relative; max-height: 80vh; display: flex; flex-direction: column;">
    <button onclick="document.getElementById('q4TicketHistoryModal').style.display='none'" style="position: absolute; top: 15px; right: 15px; background: none; border: none; font-size: 24px; cursor: pointer; color: #a0aec0;">&times;</button>
    <div style="font-size: 18px; font-weight: 900; color: #2d3748; margin-bottom: 20px; text-align: center;">TICKET ACQUISITION HISTORY</div>
    
    <div id="q4TicketHistoryEmpty" style="display: flex; flex: 1; min-height: 200px; flex-direction: column; align-items: center; justify-content: center; background: #f7fafc; border: 1px dashed #cbd5e0; border-radius: 8px;">
      <span style="font-size: 14px; color: #a0aec0; font-weight: 600;">No history yet.</span>
    </div>
    
    <div id="q4TicketHistoryList" style="display: none; overflow-y: auto; flex: 1; min-height: 200px; flex-direction: column; gap: 10px; padding-right: 5px;">
       <div style="display: flex; justify-content: space-between; align-items: center; padding: 15px; background: #f7fafc; border: 1px solid #e2e8f0; border-radius: 8px;">
          <div>
             <div style="font-weight: 800; font-size: 14px; color: #2d3748;">Invite a Friend</div>
             <div style="font-size: 12px; font-weight: 600; color: #a0aec0; margin-top: 4px;">2026-05-19 14:05</div>
          </div>
          <div style="font-weight: 900; font-size: 16px; color: #3182ce;">+3 Tickets</div>
       </div>
       <div style="display: flex; justify-content: space-between; align-items: center; padding: 15px; background: #f7fafc; border: 1px solid #e2e8f0; border-radius: 8px;">
          <div>
             <div style="font-weight: 800; font-size: 14px; color: #2d3748;">Daily Login (24h)</div>
             <div style="font-size: 12px; font-weight: 600; color: #a0aec0; margin-top: 4px;">2026-05-19 09:00</div>
          </div>
          <div style="font-weight: 900; font-size: 16px; color: #48bb78;">+1 Ticket</div>
       </div>
       <div style="display: flex; justify-content: space-between; align-items: center; padding: 15px; background: #f7fafc; border: 1px solid #e2e8f0; border-radius: 8px;">
          <div>
             <div style="font-weight: 800; font-size: 14px; color: #2d3748;">Pre-registration</div>
             <div style="font-size: 12px; font-weight: 600; color: #a0aec0; margin-top: 4px;">2026-05-15 11:20</div>
          </div>
          <div style="font-weight: 900; font-size: 16px; color: #3182ce;">+3 Tickets</div>
       </div>
    </div>
  </div>
</div>"""
content = re.sub(old_history_modal, new_modals, content, flags=re.DOTALL)

# 6. Update Demo Script
demo_script_patch = """
window.setQuest4DemoState = function(state) {
  var overlay = document.getElementById('q4LoginOverlay');
  
  var btnPrereg = document.getElementById('q4BtnPrereg');
  var inviteCountBox = document.getElementById('q4InviteCountBox');
  var inviteCountNum = document.getElementById('q4InviteCountNum');
  var btnLogin = document.getElementById('q4BtnLogin');
  var startBtn = document.getElementById('q4StartBtn');
  var ticketCount = document.getElementById('q4TicketCount');
  
  var rEmpty = document.getElementById('q4RewardHistoryEmpty');
  var rList = document.getElementById('q4RewardHistoryList');
  var tEmpty = document.getElementById('q4TicketHistoryEmpty');
  var tList = document.getElementById('q4TicketHistoryList');
  
  if (state === 0) {
    if(overlay) overlay.style.display = "flex";
    if(ticketCount) ticketCount.innerText = "0";
    if(startBtn) { startBtn.disabled = true; startBtn.style.background = "#e2e8f0"; startBtn.style.color = "#4a5568"; }
    if(rEmpty) rEmpty.style.display = "flex"; if(rList) rList.style.display = "none";
    if(tEmpty) tEmpty.style.display = "flex"; if(tList) tList.style.display = "none";
  } else if (state === 1) {
    if(overlay) overlay.style.display = "none";
    if(btnPrereg) { btnPrereg.innerText = "Go to Pre-register"; btnPrereg.style.background = "#3182ce"; btnPrereg.disabled = false; }
    if(inviteCountNum) { inviteCountNum.innerText = "0 / 5"; }
    if(inviteCountBox) { inviteCountBox.style.background = "#e2e8f0"; inviteCountBox.style.color = "#4a5568"; }
    if(btnLogin) { btnLogin.innerText = "CHECK IN"; btnLogin.style.background = "#48bb78"; btnLogin.disabled = false; }
    if(ticketCount) ticketCount.innerText = "0";
    if(startBtn) { startBtn.disabled = true; startBtn.style.background = "#e2e8f0"; startBtn.style.color = "#4a5568"; }
    if(rEmpty) rEmpty.style.display = "flex"; if(rList) rList.style.display = "none";
    if(tEmpty) tEmpty.style.display = "flex"; if(tList) tList.style.display = "none";
  } else if (state === 2) {
    if(overlay) overlay.style.display = "none";
    if(btnPrereg) { btnPrereg.innerText = "Pre-registration Completed"; btnPrereg.style.background = "#a0aec0"; btnPrereg.disabled = true; }
    if(inviteCountNum) { inviteCountNum.innerText = "5 / 5"; }
    if(inviteCountBox) { inviteCountBox.style.background = "#cbd5e0"; inviteCountBox.style.color = "#a0aec0"; }
    if(btnLogin) { btnLogin.innerText = "CHECKED IN"; btnLogin.style.background = "#a0aec0"; btnLogin.disabled = true; }
    if(ticketCount) ticketCount.innerText = "7";
    if(startBtn) { startBtn.disabled = false; startBtn.style.background = "#3182ce"; startBtn.style.color = "#fff"; }
    if(rEmpty) rEmpty.style.display = "none"; if(rList) rList.style.display = "flex";
    if(tEmpty) tEmpty.style.display = "none"; if(tList) tList.style.display = "flex";
  }
};
"""
content = re.sub(r'window\.setQuest4DemoState = function\(state\) \{[\s\S]*?\n\};', demo_script_patch.strip(), content)

with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Q4 History & Machine Refinements complete.")
