#!/usr/bin/env python3
"""
Create questions-v16.json
- Remove location references
- Fix 'other' category to focus on "그 사람이 나를/내게" instead of "내가"
"""

import json
import re

# Load v15
with open('/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-v15.json', 'r', encoding='utf-8') as f:
    v15 = json.load(f)

# Location patterns to exclude
LOCATION_KEYWORDS = ['카페에서', '놀이공원에서', '음식점에서', '영화관에서', '공원에서']

def has_location(text):
    for kw in LOCATION_KEYWORDS:
        if kw in text:
            return True
    # Also check for "~에서 함께" or "~에서 서로"
    if re.search(r'.*?에서\s*(함께|서로)', text):
        return True
    return False

def is_other_correct(text):
    """Check if 'other' question is correctly focused on 상대's action toward me"""
    # Correct patterns: 그 사람이/걔가/상대가 ... 나를/내게
    patterns = [
        r'(그 사람|걔|상대).*(나를|내게|내게|내 말|나를 위해|나에게)',
        r'(그 사람|걔|상대).*(쳐다|다가와|시간을 내|장난|챙겨|귀 기울|생각해|솔직)',
    ]
    for p in patterns:
        if re.search(p, text):
            return True
    return False

# Other questions bank - rewritten to focus on "그 사람이 나를/내게"
OTHER_QUESTIONS_BANK = {
    "10": [
        {"text": "그 사람이 나를 쳐다볼 때 특별해 보여요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 먼저 다가와요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 위해 시간을 내줘요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나에게 장난스럽게 대해요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 챙겨주려 해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내 말에 귀 기울여요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 집중해요", "score": 10}]},
        {"text": "그 사람이 나를 먼저 생각해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나에게 솔직한 것 같아요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은 그래요", "score": 3}, {"text": "꽤 그래요", "score": 6}, {"text": "매우 그래요", "score": 10}]},
        {"text": "그 사람이 내게 먼저 연락해요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 웃게 해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내걸음에 맞춰줘요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내 이름을 예쁘게 불러요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 배려해줘요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내 이야기를 잘 기억해줘요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "모든 걸 기억해요", "score": 10}]},
        {"text": "그 사람이 나를 먼저 챙겨줘요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 진심으로 말해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 애타게 만들어요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은 그래요", "score": 3}, {"text": "꽤 그래요", "score": 6}, {"text": "매우 그래요", "score": 10}]},
        {"text": "그 사람이 내게 소중한 시간을 줘요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 특별하게 느끼게 해요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 편안하게 대해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
    ],
    "20e": [
        {"text": "그 사람이 나에게 관심이 있는 것 같아요", "options": [{"text": "전혀 없어 보여요", "score": 1}, {"text": "조금 있어요", "score": 3}, {"text": "꽤 있어요", "score": 6}, {"text": "많아요", "score": 10}]},
        {"text": "그 사람이 내 말에 공감해줘요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 특별하게 대해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 먼저 사진을 보여줘요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 부를 때 눈빛이 달라요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 조언을 해줘요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 믿어주는 것 같아요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 위해 노력해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 궁금한 게 많아 보여요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 의식하는 것 같아요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내 게시물에 댓글을 달아요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나에게 호감이 있다고 느껴져요", "options": [{"text": "전혀 없어요", "score": 1}, {"text": "조금 있어요", "score": 3}, {"text": "꽤 있어요", "score": 6}, {"text": "분명해요", "score": 10}]},
        {"text": "그 사람이 내게 먼저 농담해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 보며 미소 지어요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 관심 있는 척을 해요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나에게 시간을 많이 줘요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내 얘기를 먼저 꺼내요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 응원해주는 것 같아요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 호의를 보여요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나에게 질문을 많이 해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
    ],
    "20m": [
        {"text": "그 사람이 나에게 특별한 느낌을 줘요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 애교를 부려요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 위로해줘요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나에게 비밀을 얘기해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 솔직한 마음을 보여요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 먼저 생각해주는 것 같아요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 먼저 고민을 털어놔요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 믿고 의지해요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 무장해제가 돼요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 챙기는 게 느껴져요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 자신의 약점을 보여요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 향해 웃는 게 예뻐요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 먼저 사랑한다고 해요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 소중하게 여겨요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 모든 걸 보여줘요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 기다려줘요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 어린아이처럼 대해요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 돌봐주려 해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 내게 먼저 미래를 얘기해요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
        {"text": "그 사람이 나를 향해 걸어와요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔 그래요", "score": 3}, {"text": "자주 그래요", "score": 6}, {"text": "항상 그래요", "score": 10}]},
    ],
    "20l": [
        {"text": "그 사람이 나에게 인생을 걸었어요", "options": [{"text": "아니에요", "score": 1}, {"text": "조금은", "score": 4}, {"text": "꽤 그래요", "score": 7}, {"text": "분명해요", "score": 10}]},
        {"text": "그 사람이 나를 위해 삶을 바꿨어요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이 그래요", "score": 6}, {"text": "완전히 그래요", "score": 10}]},
        {"text": "그 사람이 내게 평생을 약속했어요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔", "score": 3}, {"text": "자주", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 나를 평생 지켜줄 것 같아요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 모든 것을 맡겼어요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔", "score": 3}, {"text": "자주", "score": 6}, {"text": "항상", "score": 10}]},
        {"text": "그 사람이 나에게 헌신해요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "가끔", "score": 3}, {"text": "자주", "score": 6}, {"text": "항상", "score": 10}]},
        {"text": "그 사람이 나를 위해 미래를 포기할 수 있어요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 가족이 되고 싶다고 해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔", "score": 3}, {"text": "자주", "score": 6}, {"text": "항상", "score": 10}]},
        {"text": "그 사람이 나를 영원한 동반자라고 생각해요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 늙음까지 함께하자고 해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔", "score": 3}, {"text": "자주", "score": 6}, {"text": "항상", "score": 10}]},
        {"text": "그 사람이 나를 위해 무엇이든 할 수 있어요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 뿌리를 내렸어요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔", "score": 3}, {"text": "자주", "score": 6}, {"text": "완전히", "score": 10}]},
        {"text": "그 사람이 나를 세상에서 가장 특별하게 여겨요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 평생을 함께하겠다고 약속했어요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔", "score": 3}, {"text": "자주", "score": 6}, {"text": "확실히", "score": 10}]},
        {"text": "그 사람이 나를 위해서라면 포기할 것이 없어요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 영원을 걸었어요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔", "score": 3}, {"text": "자주", "score": 6}, {"text": "확실히", "score": 10}]},
        {"text": "그 사람이 나를 인생의 마지막 사랑이라고 해요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 안식처가 되어줘요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔", "score": 3}, {"text": "자주", "score": 6}, {"text": "항상", "score": 10}]},
        {"text": "그 사람이 나를 위한 인생을 살고 있어요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 최고의 사랑을 줘요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔", "score": 3}, {"text": "자주", "score": 6}, {"text": "항상", "score": 10}]},
    ],
    "30": [
        {"text": "그 사람이 나에게 깊은 신뢰를 보여요", "options": [{"text": "전혀 안 그래요", "score": 1}, {"text": "조금", "score": 3}, {"text": "많이", "score": 6}, {"text": "완전히", "score": 10}]},
        {"text": "그 사람이 나를 위해 삶을 바꾸려 해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "조금", "score": 3}, {"text": "많이", "score": 6}, {"text": "전적으로", "score": 10}]},
        {"text": "그 사람이 내게 인생의 동반자가 되어줬어요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "완전히", "score": 10}]},
        {"text": "그 사람이 나를 위해 영원히 남을 거예요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 자신의 모든 것을 걸었어요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "조금", "score": 3}, {"text": "많이", "score": 6}, {"text": "전부", "score": 10}]},
        {"text": "그 사람이 나를 삶의 전부로 여겨요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "완전히", "score": 10}]},
        {"text": "그 사람이 내게 살아있는 이유라고 해요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "가끔", "score": 3}, {"text": "자주", "score": 6}, {"text": "항상", "score": 10}]},
        {"text": "그 사람이 나를 위해 세상과 맞서줄 거예요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 숨 쉴 이유를 줬어요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "조금", "score": 3}, {"text": "많이", "score": 6}, {"text": "전부", "score": 10}]},
        {"text": "그 사람이 나를 위험에서 지켜줄 거예요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 삶의 의미를 줬어요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "조금", "score": 3}, {"text": "많이", "score": 6}, {"text": "전부", "score": 10}]},
        {"text": "그 사람이 나를 죽을 때까지 사랑할 거예요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 세상 다 줬어요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "조금", "score": 3}, {"text": "많이", "score": 6}, {"text": "전부", "score": 10}]},
        {"text": "그 사람이 나를 향해 걸어와줄 거예요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 삶을 다 걸었어요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "조금", "score": 3}, {"text": "많이", "score": 6}, {"text": "전부", "score": 10}]},
        {"text": "그 사람이 나를 위해 천국도 갈 수 있어요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 삶을 바쳤어요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "조금", "score": 3}, {"text": "많이", "score": 6}, {"text": "전부", "score": 10}]},
        {"text": "그 사람이 나를 영원히 기억할 거예요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
        {"text": "그 사람이 내게 모든 것을 맡겼어요", "options": [{"text": "그런 적 없어요", "score": 1}, {"text": "조금", "score": 3}, {"text": "많이", "score": 6}, {"text": "전부", "score": 10}]},
        {"text": "그 사람이 나를 위해 목숨도 바칠 수 있어요", "options": [{"text": "전혀 아니에요", "score": 1}, {"text": "조금은", "score": 3}, {"text": "많이", "score": 6}, {"text": "분명히", "score": 10}]},
    ]
}

# Keep sum and self from v15 (without locations), rewrite other
v16 = {
    "version": "16.0",
    "totalQuestions": 600,
    "combinations": {}
}

combinations = ['10F', '10M', '20eF', '20eM', '20mF', '20mM', '20lF', '20lM', '30F', '30M']

for combo in combinations:
    key_base = combo.replace('F', '').replace('M', '')
    key_other = '10' if key_base == '10' else ('20e' if key_base == '20e' else ('20m' if key_base == '20m' else ('20l' if key_base == '20l' else '30')))
    
    v16['combinations'][combo] = {
        "sum": [],
        "self": [],
        "other": []
    }
    
    # Copy sum and self from v15 (filter out locations)
    for category in ['sum', 'self']:
        if category in v15['combinations'][combo]:
            for q in v15['combinations'][combo][category]:
                if not has_location(q['text']):
                    v16['combinations'][combo][category].append(q)
    
    # Replace other with new questions
    other_questions = OTHER_QUESTIONS_BANK.get(key_other, OTHER_QUESTIONS_BANK['10'])
    v16['combinations'][combo]['other'] = other_questions[:20]

# Save v16
output_path = '/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-v16.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(v16, f, ensure_ascii=False, indent=2)

print(f"✅ v16 saved to: {output_path}")
print(f"\n📊 Question counts per combination:")
for combo in combinations:
    if combo in v16['combinations']:
        s = len(v16['combinations'][combo]['sum'])
        se = len(v16['combinations'][combo]['self'])
        o = len(v16['combinations'][combo]['other'])
        print(f"  {combo}: sum={s}, self={se}, other={o}, total={s+se+o}")

# Verify no locations
print("\n🔍 Verifying no location references...")
location_found = False
for combo in combinations:
    for category in ['sum', 'self', 'other']:
        for q in v16['combinations'][combo][category]:
            if has_location(q['text']):
                print(f"  ❌ Location found: {combo}/{category}: {q['text']}")
                location_found = True
if not location_found:
    print("  ✅ No location references found")

# Verify other category focuses on "그 사람이 나를"
print("\n🔍 Verifying 'other' category format...")
other_issues = []
for combo in combinations:
    for q in v16['combinations'][combo]['other']:
        text = q['text']
        # Check if starts with 그 사람이
        if not text.startswith('그 사람이'):
            other_issues.append(f"  ⚠️ {combo}/other: '{text[:30]}...'")

if other_issues:
    print(f"  Found {len(other_issues)} questions not starting with '그 사람이'")
    for issue in other_issues[:5]:
        print(issue)
else:
    print("  ✅ All 'other' questions start with '그 사람이'")
