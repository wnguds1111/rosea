import re

with open('wireframe.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Restore PROMO MODAL and desc-script.js
restore_content = """
<!-- PROMO MODAL -->
<div id="promoModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999; align-items: center; justify-content: center; backdrop-filter: blur(2px);">
  <div style="background: #fff; width: 400px; padding: 30px; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); position: relative;">
    <button onclick="document.getElementById('promoModal').style.display='none'" style="position: absolute; top: 15px; right: 15px; background: none; border: none; font-size: 24px; cursor: pointer; color: #a0aec0;">&times;</button>
    <h3 style="margin-bottom: 15px; color: #2d3748; font-size: 18px; font-weight: 800;">Promotional Messages</h3>
    <p style="font-size: 14px; color: #4a5568; line-height: 1.6; font-weight: 500;">By agreeing to receive promotional messages, you will be notified of the latest updates, special events, and exclusive rewards for ROSEA.<br><br>You can opt out at any time through your account settings.</p>
  </div>
</div>

<script src="./description_module/desc-script.js"></script>

</body>
</html>
"""

content = content.replace('</body>\n</html>', restore_content)

with open('wireframe.html', 'w', encoding='utf-8') as f:
    f.write(content)
