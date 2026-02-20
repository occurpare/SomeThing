/**
 * SomeThing v3 - New Workflow
 * 랜딩 → 연애성향(10Q) → 테스트선택(3) → 성향별맞춤 → 결과
 */

// ===== State =====
const state = {
  currentPhase: 'landing',
  personality: {
    scores: { D: 0, C: 0, R: 0, P: 0 },
    type: null,
    currentQ: 0
  },
  selectedTest: null,
  testAnswers: [],
  testCurrentQ: 0
};

// ===== 연애 성향 테스트 (10문) =====
const personalityQuestions = [
  {
    text: '좋아하는 사람이 생기면?',
    options: [
      { text: '바로 고백한다! 시간 낭비는 싫어', scores: { D: 3, C: 0, R: 1, P: 1 } },
      { text: '신중하게 관찰하며 기회를 기다린다', scores: { D: 0, C: 3, R: 1, P: 0 } },
      { text: '먼저 조건과 상황을 따져본다', scores: { D: 0, C: 1, R: 3, P: 0 } },
      { text: '감정이 이끄는 대로 분위기를 탄다', scores: { D: 1, C: 0, R: 0, P: 3 } }
    ]
  },
  {
    text: '연애에서 나의 스타일은?',
    options: [
      { text: '솔직하게 감정을 표현한다', scores: { D: 2, C: 0, R: 0, P: 2 } },
      { text: '차근차근 신뢰를 쌓아간다', scores: { D: 0, C: 2, R: 2, P: 0 } },
      { text: '효율과 실리를 중시한다', scores: { D: 1, C: 1, R: 2, P: 0 } },
      { text: '감정과 설렘을 중시한다', scores: { D: 0, C: 0, R: 0, P: 2 } }
    ]
  },
  {
    text: '애매한 관계에서 나는?',
    options: [
      { text: '확실한 답을 원해 바로 묻는다', scores: { D: 3, C: 0, R: 1, P: 0 } },
      { text: '시간을 두고 상대 마음을 살핀다', scores: { D: 0, C: 3, R: 0, P: 1 } },
      { text: '관계의 실익을 따진다', scores: { D: 0, C: 1, R: 3, P: 0 } },
      { text: '감정의 흐름을 느끼며 기다린다', scores: { D: 0, C: 0, R: 0, P: 3 } }
    ]
  },
  {
    text: '연애 상대 선택 기준?',
    options: [
      { text: '호감이 가는 대로', scores: { D: 3, C: 0, R: 0, P: 1 } },
      { text: '검증된 신뢰감', scores: { D: 0, C: 3, R: 1, P: 0 } },
      { text: '현실적인 조건', scores: { D: 0, C: 0, R: 3, P: 0 } },
      { text: '감정적 호흡', scores: { D: 0, C: 0, R: 0, P: 3 } }
    ]
  },
  {
    text: '이성에게 호감 느낄 때?',
    options: [
      { text: '적극적으로 리드한다', scores: { D: 3, C: 0, R: 0, P: 0 } },
      { text: '내 마음부터 차근차근 정리한다', scores: { D: 0, C: 3, R: 1, P: 0 } },
      { text: '객관적으로 분석한다', scores: { D: 0, C: 1, R: 3, P: 0 } },
      { text: '감정적으로 빠져든다', scores: { D: 0, C: 0, R: 0, P: 3 } }
    ]
  },
  {
    text: '연애 중 갈등이 생기면?',
    options: [
      { text: '즉각 해결한다', scores: { D: 3, C: 0, R: 1, P: 0 } },
      { text: '시간 두고 서로의 감정을 살핀다', scores: { D: 0, C: 3, R: 0, P: 2 } },
      { text: '논리적 해결책을 찾는다', scores: { D: 1, C: 1, R: 3, P: 0 } },
      { text: '감정적으로 대화한다', scores: { D: 0, C: 0, R: 0, P: 3 } }
    ]
  },
  {
    text: '이상형을 생각할 때?',
    options: [
      { text: '명확한 스타일이 있는지', scores: { D: 3, C: 1, R: 0, P: 0 } },
      { text: '검증된 성격인지', scores: { D: 0, C: 3, R: 1, P: 0 } },
      { text: '조건 리스트를 먼저', scores: { D: 0, C: 0, R: 3, P: 0 } },
      { text: '느낌과 분위기', scores: { D: 0, C: 0, R: 0, P: 3 } }
    ]
  },
  {
    text: '새로운 사람에게 끌릴 때?',
    options: [
      { text: '바로 다가간다', scores: { D: 3, C: 0, R: 0, P: 1 } },
      { text: '신중하게 관찰한다', scores: { D: 0, C: 3, R: 1, P: 0 } },
      { text: '조건을 먼저 확인한다', scores: { D: 0, C: 0, R: 3, P: 0 } },
      { text: '감정적으로 반응한다', scores: { D: 0, C: 0, R: 0, P: 3 } }
    ]
  },
  {
    text: '연락 기다릴 때 나는?',
    options: [
      { text: '먼저 연락한다', scores: { D: 3, C: 0, R: 1, P: 0 } },
      { text: '기다리며 분석한다', scores: { D: 0, C: 3, R: 0, P: 0 } },
      { text: '다른 일 하며 유효시간 계산', scores: { D: 0, C: 0, R: 3, P: 0 } },
      { text: '감정적으로 설레거나 불안', scores: { D: 1, C: 0, R: 0, P: 3 } }
    ]
  },
  {
    text: '이별 후 나는?',
    options: [
      { text: '빨리 다음 사랑을 찾는다', scores: { D: 3, C: 0, R: 1, P: 0 } },
      { text: '깊은 회복 시간이 필요', scores: { D: 0, C: 3, R: 0, P: 1 } },
      { text: '교훈 도출 후 다음으로', scores: { D: 0, C: 1, R: 3, P: 0 } },
      { text: '감정적으로 힘들어한다', scores: { D: 0, C: 0, R: 0, P: 3 } }
    ]
  }
];

