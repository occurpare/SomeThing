// ========== SomeThing - 연애 성향 & 썸 판별 테스트 ==========
// 새로운 워크플로우 (Rebuild: New workflow)

// ========== 상태 관리 ==========
const state = {
    personality: {
        type: null,
        scores: { D: 0, C: 0, R: 0, P: 0 }
    },
    currentTest: null,
    currentQuestion: 0,
    answers: [],
    testScore: 0
};

// ========== 연애 성향 테스트 (10문항) ==========
const personalityQuestions = [
    {
        id: 'p1',
        text: '좋아하는 사람이 생기면 나는?',
        options: [
            { text: '바로 고백한다! 시간 낭비는 싫어', weights: { D: 3, C: 0, R: 0, P: 1 } },
            { text: '먼저 다가가며 신호를 본다', weights: { D: 2, C: 0, R: 0, P: 2 } },
            { text: '조심스럽게 관찰하며 기회를 기다린다', weights: { D: 0, C: 3, R: 1, P: 0 } },
            { text: '상황을 분석하고 적절한 타이밍을 고민한다', weights: { D: 0, C: 1, R: 3, P: 0 } }
        ]
    },
    {
        id: 'p2',
        text: '연애에서 나의 스타일은?',
        options: [
            { text: '솔직하게 감정을 표현하는 편', weights: { D: 2, C: 0, R: 0, P: 2 } },
            { text: '상대의 마음을 먼저 살피는 편', weights: { D: 0, C: 2, R: 0, P: 1 } },
            { text: '논리적으로 접근하며 신중한 편', weights: { D: 0, C: 1, R: 3, P: 0 } },
            { text: '분위기와 감정에 따라 유동적인 편', weights: { D: 1, C: 0, R: 0, P: 3 } }
        ]
    },
    {
        id: 'p3',
        text: '애매한 관계에서 나는?',
        options: [
            { text: '확실히 정리하고 싶어 직접 묻는다', weights: { D: 3, C: 0, R: 1, P: 0 } },
            { text: '조금 더 지켜본 뒤 신중하게 판단한다', weights: { D: 0, C: 3, R: 1, P: 0 } },
            { text: '장단점을 분석하며 현실적으로 판단한다', weights: { D: 0, C: 0, R: 3, P: 0 } },
            { text: '흐름을 느끼며 자연스럽게 두고 본다', weights: { D: 0, C: 0, R: 0, P: 3 } }
        ]
    },
    {
        id: 'p4',
        text: '연애 상대 선택 시 가장 중요한 것은?',
        options: [
            { text: '솔직함과 호감의 확신', weights: { D: 3, C: 0, R: 0, P: 1 } },
            { text: '진심과 신뢰할 수 있는 느낌', weights: { D: 0, C: 3, R: 1, P: 1 } },
            { text: '현실적 조건과 안정성', weights: { D: 0, C: 0, R: 3, P: 0 } },
            { text: '감정적 연결과 설렘', weights: { D: 1, C: 0, R: 0, P: 3 } }
        ]
    },
    {
        id: 'p5',
        text: '이성에게 호감을 느낄 때 나는?',
        options: [
            { text: '적극적으로 다가가며 표현한다', weights: { D: 3, C: 0, R: 0, P: 0 } },
            { text: '신중하게 관찰하며 신호를 기다린다', weights: { D: 0, C: 3, R: 1, P: 0 } },
            { text: '조건과 상황을 먼저 분석한다', weights: { D: 0, C: 1, R: 3, P: 0 } },
            { text: '감정을 따라 자연스럽게 행동한다', weights: { D: 1, C: 0, R: 0, P: 3 } }
        ]
    },
    {
        id: 'p6',
        text: '연애 중 갈등이 생기면?',
        options: [
            { text: '바로 터놓고 대화하며 해결한다', weights: { D: 3, C: 0, R: 0, P: 1 } },
            { text: '시간을 두고 차분히 해결책을 찾는다', weights: { D: 0, C: 3, R: 1, P: 0 } },
            { text: '논리적으로 접근하며 원인을 분석한다', weights: { D: 0, C: 0, R: 3, P: 0 } },
            { text: '서로의 감정을 중시하며 공감한다', weights: { D: 0, C: 1, R: 0, P: 3 } }
        ]
    },
    {
        id: 'p7',
        text: '이상형을 생각할 때?',
        options: [
            { text: '적극적이고 솔직한 사람이 좋다', weights: { D: 3, C: 0, R: 0, P: 0 } },
            { text: '신중하고 배려 깊은 사람이 좋다', weights: { D: 0, C: 3, R: 0, P: 1 } },
            { text: '현실적이고 안정적인 사람이 좋다', weights: { D: 0, C: 0, R: 3, P: 0 } },
            { text: '감성적이고 로맨틱한 사람이 좋다', weights: { D: 0, C: 0, R: 0, P: 3 } }
        ]
    },
    {
        id: 'p8',
        text: '새로운 사람에게 끌릴 때?',
        options: [
            { text: '호기심을 참지 못하고 바로 다가간다', weights: { D: 3, C: 0, R: 0, P: 1 } },
            { text: '조심스럽게 관찰하며 다가간다', weights: { D: 0, C: 3, R: 1, P: 0 } },
            { text: '신뢰할 수 있는지 먼저 판단한다', weights: { D: 0, C: 1, R: 3, P: 0 } },
            { text: '느낌이 오면 마음대로 다가간다', weights: { D: 1, C: 0, R: 0, P: 3 } }
        ]
    },
    {
        id: 'p9',
        text: '연락할 때 나는?',
        options: [
            { text: '먼저 연락하는 편, 답장도 빠르게 보낸다', weights: { D: 3, C: 0, R: 0, P: 1 } },
            { text: '상대가 연락할 때까지 기다리는 편', weights: { D: 0, C: 3, R: 1, P: 0 } },
            { text: '상황에 따라 효율적으로 연락한다', weights: { D: 0, C: 1, R: 3, P: 0 } },
            { text: '느낌이 있을 때 연락하는 편', weights: { D: 1, C: 0, R: 0, P: 3 } }
        ]
    },
    {
        id: 'p10',
        text: '연애의 목적은?',
        options: [
            { text: '서로를 향한 확신과 진심을 나누는 것', weights: { D: 3, C: 0, R: 0, P: 1 } },
            { text: '신뢰를 쌓으며 안정적으로 가는 것', weights: { D: 0, C: 3, R: 2, P: 0 } },
            { text: '함께 성장하며 장기적인 관계를 만드는 것', weights: { D: 0, C: 0, R: 3, P: 0 } },
            { text: '설렘과 감정을 공유하며 즐기는 것', weights: { D: 0, C: 0, R: 0, P: 3 } }
        ]
    }
];

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

