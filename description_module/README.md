# 📝 PRD Description Module

재사용 가능한 기획서 Description 패널 모듈입니다.  
다른 프로젝트에 복사하여 바로 사용할 수 있습니다.

## 사용법

### 1. 파일 복사
`description_module` 폴더 전체를 프로젝트 루트에 복사합니다.

### 2. HTML에 추가
적용할 HTML 파일의 `</body>` 바로 위에 아래 코드를 추가합니다:

```html
<!-- PRD DESCRIPTION INJECTION -->
<link rel="stylesheet" href="description_module/desc-styles.css">
<script src="description_module/desc-script.js"></script>
<div class="page-desc-btn" onclick="showDynamicDescPanel(1)">
    💡 Description
</div>
<div class="page-desc-panel" id="pageDescPanel">
    <div class="pdp-header">
        <span style="font-weight:900; font-size:18px; letter-spacing:1px; color:#0f172a;">DESCRIPTION</span>
        <div style="display:flex; gap:10px; align-items:center;">
            <button id="lockToggleBtn" onclick="toggleLock()" style="border:none; cursor:pointer; background:#0f172a; color:#fff; font-size:12px; font-weight:900; padding:8px 16px; border-radius:20px; transition:0.2s; box-shadow:0 4px 10px rgba(0,0,0,0.1);">🔒 편집 자물쇠 풀기</button>
        </div>
    </div>
    <div class="pdp-body" id="descContent"></div>
</div>
<!-- // PRD DESCRIPTION INJECTION -->
```

### 3. 페이지 번호 설정
`desc-script.js` 내의 `window.currentPrdPageNum`을 해당 페이지에 맞는 번호로 설정합니다.

### 4. 기획서 데이터
`RO_Factory_Detailed_Features.md` 파일에 `## PAGE X: 제목` 형태로 데이터를 작성합니다.

## 파일 구성
- `desc-styles.css` - Description 패널 스타일
- `desc-script.js` - Description 패널 로직 (마커, 빌더, 드래그 등)
- `README.md` - 사용 가이드
