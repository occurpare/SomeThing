// ========== SomeThing - 연애 성향 & 썸 판별 테스트 ==========
// 새로운 워크플로우 v2.0

// ========== 상태 관리 ==========
const state = {
    age: null,        // '10', '20e', '20m', '20l', '30'
    gender: null,     // 'M', 'F'
    personality: null, // 'D', 'C', 'R', 'P'
    testType: null,   // 'sum', 'self', 'other'
    currentQ: 0,
    answers: [],
    totalScore: 0
};

// ========== 데이터 저장소 ==========
let questionData = null;
let currentQuestions = [];

// ========== 유틸리티 함수 ==========
function shuffleArray(array) {
    const newArray = [...array];
    for (let i = newArray.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
    }
    return newArray;
}

// ========== 성향 타입 정의 ==========
const personalityTypes = {
    D: {
        name: 'Direzione',
        label: '직진파',
        icon: '🔥',
        desc: '좋아하면 바로 표현하고 애매한 관계를 싫어하는 당돌한 성향. 적극적이고 솔직해서 상대방에게 확신을 줄 수 있어요.',
        traits: ['솔직함', '적극적', '결단력', '충동적'],
        advice: '때로는 신중함도 필요해요. 상대의 속도를 존중하면 더 좋은 결과가 있을 거예요!'
    },
    C: {
        name: 'Cautious',
        label: '신중파',
        icon: '🤔',
        desc: '깊이 생각하고 관찰하며 확실한 신호를 기다리는 신중한 성향. 한 번 시작한 관계는 깊이 있게 가요.',
        traits: ['관찰력', '신중함', '배려심', '인내심'],
        advice: '너무 신중해서 기회를 놓치지 않도록 때로는 과감한 도전도 해보세요!'
    },
    R: {
        name: 'Rational',
        label: '합리파',
        icon: '📊',
        desc: '논리적으로 분석하고 상황/조건을 우선으로 고려하는 현실적인 성향. 안정적인 관계를 추구해요.',
        traits: ['분석력', '현실적', '계획적', '논리적'],
        advice: '논리도 중요하지만, 때로는 마음의 소리를 들어보는 것도 중요해요!'
    },
    P: {
        name: 'Passionate',
        label: '감성파',
        icon: '💭',
        desc: '감정이 풍부하고 순간의 분위기를 중시하는 감성적인 성향. 로맨틱하고 감각적인 연애를 해요.',
        traits: ['감수성', '분위기 메이커', '창의적', '로맨틱'],
        advice: '감정의 파도에 휩쓸리지 않고 현실도 조금 봐두면 더 좋아요!'
    }
};

