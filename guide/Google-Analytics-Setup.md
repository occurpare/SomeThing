# Google Analytics 측정 ID 발급 가이드

## 📊 Google Analytics 란?
웹사이트 방문자 수, 행동, 유입 경로 등을 분석하는 Google 의 무료 도구입니다.
AdSense 승인에도 도움이 됩니다.

---

## 🔑 측정 ID 발급 방법 (5 분)

### 1 단계: Google Analytics 접속
1. https://analytics.google.com/ 접속
2. Google 계정으로 로그인 (Gmail 계정)

### 2 단계: 계정 생성
1. **"관리"** (왼쪽 하단 톱니바퀴 아이콘) 클릭
2. **"계정 만들기"** 클릭
3. 계정 이름 입력 (예: `SomeThing`)
4. 데이터 공유 설정 체크 → **"다음"**

### 3 단계: 속성 설정
1. 속성 이름 입력 (예: `SomeThing Website`)
2. 보고 시간대: **한국**
3. 통화: **한국 원 (KRW)**
4. **"다음"** 클릭

### 4 단계: 비즈니스 정보
1. 산업 범주: **예술/엔터테인먼트** (또는 해당 항목)
2. 비즈니스 규모: **10 명 미만**
3. Google Analytics 사용 목적: 모두 선택 가능
4. **"만들기"** 클릭

### 5 단계: 데이터 스트림 생성
1. 플랫폼 선택: **"웹"** 클릭
2. 웹사이트 URL 입력: `https://occurpare.github.io/SomeThing/`
3. 스트림 이름 입력: `SomeThing Main`
4. **"스트림 만들기"** 클릭

### 6 단계: 측정 ID 복사
1. 스트림 세부정보 페이지에서 **측정 ID** 확인
2. 형식: `G-XXXXXXXXXX` (G + 영문자/숫자 10 자리)
3. 이 ID 를 복사합니다!

---

## 📝 적용 방법

### index.html 수정
```html
<!-- 기존 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>

<!-- 수정 후 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### 주의사항
- `G-XXXXXXXXXX` 부분을 실제 측정 ID 로 교체하세요
- 4 군데 모두 같은 ID 를 사용하세요 (index.html, privacy.html, terms.html, cookies.html)

---

## ✅ 확인 방법

1. Google Analytics 대시보드에서 **"실시간"** 메뉴 클릭
2. 새 탭에서 웹사이트 방문
3. 실시간 방문자 수에 잡히면 성공!

---

## 💡 팁

- 측정 ID 는 여러 사이트에서 재사용 가능
- 유실되면 언제든지 관리 화면에서 확인 가능
- AdSense 와 연동하면 더 자세한 분석 가능

---

*발급 소요 시간: 약 5 분*
*비용: 무료*