// ===== 테스트 1: 썸이냐? =====
const sumQuestionsByType = {
  D: [
    { text: '최근 일주일 연락 빈도는?', options: [{text: '매일', score: 10}, {text: '3~4회', score: 7}, {text: '1~2회', score: 4}, {text: '별로 없음', score: 0}] },
    { text: '상대가 먼저 만나자고 한 적이?', options: [{text: '자주', score: 10}, {text: '가끔', score: 7}, {text: '거의 없음', score: 4}, {text: '없음', score: 0}] },
    { text: '함께 있을 때 상대 표정은?', options: [{text: '밝고 즐거움', score: 10}, {text: '편안함', score: 7}, {text: '그냥 그럼', score: 4}, {text: '불편해 보임', score: 0}] },
    { text: '직접 만나자고 해본 적? (D 전용)', options: [{text: '확실하게 고백', score: 10}, {text: '솔직하게 표현', score: 7}, {text: '은근 슬쩍', score: 4}, {text: '아직 안 함', score: 0}] },
    { text: '상대 반응이 적극적이었나?', options: [{text: '매우 적극적', score: 10}, {text: '긍정적', score: 7}, {text: '애매함', score: 4}, {text: '피하는 듯', score: 0}] },
    { text: '다음 만남이 확정됐나?', options: [{text: '바로 잡음', score: 10}, {text: '긍정적', score: 7}, {text: '불확실', score: 4}, {text: '거부', score: 0}] }
  ],
  C: [
    { text: '최근 연락 패턴 분석 결과?', options: [{text: '규칙적이고 적극적', score: 10}, {text: '꾸준함', score: 7}, {text: '불규칙', score: 4}, {text: '드묾', score: 0}] },
    { text: '작은 제스처에서 느낀 바는?', options: [{text: '분명한 호감', score: 10}, {text: '관심 있음', score: 7}, {text: '보통', score: 4}, {text: '무관심', score: 0}] },
    { text: '시간 흐름에 따른 변화는?', options: [{text: '점점 가까워짐', score: 10}, {text: '유지됨', score: 7}, {text: '흐릿함', score: 4}, {text: '멀어짐', score: 0}] },
    { text: '친구들 사이 평판은? (C 전용)', options: [{text: '특별하다는 소문', score: 10}, {text: '좋아한다고 함', score: 7}, {text: '잘 어울린다', score: 4}, {text: '모르겠음', score: 0}] },
    { text: '확정적인 신호를 받았나?', options: [{text: '매우 확실함', score: 10}, {text: '그런 듯', score: 7}, {text: '불확실', score: 4}, {text: '없음', score: 0}] }
  ],
  R: [
    { text: '시간 대비 호감도는?', options: [{text: '매우 높음', score: 10}, {text: '높음', score: 7}, {text: '보통', score: 4}, {text: '낮음', score: 0}] },
    { text: '조건 일치 여부는?', options: [{text: '완벽', score: 10}, {text: '좋음', score: 7}, {text: '보통', score: 4}, {text: '별로', score: 0}] },
    { text: '효율성 판단 결과?', options: [{text: '매우 효율적', score: 10}, {text: '나쁘지 않음', score: 7}, {text: '보통', score: 4}, {text: '비효율적', score: 0}] },
    { text: '객관적 상황이 좋은가? (R 전용)', options: [{text: '완벽한 타이밍', score: 10}, {text: '좋은 상황', score: 7}, {text: '그냥 그럼', score: 4}, {text: '나쁨', score: 0}] },
    { text: '실익이 있는 관계인가?', options: [{text: '매우 있음', score: 10}, {text: '있음', score: 7}, {text: '보통', score: 4}, {text: '없음', score: 0}] }
  ],
  P: [
    { text: '함께 있을 때 감정은?', options: [{text: '매우 설렘', score: 10}, {text: '편안함', score: 7}, {text: '그냥 그럼', score: 4}, {text: '불편', score: 0}] },
    { text: '눈빛에 따뜻함이 느껴지나?', options: [{text: '매우 따뜻함', score: 10}, {text: '따뜻함', score: 7}, {text: '보통', score: 4}, {text: '차가움', score: 0}] },
    { text: '분위기 호흡감은?', options: [{text: '완벽함', score: 10}, {text: '좋음', score: 7}, {text: '보통', score: 4}, {text: '없음', score: 0}] },
    { text: '감정적 연결감이 있나? (P 전용)', options: [{text: '매우 깊음', score: 10}, {text: '있음', score: 7}, {text: '얕음', score: 4}, {text: '없음', score: 0}] },
    { text: '분위기가 타는 느낌인가?', options: [{text: '매우 그럼', score: 10}, {text: '그런 듯', score: 7}, {text: '보통', score: 4}, {text: '아님', score: 0}] }
  ]
};