// ========== 썸 테스트 (성향별 질문) ==========
const sumQuestions = {
    D: [
        { text: '상대방이 나에게 직접적인 호감 표현을 하나요?', score: 10 },
        { text: '연락을 주로 먼저 시작하는 편인가요?', score: 10 },
        { text: '둘만의 시간을 자주 만들려고 하나요?', score: 10 },
        { text: '미래에 대한 이야기를 자연스럽게 하나요?', score: 10 },
        { text: '내 감정에 대해 솔직하게 이야기하나요?', score: 10 },
        { text: '주변에 나를 특별한 사람이라고 소개하나요?', score: 10 },
        { text: '약속을 취소할 때 미안해하며 대안을 제시하나요?', score: 8 },
        { text: '내 의견을 존중하며 적극적으로 경청하나요?', score: 8 },
        { text: '나의 일상과 사소한 것들에 관심을 보이나요?', score: 8 },
        { text: '함께 있을 때 시선을 자주 보내고 미소 짓나요?', score: 8 },
        { text: '내가 어려울 때 먼저 도움을 제안하나요?', score: 8 },
        { text: '연락 빈도가 최근에 늘어난 것 같나요?', score: 8 }
    ],
    C: [
        { text: '상대방이 나를 특별히 배려해주는 모습이 있나요?', score: 10 },
        { text: '나의 작은 변화(머리, 옷 등)를 알아차리나요?', score: 10 },
        { text: '나의 이야기를 기억하고 나중에 꺼내나요?', score: 10 },
        { text: '함께 있을 때 편안한 분위기를 만들어주나요?', score: 10 },
        { text: '나의 취향이나 취미를 함께 즐기려고 하나요?', score: 10 },
        { text: '내가 힘들 때 조용히 옆에 있어주려고 하나요?', score: 10 },
        { text: '연락이 끊겨도 다시 자연스럽게 이어가나요?', score: 8 },
        { text: '함께 있을 때 핸드폰을 멀리 두고 집중하나요?', score: 8 },
        { text: '내가 추천하는 것을 진심으로 들어보려 하나요?', score: 8 },
        { text: '약속 시간을 잘 지키며 배려하는 태도를 보이나요?', score: 8 },
        { text: '나에 대해 꾸준히 알아가려는 모습이 있나요?', score: 8 },
        { text: '함께 있을 때 눈맞춤이 자연스럽나요?', score: 8 }
    ],
    R: [
        { text: '상대방이 실질적으로 신뢰할 수 있는 사람인가요?', score: 10 },
        { text: '서로의 가치관이 비슷한 것 같나요?', score: 10 },
        { text: '미래 계획을 현실적으로 함께 이야기하나요?', score: 10 },
        { text: '연락 패턴이 안정적이고 일정한가요?', score: 10 },
        { text: '서로의 장단점을 객관적으로 인정하나요?', score: 10 },
        { text: '갈등이 생겨도 논리적으로 대화하려고 하나요?', score: 10 },
        { text: '내가 중요하다고 생각하는 것을 존중하나요?', score: 8 },
        { text: '약속을 중요하게 생각하며 지키려고 노력하나요?', score: 8 },
        { text: '함께 있을 때 효율적이고 의미있는 시간을 보내나요?', score: 8 },
        { text: '서로 성장할 수 있는 관계라고 느끼나요?', score: 8 },
        { text: '내 의견을 존중하며 반박 없이 듣나요?', score: 8 },
        { text: '관계를 위해 실질적인 노력을 하는 모습이 있나요?', score: 8 }
    ],
    P: [
        { text: '상대방이 나에게 특별한 감정을 표현하나요?', score: 10 },
        { text: '함께 있을 때 설레거나 행복한가요?', score: 10 },
        { text: '감정적인 대화를 나누고 싶어하나요?', score: 10 },
        { text: '분위기 있게 데이트를 준비해오나요?', score: 10 },
        { text: '서로의 감정을 솔직하게 나누나요?', score: 10 },
        { text: '나에 대한 시적이거나 감미로운 표현을 하나요?', score: 10 },
        { text: '함께 있을 때 시간이 빨리 가는 것 같나요?', score: 8 },
        { text: '내가 좋아하는 것을 서프라이즈로 준비해오나요?', score: 8 },
        { text: '이별 후 다시 연락이 오면 설레나요?', score: 8 },
        { text: '작은 일에도 함께 웃을 수 있나요?', score: 8 },
        { text: '연락할 때 따뜻하고 애정 어린 표현이 있나요?', score: 8 },
        { text: '함께 있을 때 세상에 둘만 있는 것 같나요?', score: 8 }
    ]
};

