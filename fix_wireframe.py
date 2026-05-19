import re

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix missing closing div in Quest 1
q1_old = """              </div>

            <div style="text-align: center; margin-top: 20px; padding-bottom: 20px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Pre-Registration Precautions')">Pre-Registration precautions</span>"""
q1_new = """              </div>
            </div> <!-- END wire-content-box -->

            <div style="text-align: center; margin-top: 20px; padding-bottom: 20px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Pre-Registration Precautions')">Pre-Registration precautions</span>"""
content = content.replace(q1_old, q1_new)


# 2. Fix Quest 2
q2_old = """            <div class="wire-content-box">
              <div style="font-size:20px; font-weight:800; color:#e53e3e;">CURRENT GLOBAL PARTICIPANTS: 12,450</div>
              <div class="gauge-box">
                <div class="gauge-fill"></div>
                <div class="gauge-text">PROGRESS 45%</div>
              </div>
              <div style="display:flex; gap:20px; width:100%; max-width:700px; font-weight:700; font-size:12px; justify-content:space-between; color:#718096;">
                 <div>10K REACHED</div><div>50K REACHED</div><div>100K REACHED</div><div>200K REACHED</div><div>300K REACHED</div>
              </div>
            </div>
            <button class="wire-btn">CHECK ACCUMULATED REWARDS</button>
          </div>"""
          
q2_new = """            <div class="wire-content-box" style="padding: 40px; align-items: stretch; background: transparent; border: none;">
              <div style="display: flex; flex-direction: column; width: 100%; gap: 30px;">
                <!-- Milestone Line -->
                <div style="display: flex; align-items: center; justify-content: space-between; position: relative; padding: 0 40px;">
                  <div style="position: absolute; top: 15px; left: 40px; right: 40px; height: 6px; background: #e2e8f0; z-index: 1;"></div>
                  
                  <div style="position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; gap: 10px;">
                    <div style="width: 36px; height: 36px; background: #48bb78; border-radius: 50%; border: 5px solid #fff; box-shadow: 0 2px 6px rgba(0,0,0,0.1);"></div>
                    <div style="font-weight: 900; font-size: 18px; color: #38a169;">20K</div>
                  </div>
                  <div style="position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; gap: 10px;">
                    <div style="width: 36px; height: 36px; background: #cbd5e0; border-radius: 50%; border: 5px solid #fff; box-shadow: 0 2px 6px rgba(0,0,0,0.1);"></div>
                    <div style="font-weight: 800; font-size: 18px; color: #a0aec0;">50K</div>
                  </div>
                  <div style="position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; gap: 10px;">
                    <div style="width: 36px; height: 36px; background: #cbd5e0; border-radius: 50%; border: 5px solid #fff; box-shadow: 0 2px 6px rgba(0,0,0,0.1);"></div>
                    <div style="font-weight: 800; font-size: 18px; color: #a0aec0;">100K</div>
                  </div>
                  <div style="position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; gap: 10px;">
                    <div style="width: 36px; height: 36px; background: #cbd5e0; border-radius: 50%; border: 5px solid #fff; box-shadow: 0 2px 6px rgba(0,0,0,0.1);"></div>
                    <div style="font-weight: 800; font-size: 18px; color: #a0aec0;">150K</div>
                  </div>
                  <div style="position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; gap: 10px;">
                    <div style="width: 36px; height: 36px; background: #cbd5e0; border-radius: 50%; border: 5px solid #fff; box-shadow: 0 2px 6px rgba(0,0,0,0.1);"></div>
                    <div style="font-weight: 800; font-size: 18px; color: #a0aec0;">200K</div>
                  </div>
                </div>

                <!-- Reward Cards -->
                <div style="display: flex; gap: 15px; justify-content: space-between;">
                  <!-- Card 1 -->
                  <div style="flex: 1; height: 240px; border: 2px solid #48bb78; border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 25px; background: #f0fff4; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <div style="font-weight: 800; font-size: 14px; color: #2f855a; text-align: center;">[Event] Orange<br>Potion</div>
                  </div>
                  <!-- Card 2 -->
                  <div style="flex: 1; height: 240px; border: 2px dashed #cbd5e0; border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: linear-gradient(180deg, #f8fafc 0%, #edf2f7 100%);">
                    <div style="font-size: 50px; font-weight: 900; color: #cbd5e0;">?</div>
                  </div>
                  <!-- Card 3 -->
                  <div style="flex: 1; height: 240px; border: 2px dashed #cbd5e0; border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: linear-gradient(180deg, #f8fafc 0%, #edf2f7 100%);">
                    <div style="font-size: 50px; font-weight: 900; color: #cbd5e0;">?</div>
                  </div>
                  <!-- Card 4 -->
                  <div style="flex: 1; height: 240px; border: 2px dashed #cbd5e0; border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: linear-gradient(180deg, #f8fafc 0%, #edf2f7 100%);">
                    <div style="font-size: 50px; font-weight: 900; color: #cbd5e0;">?</div>
                  </div>
                  <!-- Card 5 -->
                  <div style="flex: 1; height: 240px; border: 2px dashed #cbd5e0; border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: linear-gradient(180deg, #f8fafc 0%, #edf2f7 100%);">
                    <div style="font-size: 50px; font-weight: 900; color: #cbd5e0;">?</div>
                  </div>
                </div>
              </div>
            </div>
            
            <div style="text-align: center; margin-top: 10px; padding-bottom: 20px;">
              <span style="font-size: 12px; font-weight: 700; color: #a0aec0; text-decoration: underline; cursor: pointer;" onclick="openPrecautions('Milestone Event Precautions')">Milestone Event precautions</span>
            </div>
          </div>"""
content = content.replace(q2_old, q2_new)

with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)
