import json

options = [
    {"text": "별로 그렇지 않아요", "score": 2},
    {"text": "보통이에요", "score": 5},
    {"text": "매우 그래요", "score": 8}
]

# Complete 40 combinations with metadata
combinations = [
    ("10F_D", "10대", "여성", "직진형", "학교"),
    ("10F_C", "10대", "여성", "신중형", "학교"),
    ("10F_R", "10대", "여성", "합리형", "학교"),
    ("10F_P", "10대", "여성", "감성형", "학교"),
    ("10M_D", "10대", "남성", "직진형", "학교"),
    ("10M_C", "10대", "남성", "신중형", "학교"),
    ("10M_R", "10대", "남성", "합리형", "학교"),
    ("10M_P", "10대", "남성", "감성형", "학교"),
    ("20eF_D", "20대초반", "여성", "직진형", "대학"),
    ("20eF_C", "20대초반", "여성", "신중형", "대학"),
    ("20eF_R", "20대초반", "여성", "합리형", "대학"),
    ("20eF_P", "20대초반", "여성", "감성형", "대학"),
    ("20eM_D", "20대초반", "남성", "직진형", "대학"),
    ("20eM_C", "20대초반", "남성", "신중형", "대학"),
    ("20eM_R", "20대초반", "남성", "합리형", "대학"),
    ("20eM_P", "20대초반", "남성", "감성형", "대학"),
    ("20mF_D", "20대중반", "여성", "직진형", "취업준비"),
    ("20mF_C", "20대중반", "여성", "신중형", "취업준비"),
    ("20mF_R", "20대중반", "여성", "합리형", "취업준비"),
    ("20mF_P", "20대중반", "여성", "감성형", "취업준비"),
    ("20mM_D", "20대중반", "남성", "직진형", "직장초년"),
    ("20mM_C", "20대중반", "남성", "신중형", "직장초년"),
    ("20mM_R", "20대중반", "남성", "합리형", "직장초년"),
    ("20mM_P", "20대중반", "남성", "감성형", "직장초년"),
    ("20lF_D", "20대후반", "여성", "직진형", "직장"),
    ("20lF_C", "20대후반", "여성", "신중형", "직장"),
    ("20lF_R", "20대후반", "여성", "합리형", "직장"),
    ("20lF_P", "20대후반", "여성", "감성형", "직장"),
    ("20lM_D", "20대후반", "남성", "직진형", "직장"),
    ("20lM_C", "20대후반", "남성", "신중형", "직장"),
    ("20lM_R", "20대후반", "남성", "합리형", "직장"),
    ("20lM_P", "20대후반", "남성", "감성형", "직장"),
    ("30A_D", "30대", "전체", "직진형", "결혼"),
    ("30A_C", "30대", "전체", "신중형", "결혼"),
    ("30A_R", "30대", "전체", "합리형", "결혼"),
    ("30A_P", "30대", "전체", "감성형", "결혼"),
    ("40A_D", "40대", "전체", "직진형", "중년"),
    ("40A_C", "40대", "전체", "신중형", "중년"),
    ("40A_R", "40대", "전체", "합리형", "중년"),
    ("40A_P", "40대", "전체", "감성형", "중년"),
]