// ========== 내 마음 테스트 (성향별 질문) ==========
const selfQuestions = {
    D: [
        { text: '이 사람에게 적극적으로 다가가고 싶나요?', score: 10 },
        { text: '좋아하는 마음을 바로 표현하고 싶나요?', score: 10 },
        { text: '이 사람과 확실한 관계를 원하나요?', score: 10 },
        { text: '시간 낭비보다 바로 결과를 알고 싶나요?', score: 10 },
        { text: '질투가 날 정도로 이 사람이 특별한가요?', score: 10 },
        { text: '내 감정을 참기보다 표현하고 싶나요?', score: 10 },
        { text: '이 사람이 연락 없으면 답답한가요?', score: 8 },
        { text: '다른 사람에게 관심이 전혀 가지 않나요?', score: 8 },
        { text: '미래를 함께 상상해 본 적이 있나요?', score: 8 },
        { text: '이 사람에게 헌신하고 싶은 마음이 있나요?', score: 8 }
    ],
    C: [
        { text: '이 사람과 천천히 관계를 쌓아가고 싶나요?', score: 10 },
        { text: '상대의 진심을 확인하고 싶은가요?', score: 10 },
        { text: '확신이 들 때까지 기다릴 의향이 있나요?', score: 10 },
        { text: '이 사람을 신중하게 판단하고 싶나요?', score: 10 },
        { text: '만약 사귀면 오래 갈 것 같나요?', score: 10 },
        { text: '상대의 성격과 가치관을 배우고 싶나요?', score: 10 },
        { text: '서로를 이해하는 시간이 필요하다고 느끼나요?', score: 8 },
        { text: '조바심보다는 차분한 마음이 큰가요?', score: 8 },
        { text: '상대의 배려에 마음이 움직이나요?', score: 8 },
        { text: '관계를 서두르고 싶지 않나요?', score: 8 }
    ],
    R: [
        { text: '이 사람과 현실적으로 잘 맞는다고 느끼나요?', score: 10 },
        { text: '신뢰할 수 있는 사람이라고 생각하나요?', score: 10 },
        { text: '장기적인 관계로 발전할 수 있을 것 같나요?', score: 10 },
        { text: '가치관이나 생활 방식이 비슷하다고 느끼나요?', score: 10 },
        { text: '논리적으로 좋은 선택이라고 판단하나요?', score: 10 },
        { text: '함께 성장할 수 있는 사람인가요?', score: 10 },
        { text: '감정뿐 아니라 조건도 괜찮다고 보나요?', score: 8 },
        { text: '문제를 현실적으로 해결할 수 있을 것 같나요?', score: 8 },
        { text: '주변 사람들도 이 사람을 긍정적으로 보나요?', score: 8 },
        { text: '객관적으로 봐도 매력적인 사람인가요?', score: 8 }
    ],
    P: [
        { text: '이 사람이 없으면 허전한가요?', score: 10 },
        { text: '함께 있을 때 설레고 행복한가요?', score: 10 },
        { text: '감정이 가는 대로 하고 싶은가요?', score: 10 },
        { text: '로맨틱한 상상을 자주 하나요?', score: 10 },
        { text: '이 사람의 표정이나 행동에 민감한가요?', score: 10 },
        { text: '감정적인 연결이 느껴지나요?', score: 10 },
        { text: '이 사람이 특별하게 느껴지나요?', score: 8 },
        { text: '함께 있을 때 시간이 빨리 가나요?', score: 8 },
        { text: '이 사람에게 위로받고 싶은 마음이 있나요?', score: 8 },
        { text: '감정이 앞서서 판단이 흐려질 정도인가요?', score: 8 }
    ]
};