// ===== 테스트 2: 나.. 얘 좋아하냐? =====
const selfQuestionsByType = {
  D: [
    { text: '자주 생각나는 정도는?', options: [{text: '계속 생각남', score: 10}, {text: '자주', score: 7}, {text: '가끔', score: 4}, {text: '잘 안 남', score: 0}] },
    { text: '행동으로 옮긴 적이?', options: [{text: '매우 많음', score: 10}, {text: '있음', score: 7}, {text: '조금', score: 4}, {text: '없음', score: 0}] },
    { text: '적극성 수준은?', options: [{text: '매우 높음', score: 10}, {text: '높음', score: 7}, {text: '보통', score: 4}, {text: '낮음', score: 0}] },
    { text: '결과와 무관하게 계속?', options: [{text: '매우 그럼', score: 10}, {text: '그런 편', score: 7}, {text: '보통', score: 4}, {text: '아님', score: 0}] },
    { text: '에너지를 얼마나 쓰는가?', options: [{text: '매우 많음', score: 10}, {text: '많음', score: 7}, {text: '보통', score: 4}, {text: '적음', score: 0}] }
  ],
  C: [
    { text: '확인된 신호들이?', options: [{text: '매우 많음', score: 10}, {text: '있음', score: 7}, {text: '조금', score: 4}, {text: '없음', score: 0}] },
    { text: '검증된 정보로 볼 때?', options: [{text: '확실한 호감', score: 10}, {text: '있는 듯', score: 7}, {text: '애매', score: 4}, {text: '아님', score: 0}] },
    { text: '시간 투자 대비 감정은?', options: [{text: '매우 큼', score: 10}, {text: '큼', score: 7}, {text: '보통', score: 4}, {text: '작음', score: 0}] },
    { text: '확신 정도는?', options: [{text: '매우 확실', score: 10}, {text: '확실', score: 7}, {text: '보통', score: 4}, {text: '없음', score: 0}] }
  ],
  R: [
    { text: '실익 분석 결과?', options: [{text: '매우 이득', score: 10}, {text: '이득', score: 7}, {text: '보통', score: 4}, {text: '손해', score: 0}] },
    { text: '조건 부합도는?', options: [{text: '완벽', score: 10}, {text: '좋음', score: 7}, {text: '보통', score: 4}, {text: '별로', score: 0}] },
    { text: '다른 대안과 비교?', options: [{text: '이게 최고', score: 10}, {text: '좋음', score: 7}, {text: '보통', score: 4}, {text: '따질 필요 없음', score: 0}] },
    { text: '효율성은?', options: [{text: '매우 높음', score: 10}, {text: '높음', score: 7}, {text: '보통', score: 4}, {text: '낮음', score: 0}] }
  ],
  P: [
    { text: '감정 기복이?', options: [{text: '매우 심함', score: 10}, {text: '심함', score: 7}, {text: '보통', score: 4}, {text: '없음', score: 0}] },
    { text: '분위기에 따라 마음이?', options: [{text: '매우 변함', score: 10}, {text: '변함', score: 7}, {text: '보통', score: 4}, {text: '안 변함', score: 0}] },
    { text: '직감적으로 확신?', options: [{text: '매우 확실', score: 10}, {text: '확실', score: 7}, {text: '보통', score: 4}, {text: '없음', score: 0}] },
    { text: '마음의 설렘은?', options: [{text: '매우 강함', score: 10}, {text: '강함', score: 7}, {text: '보통', score: 4}, {text: '약함', score: 0}] }
  ]
};

