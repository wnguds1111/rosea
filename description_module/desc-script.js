/**
 * PRD Description Module - Reusable Script
 * 다른 프로젝트에 소스 복사 후 바로 사용 가능
 */

window.currentPrdPageNum = 1;
window.currentMarks = [];
window.pageTitle = "";
window.pageOverview = "";
window.isBuilderLocked = true;
window.isAdminIP = false;

// Append Tooltip DOM for non-admin IPs
const badgeTooltip = document.createElement('div');
badgeTooltip.id = 'badgeTooltip';
badgeTooltip.style.cssText = 'position:fixed; display:none; background:rgba(15,23,42,0.95); color:#fff; padding:15px 20px; border-radius:10px; z-index:999999; max-width:320px; box-shadow:0 10px 25px rgba(0,0,0,0.3); font-family:"Pretendard", sans-serif; pointer-events:none; border:1px solid rgba(255,255,255,0.1); backdrop-filter:blur(5px);';
document.body.appendChild(badgeTooltip);

// Check IP
fetch('https://api.ipify.org?format=json')
    .then(res => res.json())
    .then(data => {
        if (data.ip === '119.192.146.202') {
            window.isAdminIP = true;
            const btn = document.querySelector('.prd-toggle');
            if (btn) btn.style.display = 'block';
        }
        if (shouldShowBadges()) loadAndRenderMarks();
    })
    .catch(err => {
        if (shouldShowBadges()) loadAndRenderMarks();
    });

function getTargetKey() {
    let key = window.currentPrdPageNum.toString();
    if (key === '1') {
        if (typeof currentStep !== 'undefined') key = '1-' + currentStep;
    } else if (key === '2') {
        const activePanel = document.querySelector('.market-panel.active');
        if (activePanel) key = '2-' + activePanel.id.replace('panel-', '');
    } else if (key === '3') {
        const activePanel = document.querySelector('.studio-main .panel.active');
        if (activePanel) key = '3-' + activePanel.id.replace('panel-', '');
    }
    return key;
}

window.lastObservedKey = getTargetKey();
window.lastShowBadgesState = false;

function shouldShowBadges() {
    return true; // Always show badges
}

function loadAndRenderMarks() {
    const targetKey = getTargetKey();
    const savedStateStr = localStorage.getItem('rofactory_marks_builder_p' + targetKey);
    let savedStateObj = savedStateStr ? JSON.parse(savedStateStr) : null;

    if (savedStateObj && !Array.isArray(savedStateObj)) {
        window.currentMarks = savedStateObj.marks || [];
        window.pageTitle = savedStateObj.title || "";
        window.pageOverview = savedStateObj.overview || "";
    } else {
        window.currentMarks = [];
        window.pageTitle = "";
        window.pageOverview = "";
    }
    renderBuilderMarks();
}

setInterval(() => {
    let currentKey = getTargetKey();
    let currentShowBadges = shouldShowBadges();

    if (currentKey !== window.lastObservedKey || currentShowBadges !== window.lastShowBadgesState) {
        window.lastObservedKey = currentKey;
        window.lastShowBadgesState = currentShowBadges;

        if (currentShowBadges) {
            loadAndRenderMarks();
        } else {
            document.querySelectorAll('.coach-mark-badge').forEach(e => e.remove());
        }
    }
}, 500);

async function showDynamicDescPanel(pageNum, silent = false) {
    const panel = document.getElementById('pageDescPanel');
    if (!silent) panel.classList.toggle('active');

    if (shouldShowBadges()) {
        loadAndRenderMarks();
    } else {
        document.querySelectorAll('.coach-mark-badge').forEach(e => e.remove());
    }
}

function saveBuilderMarks(re_render = true) {
    window.currentMarks.forEach((m, i) => m.num = i + 1);
    const obj = {
        title: window.pageTitle,
        overview: window.pageOverview.trim(),
        marks: window.currentMarks
    };
    localStorage.setItem('rofactory_marks_builder_p' + getTargetKey(), JSON.stringify(obj));
    if (re_render) renderBuilderMarks();
}