// ========== 상대 마음 테스트 (성향별 질문) ==========
const otherQuestions = {
    D: [
        { text: '상대가 나에게 직접적으로 관심을 표현하나요?', score: 10 },
        { text: '연락을 먼저 오고 자주 하는 편인가요?', score: 10 },
        { text: '만나자고 적극적으로 제안하나요?', score: 10 },
        { text: '나에 대해 솔직한 질문을 많이 하나요?', score: 10 },
        { text: '내 주변 사람들에게도 적극적으로 다가가나요?', score: 10 },
        { text: '감정을 숨기지 않고 표현하는 편인가요?', score: 10 },
        { text: '내가 다른 이성과 있을 때 신경 쓰는 모습이 있나요?', score: 8 },
        { text: '만남 후 빠르게 다음 약속을 잡으려 하나요?', score: 8 },
        { text: '내 의견을 존중하며 적극적으로 따르려 하나요?', score: 8 },
        { text: '함께 있을 때 시선이 자주 마주치나요?', score: 8 }
    ],
    C: [
        { text: '상대가 작은 것까지 세심하게 챙겨주나요?', score: 10 },
        { text: '나의 이야기를 잘 기억하고 꺼내나요?', score: 10 },
        { text: '함께 있을 때 편안한 분위기를 만들어주나요?', score: 10 },
        { text: '나의 상황을 배려하며 기다려주나요?', score: 10 },
        { text: '천천히 신뢰를 쌓아가려는 모습이 있나요?', score: 10 },
        { text: '나의 감정을 존중하며 조심스럽게 대하나요?', score: 10 },
        { text: '약속을 소중하게 여기며 잘 지키나요?', score: 8 },
        { text: '내가 힘들 때 조용히 옆을 지켜주나요?', score: 8 },
        { text: '나의 장단점을 모두 받아들이려 하나요?', score: 8 },
        { text: '깊이 있는 대화를 나누려고 하나요?', score: 8 }
    ],
    R: [
        { text: '상대가 신뢰할 수 있는 사람처럼 보이나요?', score: 10 },
        { text: '가치관이나 미래관이 서로 비슷해 보이나요?', score: 10 },
        { text: '실질적으로 관계를 위해 노력하는 모습이 있나요?', score: 10 },
        { text: '갈등이 생겨도 논리적으로 대화하려 하나요?', score: 10 },
        { text: '우리 관계를 현실적으로 고민하는 모습이 있나요?', score: 10 },
        { text: '안정적인 관계를 원하는 것처럼 보이나요?', score: 10 },
        { text: '약속 시간이나 연락 패턴이 일정한가요?', score: 8 },
        { text: '내가 중요한 가치를 존중해주나요?', score: 8 },
        { text: '서로 성장할 수 있는 관계라고 느껴지나요?', score: 8 },
        { text: '객관적으로 봐도 나에게 잘해주나요?', score: 8 }
    ],
    P: [
        { text: '상대가 나에게 특별한 감정을 보이나요?', score: 10 },
        { text: '함께 있을 때 표정이 밝고 행복해 보이나요?', score: 10 },
        { text: '감정적인 대화를 좋아하는 것 같나요?', score: 10 },
        { text: '로맨틱한 분위기를 만들려고 하나요?', score: 10 },
        { text: '나에게 시적이거나 감미로운 표현을 하나요?', score: 10 },
        { text: '함께 있을 때 세상에 둘만 있는 것 같나요?', score: 10 },
        { text: '내 감정 변화에 민감하게 반응하나요?', score: 8 },
        { text: '작은 일에도 함께 웃고 즐기나요?', score: 8 },
        { text: '감정에 따라 연락 빈도가 변하나요?', score: 8 },
        { text: '서로에게 감정적으로 의지하려 하나요?', score: 8 }
    ]
};