// ========== 연애 성향 테스트 (10문항) ==========
const personalityQuestions = [
    {
        id: 'p1',
        text: '좋아하는 사람이 생기면 나는?',
        options: [
            { text: '바로 고백한다! 시간 낭비는 싫어', type: 'D' },
            { text: '조심스럽게 관찰하며 기회를 기다린다', type: 'C' },
            { text: '상황을 분석하고 적절한 타이밍을 고민한다', type: 'R' },
            { text: '흐름을 느끼며 자연스럽게 다가간다', type: 'P' }
        ]
    },
    {
        id: 'p2',
        text: '연애에서 나의 스타일은?',
        options: [
            { text: '솔직하게 감정을 표현하는 편', type: 'D' },
            { text: '상대의 마음을 먼저 살피는 편', type: 'C' },
            { text: '논리적으로 접근하며 신중한 편', type: 'R' },
            { text: '분위기와 감정에 따라 유동적인 편', type: 'P' }
        ]
    },
    {
        id: 'p3',
        text: '애매한 관계에서 나는?',
        options: [
            { text: '확실히 정리하고 싶어 직접 묻는다', type: 'D' },
            { text: '조금 더 지켜본 뒤 신중하게 판단한다', type: 'C' },
            { text: '장단점을 분석하며 현실적으로 판단한다', type: 'R' },
            { text: '흐름을 느끼며 자연스럽게 두고 본다', type: 'P' }
        ]
    },
    {
        id: 'p4',
        text: '연애 상대 선택 시 가장 중요한 것은?',
        options: [
            { text: '솔직함과 호감의 확신', type: 'D' },
            { text: '진심과 신뢰할 수 있는 느낌', type: 'C' },
            { text: '현실적 조건과 안정성', type: 'R' },
            { text: '감정적 연결과 설렘', type: 'P' }
        ]
    },
    {
        id: 'p5',
        text: '이성에게 호감을 느낄 때 나는?',
        options: [
            { text: '적극적으로 다가가며 표현한다', type: 'D' },
            { text: '신중하게 관찰하며 신호를 기다린다', type: 'C' },
            { text: '조건과 상황을 먼저 분석한다', type: 'R' },
            { text: '감정을 따라 자연스럽게 행동한다', type: 'P' }
        ]
    },
    {
        id: 'p6',
        text: '연애 중 갈등이 생기면?',
        options: [
            { text: '바로 터놓고 대화하며 해결한다', type: 'D' },
            { text: '시간을 두고 차분히 해결책을 찾는다', type: 'C' },
            { text: '논리적으로 접근하며 원인을 분석한다', type: 'R' },
            { text: '서로의 감정을 중시하며 공감한다', type: 'P' }
        ]
    },
    {
        id: 'p7',
        text: '이상형을 생각할 때?',
        options: [
            { text: '적극적이고 솔직한 사람이 좋다', type: 'D' },
            { text: '신중하고 배려 깊은 사람이 좋다', type: 'C' },
            { text: '현실적이고 안정적인 사람이 좋다', type: 'R' },
            { text: '감성적이고 로맨틱한 사람이 좋다', type: 'P' }
        ]
    },
    {
        id: 'p8',
        text: '새로운 사람에게 끌릴 때?',
        options: [
            { text: '호기심을 참지 못하고 바로 다가간다', type: 'D' },
            { text: '조심스럽게 관찰하며 다가간다', type: 'C' },
            { text: '신뢰할 수 있는지 먼저 판단한다', type: 'R' },
            { text: '느낌이 오면 마음대로 다가간다', type: 'P' }
        ]
    },
    {
        id: 'p9',
        text: '연락할 때 나는?',
        options: [
            { text: '먼저 연락하는 편, 답장도 빠르게 보낸다', type: 'D' },
            { text: '상대가 연락할 때까지 기다리는 편', type: 'C' },
            { text: '상황에 따라 효율적으로 연락한다', type: 'R' },
            { text: '느낌이 있을 때 연락하는 편', type: 'P' }
        ]
    },
    {
        id: 'p10',
        text: '연애의 목적은?',
        options: [
            { text: '서로를 향한 확신과 진심을 나누는 것', type: 'D' },
            { text: '신뢰를 쌓으며 안정적으로 가는 것', type: 'C' },
            { text: '함께 성장하며 장기적인 관계를 만드는 것', type: 'R' },
            { text: '설렘과 감정을 공유하며 즐기는 것', type: 'P' }
        ]
    }
];

// ========== 결과 레벨 정의 ==========
// ========== 결과 레벨 정의 (6단계 세분화) ==========
const resultLevels = {
    veryHigh: {
        min: 76,
        max: 100,
        name: '높음',
        desc: '매우 긍정적인 신호예요! 지금의 감정이 진짜라면 과감하게 나아가보세요.',
        advice: '이 감정을 소중히 여기세요. 상대에게도 진심을 표현해보는 건 어떨까요?',
        color: '#FF6B6B'
    },
    high: {
        min: 56,
        max: 75,
        name: '양호',
        desc: '꽤 좋은 신호예요. 상호작용이 잘 이루어지고 있어요.',
        advice: '지금의 흐름을 유지하며 서로를 더 알아가보세요!',
        color: '#FF8E8E'
    },
    medium: {
        min: 46,
        max: 55,
        name: '중간',
        desc: '양호한 가능성이 있어요. 조금 더 지켜보며 서로를 알아가보세요.',
        advice: '더 많은 대화를 나누며 관계를 깊게 만들어보세요.',
        color: '#4ECDC4'
    },
    lowMedium: {
        min: 31,
        max: 45,
        name: '약간 낮음',
        desc: '아직은 미지수예요. 친구로서 더 알아가는 시간이 필요해요.',
        advice: '서두르지 말고 자연스러운 만남을 이어가보세요.',
        color: '#95A5A6'
    },
    low: {
        min: 16,
        max: 30,
        name: '낮음',
        desc: '지금은 친구 느낌이 더 강해요. 서두르지 않는 게 좋겠어요.',
        advice: '편하게 지내면서 상대의 진심을 조금 더 지켜보세요.',
        color: '#BDC3C7'
    },
    veryLow: {
        min: 0,
        max: 15,
        name: '매우 낮음',
        desc: '아직은 친구로 지내는 게 좋을 수도 있어요. 서두르지 마세요.',
        advice: '지금은 인연이 아닐 수 있어요. 다른 기회를 기다려보세요.',
        color: '#A8A8A8'
    }
};