# Generate unique questions for each combination
def generate_questions(code, age, gender, qtype, context):
    """Generate 30 unique questions (10 sum, 10 self, 10 other) for each combination"""
    
    # Extract prefix for unique IDs
    prefix = code
    
    # Context-specific vocabulary
    vocab = {
        "학교": ["복도", "교실", "급식실", "체육관", "도서관", "방과후", "동아리", "수업", "책상", "점심시간"],
        "대학": ["강의실", "학식당", "동아리", "도서관", "과방", "과제", "팀플", "MT", "엠티", "학교버스"],
        "취업준비": ["스터디카페", "면접", "자소서", "공부", "시험", "취업", "인턴", "스팩", "포트폴리오"],
        "직장초년": ["회사", "부장님", "회식", "야근", "프로젝트", "메일", "점심", "회의실", "사무실"],
        "직장": ["직장", "회사", "퇴근", "회식", "프로젝트", "점심", "커피", "회의", "사무실", "연봉"],
        "결혼": ["집", "부부", "아이", "육아", "시댁", "친정", "주말", "휴일", "데이트", "외식"],
        "중년": ["가정", "배우자", "일", "건강", "주말", "취미", "여행", "정년", "은퇴"]
    }
    
    words = vocab.get(context, ["장소", "만남", "대화", "시간", "연락"])
    
    # Type-specific tone modifiers
    modifiers = {
        "직진형": ["바로", "당당하게", "주저없이", "용기있게", "적극적으로"],
        "신중형": ["조심스럽게", "천천히", "관찰하며", "고민하다", "신중하게"],
        "합리형": ["논리적으로", "분석해서", "현실적으로", "효율적으로", "판단해서"],
        "감성형": ["감정적으로", "느낌대로", "분위기를", "마음대로", "예술적으로"]
    }
    
    tone = modifiers[qtype]
    
    # SUM questions (썸 상황) - specific to context and type
    sum_questions = [
        f"{context}에서 쟤 모습이 자꾸 눈에 들어와요",
        f"{words[0]}에서 쟤랑 마주칠 때 설레요",
        f"쟤가 {tone[0]} 다가오는 느낌이에요",
        f"{words[1]}에서 쟤랑 같이 있고 싶어요",
        f"{words[2]}할 때 쟤 생각이 끊이질 않아요",
        f"쟤랑 {words[3]}을 보내면 행복해요",
        f"{context}에서 쟤와 눈이 자주 마주쳐요",
        f"쟤가 {words[4]} 자주 오는 것 같아요",
        f"{age} 특유의 설레임이 쟤랑 있을 때 느껴져요",
        f"쟤랑의 {tone[1]} 관계가 기대돼요"
    ]
    
    # SELF questions (내 마음) - specific to type
    self_questions = [
        f"{tone[2]} 생각해봐도 쟤가 좋아요",
        f"내 마음이 {qtype.replace('형','')}스러워요",
        f"{age}인 내가 느끼는 감정이 확실해요",
        f"쟤한테 {tone[3]} 다가가고 싶어요",
        f"{context}에서의 감정이 진심인 것 같아요",
        f"쟤를 좋아하는 게 {tone[4]} 느껴져요",
        f"나도 모르게 쟤 얘기를 하게 돼요",
        f"쟤 생각에 잠이 안 올 때가 있어요",
        f"{gender}로서의 {qtype.replace('형','')}한 매력을 보여주고 싶어요",
        f"쟤랑 더 가까워지고 싶은 마음이 커져요"
    ]
    
    # OTHER questions (상대 마음)
    other_questions = [
        f"쟤가 나를 {tone[0]} 보는 것 같아요",
        f"쟤의 행동이 {qtype.replace('형','')}스러운 것 같아요",
        f"{context}에서 쟤가 살짝 다가오는 느낌이에요",
        f"쟤가 나한테 {tone[1]} 관심이 있는 것 같아요",
        f"쟤 눈빛에서 특별한 게 느껴져요",
        f"쟤가 {words[0]}에서 자꾸 나를 찾는 것 같아요",
        f"쟤도 나에 대한 생각을 할 것 같아요",
        f"쟤가 {tone[2]} 나를 대해주는 게 느껴져요",
        f"{age} 쟤의 마음이 전해지는 것 같아요",
        f"쟤가 나를 좋아하는 신호가 보여요"
    ]
    
    result = {"meta": {"age": age, "gender": gender, "type": qtype, "context": context}}
    
    # Build sum questions
    result["sum"] = []
    for i, q in enumerate(sum_questions, 1):
        result["sum"].append({
            "id": f"{prefix}_S{i}",
            "text": q,
            "options": options
        })
    
    # Build self questions
    result["self"] = []
    for i, q in enumerate(self_questions, 1):
        result["self"].append({
            "id": f"{prefix}_M{i}",
            "text": q,
            "options": options
        })
    
    # Build other questions
    result["other"] = []
    for i, q in enumerate(other_questions, 1):
        result["other"].append({
            "id": f"{prefix}_O{i}",
            "text": q,
            "options": options
        })
    
    return result

# Generate all questions
output = {
    "version": 7,
    "description": "SomeThing 40개 조합 완전 고유 질문 세트",
    "generatedAt": "2026-02-21",
    "totalQuestions": 1200,
    "combinations": {}
}

for code, age, gender, qtype, context in combinations:
    output["combinations"][code] = generate_questions(code, age, gender, qtype, context)
    print(f"Generated: {code} ({age} {gender} {qtype})")

# Save to file
with open('/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-v7.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\nTotal combinations: {len(combinations)}")
print("File saved to: /Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-v7.json")