window.updatePageMeta = function (type, txt) {
    if (type === 'title') window.pageTitle = txt;
    if (type === 'overview') window.pageOverview = txt;
    saveBuilderMarks(false);
};

function renderBuilderMarks() {
    document.querySelectorAll('.coach-mark-badge').forEach(e => e.remove());

    if (!shouldShowBadges()) return;

    window.currentMarks.forEach(m => {
        const mark = document.createElement('div');
        mark.className = 'coach-mark-badge';
        mark.innerText = m.num;
        mark.id = 'coach-badge-' + m.id;
        mark.style.top = m.top + 'px';
        mark.style.left = m.left + 'px';

        if (window.isAdminIP && !window.isBuilderLocked) {
            mark.classList.add('draggable');
        }

        if (!window.isAdminIP) {
            mark.addEventListener('mouseenter', (e) => {
                const tooltip = document.getElementById('badgeTooltip');
                if (tooltip) {
                    let linkHtml = m.link ? `<div style="margin-top:10px; font-size:12px; color:#0ea5e9; font-weight:700;">🔗 관련 링크 제공됨</div>` : '';
                    tooltip.innerHTML = `<div style="font-weight:900; font-size:15px; margin-bottom:6px; color:#f8fafc;">${m.title}</div><div style="font-size:13px; color:#cbd5e1; line-height:1.5;">${m.sub}</div>${linkHtml}`;
                    tooltip.style.display = 'block';
                    const rect = mark.getBoundingClientRect();
                    tooltip.style.top = (rect.top + 35) + 'px';
                    tooltip.style.left = rect.left + 'px';
                }
            });
            mark.addEventListener('mouseleave', () => {
                const tooltip = document.getElementById('badgeTooltip');
                if (tooltip) tooltip.style.display = 'none';
            });
        }

        document.body.appendChild(mark);
    });

    const target = document.getElementById('descContent');
    if (!target) return;

    if (!window.isAdminIP) {
        target.innerHTML = '';
        return;
    }
    let html = '';

    if (window.pageTitle || !window.isBuilderLocked) {
        let titleHtml = !window.isBuilderLocked
            ? `<div class="pdp-top-title editable" contenteditable="true" oninput="window.updatePageMeta('title', this.innerText)" placeholder="페이지 제목을 입력하세요">${window.pageTitle || ''}</div>`
            : `<div class="pdp-top-title">${window.pageTitle}</div>`;
        html += titleHtml;
    }
    if (window.pageOverview || !window.isBuilderLocked) {
        let overviewHtml = !window.isBuilderLocked
            ? `<div class="pdp-top-overview editable" contenteditable="true" oninput="window.updatePageMeta('overview', this.innerText)" placeholder="페이지 개요를 입력하세요">${window.pageOverview || ''}</div>`
            : `<div class="pdp-top-overview">${window.pageOverview}</div>`;
        html += overviewHtml;
    }

    if (window.currentMarks.length === 0 && window.isBuilderLocked && !window.pageTitle) {
        html += '<div style="text-align:center; padding:40px 20px; color:#94a3b8; font-weight:700;">해당 뷰에 설정된 정보가 없습니다.<br>자물쇠를 풀고 항목을 추가하세요.</div>';
    }

    window.currentMarks.forEach(m => {
        let deleteBtn = !window.isBuilderLocked ? `<button onclick="deleteMark('${m.id}')" style="position:absolute; right:5px; top:10px; background:#fee2e2; border:none; color:#ef4444; font-weight:900; width:24px; height:24px; border-radius:50%; cursor:pointer; display:flex; align-items:center; justify-content:center;" title="삭제">×</button>` : '';
        let titleHTML = !window.isBuilderLocked ?
            `<div class="mark-title editable" contenteditable="true" oninput="updateMarkText('${m.id}', 'title', this.innerText)" placeholder="제목 입력">${m.title}</div>` :
            `<div class="mark-title">${m.title}</div>`;
        let subHTML = !window.isBuilderLocked ?
            `<div class="mark-sub editable" contenteditable="true" oninput="updateMarkText('${m.id}', 'sub', this.innerText)" style="margin-top:4px;" placeholder="상세 설명 입력">${m.sub}</div>` :
            `<div class="mark-sub">${m.sub}</div>`;

        html += `<div class="md-line" onmouseenter="highlightBadge('${m.id}')" onmouseleave="resetBadge('${m.id}')" style="position:relative; padding-right:30px; display:flex;">
            <span class="badgenum" style="color:#0ea5e9; font-weight:900; margin-right:10px; vertical-align:top; font-size:16px;">${m.num}.</span>
            <div style="flex:1; display:flex; flex-direction:column;">${titleHTML}${subHTML}</div>
            ${deleteBtn}
        </div>`;
    });

    if (!window.isBuilderLocked) {
        html += `<button onclick="addMark()" style="margin-top:15px; width:100%; padding:14px; background:#f8fafc; border:2px dashed #94a3b8; border-radius:12px; color:#475569; font-weight:900; font-size:15px; cursor:pointer; transition:0.2s;" onmouseover="this.style.background='#f1f5f9';" onmouseout="this.style.background='#f8fafc';">+ 새 마커 뱃지 추가하기</button>`;
    }

    target.innerHTML = html;

    const lockBtn = document.getElementById('lockToggleBtn');
    if (lockBtn) {
        if (window.isBuilderLocked) {
            lockBtn.innerHTML = '🔒 편집 자물쇠 풀기';
            lockBtn.style.color = '#fff';
            lockBtn.style.background = '#0f172a';
        } else {
            lockBtn.innerHTML = '💾 저장 및 자물쇠 잠금';
            lockBtn.style.color = '#fff';
            lockBtn.style.background = '#ef4444';
        }
    }
}