// ========== 연애 스타일 결과 유형 ==========
const styleTypes = {
    clingy: {
        name: '밀착형',
        icon: '🤗',
        desc: '서로 붙어있는 걸 좋아하는 스타일이에요. 연락도 자주하고 함께 보내는 시간이 많아요.',
        advice: '서로에 대한 애정이 크지만, 각자의 시간도 존중해주면 더 오래갈 수 있어요!'
    },
    independent: {
        name: '독립형',
        icon: '🦅',
        desc: '자유롭게 서로의 시간을 존중하는 스타일이에요. 신뢰를 기반으로 해요.',
        advice: '각자의 시간을 잘 지키는 만큼, 함께할 때 더 특별하게 만들어보세요!'
    },
    planned: {
        name: '계획형',
        icon: '📅',
        desc: '데이트를 미리 계획하고 체계적으로 진행하는 스타일이에요.',
        advice: '계획도 좋지만 때로는 즉흥적인 데이트도 즐겨보세요!'
    },
    spontaneous: {
        name: '자유형',
        icon: '🎈',
        desc: '즉흥적이고 유쾌한 데이트를 추구하는 스타일이에요.',
        advice: '즉흥적인 즐거움도 좋지만 중요한 약속은 꼭 지켜주세요!'
    },
    communicative: {
        name: '소통형',
        icon: '💬',
        desc: '대화를 중요하게 생각하고 서로의 마음을 털어놓는 스타일이에요.',
        advice: '좋은 대화가 관계를 깊게 만드는군요. 계속해서 서로를 알아가세요!'
    },
    supportive: {
        name: '서포트형',
        icon: '🤝',
        desc: '서로의 성장을 지지하고 응원해주는 스타일이에요.',
        advice: '서로를 지지하는 힘이 관계를 더 단단하게 만들어요!'
    }
};

// ========== 이상형 결과 유형 ==========
const idealTypes = {
    leader: {
        name: '리더형',
        icon: '👑',
        desc: '듬직하게 리드해주는 사람이 이상형이에요.',
        advice: '리드해주는 사람과 함께하면 든든할 거예요!'
    },
    supporter: {
        name: '서포터형',
        icon: '🌟',
        desc: '뒤에서 응원해주는 따뜻한 사람이 이상형이에요.',
        advice: '서로 지지하는 관계는 오래갈 수 있어요!'
    },
    companion: {
        name: '동반자형',
        icon: '🚶',
        desc: '함께 성장하는 평등한 관계를 원해요.',
        advice: '서로의 페이스를 존중하며 함께 가는 관계가 좋겠네요!'
    },
    funny: {
        name: '재미있는형',
        icon: '😄',
        desc: '유머감각 좋고 즐거운 사람이 이상형이에요.',
        advice: '웃음이 있는 관계는 스트레스도 덜할 거예요!'
    },
    sincere: {
        name: '성실형',
        icon: '💎',
        desc: '책임감 있고 신뢰할 수 있는 사람이 이상형이에요.',
        advice: '신뢰를 바탕으로 한 관계가 가장 중요하죠!'
    },
    empathetic: {
        name: '공감형',
        icon: '💝',
        desc: '마음을 잘 알아주고 공감해주는 사람이 이상형이에요.',
        advice: '마음이 통하는 사람과 함께하면 행복할 거예요!'
    }
};

// ========== 페이지 전환 ==========
function showPage(pageId) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    const targetPage = document.getElementById(pageId);
    if (targetPage) {
        targetPage.classList.add('active');
        window.scrollTo(0, 0);
    }
}

// ========== 앱 시작 ==========
function startApp() {
    // 상태 초기화
    state.age = null;
    state.gender = null;
    state.personality = null;
    state.testType = null;
    state.currentQ = 0;
    state.answers = [];
    state.totalScore = 0;
    showPage('age-select');
}