// ===== 테스트 3: 얘.. 나 좋아하냐? =====
const otherQuestionsByType = {
  D: [
    { text: '직접적인 표현이 있었나?', options: [{text: '매우 많음', score: 10}, {text: '있음', score: 7}, {text: '조금', score: 4}, {text: '없음', score: 0}] },
    { text: '적극적 접근 빈도는?', options: [{text: '매우 많음', score: 10}, {text: '많음', score: 7}, {text: '보통', score: 4}, {text: '적음', score: 0}] },
    { text: '확실한 호감 신호는?', options: [{text: '매우 분명', score: 10}, {text: '분명', score: 7}, {text: '애매', score: 4}, {text: '없음', score: 0}] },
    { text: '밀고 당김 패턴이?', options: [{text: '매우 뚜렷', score: 10}, {text: '뚜렷', score: 7}, {text: '보통', score: 4}, {text: '없음', score: 0}] },
    { text: '바로 고백할 듯한 느낌?', options: [{text: '매우 그럼', score: 10}, {text: '그런 듯', score: 7}, {text: '보통', score: 4}, {text: '아님', score: 0}] }
  ],
  C: [
    { text: '패턴 분석 결과?', options: [{text: '매우 일관적', score: 10}, {text: '일관적', score: 7}, {text: '보통', score: 4}, {text: '불일관적', score: 0}] },
    { text: '시간에 따른 변화?', options: [{text: '점점 좋아짐', score: 10}, {text: '유지됨', score: 7}, {text: '보통', score: 4}, {text: '나빠짐', score: 0}] },
    { text: '확정적인 신호는?', options: [{text: '받음', score: 10}, {text: '있는 듯', score: 7}, {text: '애매', score: 4}, {text: '없음', score: 0}] },
    { text: '친구들의 관찰 결과?', options: [{text: '확실하다고 함', score: 10}, {text: '있는 듯', score: 7}, {text: '모르겠다', score: 4}, {text: '아니라고 함', score: 0}] }
  ],
  R: [
    { text: '객관적 투자 정도?', options: [{text: '매우 많음', score: 10}, {text: '많음', score: 7}, {text: '보통', score: 4}, {text: '적음', score: 0}] },
    { text: '시간 대비 호감 비율?', options: [{text: '매우 높음', score: 10}, {text: '높음', score: 7}, {text: '보통', score: 4}, {text: '낮음', score: 0}] },
    { text: '조건적 접근인가?', options: [{text: '매우 그럼', score: 10}, {text: '그런 듯', score: 7}, {text: '보통', score: 4}, {text: '아님', score: 0}] },
    { text: '계산된 행동인가?', options: [{text: '매우 그럼', score: 10}, {text: '그런 듯', score: 7}, {text: '보통', score: 4}, {text: '아님', score: 0}] }
  ],
  P: [
    { text: '따뜻한 감정이 느껴지나?', options: [{text: '매우 느껴짐', score: 10}, {text: '느껴짐', score: 7}, {text: '보통', score: 4}, {text: '안 �껴짐', score: 0}] },
    { text: '눈빛에 정이 담겨있나?', options: [{text: '매우 담겨있음', score: 10}, {text: '담겨있음', score: 7}, {text: '보통', score: 4}, {text: '아님', score: 0}] },
    { text: '분위기가 타고 있나?', options: [{text: '매우 그럼', score: 10}, {text: '그런 듯', score: 7}, {text: '보통', score: 4}, {text: '아님', score: 0}] },
    { text: '감정적 접근인가?', options: [{text: '매우 그럼', score: 10}, {text: '그런 듯', score: 7}, {text: '보통', score: 4}, {text: '아님', score: 0}] }
  ]
};

