// ========== SomeThing - 연애 성향 & 썸 판별 테스트 ==========
// 통합 데이터 + 앱 로직

// ========== 상태 관리 ==========
const state = {
  profile: {
    gender: null,
    ageRange: null
  },
  personality: {
    type: null,
    scores: { D: 0, C: 0, R: 0, P: 0 }
  },
  sumTest: {
    answers: [],
    totalScore: 0,
    percentage: 0,
    level: null
  },
  subTest: {
    type: null,
    answers: [],
    currentQuestion: 0
  },
  currentPhase: 'landing', // landing, profile, personality, sum, result, subtest
  currentQuestion: 0
};

// ========== 연애 성향 테스트 (8문항) ==========
const personalityQuestions = [
  {
    id: 'p1',
    text: '좋아하는 사람이 생기면?',
    options: [
      { text: '바로 고백한다! 시간 낭비는 싫어', weights: { D: 3, C: 0, R: 1, P: 1 } },
      { text: '신중하게 관찰하며 기회를 기다린다', weights: { D: 0, C: 3, R: 1, P: 0 } }
    ]
  },
  {
    id: 'p2',
    text: '연애에서 나의 스타일은?',
    options: [
      { text: '솔직하게 감정을 표현하는 편', weights: { D: 2, C: 0, R: 0, P: 2 } },
      { text: '차근차근 신뢰를 쌓아가는 편', weights: { D: 0, C: 2, R: 2, P: 0 } }
    ]
  },
  {
    id: 'p3',
    text: '애매한 관계에서 나는?',
    options: [
      { text: '확실히 정리하고 싶어 직접 묻는다', weights: { D: 3, C: 1, R: 2, P: 0 } },
      { text: '상황을 지켜보며 흐름을 느낀다', weights: { D: 0, C: 1, R: 0, P: 3 } }
    ]
  },
  {
    id: 'p4',
    text: '연애 상대 선택 시 중요한 것은?',
    options: [
      { text: '현실적 조건과 안정성', weights: { D: 0, C: 1, R: 3, P: 0 } },
      { text: '감정적 연결과 설렘', weights: { D: 1, C: 0, R: 0, P: 3 } }
    ]
  },
  {
    id: 'p5',
    text: '이성에게 호감을 느낄 때 나는?',
    options: [
      { text: '먼저 적극적으로 다가간다', weights: { D: 3, C: 0, R: 0, P: 1 } },
      { text: '상대의 신호를 기다린다', weights: { D: 0, C: 3, R: 1, P: 0 } }
    ]
  },
  {
    id: 'p6',
    text: '연애 중 갈등이 생기면?',
    options: [
      { text: '바로 터놓고 대화하며 해결한다', weights: { D: 2, C: 0, R: 1, P: 1 } },
      { text: '시간을 두고 차분히 해결책을 찾는다', weights: { D: 0, C: 2, R: 2, P: 1 } }
    ]
  },
  {
    id: 'p7',
    text: '이상형을 생각할 때?',
    options: [
      { text: '구체적인 조건을 먼저 생각한다', weights: { D: 0, C: 1, R: 3, P: 0 } },
      { text: '느낌과 감정적인 연결을 중시한다', weights: { D: 1, C: 0, R: 0, P: 3 } }
    ]
  },
  {
    id: 'p8',
    text: '새로운 사람에게 끌릴 때?',
    options: [
      { text: '호기심을 참지 못하고 바로 친해지려 한다', weights: { D: 2, C: 0, R: 1, P: 2 } },
      { text: '조심스럽게 관찰하며 다가간다', weights: { D: 0, C: 3, R: 2, P: 0 } }
    ]
  }
];