// ========== 나이 선택 ==========
function selectAge(age) {
    state.age = age;
    showPage('gender-select');
}

function goToAgeSelect() {
    showPage('age-select');
}

function goToLanding() {
    showPage('landing');
}

// ========== 성별 선택 ==========
function selectGender(gender) {
    state.gender = gender;
    startPersonalityTest();
}

function goToGenderSelect() {
    showPage('gender-select');
}

// ========== 연애 성향 테스트 ==========
function startPersonalityTest() {
    state.personality = null;
    state.currentQ = 0;
    document.getElementById('p-total').textContent = personalityQuestions.length;
    showPersonalityQuestion(0);
    showPage('personality');
}

function updateProgress(elementId, current, total) {
    const percentage = (current / total) * 100;
    document.getElementById(elementId).style.width = percentage + '%';
}

function showPersonalityQuestion(index) {
    const q = personalityQuestions[index];
    document.getElementById('p-current').textContent = index + 1;
    document.getElementById('p-question').textContent = q.text;
    updateProgress('p-progress-fill', index, personalityQuestions.length);
    
    const optionsContainer = document.getElementById('p-options');
    optionsContainer.innerHTML = '';
    
    q.options.forEach((opt) => {
        const btn = document.createElement('button');
        btn.className = 'btn btn-option';
        btn.textContent = opt.text;
        btn.onclick = () => handlePersonalityAnswer(index, opt.type);
        optionsContainer.appendChild(btn);
    });
}

function handlePersonalityAnswer(questionIndex, personalityType) {
    state.personality = personalityType;
    
    if (questionIndex + 1 >= personalityQuestions.length) {
        // 마지막 문항 - 결과 계산 및 표시
        finishPersonalityTest();
    } else {
        // 다음 문항
        showPersonalityQuestion(questionIndex + 1);
    }
}

function finishPersonalityTest() {
    const pType = personalityTypes[state.personality];
    document.getElementById('pr-icon').textContent = pType.icon;
    document.getElementById('pr-type-name').textContent = pType.label;
    document.getElementById('pr-type-desc').textContent = pType.desc;
    
    const traitsList = document.getElementById('pr-traits');
    traitsList.innerHTML = '';
    pType.traits.forEach(trait => {
        const li = document.createElement('li');
        li.textContent = trait;
        traitsList.appendChild(li);
    });
    
    // 조합 정보 표시
    const comboKey = getCombinationKey();
    const ageLabels = {
        '10': '10대',
        '20e': '20대 초반',
        '20m': '20대 중반',
        '20l': '20대 후반',
        '30': '30대 이상'
    };
    const genderLabels = { 'M': '남성', 'F': '여성' };
    document.getElementById('pr-combo').textContent = 
        `${ageLabels[state.age]} · ${genderLabels[state.gender]} · ${pType.label} (${comboKey})`;
    
    showPage('personality-result');
}

function goToPersonalityResult() {
    showPage('personality-result');
}

// ========== 조합 키 생성 ==========
function getCombinationKey() {
    // 데이터 파일의 조합 키 구조에 맞게 매핑
    // 10F_D, 20F_D, 20eF_R, 20mF_D, 20lF_D, 25F_C, 30M_R 등
    
    let ageCode = state.age;
    
    // 20대 세분화 매핑
    if (state.age === '20e') ageCode = '20e';
    else if (state.age === '20m') ageCode = '20m';
    else if (state.age === '20l') ageCode = '20l';
    
    return `${ageCode}${state.gender}_${state.personality}`;
}

// ========== 폴백 조합 키 생성 (데이터가 없을 경우) ==========
function getFallbackCombinationKey() {
    // v4 데이터에는 20e/20m/20l 세분화만 있음
    // 중간값인 20m(20대중반)으로 폴백
    return `20m${state.gender}_${state.personality}`;
}

// ========== 테스트 선택 ==========
function goToTestSelect() {
    showPage('test-select');
}