// ===== 성향 결과 =====
const personalityTypes = {
  D: { name: '직진파', icon: '🔥', desc: '좋아하면 바로 표현하는 적극적인 연애 전사', keywords: ['적극적', '솔직함', '빠른 추진'] },
  C: { name: '신중파', icon: '🤔', desc: '깊이 관찰하고 신뢰를 쌓아가는 전략가', keywords: ['분석적', '관찰력', '깊은 관계'] },
  R: { name: '합리파', icon: '📊', desc: '논리와 현실을 중시하는 실리주의자', keywords: ['논리적', '현실적', '효율 중시'] },
  P: { name: '감성파', icon: '💭', desc: '감정과 분위기로 연애하는 감성 연예인', keywords: ['감정 중심', '분위기', '진정성'] }
};

// ===== Navigation =====
function showPage(id) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.getElementById(id).classList.add('active');
}

// ===== Phase 1: Landing =====
function startApp() {
  showPage('personality');
  state.personality.currentQ = 0;
  state.personality.scores = { D: 0, C: 0, R: 0, P: 0 };
  renderPersonalityQuestion();
}

function renderPersonalityQuestion() {
  const q = personalityQuestions[state.personality.currentQ];
  document.getElementById('p-question').textContent = `${state.personality.currentQ + 1}. ${q.text}`;
  document.getElementById('p-progress').textContent = `${state.personality.currentQ + 1}/10`;
  
  const container = document.getElementById('p-options');
  container.innerHTML = '';
  q.options.forEach((opt, i) => {
    const btn = document.createElement('button');
    btn.className = 'option-btn';
    btn.textContent = opt.text;
    btn.onclick = () => selectPersonalityOption(i);
    container.appendChild(btn);
  });
}

function selectPersonalityOption(index) {
  const q = personalityQuestions[state.personality.currentQ];
  const option = q.options[index];
  Object.entries(option.scores).forEach(([k, v]) => {
    state.personality.scores[k] += v;
  });
  
  state.personality.currentQ++;
  if (state.personality.currentQ >= personalityQuestions.length) {
    finishPersonalityTest();
  } else {
    renderPersonalityQuestion();
  }
}