function updateMarkText(id, field, newText) {
    const m = window.currentMarks.find(x => x.id === id);
    if (m) {
        m[field] = newText;
        saveBuilderMarks(field === 'link');
    }
}

function deleteMark(id) {
    if (confirm('해당 위치 정보를 영구 삭제하시겠습니까?')) {
        window.currentMarks = window.currentMarks.filter(x => x.id !== id);
        saveBuilderMarks();
    }
}

function addMark() {
    const newNum = window.currentMarks.length + 1;
    window.currentMarks.push({
        id: 'id_' + Date.now(),
        num: newNum,
        title: "새 뱃지 제목",
        sub: "상세 기획 설명을 입력하세요.",
        link: "",
        top: window.scrollY + window.innerHeight / 2,
        left: window.scrollX + window.innerWidth / 2
    });
    saveBuilderMarks();
}

function highlightBadge(id) {
    const badge = document.getElementById('coach-badge-' + id);
    if (badge) {
        badge.classList.add('pulsing');
        badge.style.transform = 'scale(1.5)';
        badge.style.zIndex = '999999';
        badge.style.boxShadow = '0 0 0 10px rgba(239,68,68,0.3)';
    }
}

function resetBadge(id) {
    const badge = document.getElementById('coach-badge-' + id);
    if (badge) {
        badge.classList.remove('pulsing');
        badge.style.transform = '';
        badge.style.zIndex = '99999';
        badge.style.boxShadow = '';
    }
}

