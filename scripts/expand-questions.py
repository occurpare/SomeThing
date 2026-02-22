#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SomeThing 질문지 확장 스크립트
각 조합별 3개 테스트(sum, self, other)에 2-3개 질문 추가
"""

import json
import os

# 추가 질문 템플릿
ADDITIONAL_QUESTIONS = {
    "sum": [
        {
            "text": "함께 미래를 상상해본 적 있나요?",
            "options": [
                {"text": "구체적으로 상상함", "score": 10},
                {"text": "가끔 상상함", "score": 7},
                {"text": "얕게 상상함", "score": 4},
                {"text": "상상 안 함", "score": 0}
            ]
        },
        {
            "text": "주변 사람들이 우리 관계를 어떻게 보나요?",
            "options": [
                {"text": "벌써 커플이라고 함", "score": 10},
                {"text": "썸난다고 놀림", "score": 7},
                {"text": "잘 어울린다고 함", "score": 4},
                {"text": "그냥 친구라고 함", "score": 0}
            ]
        },
        {
            "text": "기억에 남는 특별한 순간이 있나요?",
            "options": [
                {"text": "여러 번 설렘", "score": 10},
                {"text": "한 번씩 설렘", "score": 7},
                {"text": "딱히 없음", "score": 4},
                {"text": "불편했음", "score": 0}
            ]
        }
    ],
    "self": [
        {
            "text": "얼마나 진심인 것 같나요?",
            "options": [
                {"text": "완전히 진심", "score": 10},
                {"text": "꽤 진심", "score": 7},
                {"text": "반반", "score": 4},
                {"text": "그냥 호기심", "score": 0}
            ]
        },
        {
            "text": "얼마나 양보해줄 수 있나요?",
            "options": [
                {"text": "최대한 양보", "score": 10},
                {"text": "꽤 양보", "score": 7},
                {"text": "보통", "score": 4},
                {"text": "잘 못함", "score": 0}
            ]
        },
        {
            "text": "함께할 미래에 자신 있나요?",
            "options": [
                {"text": "매우 확신", "score": 10},
                {"text": "꽤 확신", "score": 7},
                {"text": "반반", "score": 4},
                {"text": "불확실", "score": 0}
            ]
        }
    ],
    "other": [
        {
            "text": "상대의 진심이 느껴지나요?",
            "options": [
                {"text": "완전히 느껴짐", "score": 10},
                {"text": "느껴짐", "score": 7},
                {"text": "반반", "score": 4},
                {"text": "안 느껴짐", "score": 0}
            ]
        },
        {
            "text": "상대가 얼마나 투자하나요?",
            "options": [
                {"text": "매우 많이", "score": 10},
                {"text": "꽤 많이", "score": 7},
                {"text": "보통", "score": 4},
                {"text": "적게", "score": 0}
            ]
        },
        {
            "text": "상대의 미래 계획에 나는?",
            "options": [
                {"text": "구체적으로 포함", "score": 10},
                {"text": "포함되어 있음", "score": 7},
                {"text": "얕게 언급", "score": 4},
                {"text": "없음", "score": 0}
            ]
        }
    ]
}

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def expand_questions(data):
    """각 조합별로 3개 테스트에 2-3개 질문 추가"""
    combinations = data['combinations']
    
    total_added = 0
    
    for combo_key, combo_data in combinations.items():
        for test_type in ['sum', 'self', 'other']:
            if test_type not in combo_data:
                continue
            
            current_questions = combo_data[test_type]
            
            # 현재 질문 수 확인
            current_count = len(current_questions)
            
            # 추가할 질문 수 결정 (7-8개 목표)
            if current_count >= 7:
                continue  # 이미 충분함
            
            to_add = min(3, 8 - current_count)  # 최대 3개, 총 8개까지
            
            # 추가 질문 선택 (순환)
            additional = ADDITIONAL_QUESTIONS[test_type][:to_add]
            
            # 질문 추가
            current_questions.extend(additional)
            total_added += len(additional)
            
            print(f"  {combo_key}/{test_type}: {current_count} -> {len(current_questions)} (+{len(additional)})")
    
    return data, total_added

def main():
    input_path = '/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-full.json'
    output_path = '/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-expanded.json'
    
    print("Loading questions-full.json...")
    data = load_json(input_path)
    
    original_total = data['metadata']['total_questions']
    print(f"Original total questions: {original_total}")
    
    print("\nExpanding questions...")
    data, added = expand_questions(data)
    
    # 메타데이터 업데이트
    new_total = original_total + added
    data['metadata']['version'] = '2.1'
    data['metadata']['expanded'] = '2026-02-21'
    data['metadata']['total_questions'] = new_total
    data['metadata']['target_questions_per_test'] = '7-8'
    
    print(f"\nAdded {added} questions")
    print(f"New total: {new_total}")
    
    print(f"\nSaving to {output_path}...")
    save_json(output_path, data)
    
    # 파일 크기 확인
    size = os.path.getsize(output_path)
    print(f"File size: {size:,} bytes ({size/1024:.1f} KB)")
    
    print("\n✅ Done!")

if __name__ == '__main__':
    main()
