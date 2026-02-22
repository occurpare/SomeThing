#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

# Define all 40 combinations
combinations = [
    # 10대 Female
    "10F_D", "10F_C", "10F_R", "10F_P",
    # 10대 Male
    "10M_D", "10M_C", "10M_R", "10M_P",
    # 20대초반 Female
    "20eF_D", "20eF_C", "20eF_R", "20eF_P",
    # 20대초반 Male
    "20eM_D", "20eM_C", "20eM_R", "20eM_P",
    # 20대중반 Female
    "20mF_D", "20mF_C", "20mF_R", "20mF_P",
    # 20대중반 Male
    "20mM_D", "20mM_C", "20mM_R", "20mM_P",
    # 20대후반 Female
    "20lF_D", "20lF_C", "20lF_R", "20lF_P",
    # 20대후반 Male
    "20lM_D", "20lM_C", "20lM_R", "20lM_P",
    # 30대 Female
    "30F_D", "30F_C", "30F_R", "30F_P",
    # 30대 Male
    "30M_D", "30M_C", "30M_R", "30M_P",
]

# Question templates for each test type
sum_questions = [
    {"text": "일주일에 서로 연락하는 횟수는?", "options": [{"text": "일주일에 1-2번", "score": 2}, {"text": "거의 매일 연락해", "score": 5}, {"text": "하루에도 여러 번 연락해", "score": 8}]},
    {"text": "서로 만날 때의 분위기는?", "options": [{"text": "친구들이랑 별 차이 없어", "score": 2}, {"text": "좀 특별하고 설레는 느낌이야", "score": 5}, {"text": "둘만 있고 싶은 마음이 커", "score": 8}]},
    {"text": "주변 친구들이 우리를 볼 때?", "options": [{"text": "그냥 친구라고 생각할 것 같아", "score": 2}, {"text": "뭔가 있는 것 같다고 놀려", "score": 5}, {"text": "커플인 줄 알 것 같아", "score": 8}]},
    {"text": "감정을 주고받을 때 느끼는 것은?", "options": [{"text": "딱히 특별한 감정 없어", "score": 2}, {"text": "가끔 마음이 흔들려", "score": 5}, {"text": "자주 설레고 떨려", "score": 8}]},
    {"text": "둘이 있을 때의 대화는?", "options": [{"text": "일상적인 얘기만 해", "score": 2}, {"text": "속마음도 조금씩 얘기해", "score": 5}, {"text": "편하게 모든 얘기를 나눠", "score": 8}]},
    {"text": "서로를 대하는 태도는?", "options": [{"text": "다른 친구들이랑 비슷해", "score": 2}, {"text": "조금 더 챙겨주는 것 같아", "score": 5}, {"text": "특별하게 신경 써줘", "score": 8}]},
    {"text": "연락할 때 누가 먼저 하는 편이야?", "options": [{"text": "대게 내가 먼저", "score": 2}, {"text": "서로 번갈아가며", "score": 5}, {"text": "대게 상대가 먼저", "score": 8}]},
    {"text": "함께 있는 시간이 끝날 때 느낌은?", "options": [{"text": "그냥 헤어지는구나", "score": 2}, {"text": "아쉬운 정도?", "score": 5}, {"text": "더 함께 있고 싶어", "score": 8}]},
    {"text": "상대의 사소한 것까지 알고 싶은 마음은?", "options": [{"text": "크게 궁금하진 않아", "score": 2}, {"text": "가끔 궁금해", "score": 5}, {"text": "모든 게 알고 싶어", "score": 8}]},
    {"text": "같이 있을 때 웃음이 많아지는 편이야?", "options": [{"text": "평소랑 똑같아", "score": 2}, {"text": "조금 더 웃는 것 같아", "score": 5}, {"text": "너무 신나서 자주 웃어", "score": 8}]}
]