function finishPersonalityTest() {
  const scores = state.personality.scores;
  let max = 'D';
  Object.entries(scores).forEach(([k, v]) => {
    if (v > scores[max]) max = k;
  });
  state.personality.type = max;
  
  const type = personalityTypes[max];
  document.getElementById('pr-icon').textContent = type.icon;
  document.getElementById('pr-name').textContent = type.name;
  document.getElementById('pr-desc').textContent = type.desc;
  document.getElementById('pr-keywords').textContent = type.keywords.join(' · ');
  
  showPage('personality-result');
}

// ===== Phase 2: Test Selection =====
function goToTestSelect() {
  showPage('test-select');
}

function selectTest(testType) {
  state.selectedTest = testType;
  state.testAnswers = [];
  state.testCurrentQ = 0;
  
  const questionsByType = {
    'sum': sumQuestionsByType,
    'self': selfQuestionsByType,
    'other': otherQuestionsByType
  };
  
  const questions = questionsByType[testType][state.personality.type];
  state.currentQuestions = questions;
  
  const titles = { sum: '썸이냐?', self: '나.. 얘 좋아하냐?', other: '얘.. 나 좋아하냐?' };
  document.getElementById('t-title').textContent = titles[testType];
  
  renderTestQuestion();
  showPage('test-page');
}

function renderTestQuestion() {
  const q = state.currentQuestions[state.testCurrentQ];
  document.getElementById('t-question').textContent = `${state.testCurrentQ + 1}. ${q.text}`;
  document.getElementById('t-progress').textContent = `${state.testCurrentQ + 1}/${state.currentQuestions.length}`;
  
  const container = document.getElementById('t-options');
  container.innerHTML = '';
  q.options.forEach((opt, i) => {
    const btn = document.createElement('button');
    btn.className = 'option-btn';
    btn.textContent = opt.text;
    btn.onclick = () => selectTestOption(i);
    container.appendChild(btn);
  });
}

function selectTestOption(index) {
  const q = state.currentQuestions[state.testCurrentQ];
  state.testAnswers.push({ text: q.text, score: q.options[index].score });
  
  state.testCurrentQ++;
  if (state.testCurrentQ >= state.currentQuestions.length) {
    finishTest();
  } else {
    renderTestQuestion();
  }
}

function finishTest() {
  const totalScore = state.testAnswers.reduce((sum, a) => sum + a.score, 0);
  const maxScore = state.currentQuestions.length * 10;
  const percentage = Math.round((totalScore / maxScore) * 100);
  
  const resultText = getTestResult(state.selectedTest, percentage);
  
  document.getElementById('result-percentage').textContent = `${percentage}%`;
  document.getElementById('result-level').textContent = resultText.level;
  document.getElementById('result-desc').textContent = resultText.desc;
  
  showPage('result');
}

function getTestResult(testType, percentage) {
  const levels = {
    sum: { high: '썸 확실 💕', mid: '썸 가능성 있음 💫', low: '아직 썸 아님 💭' },
    self: { high: '좋아하고 있어 😊', mid: '호감 있는 듯 🤔', low: '친구 정도 💭' },
    other: { high: '당신을 좋아해 💕', mid: '관심 있는 듯 👀', low: '아직 모르겠어 💭' }
  };
  
  const t = testType;
  if (percentage >= 70) return { level: levels[t].high, desc: '확신할 수 있는 신호들이 많아요!' };
  if (percentage >= 40) return { level: levels[t].mid, desc: '좋은 신호가 보이지만 아직은 애매해요.' };
  return { level: levels[t].low, desc: '아직은 친구 사이에 가까워 보여요.' };
}

// ===== Restart =====
function restart() {
  state.currentPhase = 'landing';
  state.personality = { scores: { D: 0, C: 0, R: 0, P: 0 }, type: null, currentQ: 0 };
  state.selectedTest = null;
  state.testAnswers = [];
  state.testCurrentQ = 0;
  showPage('landing');
}

// ===== Expose to Global =====
window.startApp = startApp;
window.selectTest = selectTest;
window.goToTestSelect = goToTestSelect;
window.restart = restart;

console.log('[SomeThing v3] Loaded');