// ========== 썸 판별 테스트 (20문항) ==========
const sumTestQuestions = [
  {
    id: 's1',
    text: '최근 1주일간 연락 빈도는?',
    options: [
      { text: '거의 없거나 한두 번', score: 0 },
      { text: '주 2-3회 정도', score: 4 },
      { text: '매일 또는 거의 매일', score: 7 },
      { text: '하루에도 여러 번', score: 10 }
    ]
  },
  {
    id: 's2',
    text: '상대방이 나에게 보이는 관심도는?',
    options: [
      { text: '별다른 관심이 없어 보임', score: 0 },
      { text: '가끔 눈길이 가는 정도', score: 4 },
      { text: '꽤 관심 있어 보이는 눈빛', score: 7 },
      { text: '뜨겁고 적극적인 관심', score: 10 }
    ]
  },
  {
    id: 's3',
    text: '함께 있을 때 상대방의 표정은?',
    options: [
      { text: '표정 변화가 크지 않음', score: 0 },
      { text: '가끔 웃음 짓는 정도', score: 4 },
      { text: '즐거워 보이는 표정', score: 7 },
      { text: '계속해서 밝고 행복해 보임', score: 10 }
    ]
  },
  {
    id: 's4',
    text: '미래에 대한 언급은?',
    options: [
      { text: '미래 이야기를 거의 안 함', score: 0 },
      { text: '먼 미래는 모르겠다는 뉘앙스', score: 4 },
      { text: '함께하고 싶은 미래를 가끔 언급', score: 7 },
      { text: '구체적인 미래 계획을 함께 이야기함', score: 10 }
    ]
  },
  {
    id: 's5',
    text: '서로를 주변에 소개하는 방식은?',
    options: [
      { text: '전혀 소개하지 않음', score: 0 },
      { text: '친구라고만 소개', score: 4 },
      { text: '특별한 사람이라는 뉘앙스', score: 7 },
      { text: '자랑스럽게, 특별하게 소개', score: 10 }
    ]
  },
  {
    id: 's6',
    text: '내 취향이나 취미를 기억해주나요?',
    options: [
      { text: '잘 기억하지 못함', score: 0 },
      { text: '가끔 기억해내는 정도', score: 4 },
      { text: '꽤 잘 기억하고 챙겨줌', score: 7 },
      { text: '세세한 것까지 다 기억함', score: 10 }
    ]
  },
  {
    id: 's7',
    text: '둘만의 시간을 갖는 빈도는?',
    options: [
      { text: '거의 없음 (단체 위주)', score: 0 },
      { text: '가끔 생김', score: 4 },
      { text: '자주 둘이 시간을 보냄', score: 7 },
      { text: '대부분 둘이 만남', score: 10 }
    ]
  },
  {
    id: 's8',
    text: '상대가 해주는 말 중 가장 많이 듣는 것은?',
    options: [
      { text: '예의 바른 인사말 정도', score: 0 },
      { text: '일상적인 대화', score: 4 },
      { text: '배려와 걱정이 담긴 말', score: 7 },
      { text: '달콤하고 애정 어린 표현', score: 10 }
    ]
  },
  {
    id: 's9',
    text: '내가 연락했을 때 상대방의 반응은?',
    options: [
      { text: '답장이 늦거나 짧음', score: 0 },
      { text: '보통 정도의 반응', score: 4 },
      { text: '반갑게 받아주고 대화 이어감', score: 7 },
      { text: '아주 기뻐하며 적극적으로 대화', score: 10 }
    ]
  },
  {
    id: 's10',
    text: '이 관계가 나에게 얼마나 중요한가요?',
    options: [
      { text: '별로 중요하지 않음', score: 0 },
      { text: '있으면 좋은 정도', score: 4 },
      { text: '꽤 중요한 관계', score: 7 },
      { text: '매우 중요하고 소중함', score: 10 }
    ]
  },
  {
    id: 's11',
    text: '경계선을 넘는 행동(스킨십 등)이?',
    options: [
      { text: '전혀 없음', score: 0 },
      { text: '우연히 겹치는 정도', score: 4 },
      { text: '자연스러운 스킨십 있음', score: 7 },
      { text: '자주 있고 둘 다 편함', score: 10 }
    ]
  },
  {
    id: 's12',
    text: '상대를 신뢰할 수 있는 수준은?',
    options: [
      { text: '잘 모르겠음', score: 0 },
      { text: '일부 정도는 신뢰', score: 4 },
      { text: '대부분 신뢰함', score: 7 },
      { text: '완전히 신뢰함', score: 10 }
    ]
  },
  {
    id: 's13',
    text: '주변 사람들에게 이 분을 언급하는 정도는?',
    options: [
      { text: '언급하지 않음', score: 0 },
      { text: '가끔 이야기함', score: 4 },
      { text: '자주 이야기함', score: 7 },
      { text: '항상 관심사이며 자주 언급', score: 10 }
    ]
  },
  {
    id: 's14',
    text: '서로에게 시간을 할애하는 정도는?',
    options: [
      { text: '바쁘다는 핑계로 피함', score: 0 },
      { text: '시간 되면 만남', score: 4 },
      { text: '시간을 만들어 만남', score: 7 },
      { text: '우선순위로 두고 시간 투자', score: 10 }
    ]
  },
  {
    id: 's15',
    text: '갈등이 생겼을 때 해결 방식은?',
    options: [
      { text: '피하거나 무시함', score: 0 },
      { text: '시간이 지나면 풀림', score: 4 },
      { text: '대화로 풀려고 함', score: 7 },
      { text: '적극적으로 소통하며 해결', score: 10 }
    ]
  },
  {
    id: 's16',
    text: '서로를 위하는 모습이 보이나요?',
    options: [
      { text: '거의 없음', score: 0 },
      { text: '가끔 생각날 때', score: 4 },
      { text: '자주 챙겨줌', score: 7 },
      { text: '항상 서로를 먼저 생각함', score: 10 }
    ]
  },
  {
    id: 's17',
    text: '대화할 때 주제의 깊이는?',
    options: [
      { text: '겉핥기식 대화', score: 0 },
      { text: '일상적인 이야기 위주', score: 4 },
      { text: '속마음도 가끔 나눔', score: 7 },
      { text: '깊은 대화, 비밀도 공유', score: 10 }
    ]
  },
  {
    id: 's18',
    text: '만남 후 연락은?',
    options: [
      { text: '연락이 없음', score: 0 },
      { text: '하루 정도 있다가 연락', score: 4 },
      { text: '얼마 안 가 연락 옴', score: 7 },
      { text: '헤어지자마자 연락 옴', score: 10 }
    ]
  },
  {
    id: 's19',
    text: '둘이 있을 때 태도는?',
    options: [
      { text: '딱딱하고 어색함', score: 0 },
      { text: '편안하지만 예의 차림', score: 4 },
      { text: '재미있고 즐거움', score: 7 },
      { text: '완전히 편하고 행복함', score: 10 }
    ]
  },
  {
    id: 's20',
    text: '이 관계를 어떻게 정의할 수 있나요?',
    options: [
      { text: '그냥 아는 사이', score: 0 },
      { text: '조금 친한 사이', score: 4 },
      { text: '특별한 사이일 수도', score: 7 },
      { text: '연애 직전 또는 연애 중', score: 10 }
    ]
  }
];

