import re

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Quest 3 HTML inside wire-body
pattern = re.compile(r'<div class="tier-container".*?</button>\s*</div>', re.DOTALL)

new_q3_html = """<div class="tier-container" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; width: 100%; max-width: 900px; margin: 10px 0 30px 0;">
                 <!-- DIAMOND -->
                 <div class="tier-box" style="height: 240px; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px 10px; gap: 15px; border: 1px solid #cbd5e0; border-radius: 8px; background: #fdfbfb;">
                   <div style="text-align: center;">
                     <div class="tier-title" style="font-size: 18px; font-weight: 900; color: #2d3748; margin-bottom: 4px;">DIAMOND</div>
                     <div class="tier-desc" style="font-size: 12px; font-weight: 700; color: #718096;">OVER 5 YEARS</div>
                   </div>
                   <div style="width: 70px; height: 70px; background: #e2e8f0; border-radius: 8px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 11px; color: #a0aec0; font-weight: 700; border: 1px dashed #cbd5e0;">IMAGE</div>
                   <div style="text-align: center; font-size: 12px; color: #38a169; font-weight: 800; line-height: 1.4;">Exclusive Title<br>+ 5000 Cash</div>
                 </div>
                 <!-- PLATINUM -->
                 <div class="tier-box" style="height: 240px; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px 10px; gap: 15px; border: 1px solid #cbd5e0; border-radius: 8px; background: #fdfbfb;">
                   <div style="text-align: center;">
                     <div class="tier-title" style="font-size: 18px; font-weight: 900; color: #2d3748; margin-bottom: 4px;">PLATINUM</div>
                     <div class="tier-desc" style="font-size: 12px; font-weight: 700; color: #718096;">OVER 3 YEARS</div>
                   </div>
                   <div style="width: 70px; height: 70px; background: #e2e8f0; border-radius: 8px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 11px; color: #a0aec0; font-weight: 700; border: 1px dashed #cbd5e0;">IMAGE</div>
                   <div style="text-align: center; font-size: 12px; color: #3182ce; font-weight: 800; line-height: 1.4;">Rare Costume<br>+ 3000 Cash</div>
                 </div>
                 <!-- GOLD -->
                 <div class="tier-box" style="height: 240px; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px 10px; gap: 15px; border: 1px solid #cbd5e0; border-radius: 8px; background: #fdfbfb;">
                   <div style="text-align: center;">
                     <div class="tier-title" style="font-size: 18px; font-weight: 900; color: #2d3748; margin-bottom: 4px;">GOLD</div>
                     <div class="tier-desc" style="font-size: 12px; font-weight: 700; color: #718096;">OVER 1 YEAR</div>
                   </div>
                   <div style="width: 70px; height: 70px; background: #e2e8f0; border-radius: 8px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 11px; color: #a0aec0; font-weight: 700; border: 1px dashed #cbd5e0;">IMAGE</div>
                   <div style="text-align: center; font-size: 12px; color: #d69e2e; font-weight: 800; line-height: 1.4;">Costume Box<br>+ 1000 Cash</div>
                 </div>
                 <!-- SILVER -->
                 <div class="tier-box" style="height: 240px; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px 10px; gap: 15px; border: 1px solid #cbd5e0; border-radius: 8px; background: #fdfbfb;">
                   <div style="text-align: center;">
                     <div class="tier-title" style="font-size: 18px; font-weight: 900; color: #2d3748; margin-bottom: 4px;">SILVER</div>
                     <div class="tier-desc" style="font-size: 12px; font-weight: 700; color: #718096;">UNDER 1 YEAR</div>
                   </div>
                   <div style="width: 70px; height: 70px; background: #e2e8f0; border-radius: 8px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 11px; color: #a0aec0; font-weight: 700; border: 1px dashed #cbd5e0;">IMAGE</div>
                   <div style="text-align: center; font-size: 12px; color: #718096; font-weight: 800; line-height: 1.4;">Newbie Pack<br>+ 500 Cash</div>
                 </div>
              </div>

              <div id="q3ActionArea" style="width: 100%; max-width: 500px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
                <!-- Default Auth Button -->
                <button id="vetAuthBtn" class="wire-btn" style="width: 100%; background: #fff; color: var(--text-color); opacity: 0.5; border: 1px solid #cbd5e0; transition: 0.2s; box-shadow: 0 4px 6px rgba(49, 130, 206, 0.2);" onclick="openVetAuthModal()">VETERAN AUTHENTICATION</button>
                
                <!-- Completed State -->
                <div id="q3CompleteArea" style="display: none; width: 100%; flex-direction: column; align-items: center; justify-content: center; background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 6px; padding: 20px;">
                  <div style="font-weight: 900; font-size: 18px; margin-bottom: 5px; color: #276749;">AUTHENTICATION COMPLETED!</div>
                  <div style="font-size: 13px; font-weight: 600; color: #2f855a; margin-bottom: 15px;">YOUR VETERAN TIER HAS BEEN CONFIRMED.</div>
                  <div style="display: flex; align-items: center; justify-content: center; background: #fff; border: 2px dashed #48bb78; padding: 10px 20px; border-radius: 6px; width: 100%;">
                    <span style="font-weight: 800; color: #2f855a; font-size: 14px;">CONFIRMED TIER: <span style="color: #276749; text-decoration: underline; font-size: 18px; margin-left: 5px;">DIAMOND</span></span>
                  </div>
                </div>
              </div>"""

