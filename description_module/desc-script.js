/**
 * PRD Description Module - Reusable Script
 * 다른 프로젝트에 소스 복사 후 바로 사용 가능
 * 
 * 사용법:
 * 1. desc-styles.css와 desc-script.js를 프로젝트에 복사
 * 2. HTML에서 window.currentPrdPageNum 설정
 * 3. RO_Factory_Detailed_Features.md 파일에 기획 데이터 작성
 */

window.currentPrdPageNum = 1; // 페이지 번호: 프로젝트별로 변경
window.currentMarks = [];
window.pageTitle = "";
window.pageOverview = "";
window.isBuilderLocked = true;

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

setInterval(() => {
    let currentKey = getTargetKey();
    if (currentKey !== window.lastObservedKey) {
        window.lastObservedKey = currentKey;
        const panel = document.getElementById('pageDescPanel');
        if (panel && panel.classList.contains('active')) {
            showDynamicDescPanel(window.currentPrdPageNum, true);
        }
    }
}, 500);

async function showDynamicDescPanel(pageNum, silent = false) {
    const panel = document.getElementById('pageDescPanel');
    if (!silent) panel.classList.toggle('active');

    if (panel.classList.contains('active')) {
        const targetKey = getTargetKey();
        const savedStateStr = localStorage.getItem('rofactory_marks_builder_p' + targetKey);
        let savedStateObj = savedStateStr ? JSON.parse(savedStateStr) : null;

        if (savedStateObj && !Array.isArray(savedStateObj)) {
            window.currentMarks = savedStateObj.marks || [];
            window.pageTitle = savedStateObj.title || "";
            window.pageOverview = savedStateObj.overview || "";
            renderBuilderMarks();
        } else {
            document.getElementById('descContent').innerHTML = '<div style="text-align:center; padding:20px;">로딩 중...</div>';
            try {
                const res = await fetch('RO_Factory_Detailed_Features.md?t=' + new Date().getTime());
                if (!res.ok) throw new Error("Failed to load MD file");
                const text = await res.text();

                const searchStr = '## PAGE ' + targetKey;
                const startIdx = text.indexOf(searchStr);
                if (startIdx === -1) {
                    document.getElementById('descContent').innerHTML = '<div style="text-align:center; padding:40px 20px; color:#94a3b8; font-weight:700;">해당 뷰(PAGE ' + targetKey + ')에 작성된 데이터가 없습니다.<br>빌더 모드를 켜고 직접 기획서를 생성하세요.</div>';
                    window.currentMarks = [];
                    window.pageTitle = "";
                    window.pageOverview = "";
                    renderBuilderMarks();
                    return;
                }

                let endIdx = text.indexOf('---', startIdx + 1);
                let endIdx2 = text.indexOf('## PAGE', startIdx + 1);
                endIdx = endIdx === -1 ? endIdx2 : (endIdx2 === -1 ? endIdx : Math.min(endIdx, endIdx2));
                if (endIdx === -1) endIdx = text.length;

                window.currentMarks = [];
                window.pageTitle = "";
                window.pageOverview = "";

                const rawLines = text.substring(startIdx, endIdx).split('\n');
                let isParsingList = false;

                rawLines.forEach(line => {
                    line = line.trim();
                    if (line.startsWith(searchStr)) {
                        const colonIdx = line.indexOf(':');
                        if (colonIdx !== -1) {
                            window.pageTitle = line.substring(colonIdx + 1).trim();
                        }
                    } else if (line.length > 0 && !line.match(/^\d+\./) && !isParsingList && !line.startsWith('##')) {
                        window.pageOverview += line + " ";
                    } else if (line.match(/^\d+\./)) {
                        isParsingList = true;
                        const num = parseInt(line.substring(0, line.indexOf('.')));
                        let content = line.substring(line.indexOf('.') + 1).trim();

                        let selector = '';
                        let top = window.scrollY + 100 + (num * 40);
                        let left = window.scrollX + 100 + (num * 40);

                        const selMatch = content.match(/\{selector:(.*?)\}/);
                        if (selMatch) {
                            selector = selMatch[1].trim();
                            content = content.replace(selMatch[0], '').trim();
                            const el = document.querySelector(selector);
                            if (el && el.offsetParent !== null) {
                                const rect = el.getBoundingClientRect();
                                top = window.scrollY + Math.max(0, rect.top - 10);
                                left = window.scrollX + Math.max(0, rect.left - 10);
                            }
                        }

                        let link = '';
                        const linkMatch = content.match(/\{link:(.*?)\}/);
                        if (linkMatch) {
                            link = linkMatch[1].trim();
                            content = content.replace(linkMatch[0], '').trim();
                        }

                        content = content.replace(/\*\*(.*?)\*\*/g, '$1');

                        let titleStr = "설명없음";
                        let subStr = content;

                        if (content.includes(':')) {
                            let splitIdx = content.indexOf(':');
                            titleStr = content.substring(0, splitIdx).trim();
                            subStr = content.substring(splitIdx + 1).trim();
                        }

                        window.currentMarks.push({
                            id: 'id_' + Date.now() + Math.random().toString(36).substr(2, 5),
                            num: num,
                            title: titleStr,
                            sub: subStr,
                            top: top,
                            left: left,
                            link: link
                        });
                    }
                });

                saveBuilderMarks(false);
                renderBuilderMarks();
            } catch (e) {
                console.error(e);
                document.getElementById('descContent').innerHTML = '초기 파일 파싱 에러: ' + e.message;
            }
        }
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
    window.currentMarks.forEach(m => {
        const mark = document.createElement('div');
        mark.className = 'coach-mark-badge';
        mark.innerText = m.num;
        mark.id = 'coach-badge-' + m.id;
        mark.style.top = m.top + 'px';
        mark.style.left = m.left + 'px';
        if (!window.isBuilderLocked) mark.classList.add('draggable');
        document.body.appendChild(mark);
    });

    const target = document.getElementById('descContent');
    let html = '';

    if (window.pageTitle || !window.isBuilderLocked) {
        let titleHtml = !window.isBuilderLocked
            ? `<div class="pdp-top-title editable" contenteditable="true" onblur="window.updatePageMeta('title', this.innerText)" placeholder="페이지 제목을 입력하세요">${window.pageTitle || ''}</div>`
            : `<div class="pdp-top-title">${window.pageTitle}</div>`;
        html += titleHtml;
    }
    if (window.pageOverview || !window.isBuilderLocked) {
        let overviewHtml = !window.isBuilderLocked
            ? `<div class="pdp-top-overview editable" contenteditable="true" onblur="window.updatePageMeta('overview', this.innerText)" placeholder="페이지 개요를 입력하세요">${window.pageOverview || ''}</div>`
            : `<div class="pdp-top-overview">${window.pageOverview}</div>`;
        html += overviewHtml;
    }

    if (window.currentMarks.length === 0 && window.isBuilderLocked && !window.pageTitle) {
        html += '<div style="text-align:center; padding:40px 20px; color:#94a3b8; font-weight:700;">해당 뷰에 설정된 정보가 없습니다.<br>자물쇠를 풀고 항목을 추가하세요.</div>';
    }

    window.currentMarks.forEach(m => {
        let deleteBtn = !window.isBuilderLocked ? `<button onclick="deleteMark('${m.id}')" style="position:absolute; right:5px; top:10px; background:#fee2e2; border:none; color:#ef4444; font-weight:900; width:24px; height:24px; border-radius:50%; cursor:pointer; display:flex; align-items:center; justify-content:center;" title="삭제">×</button>` : '';
        let titleHTML = !window.isBuilderLocked ?
            `<div class="mark-title editable" contenteditable="true" onblur="updateMarkText('${m.id}', 'title', this.innerText)" placeholder="제목 입력">${m.title}</div>` :
            `<div class="mark-title">${m.title}</div>`;
        let subHTML = !window.isBuilderLocked ?
            `<div class="mark-sub editable" contenteditable="true" onblur="updateMarkText('${m.id}', 'sub', this.innerText)" style="margin-top:4px;" placeholder="상세 설명 입력">${m.sub}</div>` :
            `<div class="mark-sub">${m.sub}</div>`;

        let linkHTML = '';
        if (!window.isBuilderLocked) {
            if (m.link) {
                linkHTML = `<div style="margin-top:10px;"><input type="text" value="${m.link}" onblur="updateMarkText('${m.id}', 'link', this.value)" style="width:70%; border:1px solid #cbd5e1; border-radius:6px; padding:6px 10px; font-size:12px; margin-right:5px; outline:none;" placeholder="https://"><button onclick="updateMarkText('${m.id}', 'link', '')" style="background:#fee2e2; border:none; color:#ef4444; padding:6px 10px; border-radius:6px; font-size:11px; font-weight:800; cursor:pointer;" title="링크 삭제">[X]</button></div>`;
            } else {
                linkHTML = `<div style="margin-top:10px;"><button onclick="promptForLink('${m.id}')" style="background:#f1f5f9; border:none; color:#0ea5e9; font-weight:800; font-size:12px; padding:6px 12px; border-radius:8px; cursor:pointer; display:flex; align-items:center;">+ 🔗 외부 링크 삽입</button></div>`;
            }
        } else {
            if (m.link) {
                linkHTML = `<div style="margin-top:10px;"><a href="${m.link}" target="_blank" style="display:inline-block; background:#0ea5e9; color:#fff; text-decoration:none; padding:6px 12px; border-radius:20px; font-size:12px; font-weight:800; transition:0.2s;" onmouseover="this.style.background='#0284c7'" onmouseout="this.style.background='#0ea5e9'">🔗 관련 링크 이동 ></a></div>`;
            }
        }

        html += `<div class="md-line" onmouseenter="highlightBadge('${m.id}')" onmouseleave="resetBadge('${m.id}')" style="position:relative; padding-right:30px; display:flex;">
            <span class="badgenum" style="color:#0ea5e9; font-weight:900; margin-right:10px; vertical-align:top; font-size:16px;">${m.num}.</span>
            <div style="flex:1; display:flex; flex-direction:column;">${titleHTML}${subHTML}${linkHTML}</div>
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

function promptForLink(id) {
    let url = prompt("연결할 외부 링크 URL을 입력하세요. (예: https://example.com)");
    if (url && url.trim().length > 0) {
        updateMarkText(id, 'link', url.trim());
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
