#!/usr/bin/env python3
"""
SomeThing Questions Generator - 1200 questions for 40 combinations
Age groups: 10, 20e, 20m, 20l, 30
Genders: F, M
Traits: D, C, R, P
Types: sum(10), self(10), other(10)
"""

import json
from typing import Dict, List

def create_questions() -> Dict[str, List[Dict]]:
    questions = {}
    
    # Define all age groups with their themes and question styles
    ages = {
        "10": {"theme": "첫사랑_학교", "context": "학교, 동아리, 급식실"},
        "20e": {"theme": "대학새내기", "context": "과팅, MT, 동아리"},
        "20m": {"theme": "현실고민", "context": "인턴, 과제, 미래"},
        "20l": {"theme": "진지한만남", "context": "취업, 독립, 결혼"},
        "30": {"theme": "성숙한연애", "context": "직장, 결혼, 가족"},
    }
    
    genders = ["F", "M"]
    traits = ["D", "C", "R", "P"]  # Direct, Cautious, Rational, Passionate
    
    # Trait-specific question patterns
    trait_patterns = {
        "D": {
            "sum": ["바로", "먼저", "당당하게", "확실히", "적극적으로"],
            "self": ["솔직하게", "당장", "자신 있게", "주저없이", "적극적으로"],
            "other": ["바로", "확신", "당연하게", "신호", "기회"],
        },
        "C": {
            "sum": ["천천히", "조심스럽게", "지켜보며", "확신이 들면", "자연스럽게"],
            "self": ["깊이", "조용히", "간직하며", "확신할 때까지", "느끼며"],
            "other": ["지켜보며", "살펴보고", "여러 번", "확인하고", "신중하게"],
        },
        "R": {
            "sum": ["분석해서", "장단점을", "논리적으로", "상황을 따져", "현실적으로"],
            "self": ["판단해서", "고려해보고", "결과를", "이득인지", "타이밍을"],
            "other": ["분석하며", "확률을", "의도를", "전략적으로", "계산해서"],
        },
        "P": {
            "sum": ["느껴지는 대로", "순간의", "설레며", "감정에", "로맨틱하게"],
            "self": ["온전히", "마법같이", "깊숙이", "따뜻하게", "감동하며"],
            "other": ["느껴지는", "진심이", "따뜻함이", "분위기", "감정이"],
        },
    }
    
    # Question templates by age group and type
    templates = {
        "10": {
            "sum": [
                "좋아하는 사람이 있으면 그 사람과 눈이 마주치면 {pattern} 다가가요",
                "호감 가는 사람과 같은 반이면 {pattern} 옆자리로 가서 앉아요",
                "썸이 생기면 {pattern} 연락을 시작해요",
                "학교 급식실에서 {pattern} 같이 먹자고 해요",
                "애인이 생기면 {pattern} SNS에 올리고 다녀요",
                "좋아하는 사람과 눈 마주치면 {pattern} 인사해요",
                "같은 동아리면 {pattern} 시간을 보내요",
                "상대가 고백하면 {pattern} 대답해요",
                "좋아하는 사람과 {pattern} 번호를 교환해요",
                "학교에서 {pattern} 대화를 시도해요",
            ],
            "self": [
                "설렘이 오면 {pattern} 마음을 즐겨요",
                "좋아하는 감정이 생기면 {pattern} 느껴요",
                "내 마음이 {pattern} 표현해요",
                "감정이 커지면 {pattern} 생각해요",
                "좋아하는 게 {pattern} 다가가요",
                "설레는 마음을 {pattern} 느껴요",
                "감정이 생기면 {pattern} 간직해요",
                "호감이 생기면 {pattern} 기뻐해요",
                "좋아하는 생각만 해도 {pattern} 미소 지어요",
                "처음 느껴보는 감정을 {pattern} 받아들여요",
            ],
            "other": [
                "상대가 나를 {pattern} 볼 때 마음을 읽어요",
                "상대의 눈빛에서 {pattern} 관심을 알아채요",
                "상대가 {pattern} 다가오면 신호라고 생각해요",
                "상대의 메시지를 {pattern} 확인하고 분석해요",
                "상대가 친구들에게 {pattern} 물어보면 의미있다고 봐요",
                "상대가 {pattern} 웃으면 호감이 있다고 알아요",
                "상대의 태도에서 {pattern} 진심을 알아차려요",
                "상대가 {pattern} 챙겨주면 마음이 있다고 믿어요",
                "상대의 반응을 {pattern} 살펴봐요",
                "상대가 나에게 {pattern} 시간을 쓰면 관심있다고 생각해요",
            ],
        },
        "20e": {
            "sum": [
                "같은 강의나 동아리에 있으면 {pattern} 옆자리로 가요",
                "호감 가는 사람에게 {pattern} 연락을 시작해요",
                "좋아하는 사람이 생기면 {pattern} 주변에 얘기해요",
                "썸 탈 때 {pattern} 만나자고 해요",
                "상대가 카톡 오면 {pattern} 답해요",
                "연애가 시작되면 {pattern} SNS에 올려요",
                "기분 좋을 때 {pattern} 표정에 드러내요",
                "좋아하면 {pattern} 다가가서 마음을 보여줘요",
                "시험기간에도 {pattern} 만나러 가요",
                "학교나 카페에서 {pattern} 말을 걸어요",
            ],
            "self": [
                "호감이 생기면 {pattern} 드러내서 티가 나요",
                "설레는 기분을 {pattern} 나누고 싶어져요",
                "좋아하는 생각이 {pattern} 매일 떠올라요",
                "이 감정이 {pattern} 맞는지 확신해요",
                "좋아하는 내 모습이 {pattern} 즐거워요",
                "감정의 진짜 의미를 {pattern} 즐겨요",
                "하루 종일 {pattern} 기분이 좋아져요",
                "감정이 생기면 {pattern} 표현하고 싶어요",
                "새로운 감정에 {pattern} 빠져들어요",
                "설렘이 오면 {pattern} 느껴져요",
            ],
            "other": [
                "상대가 {pattern} 물어보면 관심 있다고 생각해요",
                "상대가 바로 답장 오면 {pattern} 대화를 이어가요",
                "상대가 학교에서 {pattern} 웃으면 호감이 있다고 봐요",
                "상대가 친구들에게 {pattern} 언급하면 확신해요",
                "상대가 같이 밥 먹자고 하면 {pattern} 썸이라고 봐요",
                "상대가 카페에 {pattern} 응하면 진행중이에요",
                "상대가 내 일상에 {pattern} 관심 보이면 애틋하다고 봐요",
                "상대가 다른 사람이랑 {pattern} 웃어도 질투가 나요",
                "상대가 늦은 시간에 {pattern} 연락하면 특별하다고 느껴요",
                "상대가 SNS에 {pattern} 반응하면 신호라고 생각해요",
            ],
        },
        "20m": {
            "sum": [
                "같은 공간에 있으면 {pattern} 시간을 보내요",
                "호감이 생기면 {pattern} 연락을 취해요",
                "좋아하는 사람이 생기면 {pattern} 관계를 발전시켜요",
                "썸이 심화되면 {pattern} 만남을 가져요",
                "상대가 연락하면 {pattern} 답장해요",
                "연애가 깊어지면 {pattern} 서로를 소개해요",
                "계획이 생기면 {pattern} 얘기하고 조율해요",
                "좋아하면 {pattern} 다가가서 솔직하게 얘기해요",
                "바쁠 때도 {pattern} 시간을 내서 만나요",
                "회사나 학교에서 {pattern} 대화를 시작해요",
            ],
            "self": [
                "호감이 생기면 {pattern} 티를 내어 신뢰를 쌓아요",
                "갈등이 생기면 {pattern} 대화하며 해결해요",
                "좋아하는 생각이 {pattern} 미래까지 떠올라요",
                "이 감정이 {pattern} 장기적인지 판단해요",
                "좋아하는 내 모습이 {pattern} 성숙하게 느껴져요",
                "감정의 깊이를 {pattern} 확인하고 싶어요",
                "경제적인 부분도 {pattern} 따져보게 돼요",
                "감정이 생기면 {pattern} 현실과 균형을 맞춰요",
                "진지한 연애를 {pattern} 생각하게 돼요",
                "설렘이 오면 {pattern} 고민도 해요",
            ],
            "other": [
                "상대가 나를 {pattern} 대할 때 진심이라고 느껴요",
    "상대의 눈빛에서 {pattern} 미래를 볼 수 있어요",
                "상대가 취업이나 인턴에 {pattern} 대하면 호감이 커요",
                "상대가 경제적 현실을 {pattern} 고려할 때 감동해요",
                "상대가 장기적인 관계를 {pattern} 원한다고 봐요",
                "상대가 내 의견을 {pattern} 존중해 주면 신뢰가 가요",
                "상대가 가족이나 친구 이야기를 {pattern} 나누면 깊어졌다고 봐요",
                "상대가 다른 사람이랑 {pattern} 교류해도 이해해요",
                "상대가 진지한 미래를 {pattern} 그리면 안심이 돼요",
                "상대가 성실하게 {pattern} 생활하면 매력적으로 느껴요",
            ],
        },
        "20l": {
            "sum": [
                "만남이 생기면 {pattern} 결혼까지 생각하며 만나요",
                "호감이 생기면 {pattern} 부모님 생각도 해요",
                "좋아하는 사람과 {pattern} 미래를 계획해요",
                "관계가 깊어지면 {pattern} 함께 살 곳도 찾아봐요",
                "상대가 연락하면 {pattern} 중요한 일처럼 받아요",
                "장기적인 만남이 되면 {pattern} 경제도 함께 계획해요",
                "데이트할 때 {pattern} 의미 있는 시간을 보내요",
                "좋아하면 {pattern} 진지하게 어필해요",
                "취업 후에도 {pattern} 관계를 유지하려 해요",
                "친구들 결혼식에도 {pattern} 함께 가고 싶어해요",
            ],
            "self": [
                "호감이 생기면 {pattern} 결혼까지 생각하게 돼요",
                "내 마음이 {pattern} 장기적인지 확인해요",
                "좋아하면 {pattern} 부모님과도 상의하게 돼요",
                "이 관계가 {pattern} 평생 갈 수 있을지 고민해요",
                "좋아하면서도 {pattern} 현실적인 고민을 해요",
                "감정이 깊어지면 {pattern} 가족까지 생각해요",
                "미래를 함께 {pattern} 그리고 싶어져요",
                "감정이 {pattern} 안정적인지 봐요",
                "연애만 {pattern} 중요한 게 아니라고 느껴요",
    "설렘이 지나도 {pattern} 따뜻함이 남아 있어요",
            ],
            "other": [
                "상대가 {pattern} 결혼을 생각하는지 묻고 싶어져요",
                "상대의 눈빛에서 {pattern} 진지함이 느껴져요",
                "상대가 부모님을 {pattern} 존중하면 더 좋아하게 돼요",
                "상대가 미래 계획을 {pattern} 세우면 함께하고 싶어요",
                "상대가 장기 관계를 {pattern} 원한다고 느낄 때 안심돼요",
                "상대가 경제적으로 {pattern} 준비된 모습이 믿음직해요",
                "상대가 나를 {pattern} 배려해 주면 평생 함께하고 싶어져요",
                "상대가 과거 연애를 {pattern} 말해줄 때 신뢰가 가요",
                "상대가 가족과의 {pattern} 관계를 중요하게 여기면 매력적이에요",
                "상대가 진지하게 {pattern} 대하면 더 빠져들어요",
            ],
        },
        "30": {
            "sum": [
    "좋아하는 사람이 생기면 {pattern} 가족과도 어울릴지 봐요",
                "만남이 생기면 {pattern} 서로의 가정환경도 고려해요",
                "관계가 깊어지면 {pattern} 가족들과도 만남을 가져요",
                "연애가 진행되면 {pattern} 서로의 직장도 존중해요",
                "상대가 연락하면 {pattern} 성숙하게 대해요",
                "데이트할 때 {pattern} 품격 있게 시간을 보내요",
                "갈등이 생겨도 {pattern} 대화로 풀어요",
                "좋아하면 {pattern} 책임감 있게 다가가요",
                "생활패턴이 달라도 {pattern} 조율하며 만나요",
                "가정을 꾸리는 걸 {pattern} 상상해봐요",
            ],
            "self": [
                "호감이 생기면 {pattern} 서로의 삶을 존중해요",
                "내 마음이 {pattern} 성숙한지 확인해요",
                "좋아하면 {pattern} 가족을 생각하게 돼요",
                "이 연애가 {pattern} 모두에게 좋은지 고민해요",
                "감정이 {pattern} 현실과 함께 자라요",
                "설렘보다 {pattern} 따뜻함이 중요해져요",
                "미래를 {pattern} 함께 구체적으로 그려봐요",
                "상대를 {pattern} 배려하며 사랑해요",
                "감정이 {pattern} 안정되면 편안해져요",
                "나이가 들어도 {pattern} 사랑이 소중해요",
            ],
            "other": [
                "상대가 나를 {pattern} 존중해 주면 감사해요",
                "상대의 눈빛에서 {pattern} 성숙함이 느껴져요",
                "상대가 가족을 {pattern} 생각할 때 든든해요",
                "상대가 미래를 {pattern} 계획하면 함께하고 싶어져요",
                "상대가 내 의견을 {pattern} 경청해 주면 신뢰가 가요",
                "상대가 직장생활을 {pattern} 잘하면 매력적이에요",
                "상대가 과거를 {pattern} 솔직하게 말해줄 때 마음이 열려요",
                "상대가 내 가족과 {pattern} 잘 지낼 수 있을지 봐요",
                "상대가 성실하게 {pattern} 생활하면 더 좋아하게 돼요",
                "상대가 저와 {pattern} 진지하게 대하면 행복해요",
            ],
        },
    }
    
    # Generate all questions
    for age_code, age_info in ages.items():
        for gender in genders:
            for trait in traits:
                key = f"{age_code}{gender}_{trait}"
                q_list = []
                
                # Get templates for this age
                age_templates = templates[age_code]
                
                # Generate 10 questions of each type
                for i in range(10):
                    q_type = ["sum", "self", "other"][i // 10 if i < 10 else (i // 10 if i < 20 else 2)]
                    if i < 10:
                        q_type = "sum"
                        tpl = age_templates["sum"][i]
                    elif i < 20:
                        q_type = "self"
                        tpl = age_templates["self"][i - 10]
                    else:
                        q_type = "other"
                        tpl = age_templates["other"][i - 20]
                    
                    # Format with trait pattern
                    pattern = trait_patterns[trait][q_type][i % 5]
                    text = tpl.format(pattern=pattern)
                    
                    q_id = f"{key}_{q_type}_{i+1:02d}"
                    q_list.append({"id": q_id, "text": text, "type": q_type})
                
    questions[key] = q_list
    
    return questions

if __name__ == "__main__":
    print("Generating SomeThing questions...")
    q = create_questions()
    
    total = sum(len(v) for v in q.values())
    print(f"Generated {len(q)} groups, {total} questions total")
    
    with open("/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-v10.json", "w", encoding="utf-8") as f:
        json.dump(q, f, ensure_ascii=False, indent=2)
    
    print("Saved to questions-v10.json")