// ========== 결과 레벨 정의 ==========
const resultLevels = [
    {
        min: 80,
        max: 100,
        name: '매우 높음',
        desc: '확실한 신호예요! 적극적으로 고민해볼 만한 관계입니다.',
        color: '#FF6B6B'
    },
    {
        min: 60,
        max: 79,
        name: '높은 편',
        desc: '좋은 가능성이 있어요. 조금 더 지켜보며 확인해보세요.',
        color: '#4ECDC4'
    },
    {
        min: 40,
        max: 59,
        name: '보통',
        desc: '애매한 상황이에요. 서로의 마음을 조금 더 알아가보세요.',
        color: '#FFD93D'
    },
    {
        min: 0,
        max: 39,
        name: '낮은 편',
        desc: '아직은 친구로 지내는 게 좋을 수도 있어요.',
        color: '#A8A8A8'
    }
];

// ========== 페이지 전환 ==========
function showPage(pageId) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    const targetPage = document.getElementById(pageId);
    if (targetPage) {
        targetPage.classList.add('active');
        window.scrollTo(0, 0);
    }
}

function goToLanding() {
    showPage('landing');
}

function goToPersonalityResult() {
    showPage('personality-result');
}

function goToTestSelect() {
    showPage('test-select');
}

// ========== 연애 성향 테스트 ==========
function startPersonalityTest() {
    state.personality.scores = { D: 0, C: 0, R: 0, P: 0 };
    state.currentQuestion = 0;
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
    
    q.options.forEach((opt, i) => {
        const btn = document.createElement('button');
        btn.className = 'btn btn-option';
        btn.textContent = opt.text;
        btn.onclick = () => handlePersonalityAnswer(index, i);
        optionsContainer.appendChild(btn);
    });
}