// ========== 성향 타입 정의 ==========
const personalityTypes = {
  D: {
    name: 'Direzione',
    label: '직진파',
    icon: '🔥',
    desc: '좋아하면 바로 표현하고 애매한 관계를 싫어하는 당돌한 성향',
    traits: ['솔직함', '적극적', '결단력', '충동적'],
    advice: '때로는 신중함도 필요해요. 상대의 속도를 존중하면 더 좋은 결과가 있을 거예요!'
  },
  C: {
    name: 'Cautious',
    label: '신중파',
    icon: '🤔',
    desc: '깊이 생각하고 관찰하며 확실한 신호를 기다리는 신중한 성향',
    traits: ['관찰력', '신중함', '배려심', '인내심'],
    advice: '너무 신중해서 기회를 놓치지 않도록 때로는 과감한 도전도 해보세요!'
  },
  R: {
    name: 'Rational',
    label: '합리파',
    icon: '📊',
    desc: '논리적으로 분석하고 상황/조건을 우선으로 고려하는 현실적인 성향',
    traits: ['분석력', '현실적', '계획적', '논리적'],
    advice: '논리도 중요하지만, 때로는 마음의 소리를 들어보는 것도 중요해요!'
  },
  P: {
    name: 'Passionate',
    label: '감성파',
    icon: '💭',
    desc: '감정이 풍부하고 순간의 분위기를 중시하는 감성적인 성향',
    traits: ['감수성', '분위기 메이커', '창의적', '로맨틱'],
    advice: '감정의 파도에 휩쓸리지 않고 현실도 조금 봐두면 더 좋아요!'
  }
};

