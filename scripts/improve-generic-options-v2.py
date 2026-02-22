#!/usr/bin/env python3
"""
SomeThing v28.2 - 단순 패턴 선택지 개선 스크립트 (보완판)
"전혀 안 그래요, 가끔 그래요, 자주 그래요, 항상 그래요" 패턴을 문맥별 선택지로 교체
"""

import json
import re

# 파일 로드
with open('questions-v28.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 개선할 패턴 정의
GENERIC_PATTERNS = ['전혀 안 그래요', '가끔 그래요', '자주 그래요', '항상 그래요', '그런 적 없어요']

def has_generic_pattern(options):
    """선택지에 단순 패턴이 있는지 확인"""
    for opt in options:
        text = opt['text']
        if any(pattern in text for pattern in GENERIC_PATTERNS):
            return True
    return False

def get_improved_option(question_text, score):
    """질문 내용에 맞는 문맥별 선택지 생성"""
    text = question_text
    
    # ========== SELF 테스트 (내 감정) ==========
    
    if '뒤척여' in text or '잠' in text:
        return {
            1: "숙면을 취해요",
            3: "가끔 뒤척여요",
            6: "자주 뒤척여요",
            10: "해 뜰 때까지 뒤척여요"
        }[score]
    
    if '숨이 빨라져' in text or '호흡' in text:
        return {
            1: "전혀 안 그래요",
            3: "조금 달라져요",
            6: "호흡이 가빠져요",
            10: "들이쉬는 것도 잊어요"
        }[score]
    
    if '생각나' in text:
        return {
            1: "전혀 안 떠올라요",
            3: "가끔 떠올라요",
            6: "자주 떠올라요",
            10: "온종일 머릿속에 있어요"
        }[score]
    
    # ========== OTHER 테스트 (상대의 나에 대한 행동) ==========
    
    if '믿어주' in text or '신뢰' in text or '믿음' in text:
        return {
            1: "전혀 안 믿어줘요",
            3: "가끔 믿어줘요",
            6: "자주 믿어줘요",
            10: "무조건 믿어줘요"
        }[score]
    
    if '의식' in text or '신경' in text:
        return {
            1: "전혀 안 의식해요",
            3: "가끔 의식해요",
            6: "자주 의식해요",
            10: "항상 신경 쓰는 것 같아요"
        }[score]
    
    if '질문' in text or '물어봐' in text:
        return {
            1: "전혀 안 물어봐요",
            3: "가끔 물어봐요",
            6: "자주 물어봐요",
            10: "꼬리에 꼬리를 무는 질문이에요"
        }[score]
    
    if '관심' in text and '보' in text:
        return {
            1: "전혀 관심 없어요",
            3: "가끔 보여요",
            6: "자주 보여요",
            10: "분명하게 느껴져요"
        }[score]
    
    # ========== SUM 테스트 (상호작용) ==========
    
    if '따라 웃어' in text or '같이 웃어' in text:
        return {
            1: "아무런 반응 없어요",
            3: "가끔 미소 지어요",
            6: "자주 환하게 웃어요",
            10: "함께 크게 웃어요"
        }[score]
    
    if '위로해줘' in text or '힘들' in text:
        return {
            1: "모른 척해요",
            3: "가끔 위로해줘요",
            6: "자주 위로해줘요",
            10: "내 마음을 녹여줘요"
        }[score]
    
    if '들어줘' in text or '듣' in text:
        return {
            1: "전혀 안 들어줘요",
            3: "가끔 들어줘요",
            6: "자주 들어줘요",
            10: "끝까지 집중해줘요"
        }[score]
    
    if '반겨줘' in text:
        return {
            1: "외면돼요",
            3: "가끔 반겨줘요",
            6: "자주 반겨줘요",
            10: "가장 먼저 달려와요"
        }[score]
    
    if '실수' in text:
        return {
            1: "화를 내요",
            3: "가끔 웃어요",
            6: "자주 넘어가줘요",
            10: "귀엽다고 해요"
        }[score]
    
    if '에너지' in text:
        return {
            1: "전혀 안 생겨요",
            3: "가끔 생겨요",
            6: "자주 생겨요",
            10: "활력이 넘쳐요"
        }[score]
    
    if '농담' in text or '장난' in text:
        return {
            1: "전혀 안 웃어요",
            3: "가끔 웃어요",
            6: "자주 크게 웃어요",
            10: "배꼽이 빠질 것 같아요"
        }[score]
    
    if '발걸음' in text or '맞춰' in text:
        return {
            1: "전혀 안 맞춰요",
            3: "가끔 맞춰요",
            6: "자주 맞춰요",
            10: "하나가 같이 걸어요"
        }[score]
    
    if '눈치' in text:
        return {
            1: "전혀 몰라요",
            3: "가끔 알아차려요",
            6: "자주 알아차려요",
            10: "눈빛만으로도 통해요"
        }[score]
    
    if '행복' in text:
        return {
            1: "전혀 안 그래요",
            3: "가끔 행복해 보여요",
            6: "자주 행복해 보여요",
            10: "세상에서 가장 행복해 보여요"
        }[score]
    
    # ========== 기본 패턴 ==========
    default_templates = {
        1: ["전혀 그렇지 않아요", "전혀 안 그래요", "그런 적 없어요", "전혀 못 느껴요", "아무것도 몰라요"],
        3: ["조금은 그래요", "가끔 그래요", "가끔 느껴요", "간혹 그래요"],
        6: ["자주 그래요", "꽤 그래요", "대체로 그래요", "잘 그래요"],
        10: ["항상 그래요", "매일 그래요", "완벽하게 그래요", "온전히 그래요"]
    }
    
    import random
    return random.choice(default_templates[score])


# 통계용
stats = {
    'improved': 0,
    'by_test': {'sum': 0, 'self': 0, 'other': 0, 'style': 0}
}

# 각 조합별 처리
for combo_id, tests in data['combinations'].items():
    for test_type, questions in tests.items():
        if test_type == 'ideal':
            continue
            
        for q_idx, question in enumerate(questions):
            if not has_generic_pattern(question['options']):
                continue
                
            # 개선
            stats['improved'] += 1
            stats['by_test'][test_type] += 1
            
            for opt_idx, option in enumerate(question['options']):
                score = option['score']
                old_text = option['text']
                
                if any(pattern in old_text for pattern in GENERIC_PATTERNS):
                    new_text = get_improved_option(question['text'], score)
                    data['combinations'][combo_id][test_type][q_idx]['options'][opt_idx]['text'] = new_text

print(f"✅ 추가 개선: {stats['improved']}개 질문")
print("\n📊 테스트별:")
for t, c in stats['by_test'].items():
    print(f"  - {t}: {c}개")

# 저장
with open('questions-v28.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n💾 저장 완료!")