content = pattern.sub(new_q3_html, content)

# 2. Update setQuest3DemoState logic
old_q3_demo_logic = """  window.setQuest3DemoState = function(state) {
    window.currentQuest3State = state;
    const btn = document.getElementById('vetAuthBtn');
    const prompt = document.getElementById('q3LoginPrompt');
    
    if (state === 0) {
      if(prompt) prompt.style.display = "flex";
      if(btn) {
        btn.innerText = "VETERAN AUTHENTICATION";
        btn.style.background = "#fff";
        btn.style.color = "var(--text-color)";
        btn.style.borderColor = "#cbd5e0";
        btn.disabled = true;
        btn.style.opacity = "0.5";
      }
    } else if (state === 1) {
      if(prompt) prompt.style.display = "none";
      if(btn) {
        btn.innerText = "VETERAN AUTHENTICATION";
        btn.style.background = "#fff";
        btn.style.color = "var(--text-color)";
        btn.style.borderColor = "#cbd5e0";
        btn.disabled = false;
        btn.style.opacity = "1";
      }
    } else if (state === 2) {
      if(prompt) prompt.style.display = "none";
      if(btn) {
        btn.innerText = "AUTHENTICATION COMPLETED (DIAMOND)";
        btn.style.background = "#48bb78";
        btn.style.color = "#fff";
        btn.style.borderColor = "#48bb78";
        btn.disabled = true;
        btn.style.opacity = "1";
      }
    }
  };"""

new_q3_demo_logic = """  window.setQuest3DemoState = function(state) {
    window.currentQuest3State = state;
    const btn = document.getElementById('vetAuthBtn');
    const completeArea = document.getElementById('q3CompleteArea');
    
    if (state === 0) {
      if(btn) {
        btn.style.display = "flex";
        btn.style.background = "#fff";
        btn.style.color = "var(--text-color)";
        btn.disabled = true;
        btn.style.opacity = "0.5";
      }
      if(completeArea) completeArea.style.display = "none";
    } else if (state === 1) {
      if(btn) {
        btn.style.display = "flex";
        btn.style.background = "#3182ce"; // Pre-reg color
        btn.style.color = "#fff";
        btn.disabled = false;
        btn.style.opacity = "1";
      }
      if(completeArea) completeArea.style.display = "none";
    } else if (state === 2) {
      if(btn) {
        btn.style.display = "none";
      }
      if(completeArea) completeArea.style.display = "flex";
    }
  };"""

content = content.replace(old_q3_demo_logic, new_q3_demo_logic)

# 3. Add VetAuthModal
new_auth_modal = """<!-- VETERAN AUTH MODAL -->
<div id="vetAuthModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 10000; align-items: center; justify-content: center; backdrop-filter: blur(2px);">
  <div style="background: #fff; width: 350px; padding: 40px 30px; border-radius: 8px; text-align: center; position: relative;">
    <button onclick="document.getElementById('vetAuthModal').style.display='none'" style="position: absolute; top: 15px; right: 15px; background: none; border: none; font-size: 24px; cursor: pointer; color: #a0aec0;">&times;</button>
    <div style="font-size: 20px; font-weight: 900; color: #2d3748; margin-bottom: 10px;">MEMBER AUTHENTICATION</div>
    <div style="font-size: 12px; font-weight: 600; color: #718096; margin-bottom: 20px;">Please enter your GGH/GGL account details to verify your play record.</div>
    <input type="text" placeholder="GNJOY ID" style="width: 100%; height: 45px; margin-bottom: 10px; padding: 0 15px; border: 1px solid #cbd5e0; border-radius: 4px; font-size: 14px; background: #f7fafc;">
    <input type="password" placeholder="Password" style="width: 100%; height: 45px; margin-bottom: 20px; padding: 0 15px; border: 1px solid #cbd5e0; border-radius: 4px; font-size: 14px; background: #f7fafc;">
    <button onclick="document.getElementById('vetAuthModal').style.display='none'; document.getElementById('vetSuccessModal').style.display='flex'; setQuest3DemoState(2);" style="width: 100%; height: 45px; background: #2d3748; color: #fff; border: none; border-radius: 4px; font-weight: 800; cursor: pointer; font-size: 14px;">AUTHENTICATE</button>
  </div>
</div>
"""

old_openAuth = """  function openVetAuthModal() {
    if (window.currentQuest3State === 1) {
      document.getElementById('vetSuccessModal').style.display = 'flex';
      setQuest3DemoState(2);
    }
  }"""

new_openAuth = """  function openVetAuthModal() {
    if (window.currentQuest3State === 1) {
      document.getElementById('vetAuthModal').style.display = 'flex';
    }
  }"""

content = content.replace(old_openAuth, new_openAuth)
content = content.replace('<!-- VETERAN SUCCESS MODAL -->', new_auth_modal + '\n<!-- VETERAN SUCCESS MODAL -->')

with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)