// ========== 썸 결과 레벨 ==========
const sumResultLevels = [
  {
    min: 80,
    max: 100,
    name: '썸 진행중',
    icon: '💕',
    desc: '서로에게 진심이 느껴져요. 썸이 아니라 이미 연애의 시작일지도?',
    color: '#FF6B6B'
  },
  {
    min: 60,
    max: 79,
    name: '썸 가능성 있음',
    icon: '💫',
    desc: '뭔가 있는 것 같아요! 조금 더 다가가면 관계가 발전할 수 있어요.',
    color: '#4ECDC4'
  },
  {
    min: 40,
    max: 59,
    name: '애매한 사이',
    icon: '🤔',
    desc: '애매하네요... 서로의 마음을 확인해보는 시간이 필요해요.',
    color: '#FFD93D'
  },
  {
    min: 0,
    max: 39,
    name: '친구 수준',
    icon: '💭',
    desc: '아직은 친구 사이일 가능성이 높아요. 서로를 더 알아가봐요!',
    color: '#A8A8A8'
  }
];

// ========== 서브테스트 데이터 ==========
const subTests = [
  {
    id: 'does-he-like-me',
    title: '얘 나 좋아하나..?',
    emoji: '👀',
    desc: '상대방의 마음을 알아보는 테스트',
    questions: [
      { text: '나를 볼 때 눈빛이 특별한가요?', score: 'yes_no' },
      { text: '다른 이성과 있을 때 신경쓰이게 하나요?', score: 'yes_no' },
      { text: '제 사소한 변화(머리, 옷 등)를 알아채나요?', score: 'yes_no' },
      { text: '먼저 연락을 자주 하나요?', score: 'yes_no' },
      { text: '함께 있을 때 신체적 거리가 가까운가요?', score: 'yes_no' }
    ]
  },
  {
    id: 'do-i-like-him',
    title: '나 걔 좋아하나..?',
    emoji: '💘',
    desc: '내 마음을 알아보는 테스트',
    questions: [
      { text: '연락이 오면 마음이 설레나요?', score: 'yes_no' },
      { text: '하루에 한 번 이상 생각하나요?', score: 'yes_no' },
      { text: '함께하는 미래를 상상하나요?', score: 'yes_no' },
      { text: '다른 사람과 있을 때 질투가 나나요?', score: 'yes_no' },
      { text: '하고 싶은 말이 많지만 망설여지나요?', score: 'yes_no' }
    ]
  },
  {
    id: 'dating-well',
    title: '연애 잘하고 있을까?',
    emoji: '🌟',
    desc: '현재 연애 관계 진단',
    questions: [
      { text: '서로의 대화가 깊이 있나요?', score: 'yes_no' },
      { text: '갈등이 생겨도 건강하게 해결하나요?', score: 'yes_no' },
      { text: '상대를 신뢰할 수 있나요?', score: 'yes_no' },
      { text: '현재 연애에 만족하고 있나요?', score: 'yes_no' }
    ]
  },
  {
    id: 'ideal-type',
    title: '이상형 분석',
    emoji: '✨',
    desc: '나의 이상형을 찾아보세요',
    questions: [
      { text: '외모 vs 성격 중 더 중요한 것은?', options: ['외모', '성격'] },
      { text: '같은 취미 vs 다른 취미?', options: ['같은 취미', '다른 취미'] },
      { text: '활발한 사람 vs 조용한 사람?', options: ['활발한', '조용한'] },
      { text: '리드하는 사람 vs 따라주는 사람?', options: ['리드하는', '따라주는'] }
    ]
  },
  {
    id: 'compatibility',
    title: '궁합 테스트',
    emoji: '🔮',
    desc: '우리 둘의 궁합은?',
    questions: [
      { text: '가치관이 비슷하다고 느끼나요?', score: 'yes_no' },
      { text: '취미나 관심사가 겹치나요?', score: 'yes_no' },
      { text: '문제 해결 방식이 잘 맞나요?', score: 'yes_no' },
      { text: '미래 목표가 비슷한가요?', score: 'yes_no' }
    ]
  }
];