self_questions = [
    {"text": "평소에 상대를 얼마나 자주 생각해?", "options": [{"text": "별로 생각 안 해", "score": 2}, {"text": "하루에 몇 번 생각해", "score": 5}, {"text": "자주 떠오르고 궁금해", "score": 8}]},
    {"text": "상대와의 관계에 대해 느끼는 감정은?", "options": [{"text": "그냥 친구일 뿐이야", "score": 2}, {"text": "특별한 친구인 것 같아", "score": 5}, {"text": "뭔가 더 깊은 감정이 있어", "score": 8}]},
    {"text": "상대랑 미래를 상상해본 적 있어?", "options": [{"text": "거의 안 해봤어", "score": 2}, {"text": "가끔 생각해봤어", "score": 5}, {"text": "종종 같을 미래를 상상해", "score": 8}]},
    {"text": "상대에게 보여주고 싶은 모습은?", "options": [{"text": "평소 그대로", "score": 2}, {"text": "조금 더 예쁘게/멋지게", "score": 5}, {"text": "더 나은 모습을 보여주고 싶어", "score": 8}]},
    {"text": "상대가 다른 이성이랑 있을 때 기분은?", "options": [{"text": "신경 안 써", "score": 2}, {"text": "조금 신경 쓰여", "score": 5}, {"text": "질투나고 마음이 불편해", "score": 8}]},
    {"text": "상대에게 받고 싶은 것은?", "options": [{"text": "친구로서의 관심", "score": 2}, {"text": "특별한 배려", "score": 5}, {"text": "사랑스러운 감정", "score": 8}]},
    {"text": "상대와 1:1로 만나고 싶은 마음은?", "options": [{"text": "딱히 없어", "score": 2}, {"text": "가끔은", "score": 5}, {"text": "종종 그러고 싶어", "score": 8}]},
    {"text": "내 우선순위에서 상대는?", "options": [{"text": "그냥 친구 중 하나", "score": 2}, {"text": "중요한 친구", "score": 5}, {"text": "아주 특별한 사람", "score": 8}]},
    {"text": "상대에게 고민을 털어놓고 싶은 마음은?", "options": [{"text": "별로 없어", "score": 2}, {"text": "가끔은", "score": 5}, {"text": "많이 의지하고 싶어", "score": 8}]},
    {"text": "상대와의 관계를 어떻게 정의하고 싶어?", "options": [{"text": "좋은 친구", "score": 2}, {"text": "특별한 친구", "score": 5}, {"text": "더 깊은 관계로", "score": 8}]}
]

other_questions = [
    {"text": "상대가 나에게 노력을 얼마나 하는 것 같아?", "options": [{"text": "다른 친구들이랑 비슷", "score": 2}, {"text": "조금 더 신경 쓰는 것 같아", "score": 5}, {"text": "많이 노력하는 것 같아", "score": 8}]},
    {"text": "상대가 나에게 호감을 표현하는 편이야?", "options": [{"text": "거의 안 해", "score": 2}, {"text": "가끔 느껴져", "score": 5}, {"text": "자주 표현하는 것 같아", "score": 8}]},
    {"text": "상대가 내 감정을 배려해주는 것 같아?", "options": [{"text": "잘 못 느껴", "score": 2}, {"text": "가끔 느껴", "score": 5}, {"text": "세심하게 신경 써줘", "score": 8}]},
    {"text": "상대가 나를 얼마나 기억해주는 것 같아?", "options": [{"text": "내가 얘기한 건 잘 몰라", "score": 2}, {"text": "가끔 기억해줘", "score": 5}, {"text": "사소한 것까지 기억해줘", "score": 8}]},
    {"text": "상대가 나에게 시간을 얼마나 내는 것 같아?", "options": [{"text": "바쁘면 못 만나", "score": 2}, {"text": "가끔 시간 내줘", "score": 5}, {"text": "일정 조율해서 만나려 해", "score": 8}]},
    {"text": "상대가 나와 미래에 대해 얘기하는 편이야?", "options": [{"text": "거의 안 해", "score": 2}, {"text": "가끔 얘기해", "score": 5}, {"text": "함께할 미래를 자주 얘기해", "score": 8}]},
    {"text": "상대가 나의 일에 얼마나 관심을 보여?", "options": [{"text": "큰 관심 없어 보여", "score": 2}, {"text": "가끔 물어봐줘", "score": 5}, {"text": "세심하게 챙겨줘", "score": 8}]},
    {"text": "상대가 내 감정을 얼마나 알아주는 것 같아?", "options": [{"text": "잘 모르는 것 같아", "score": 2}, {"text": "가끔 알아줘", "score": 5}, {"text": "내 기분을 잘 캐치해줘", "score": 8}]},
    {"text": "상대가 나를 위해 무언가를 해주는 편이야?", "options": [{"text": "별로 없어", "score": 2}, {"text": "가끔 해줘", "score": 5}, {"text": "종종 깜짝 선물이나 배려를 해줘", "score": 8}]},
    {"text": "상대가 나에 대한 마음을 얼마나 솔직하게 표현해?", "options": [{"text": "듣기 어려워", "score": 2}, {"text": "가끔 티를 내", "score": 5}, {"text": "자신의 감정을 꽤 표현해", "score": 8}]}
]

# Build the complete data structure
data = {
    "version": "5.0",
    "totalQuestions": 1200,
    "metadata": {
        "generatedAt": "2026-02-21",
        "combinations": 40,
        "testsPerCombination": 3,
        "questionsPerTest": 10
    },
    "questions": {}
}

for combo in combinations:
    data["questions"][combo] = {
        "sum": sum_questions.copy(),
        "self": self_questions.copy(),
        "other": other_questions.copy()
    }

# Write to file
output_path = "/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-v5.json"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Generated questions-v5.json")
print(f"   - Total combinations: {len(combinations)}")
print(f"   - Total questions: {len(combinations) * 3 * 10}")
print(f"   - File: {output_path}")
