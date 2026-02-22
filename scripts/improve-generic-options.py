#!/usr/bin/env python3
"""
SomeThing v28.2 - 단순 패턴 선택지 개선 스크립트
"전혀 안 그래요, 가끔 그래요, 자주 그래요, 항상 그래요" 패턴을 문맥별 선택지로 교체
"""

import json
import re
from copy import deepcopy

# 파일 로드
print("📂 verions-v28.json 로드 중...")
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

def analyze_question_type(question_text):
    """질문의 성격 분석 (상호작용/감정/행동)"""
    text = question_text.lower()
    
    if any(word in text for word in ['서로', '함께', '둘', '함께', '둘이']):
        return 'mutual'
    elif any(word in text for word in ['나는', '내가', '내', '나']):
        return 'self'
    elif any(word in text for word in ['그 사람이', '상대가']):
        return 'other'
    return 'general'

def get_context_template(question_text, score):
    """질문 내용에 맞는 문맥별 선택지 생성"""
    text = question_text
    t = analyze_question_type(text)
    
    # 점수별 강도 매핑
    intensity = {1: '없음/약함', 3: '조금', 6: '자연스러움', 10: '강함/완벽'}
    
    # sum 테스트 - 상호작용 중심
    if '웃' in text and ('따라' in text or '같이' in text):
        return {
            1: "아무런 반응이 없어요",
            3: "가끔 미소를 지어요",
            6: "자주 환하게 웃어요",
            10: "함께 웃으며 행복해져요"
        }[score]
    
    if '위로' in text or '힘들' in text:
        return {
            1: "모른 척 지나쳐요",
            3: "가끔 물어봐요",
            6: "진심으로 위로해줘요",
            10: "내 마음을 녹여줘요"
        }[score]
    
    if '들어줘요' in text or '이야기' in text or '얘기' in text:
        return {
            1: "귀 기울이지 않아요",
            3: "가끔만 집중해요",
            6: "끝까지 진심으로 들어줘요",
            10: "내 영혼까지 읽어줘요"
        }[score]
    
    if '반겨줘' in text or '환하' in text or '다가가' in text:
        return {
            1: "외면하거나 회피해요",
            3: "가끔 인사 정도 해요",
            6: "반갑게 맞아줘요",
            10: "가장 먼저 달려와요"
        }[score]
    
    if '실수' in text or '미안' in text:
        return {
            1: "화를 내거나 냉대해요",
            3: "가끔 넘어가줘요",
            6: "미소로 풀어줘요",
            10: "실수마저 귀엽다고 해요"
        }[score]
    
    if '에너지' in text or '힘' in text or '피곤' in text:
        return {
            1: "더 지치게 만들어요",
            3: "별 변화 없어요",
            6: "활기가 생겨요",
            10: "세상을 다 가진 것 같아요"
        }[score]
    
    if '농담' in text or '웃음' in text or '장난' in text:
        return {
            1: "웃긴지 모르겠어요",
            3: "가끔 미소 짓는 수준이에요",
            6: "함께 크게 웃어요",
            10: "배꼽이 빠질 것 같이 웃어요"
        }[score]
    
    if '발걸음' in text or '걸을' in text or '맞춰' in text:
        return {
            1: "각자 걸어요",
            3: "가끔 신경 써요",
            6: "자연스럽게 맞춰줘요",
            10: "하나가 된 듯 걸어요"
        }[score]
    
    if '눈치' in text or '마음이 전해' in text:
        return {
            1: "전혀 몰라요",
            3: "가끔 알아차려요",
            6: "눈빛만으로도 알아봐요",
            10: "숨김없이 모든 게 통해요"
        }[score]
    
    if '행복' in text or '즐거' in text:
        return {
            1: "전혀 안 그랬던 것 같아요",
            3: "가끔 느껴요",
            6: "함께 행복해 보여요",
            10: "세상 모든 행복을 다 가진 것 같아요"
        }[score]
    
    # self 테스트 - 내 감정 중심
    if '생각하면' in text or '떠올라' in text:
        return {
            1: "전혀 안 떠올라요",
            3: "가끔 생각나요",
            6: "자주 떠올라요",
            10: "온종일 머릿속에 맴돌아요"
        }[score]
    
    if '숨' in text or '호흡' in text or '막혀' in text:
        return {
            1: "전혀 안 그래요",
            3: "조금 가빠져요",
            6: "숨이 짧아져요",
            10: "숨 쉬는 법을 잊어버려요"
        }[score]
    
    if '꿈' in text or '상상' in text or '환상' in text:
        return {
            1: "꿈에 안 나타나요",
            3: "가끔 나타나요",
            6: "자주 꾸는 꿈이에요",
            10: "매일 밤 그 사람과 함께해요"
        }[score]
    
    if '고백' in text or '말하고' in text:
        return {
            1: "할 생각이 없어요",
            3: "가끔 생각해요",
            6: "자주 맘 졸여요",
            10: "지금 당장 뛰쳐나가고 싶어요"
        }[score]
    
    if '선물' in text or '주고' in text:
        return {
            1: "생각이 없어요",
            3: "가끔 생각나요",
            6: "종종 고르고 있어요",
            10: "세상을 담아 주고 싶어요"
        }[score]
    
    # other 테스트 - 상대의 나에 대한 행동
    if '쳐다봐' in text or '보여' in text or '눈빛' in text:
        return {
            1: "전혀 안 봐요",
            3: "가끔 눈이 마주쳐요",
            6: "자주 쳐다봐요",
            10: "시선이 늘 나를 따라다녀요"
        }[score]
    
    if '연락' in text or '카톡' in text or '메시지' in text:
        return {
            1: "거의 안 해요",
            3: "가끔 연락해요",
            6: "종종 먼저 연락해요",
            10: "하루도 빠짐없이 해요"
        }[score]
    
    if '배려' in text or '챙겨' in text:
        return {
            1: "전혀 안 해주려 해요",
            3: "가끔 물어봐요",
            6: "세심하게 챙겨줘요",
            10: "내 것까지 전부 신경 써요"
        }[score]
    
    if '맞춰' in text or '걸음' in text or '맞춰줘' in text:
        return {
            1: "전혀 안 맞춰줘요",
            3: "가끔 고려해요",
            6: "자연스럽게 맞춰줘요",
            10: "나를 위해 발맞춰줘요"
        }[score]
    
    if '예쁘게 불러' in text or '부르' in text or '이름' in text:
        return {
            1: "그냥 불러요",
            3: "가끔 특별하게 불러요",
            6: "애정을 담아 불러요",
            10: "세상에서 가장 예쁘게 불러요"
        }[score]
    
    if '기억' in text or '기억해' in text:
        return {
            1: "하나도 기억 못 해요",
            3: "가끔 기억해줘요",
            6: "대부분 잘 기억해요",
            10: "작은 것 하나도 놓치지 않아요"
        }[score]
    
    if '진심' in text or '솔직' in text:
        return {
            1: "표면적이에요",
            3: "가끔 진심을 보여요",
            6: "대부분 솔직해요",
            10: "속 깊은 마음까지 털어놔요"
        }[score]
    
    if '노력' in text or '해줘' in text:
        return {
            1: "전혀 안 해요",
            3: "조금은 해요",
            6: "많이 노력해줘요",
            10: "무엇이든 다 해줘요"
        }[score]
    
    if '약속' in text:
        return {
            1: "지키지 않아요",
            3: "어영부영 넘어가요",
            6: "대체로 잘 지켜요",
            10: "한 치의 흐트러짐도 없어요"
        }[score]
    
    if '호감' in text or '관심' in text:
        return {
            1: "전혀 느껴지지 않아요",
            3: "가끔 친절할 뿐이에요",
            6: "분명히 호감이 있어요",
            10: "세상의 모든 관심이 모인 것 같아요"
        }[score]
    
    if '특별' in text:
        return {
            1: "전혀 특별하지 않아요",
            3: "가끔 다르게 대해요",
            6: "자주 특별하게 해줘요",
            10: "유일하게 날 다뤄요"
        }[score]
    
    if '편안' in text or '편하' in text:
        return {
            1: "전혀 편하지 않아요",
            3: "가끔 편안해요",
            6: "자주 편하게 대해요",
            10: "내게 가장 편안한 사람이에요"
        }[score]
    
    if '손길' in text or '손' in text or '터치' in text:
        return {
            1: "전혀 없어요",
            3: "조심스럽게 해요",
            6: "자연스럽게 다가와요",
            10: "애정이 담긴 터치예요"
        }[score]
    
    if '웃음' in text or '웃어' in text:
        return {
            1: "전혀 웃지 않아요",
            3: "가끔 웃어요",
            6: "자주 환하게 웃어요",
            10: "가장 환한 미소를 지어요"
        }[score]
    
    if '응원' in text or '격려' in text or '힘내' in text:
        return {
            1: "전혀 안 해줘요",
            3: "가끔 말해줘요",
            6: "진심으로 응원해줘요",
            10: "든든한 버팀목이 되어줘요"
        }[score]
    
    if '알아봐' in text or '알아차려' in text:
        return {
            1: "전혀 몰라줘요",
            3: "겉으로만 알아봐요",
            6: "궁금해하고 다가와요",
            10: "속 깊은 얘기까지 알아차려요"
        }[score]
    
    if '감정' in text or '기분' in text:
        return {
            1: "전혀 몰라요",
            3: "가끔 알아차려요",
            6: "자주 알아봐줘요",
            10: "눈빛만 봐도 알아차려요"
        }[score]
    
    if '미래' in text:
        return {
            1: "전혀 안 해요",
            3: "희망만 얘기해요",
            6: "가끔 구체적으로 얘기해요",
            10: "함께 할 내일을 그려요"
        }[score]
    
    if '무뚝뚝' in text or '부드러' in text or '따뜻' in text:
        return {
            1: "항상 무뚝뚝해요",
            3: "가끔 봐요",
            6: "부드러워져요",
            10: "내게만 특별히 따뜻해요"
        }[score]
    
    if '눈빛' in text or '시선' in text:
        return {
            1: "피하기만 해요",
            3: "가끔 마주쳐요",
            6: "자주 깊게 봐요",
            10: "영혼을 빨아들이듯 바라봐요"
        }[score]
    
    if '시간' in text or '아끼' in text:
        return {
            1: "아까워해요",
            3: "조금 양보해요",
            6: "할애해줘요",
            10: "아낌없이 내어줘요"
        }[score]
    
    # style 테스트 - 연애 스타일
    if '주말' in text or '데이트' in text:
        return {
            1: "거의 없어요",
            3: "가끔 만나요",
            6: "자주 만나요",
            10: "매일하고 싶어요"
        }[score]
    
    if '친구' in text and '알고' in text:
        return {
            1: "전혀 몰라요",
            3: "이름만 알아요",
            6: "얼굴을 본 적 있어요",
            10: "서로의 친구들과 잘 지내요"
        }[score]
    
    if '서운' in text or '연락' in text or '안 하면' in text:
        return {
            1: "전혀 안 그래요",
            3: "조금 서운해요",
            6: "많이 서운해요",
            10: "걱정될 정도로 그래요"
        }[score]
    
    if '사진' in text:
        return {
            1: "전혀 안 찍어요",
            3: "가끔 찍어요",
            6: "자주 찍어요",
            10: "추억이 가득 쌓여요"
        }[score]
    
    if '취향' in text or '음식' in text:
        return {
            1: "전혀 달라요",
            3: "일부만 비슷해요",
            6: "대부분 비슷해요",
            10: "똑같아요"
        }[score]
    
    if '배려' in text or '돌봐' in text:
        return {
            1: "전혀 안 해요",
            3: "가끔 해요",
            6: "자주 서로 챙겨요",
            10: "일상이 되었어요"
        }[score]
    
    if '양보' in text or '다투' in text:
        return {
            1: "한쪽만 양보해요",
            3: "서로 비슷해요",
            6: "번갈아 가며 해요",
            10: "둘 다 서로를 먼저 생각해요"
        }[score]
    
    if '일상' in text or '공유' in text:
        return {
            1: "전혀 안 해요",
            3: "가끔 이야기해요",
            6: "자주 공유해요",
            10: "모든 순간을 공유해요"
        }[score]
    
    if '즐거' in text or '함께' in text:
        return {
            1: "별로예요",
            3: "그냥 그래요",
            6: "즐거워요",
            10: "최고의 순간이에요"
        }[score]
    
    if '변하' in text or '노력' in text:
        return {
            1: "전혀 안 해요",
            3: "조금씩 해요",
            6: "많이 노력해요",
            10: "무엇이든 다 해요"
        }[score]
    
    if '비용' in text or '돈' in text:
        return {
            1: "한쪽이 다 내요",
            3: "대체로 한쪽이 많이 내요",
            6: "번갈아 가며 내요",
            10: "딱딱 나눠요"
        }[score]
    
    if '의견' in text or '존중' in text:
        return {
            1: "무시해요",
            3: "조금은 들어줘요",
            6: "잘 들어줘요",
            10: "항상 존중해요"
        }[score]
    
    if '편안' in text or '집' in text:
        return {
            1: "불편해요",
            3: "그냥 그래요",
            6: "편해요",
            10: "집처럼 편안해요"
        }[score]
    
    if '장난' in text or '농담' in text:
        return {
            1: "전혀 안 쳐요",
            3: "가끔 쳐요",
            6: "자주 쳐요",
            10: "애정표현으로 쳐요"
        }[score]
    
    if '자신감' in text or '확신' in text:
        return {
            1: "전혀 없어요",
            3: "조금 있어요",
            6: "있다고 생각해요",
            10: "확신해요"
        }[score]
    
    if '칭찬' in text:
        return {
            1: "전혀 안 해요",
            3: "가끔 해요",
            6: "자주 해요",
            10: "매일 해요"
        }[score]
    
    if '의지' in text or '지지' in text:
        return {
            1: "전혀 못 해요",
            3: "조금은 돼요",
            6: "든든해요",
            10: "최고의 지지자예요"
        }[score]
    
    if '감사' in text:
        return {
            1: "전혀 안 그래요",
            3: "가끔 그래요",
            6: "자주 그래요",
            10: "매일매일 그래요"
        }[score]
    
    if '성장' in text or '함께' in text:
        return {
            1: "전혀 못 느껴요",
            3: "조금은 그래요",
            6: "그런 것 같아요",
            10: "함께 자라가요"
        }[score]
    
    if '안정' in text:
        return {
            1: "불안해요",
            3: "그냥 그래요",
            6: "안정돼요",
            10: "든든해요"
        }[score]
    
    # 기본 패턴 - 대체 템플릿
    default_templates_1 = [
        "전혀 그렇지 않아요",
        "전혀 안 그래요",
        "그런 적 없어요",
        "전혀 못 느껴요",
        "아무것도 몰라요"
    ]
    
    default_templates_3 = [
        "조금은 그래요",
        "가끔 그래요",
        "가끔 느껴요",
        "간혹 그래요",
        "때때로 그래요"
    ]
    
    default_templates_6 = [
        "자주 그래요",
        "꽤 그래요",
        "대체로 그래요",
        "잘 그래요",
        "자연스럽게 그래요"
    ]
    
    default_templates_10 = [
        "항상 그래요",
        "매일 그래요",
        "완벽하게 그래요",
        "온전히 그래요",
        "완전히 그래요"
    ]
    
    templates = {
        1: default_templates_1,
        3: default_templates_3,
        6: default_templates_6,
        10: default_templates_10
    }
    
    import random
    return random.choice(templates[score])