// ========== DOM 요소 캐싱 ==========
let currentPage = 'landing';

// ========== 페이지 전환 ==========
function showPage(pageId) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  const targetPage = document.getElementById(pageId);
  if (targetPage) {
    targetPage.classList.add('active');
    currentPage = pageId;
    window.scrollTo(0, 0);
  }
}

// ========== 랜딩 페이지 ==========
function initLanding() {
  document.getElementById('start-btn').addEventListener('click', () => {
    showPage('profile-page');
  });
}

// ========== 프로필 페이지 ==========
function initProfile() {
  // 성별 선택
  document.querySelectorAll('.btn-gender').forEach(btn => {
    btn.addEventListener('click', () => {
      const gender = btn.dataset.gender;
      state.profile.gender = gender;
      document.querySelectorAll('.btn-gender').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      checkProfileComplete();
    });
  });

  // 연령대 선택
  document.querySelectorAll('.btn-age').forEach(btn => {
    btn.addEventListener('click', () => {
      const age = btn.dataset.age;
      state.profile.ageRange = age;
      document.querySelectorAll('.btn-age').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      checkProfileComplete();
    });
  });
}

function checkProfileComplete() {
  const nextBtn = document.getElementById('profile-next-btn');
  if (state.profile.gender && state.profile.ageRange) {
    nextBtn.disabled = false;
    nextBtn.style.opacity = '1';
  }
}

document.getElementById('profile-next-btn')?.addEventListener('click', () => {
  if (state.profile.gender && state.profile.ageRange) {
    startPersonalityTest();
  }
});

// ========== 연애 성향 테스트 ==========
function startPersonalityTest() {
  state.currentPhase = 'personality';
  state.currentQuestion = 0;
  state.personality.scores = { D: 0, C: 0, R: 0, P: 0 };
  updateProgress('personality-progress', 0, personalityQuestions.length, '연애 성향 테스트');
  showQuestion('personality', 0);
  showPage('personality-page');
}

function updateProgress(elementId, current, total, title) {
  const el = document.getElementById(elementId);
  if (!el) return;
  const fill = el.querySelector('.progress-fill');
  const count = el.querySelector('.progress-count');
  const titleEl = el.querySelector('.progress-title');
  
  const percentage = (current / total) * 100;
  fill.style.width = percentage + '%';
  count.textContent = `${current}/${total}`;
  if (title) titleEl.textContent = title;
}

function showQuestion(type, index) {
  const questions = type === 'personality' ? personalityQuestions : sumTestQuestions;
  const containerId = type === 'personality' ? 'personality-questions' : 'sum-questions';
  const container = document.getElementById(containerId);
  
  if (index >= questions.length) {
    if (type === 'personality') {
      finishPersonalityTest();
    } else {
      finishSumTest();
    }
    return;
  }

  const q = questions[index];
  container.innerHTML = `
    <div class="question-text">
      <span class="question-number">Q${index + 1}</span>
      ${q.text}
    </div>
    <div class="options-container">
      ${q.options.map((opt, i) => `
        <button class="btn btn-option" data-index="${i}">
          ${opt.text}
        </button>
      `).join('')}
    </div>
  `;

  container.querySelectorAll('.btn-option').forEach(btn => {
    btn.addEventListener('click', () => {
      const optionIndex = parseInt(btn.dataset.index);
      handleAnswer(type, index, optionIndex);
    });
  });
}

function handleAnswer(type, questionIndex, optionIndex) {
  const questions = type === 'personality' ? personalityQuestions : sumTestQuestions;
  const question = questions[questionIndex];
  const option = question.options[optionIndex];

  if (type === 'personality') {
    // 성향 가중치 계산
    Object.entries(option.weights).forEach(([type, weight]) => {
      state.personality.scores[type] += weight;
    });
    
    updateProgress('personality-progress', questionIndex + 1, personalityQuestions.length);
    
    if (questionIndex + 1 >= personalityQuestions.length) {
      finishPersonalityTest();
    } else {
      state.currentQuestion = questionIndex + 1;
      setTimeout(() => showQuestion('personality', questionIndex + 1), 200);
    }
  } else {
    // 썸 테스트 점수
    state.sumTest.answers.push({
      questionId: question.id,
      score: option.score
    });
    state.sumTest.totalScore += option.score;
    
    updateProgress('sum-progress', questionIndex + 1, sumTestQuestions.length);
    
    if (questionIndex + 1 >= sumTestQuestions.length) {
      finishSumTest();
    } else {
      setTimeout(() => showQuestion('sum', questionIndex + 1), 200);
    }
  }
}