function toggleLock() {
    if (window.isBuilderLocked) {
        if (!document.getElementById('pwdLayer')) {
            const layerHtml = `<div id="pwdLayer" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:9999999; background:rgba(15,23,42,0.8); display:flex; align-items:center; justify-content:center; backdrop-filter:blur(3px);">
                <div style="background:#fff; padding:35px 30px; border-radius:20px; width:340px; text-align:center; box-shadow:0 20px 40px rgba(0,0,0,0.3);">
                    <h3 style="margin-top:0; color:#0f172a; font-size:20px; font-weight:900; margin-bottom:25px;">🔒 관리자 인증</h3>
                    <input type="password" id="pwdInput" style="width:100%; padding:14px; border:2px solid #e2e8f0; border-radius:12px; margin-bottom:25px; outline:none; text-align:center; letter-spacing:10px; font-size:24px; font-weight:900; box-sizing:border-box;" maxlength="4" placeholder="****" onkeyup="if(event.key==='Enter') window.checkPwdLayer()">
                    <div style="display:flex; gap:10px;">
                        <button onclick="document.getElementById('pwdLayer').style.display='none'" style="flex:1; padding:14px; border:none; border-radius:12px; background:#f1f5f9; color:#475569; font-weight:900; font-size:15px; cursor:pointer;">이전</button>
                        <button onclick="window.checkPwdLayer()" style="flex:1; padding:14px; border:none; border-radius:12px; background:#0ea5e9; color:#fff; font-weight:900; font-size:15px; cursor:pointer;">확인</button>
                    </div>
                </div>
            </div>`;
            document.body.insertAdjacentHTML('beforeend', layerHtml);
        }
        document.getElementById('pwdLayer').style.display = 'flex';
        document.getElementById('pwdInput').value = '';
        setTimeout(() => document.getElementById('pwdInput').focus(), 100);

        window.checkPwdLayer = function () {
            const pwd = document.getElementById('pwdInput').value;
            if (pwd === "0000") {
                document.getElementById('pwdLayer').style.display = 'none';
                window.isBuilderLocked = false;
                renderBuilderMarks();
            } else {
                const input = document.getElementById('pwdInput');
                input.style.borderColor = '#ef4444';
                input.style.transform = 'translateX(-5px)';
                setTimeout(() => input.style.transform = 'translateX(5px)', 50);
                setTimeout(() => input.style.transform = 'translateX(-5px)', 100);
                setTimeout(() => { input.style.transform = 'translateX(0)'; input.value = ''; input.focus(); }, 150);
            }
        };
    } else {
        window.isBuilderLocked = true;
        renderBuilderMarks();
    }
}

// Drag support for badges
let draggedBadge = null;
let badgeOffsetX = 0, badgeOffsetY = 0;

document.addEventListener('mousedown', function (e) {
    if (e.target.classList.contains('coach-mark-badge') && e.target.classList.contains('draggable')) {
        draggedBadge = e.target;
        badgeOffsetX = e.clientX - parseFloat(draggedBadge.style.left || 0);
        badgeOffsetY = e.clientY - parseFloat(draggedBadge.style.top || 0);
        draggedBadge.classList.remove('pulsing');
        e.preventDefault();
    }
});
document.addEventListener('mousemove', function (e) {
    if (draggedBadge) {
        draggedBadge.style.left = (e.clientX - badgeOffsetX) + 'px';
        draggedBadge.style.top = (e.clientY - badgeOffsetY) + 'px';
    }
});
document.addEventListener('mouseup', function (e) {
    if (draggedBadge) {
        const top = parseFloat(draggedBadge.style.top);
        const left = parseFloat(draggedBadge.style.left);
        const idStr = draggedBadge.id.replace('coach-badge-', '');
        const m = window.currentMarks.find(x => x.id === idStr);
        if (m) {
            m.top = top;
            m.left = left;
            saveBuilderMarks(false);
        }
        draggedBadge = null;
    }
});

window.scrollToBadge = function (id) {
    const badge = document.getElementById('coach-badge-' + id);
    if (badge) {
        badge.scrollIntoView({ behavior: 'smooth', block: 'center' });
        badge.style.transform = 'scale(1.8)';
        badge.style.boxShadow = '0 0 0 15px rgba(239,68,68,0.4)';
        setTimeout(() => {
            badge.style.transform = '';
            badge.style.boxShadow = '';
        }, 1200);
    }
};