function handlePersonalityAnswer(questionIndex, optionIndex) {
    const question = personalityQuestions[questionIndex];
    const option = question.options[optionIndex];
    
    // 가중치 계산
    Object.entries(option.weights).forEach(([type, weight]) => {
        state.personality.scores[type] += weight;
    });
    
    if (questionIndex + 1 >= personalityQuestions.length) {
        finishPersonalityTest();
    } else {
        showPersonalityQuestion(questionIndex + 1);
    }
}

function finishPersonalityTest() {
    const scores = state.personality.scores;
    const maxScore = Math.max(scores.D, scores.C, scores.R, scores.P);
    const type = Object.keys(scores).find(key => scores[key] === maxScore);
    state.personality.type = type;
    
    const pType = personalityTypes[type];
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
    
    showPage('personality-result');
}

// ========== 테스트 선택 및 진행 ==========
function startSumTest() {
    startTest('sum', sumQuestions[state.personality.type]);
}

function startSelfTest() {
    startTest('self', selfQuestions[state.personality.type]);
}

function startOtherTest() {
    startTest('other', otherQuestions[state.personality.type]);
}

function startTest(testType, questions) {
    state.currentTest = testType;
    state.currentQuestion = 0;
    state.answers = [];
    state.testScore = 0;
    
    document.getElementById(`${testType}-total`).textContent = questions.length;
    showTestQuestion(testType, questions, 0);
    showPage(`${testType}-test`);
}

function showTestQuestion(testType, questions, index) {
    const q = questions[index];
    document.getElementById(`${testType}-current`).textContent = index + 1;
    document.getElementById(`${testType}-question`).textContent = q.text;
    updateProgress(`${testType}-progress-fill`, index, questions.length);
    
    const optionsContainer = document.getElementById(`${testType}-options`);
    optionsContainer.innerHTML = '';
    
    const options = [
        { text: '그렇다 👍', score: q.score },
        { text: '보통이다 😐', score: q.score * 0.5 },
        { text: '아니다 👎', score: 0 }
    ];
    
    options.forEach((opt, i) => {
        const btn = document.createElement('button');
        btn.className = 'btn btn-option';
        btn.textContent = opt.text;
        btn.onclick = () => handleTestAnswer(testType, questions, index, opt.score);
        optionsContainer.appendChild(btn);
    });
}

function handleTestAnswer(testType, questions, questionIndex, score) {
    state.answers.push(score);
    state.testScore += score;
    
    if (questionIndex + 1 >= questions.length) {
        finishTest(testType, questions.length);
    } else {
        showTestQuestion(testType, questions, questionIndex + 1);
    }
}

function finishTest(testType, totalQuestions) {
    const maxScore = totalQuestions * 10;
    const percentage = Math.round((state.testScore / maxScore) * 100);
    
    // 레벨 결정
    const level = resultLevels.find(l => percentage >= l.min && percentage <= l.max);
    
    document.getElementById('r-percentage').textContent = percentage;
    document.getElementById('r-percentage').style.color = level.color;
    
    const levelEl = document.getElementById('r-level');
    levelEl.textContent = level.name;
    levelEl.style.color = level.color;
    
    // 테스트 타입별 제목
    const testTypeNames = {
        'sum': '썸 테스트',
        'self': '내 마음 테스트',
        'other': '상대 마음 테스트'
    };
    document.getElementById('r-test-type').textContent = testTypeNames[testType] + ' 결과';
    document.getElementById('r-summary').textContent = level.desc;
    
    // 성향 정보
    const pType = personalityTypes[state.personality.type];
    document.getElementById('r-p-icon').textContent = pType.icon;
    document.getElementById('r-p-name').textContent = pType.label + ' (' + pType.name + ')';
    document.getElementById('r-p-advice').textContent = '💡 ' + pType.advice;
    
    showPage('result');
}

// ========== 재시작 ==========
function restartApp() {
    state.personality.type = null;
    state.personality.scores = { D: 0, C: 0, R: 0, P: 0 };
    state.currentTest = null;
    state.currentQuestion = 0;
    state.answers = [];
    state.testScore = 0;
    showPage('landing');
}