// ========== 테스트 시작 (JSON 데이터 로드) ==========
async function startTest(testType) {
    state.testType = testType;
    state.currentQ = 0;
    state.answers = [];
    state.totalScore = 0;
    
    // JSON 데이터 로드
    if (!questionData) {
        try {
            const response = await fetch('data/questions-v26.json?t=' + Date.now());
            questionData = await response.json();
        } catch (error) {
            console.error('데이터 로드 실패:', error);
            alert('질문 데이터를 불러오는데 실패했습니다. 다시 시도해주세요.');
            return;
        }
    }

    // 조합 키 생성
    const comboKey = getCombinationKey();
    
    // 해당 조합의 질문 로드 (없으면 폴백)
    let allQuestions = [];
    if (questionData.combinations[comboKey] && questionData.combinations[comboKey][testType]) {
        allQuestions = questionData.combinations[comboKey][testType];
    } else if (questionData.combinations[getFallbackCombinationKey()] && questionData.combinations[getFallbackCombinationKey()][testType]) {
        // 폴백: 기본 20대 조합 사용
        const fallbackKey = getFallbackCombinationKey();
        console.log('폴백 사용:', comboKey, '→', fallbackKey);
        allQuestions = questionData.combinations[fallbackKey][testType];
    } else {
        // 최종 폴백: 유효한 조합 찾기
        const availableKeys = Object.keys(questionData.combinations);
        const validKey = availableKeys.find(k => questionData.combinations[k][testType]);
        if (validKey) {
            console.log('최종 폴백 사용:', comboKey, '→', validKey);
            allQuestions = questionData.combinations[validKey][testType];
        } else {
            console.error('오류: 사용 가능한 테스트 데이터가 없습니다');
            alert('테스트 데이터를 불러올 수 없습니다. 다시 시도해주세요.');
            return;
        }
    }
    
    // 랜덤으로 20개 선택 (100개 중)
    currentQuestions = shuffleArray(allQuestions).slice(0, 20);
    
    // 테스트 제목 설정
    const testTitles = {
        'sum': '썸 테스트',
        'self': '내 마음 테스트',
        'other': '상대 마음 테스트',
        'style': '연애 스타일 테스트',
        'ideal': '이상형 테스트'
    };
    document.getElementById('tq-title').textContent = testTitles[testType];
    document.getElementById('tq-total').textContent = currentQuestions.length;
    
    showTestQuestion(0);
    showPage('test-question');
}

function showTestQuestion(index) {
    if (!currentQuestions || !Array.isArray(currentQuestions) || currentQuestions.length === 0) {
        console.error('오류: 질문 데이터가 없습니다');
        alert('테스트 데이터를 불러올 수 없습니다. 다시 시도해주세요.');
        showPage('test-select');
        return;
    }
    
    const q = currentQuestions[index];
    if (!q) {
        console.error('오류: 유효하지 않은 질문 인덱스:', index);
        finishTest();
        return;
    }
    
    document.getElementById('tq-current').textContent = index + 1;
    document.getElementById('tq-question').textContent = q.text;
    updateProgress('tq-progress-fill', index, currentQuestions.length);
    
    const optionsContainer = document.getElementById('tq-options');
    optionsContainer.innerHTML = '';
    
    if (!q.options || !Array.isArray(q.options)) {
        console.error('오류: 질문 옵션이 없습니다', q);
        return;
    }
    
    q.options.forEach((opt) => {
        const btn = document.createElement('button');
        btn.className = 'btn btn-option';
        btn.textContent = opt.text;
        btn.onclick = () => handleTestAnswer(index, opt.score);
        optionsContainer.appendChild(btn);
    });
}

function handleTestAnswer(questionIndex, score) {
    state.answers.push(score);
    state.totalScore += score;
    
    if (questionIndex + 1 >= currentQuestions.length) {
        finishTest();
    } else {
        showTestQuestion(questionIndex + 1);
    }
}