// ========== 성향 테스트 완료 ==========
function finishPersonalityTest() {
  const scores = state.personality.scores;
  const maxScore = Math.max(scores.D, scores.C, scores.R, scores.P);
  const type = Object.keys(scores).find(key => scores[key] === maxScore);
  state.personality.type = type;
  
  startSumTest();
}

// ========== 썸 테스트 ==========
function startSumTest() {
  state.currentPhase = 'sum';
  state.currentQuestion = 0;
  state.sumTest.answers = [];
  state.sumTest.totalScore = 0;
  
  updateProgress('sum-progress', 0, sumTestQuestions.length, '썸 판별 테스트');
  showQuestion('sum', 0);
  showPage('sum-page');
}

function finishSumTest() {
  const total = state.sumTest.totalScore;
  const max = sumTestQuestions.length * 10;
  state.sumTest.percentage = Math.round((total / max) * 100);
  
  // 레벨 결정
  state.sumTest.level = sumResultLevels.find(l => 
    state.sumTest.percentage >= l.min && state.sumTest.percentage <= l.max
  );
  
  showResult();
}

// ========== 결과 페이지 ==========
function showResult() {
  const personality = personalityTypes[state.personality.type];
  const level = state.sumTest.level;
  
  // 성향 결과 채우기
  const persSection = document.getElementById('result-personality');
  persSection.innerHTML = `
    <div class="personality-header">
      <div class="personality-icon">${personality.icon}</div>
      <div class="personality-info">
        <h3>${personality.label} (${personality.name})</h3>
        <p>${personality.traits.join(' · ')}</p>
      </div>
    </div>
    <p class="personality-desc">${personality.desc}</p>
    <p class="personality-desc" style="margin-top: 12px; color: #FF6B6B; font-weight: 500;">💡 ${personality.advice}</p>
  `;
  
  // 점수 및 레벨 채우기
  document.getElementById('result-score').textContent = state.sumTest.percentage + '%';
  
  const levelSection = document.getElementById('result-level');
  levelSection.innerHTML = `
    <div class="result-level-icon">${level.icon}</div>
    <div class="result-level-title" style="color: ${level.color}">${level.name}</div>
    <p class="result-level-desc">${level.desc}</p>
  `;
  
  // 서브테스트 추천 생성
  renderSubtests();
  
  // 버튼 이벤트
  document.getElementById('restart-btn').addEventListener('click', restart);
  document.getElementById('share-btn').addEventListener('click', shareResult);
  
  showPage('result-page');
}

function renderSubtests() {
  const container = document.getElementById('subtest-grid');
  container.innerHTML = subTests.map(test => `
    <div class="subtest-card" data-subtest="${test.id}">
      <span class="emoji">${test.emoji}</span>
      <h4>${test.title}</h4>
      <p>${test.desc}</p>
    </div>
  `).join('');
  
  container.querySelectorAll('.subtest-card').forEach(card => {
    card.addEventListener('click', () => {
      const testId = card.dataset.subtest;
      startSubtest(testId);
    });
  });
}

// ========== 서브테스트 ==========
function startSubtest(testId) {
  const test = subTests.find(t => t.id === testId);
  state.subTest.type = testId;
  state.subTest.currentQuestion = 0;
  state.subTest.answers = [];
  
  const container = document.getElementById('subtest-questions');
  document.getElementById('subtest-title').textContent = test.title;
  
  showSubtestQuestion(test, 0);
  showPage('subtest-detail-page');
}