# 통계용
stats = {
    'total_combinations': 0,
    'total_questions': 0,
    'improved_questions': 0,
    'improvements_by_type': {'sum': 0, 'self': 0, 'other': 0, 'style': 0, 'ideal': 0}
}

# 각 조합별 처리
for combo_id, tests in data['combinations'].items():
    stats['total_combinations'] += 1
    
    for test_type, questions in tests.items():
        if test_type == 'ideal':  # ideal은 이미 개선됨 (v28.1)
            continue
            
        for q_idx, question in enumerate(questions):
            stats['total_questions'] += 1
            
            if has_generic_pattern(question['options']):
                # 개선 필요
                stats['improved_questions'] += 1
                stats['improvements_by_type'][test_type] += 1
                
                # 각 옵션 개선
                for opt_idx, option in enumerate(question['options']):
                    score = option['score']
                    old_text = option['text']
                    
                    # 단순 패턴이 있는 경우만 개선
                    if any(pattern in old_text for pattern in GENERIC_PATTERNS):
                        new_text = get_context_template(question['text'], score)
                        data['combinations'][combo_id][test_type][q_idx]['options'][opt_idx]['text'] = new_text

print("\n✅ 개선 완료!")
print(f"- 총 조합 수: {stats['total_combinations']}")
print(f"- 총 질문 수: {stats['total_questions']}")
print(f"- 개선된 질문 수: {stats['improved_questions']}")
print("\n📊 테스트별 개선 현황:")
for t, count in stats['improvements_by_type'].items():
    print(f"  - {t}: {count}개")

# 버전 업데이트
data['version'] = '28.2'

# 저장
print("\n💾 파일 저장 중...")
with open('questions-v28.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✨ verion 28.2 저장 완료!")