// ========== 테스트 결과 계산 ==========
function finishTest() {
    // style, ideal 테스트는 유형 결과로 표시
    if (state.testType === 'style' || state.testType === 'ideal') {
        finishTypeTest();
        return;
    }
    
    const maxScore = currentQuestions.length * 10;
    const percentage = Math.round((state.totalScore / maxScore) * 100);
    
    // 레벨 결정 (6단계)
    let level;
    if (percentage >= 76) {
        level = resultLevels.veryHigh;
    } else if (percentage >= 56) {
        level = resultLevels.high;
    } else if (percentage >= 46) {
        level = resultLevels.medium;
    } else if (percentage >= 31) {
        level = resultLevels.lowMedium;
    } else if (percentage >= 16) {
        level = resultLevels.low;
    } else {
        level = resultLevels.veryLow;
    }
    
    // 결과 표시
    const percentageEl = document.getElementById('r-percentage');
    percentageEl.textContent = percentage;
    percentageEl.style.color = level.color;
    percentageEl.style.display = 'block';
    
    const levelEl = document.getElementById('r-level');
    levelEl.textContent = level.name;
    levelEl.style.color = level.color;
    levelEl.style.display = 'block';
    levelEl.style.fontSize = '';
    levelEl.style.fontWeight = '';
    
    // 유형 결과 클래스 제거 (퍼센트 테스트는 기본 스타일)
    document.querySelector('#result .result-content').classList.remove('type-result');
    
    // 테스트 타입별 제목
    const testTypeNames = {
        'sum': '썸 테스트',
        'self': '내 마음 테스트',
        'other': '상대 마음 테스트',
        'style': '연애 스타일 테스트',
        'ideal': '이상형 테스트'
    };
    document.getElementById('r-test-type').textContent = testTypeNames[state.testType] + ' 결과';
    document.getElementById('r-summary').textContent = level.desc;
    
    // 성향 정보
    const pType = personalityTypes[state.personality];
    document.getElementById('r-p-icon').textContent = pType.icon;
    document.getElementById('r-p-name').textContent = `${pType.label} (${pType.name})`;
    
    // 조합 정보
    const comboKey = getCombinationKey();
    document.getElementById('r-combo').textContent = `조합: ${comboKey}`;
    document.getElementById('r-p-advice').textContent = '💡 ' + pType.advice;
    
    showPage('result');
}

// ========== 유형 테스트 결과 (style, ideal) ==========
function finishTypeTest() {
    const totalScore = state.totalScore;
    const maxScore = currentQuestions.length * 10;
    const percentage = Math.round((totalScore / maxScore) * 100);
    
    // 점수 구간에 따른 유형 결정
    let resultType;
    const types = state.testType === 'style' 
        ? ['clingy', 'independent', 'planned', 'spontaneous', 'communicative', 'supportive']
        : ['leader', 'supporter', 'companion', 'funny', 'sincere', 'empathetic'];
    
    // 점수 구간별 유형 매핑 (6구간)
    const typeIndex = Math.min(Math.floor(percentage / 17), 5); // 0-16, 17-33, 34-50, 51-67, 68-84, 85-100
    resultType = types[typeIndex];
    
    const typeData = state.testType === 'style' ? styleTypes[resultType] : idealTypes[resultType];
    
    // 퍼센트 숨기고 유형 표시
    const percentageEl = document.getElementById('r-percentage');
    percentageEl.style.display = 'none';
    
    const levelEl = document.getElementById('r-level');
    levelEl.textContent = typeData.name;
    levelEl.style.color = state.testType === 'style' ? '#FF6B6B' : '#9B59B6';
    levelEl.style.display = 'block';
    levelEl.style.fontSize = '32px';
    levelEl.style.fontWeight = '700';
    
    // 테스트 타입별 제목
    const testTypeNames = {
        'style': '연애 스타일 테스트',
        'ideal': '이상형 테스트'
    };
    document.getElementById('r-test-type').textContent = testTypeNames[state.testType] + ' 결과';
    document.getElementById('r-summary').textContent = typeData.desc;
    
    // 유형 결과 클래스 추가 (퍼센트 숨김)
    document.querySelector('#result .result-content').classList.add('type-result');
    
    // 성향 정보
    const pType = personalityTypes[state.personality];
    document.getElementById('r-p-icon').textContent = typeData.icon;
    document.getElementById('r-p-name').textContent = `${pType.label} (${pType.name})`;
    
    // 조합 정보
    const comboKey = getCombinationKey();
    document.getElementById('r-combo').textContent = `조합: ${comboKey}`;
    document.getElementById('r-p-advice').textContent = '💡 ' + typeData.advice;
    
    showPage('result');
}

// ========== 재시작 ==========
function restartApp() {
    state.age = null;
    state.gender = null;
    state.personality = null;
    state.testType = null;
    state.currentQ = 0;
    state.answers = [];
    state.totalScore = 0;
    questionData = null;
    currentQuestions = [];
    showPage('landing');
}