function showSubtestQuestion(test, index) {
  const container = document.getElementById('subtest-questions');
  const q = test.questions[index];
  
  const progress = ((index + 1) / test.questions.length) * 100;
  
  container.innerHTML = `
    <div class="progress-container" style="margin: 0 0 24px 0; position: relative;">
      <div class="progress-header">
        <span class="progress-title">${test.title}</span>
        <span class="progress-count">${index + 1}/${test.questions.length}</span>
      </div>
      <div class="progress-bar">
        <div class="progress-fill" style="width: ${progress}%"></div>
      </div>
    </div>
    <div class="question-text" style="margin-bottom: 32px;">
      <span class="question-number">Q${index + 1}</span>
      ${q.text}
    </div>
    <div class="options-container">
      ${q.options ? 
        q.options.map((opt, i) => `<button class="btn btn-option subtest-opt" data-index="${i}">${opt}</button>`).join('') :
        `
        <button class="btn btn-option subtest-opt" data-score="1">네 👍</button>
        <button class="btn btn-option subtest-opt" data-score="0">아니요 👎</button>
        `
      }
    </div>
  `;
  
  container.querySelectorAll('.subtest-opt').forEach(btn => {
    btn.addEventListener('click', () => {
      if (btn.dataset.score) {
        state.subTest.answers.push(parseInt(btn.dataset.score));
      } else {
        state.subTest.answers.push(parseInt(btn.dataset.index) === 0 ? 1 : 0);
      }
      
      if (index + 1 >= test.questions.length) {
        finishSubtest(test);
      } else {
        showSubtestQuestion(test, index + 1);
      }
    });
  });
}

function finishSubtest(test) {
  const score = state.subTest.answers.reduce((a, b) => a + b, 0);
  const max = test.questions.length;
  const percentage = Math.round((score / max) * 100);
  
  const container = document.getElementById('subtest-questions');
  
  let resultMsg = '';
  if (percentage >= 80) resultMsg = '매우 높음! 💕';
  else if (percentage >= 60) resultMsg = '높은 편이에요 💫';
  else if (percentage >= 40) resultMsg = '중간 정도예요 🤔';
  else resultMsg = '낮은 편이네요 💭';
  
  container.innerHTML = `
    <div class="result-container animate-pop" style="padding: 40px 20px;">
      <div class="result-score" style="font-size: 56px;">${percentage}%</div>
      <p class="result-score-label">${test.title} 결과</p>
      <div class="result-level" style="margin-top: 24px;">
        <div class="result-level-title">${resultMsg}</div>
        <p class="result-level-desc">${test.questions.length}개 문항 중 ${score}개 긍정 응답</p>
      </div>
      <button class="btn btn-primary" id="subtest-back-btn" style="margin-top: 24px;">결과 페이지로 돌아가기</button>
    </div>
  `;
  
  document.getElementById('subtest-back-btn').addEventListener('click', () => {
    showPage('result-page');
  });
}

document.getElementById('subtest-back').addEventListener('click', () => {
  showPage('result-page');
});

// ========== 공유/재시작 ==========
function restart() {
  // 상태 초기화
  state.profile = { gender: null, ageRange: null };
  state.personality = { type: null, scores: { D: 0, C: 0, R: 0, P: 0 } };
  state.sumTest = { answers: [], totalScore: 0, percentage: 0, level: null };
  state.subTest = { type: null, answers: [], currentQuestion: 0 };
  
  // UI 초기화
  document.querySelectorAll('.btn-gender, .btn-age').forEach(b => b.classList.remove('selected'));
  document.getElementById('profile-next-btn').disabled = true;
  document.getElementById('profile-next-btn').style.opacity = '0.5';
  
  showPage('landing-page');
}

function shareResult() {
  const text = `썸 판별 결과: ${state.sumTest.percentage}% - ${state.sumTest.level?.name || ''}\n내 연애 성향: ${personalityTypes[state.personality.type]?.label || ''}`;
  
  if (navigator.share) {
    navigator.share({
      title: 'SomeThing - 썸 판별 테스트',
      text: text,
      url: window.location.href
    }).catch(() => {});
  } else {
    // 클립보드 복사
    navigator.clipboard.writeText(text + '\n' + window.location.href).then(() => {
      alert('결과가 클립보드에 복사되었어요!');
    });
  }
}

// ========== 초기화 ==========
document.addEventListener('DOMContentLoaded', () => {
  initLanding();
  initProfile();
  
  // 시작 페이지로
  showPage('landing-page');
});
