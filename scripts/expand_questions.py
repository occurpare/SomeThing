#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SomeThing 질문지 확장 스크립트
각 테스트(sum, self, other)를 10문항으로 확장
"""

import json
import os

# 추가 질문 템플릿
ADDITIONAL_QUESTIONS = {
    "sum": [
        {
            "text": "다른 이성을 언급했을 때 상대의 반응은?",
            "options": [
                {"text": "질투하거나 신경 쓰는 모습", "score": 10},
                {"text": "조금 신경 쓰는 듯", "score": 7},
                {"text": "별 반응 없음", "score": 4},
                {"text": "오히려 좋아함", "score": 0}
            ]
        },
        {
            "text": "사소한 일도 서로 공유하나요?",
            "options": [
                {"text": "매일매일 작은 일도 공유", "score": 10},
                {"text": "자주 공유함", "score": 7},
                {"text": "가끔 공유함", "score": 4},
                {"text": "거의 안 함", "score": 0}
            ]
        },
        {
            "text": "다투거나 어려운 상황에서 서로의 반응은?",
            "options": [
                {"text": "서로를 배려하며 극복함", "score": 10},
                {"text": "대화로 풀려고 함", "score": 7},
                {"text": "시간이 필요함", "score": 4},
                {"text": "피하거나 멀어짐", "score": 0}
            ]
        }
    ],
    "self": [
        {
            "text": "이 사람을 위해 얼마까지 양보할 수 있나요?",
            "options": [
                {"text": "원칙까지도 바꿀 수 있음", "score": 10},
                {"text": "상당히 양보 가능", "score": 7},
                {"text": "보통 수준", "score": 4},
                {"text": "거의 양보 못함", "score": 0}
            ]
        },
        {
            "text": "실패하더라도 후회 없을 것 같나요?",
            "options": [
                {"text": "전혀 후회 없을 것 같음", "score": 10},
                {"text": "후회는 별로 안 할 듯", "score": 7},
                {"text": "모르겠음", "score": 4},
                {"text": "후회할 것 같음", "score": 0}
            ]
        },
        {
            "text": "다른 사람과 비교했을 때 이 사람은?",
            "options": [
                {"text": "비교 자체가 안 됨", "score": 10},
                {"text": "확실히 더 나음", "score": 7},
                {"text": "비슷함", "score": 4},
                {"text": "더 나은 사람 있음", "score": 0}
            ]
        }
    ],
    "other": [
        {
            "text": "노력의 균형은 어떤가요?",
            "options": [
                {"text": "상대가 더 많이 하는 느낌", "score": 10},
                {"text": "비슷하게 하는 느낌", "score": 7},
                {"text": "내가 조금 더 하는 느낌", "score": 4},
                {"text": "내가 훨씬 더 하는 느낌", "score": 0}
            ]
        },
        {
            "text": "상대의 미래 계획에 나는 포함되어 있나요?",
            "options": [
                {"text": "명확하게 포함됨", "score": 10},
                {"text": "암시적으로 포함됨", "score": 7},
                {"text": "모르겠음", "score": 4},
                {"text": "제외된 느낌", "score": 0}
            ]
        },
        {
            "text": "나 말고 다른 사람도 가능할 것 같나요?",
            "options": [
                {"text": "절대 불가능할 것 같음", "score": 10},
                {"text": "어려울 것 같음", "score": 7},
                {"text": "모르겠음", "score": 4},
                {"text": "다른 사람도 가능할 것 같음", "score": 0}
            ]
        }
    ]
}

def load_json(filepath):
    """JSON 파일 로드"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    """JSON 파일 저장"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def expand_questions(data):
    """각 테스트별로 10문항이 되도록 확장"""
    expanded = {
        "metadata": {
            **data["metadata"],
            "version": "3.0",
            "updated": "2026-02-21",
            "total_questions": 1200
        },
        "combinations": {}
    }
    
    for combo_key, combo_data in data["combinations"].items():
        expanded["combinations"][combo_key] = {
            "name": combo_data["name"],
            "profile": combo_data["profile"],
        }
        
        for test_type in ["sum", "self", "other"]:
            existing = combo_data.get(test_type, [])
            
            # 기존 질문이 객체 형태인지 문자열 형태인지 확인
            if existing and isinstance(existing[0], str):
                # 문자열 형태 - 10대 질문들
                # 10대 질문은 이미 충분히 있으므로 그대로 유지
                # 하지만 10개가 안 되는 경우 추가
                if len(existing) < 10:
                    # 추가 질문 생성 (간단한 문자열 형태)
                    additional = generate_simple_questions(test_type, 10 - len(existing))
                    existing = existing + additional
                expanded["combinations"][combo_key][test_type] = existing[:10]
            else:
                # 객체 형태 - 20대 이상 질문들
                current_count = len(existing)
                needed = 10 - current_count
                
                if needed > 0:
                    # 추가 질문 가져오기
                    additional = ADDITIONAL_QUESTIONS[test_type][:needed]
                    existing = existing + additional
                
                expanded["combinations"][combo_key][test_type] = existing[:10]
    
    return expanded

def generate_simple_questions(test_type, count, age_group="10"):
    """간단한 문자열 형태의 추가 질문 생성 (10대용)"""
    templates = {
        "sum": [
            "다른 이성 언급했을 때 서로의 반응이 특별했나요? 이건 썸인가요?",
            "사소한 일도 서로 먼저 공유하나요? 이건 썸이겠죠?",
            "다투거나 어려울 때 서로를 배려하나요? 이건 썸인가요?"
        ],
        "self": [
            "얼마까지 양보할 수 있을 것 같나요? 이건 좋아하는 거죠?",
            "실패해도 후회 없을 것 같나요? 진짜 좋아하는 건가요?",
            "다른 사람과 비교해도 이 사람이 최고인가요?"
        ],
        "other": [
            "내가 더 노력하는 느낌인가요? 아니면 상대도 그런가요?",
            "상대의 미래 계획에 내가 포함되어 있나요?",
            "나 말고 다른 사람도 가능할 것 같나요?"
        ]
    }
    return templates[test_type][:count]

def generate_object_questions(test_type, count, age_group="20"):
    """객체 형태의 추가 질문 생성 (20대 이상용)"""
    templates = {
        "sum": [
            {
                "text": "다른 이성을 언급했을 때 상대의 반응은?",
                "options": [
                    {"text": "질투하거나 신경 쓰는 모습", "score": 10},
                    {"text": "조금 신경 쓰는 듯", "score": 7},
                    {"text": "별 반응 없음", "score": 4},
                    {"text": "오히려 좋아함", "score": 0}
                ]
            },
            {
                "text": "사소한 일도 서로 공유하나요?",
                "options": [
                    {"text": "매일매일 작은 일도 공유", "score": 10},
                    {"text": "자주 공유함", "score": 7},
                    {"text": "가끔 공유함", "score": 4},
                    {"text": "거의 안 함", "score": 0}
                ]
            },
            {
                "text": "다투거나 어려운 상황에서 서로의 반응은?",
                "options": [
                    {"text": "서로를 배려하며 극복함", "score": 10},
                    {"text": "대화로 풀려고 함", "score": 7},
                    {"text": "시간이 필요함", "score": 4},
                    {"text": "피하거나 멀어짐", "score": 0}
                ]
            }
        ],
        "self": [
            {
                "text": "이 사람을 위해 얼마까지 양보할 수 있나요?",
                "options": [
                    {"text": "원칙까지도 바꿀 수 있음", "score": 10},
                    {"text": "상당히 양보 가능", "score": 7},
                    {"text": "보통 수준", "score": 4},
                    {"text": "거의 양보 못함", "score": 0}
                ]
            },
            {
                "text": "실패하더라도 후회 없을 것 같나요?",
                "options": [
                    {"text": "전혀 후회 없을 것 같음", "score": 10},
                    {"text": "후회는 별로 안 할 듯", "score": 7},
                    {"text": "모르겠음", "score": 4},
                    {"text": "후회할 것 같음", "score": 0}
                ]
            },
            {
                "text": "다른 사람과 비교했을 때 이 사람은?",
                "options": [
                    {"text": "비교 자체가 안 됨", "score": 10},
                    {"text": "확실히 더 나음", "score": 7},
                    {"text": "비슷함", "score": 4},
                    {"text": "더 나은 사람 있음", "score": 0}
                ]
            }
        ],
        "other": [
            {
                "text": "노력의 균형은 어떤가요?",
                "options": [
                    {"text": "상대가 더 많이 하는 느낌", "score": 10},
                    {"text": "비슷하게 하는 느낌", "score": 7},
                    {"text": "내가 조금 더 하는 느낌", "score": 4},
                    {"text": "내가 훨씬 더 하는 느낌", "score": 0}
                ]
            },
            {
                "text": "상대의 미래 계획에 나는 포함되어 있나요?",
                "options": [
                    {"text": "명확하게 포함됨", "score": 10},
                    {"text": "암시적으로 포함됨", "score": 7},
                    {"text": "모르겠음", "score": 4},
                    {"text": "제외된 느낌", "score": 0}
                ]
            },
            {
                "text": "나 말고 다른 사람도 가능할 것 같나요?",
                "options": [
                    {"text": "절대 불가능할 것 같음", "score": 10},
                    {"text": "어려울 것 같음", "score": 7},
                    {"text": "모르겠음", "score": 4},
                    {"text": "다른 사람도 가능할 것 같음", "score": 0}
                ]
            }
        ]
    }
    return templates[test_type][:count]

def load_json(filepath):
    """JSON 파일 로드"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    """JSON 파일 저장"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def expand_questions(data):
    """각 테스트별로 10문항이 되도록 확장"""
    expanded = {
        "metadata": {
            **data["metadata"],
            "version": "3.0",
            "updated": "2026-02-21",
            "total_questions": 1200
        },
        "combinations": {}
    }
    
    for combo_key, combo_data in data["combinations"].items():
        expanded["combinations"][combo_key] = {
            "name": combo_data["name"],
            "profile": combo_data["profile"],
        }
        
        for test_type in ["sum", "self", "other"]:
            existing = combo_data.get(test_type, [])
            
            # 기존 질문이 객체 형태인지 문자열 형태인지 확인
            if existing and isinstance(existing[0], str):
                # 문자열 형태 - 10대 질문들
                if len(existing) < 10:
                    additional = generate_simple_questions(test_type, 10 - len(existing))
                    existing = existing + additional
                expanded["combinations"][combo_key][test_type] = existing[:10]
            else:
                # 객체 형태 - 20대 이상 질문들
                current_count = len(existing)
                needed = 10 - current_count
                
                if needed > 0:
                    # 더 많은 추가 질문 생성
                    additional = generate_object_questions(test_type, needed)
                    # 추가 질문이 부족하면 더 생성
                    if len(additional) < needed:
                        extra = generate_more_questions(test_type, needed - len(additional))
                        additional = additional + extra
                    existing = existing + additional
                
                expanded["combinations"][combo_key][test_type] = existing[:10]
    
    return expanded

def generate_more_questions(test_type, count):
    """추가 질문이 더 필요할 때 생성"""
    extra_templates = {
        "sum": [
            {
                "text": "위기 상황에서 서로를 의지하나요?",
                "options": [
                    {"text": "서로를 먼저 생각함", "score": 10},
                    {"text": "의지하게 됨", "score": 7},
                    {"text": "가끔 의지함", "score": 4},
                    {"text": "의지하지 않음", "score": 0}
                ]
            },
            {
                "text": "일상 속에서 특별함을 느끼나요?",
                "options": [
                    {"text": "항상 특별함", "score": 10},
                    {"text": "자주 느낌", "score": 7},
                    {"text": "가끔 느낌", "score": 4},
                    {"text": "별로 없음", "score": 0}
                ]
            },
            {
                "text": "서로에 대한 배려가 자연스럽나요?",
                "options": [
                    {"text": "매우 자연스러움", "score": 10},
                    {"text": "자연스러움", "score": 7},
                    {"text": "보통", "score": 4},
                    {"text": "어색함", "score": 0}
                ]
            }
        ],
        "self": [
            {
                "text": "이 사람 없이도 괜찮을 것 같나요?",
                "options": [
                    {"text": "상상도 안 됨", "score": 10},
                    {"text": "힘들 것 같음", "score": 7},
                    {"text": "적응할 수 있을 듯", "score": 4},
                    {"text": "괜찮을 것 같음", "score": 0}
                ]
            },
            {
                "text": "이 감정이 일시적이라고 생각하나요?",
                "options": [
                    {"text": "절대 일시적이 아님", "score": 10},
                    {"text": "오래갈 것 같음", "score": 7},
                    {"text": "모르겠음", "score": 4},
                    {"text": "일시적일 것 같음", "score": 0}
                ]
            },
            {
                "text": "이 사람을 위해 포기할 수 있는 것이 있나요?",
                "options": [
                    {"text": "무엇이든 포기 가능", "score": 10},
                    {"text": "중요한 것도 포기 가능", "score": 7},
                    {"text": "작은 것 정도", "score": 4},
                    {"text": "포기할 수 없음", "score": 0}
                ]
            }
        ],
        "other": [
            {
                "text": "상대가 나를 특별하게 대하나요?",
                "options": [
                    {"text": "매우 특별하게 대함", "score": 10},
                    {"text": "특별하게 대함", "score": 7},
                    {"text": "보통", "score": 4},
                    {"text": "평범하게 대함", "score": 0}
                ]
            },
            {
                "text": "상대가 나를 얼마나 이해하나요?",
                "options": [
                    {"text": "완벽하게 이해함", "score": 10},
                    {"text": "잘 이해함", "score": 7},
                    {"text": "보통", "score": 4},
                    {"text": "잘 몰라줌", "score": 0}
                ]
            },
            {
                "text": "상대가 나를 위해 얼마나 노력하나요?",
                "options": [
                    {"text": "최선을 다함", "score": 10},
                    {"text": "많이 노력함", "score": 7},
                    {"text": "보통", "score": 4},
                    {"text": "거의 안 함", "score": 0}
                ]
            }
        ]
    }
    return extra_templates[test_type][:count]

def main():
    input_file = "/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-expanded.json"
    output_file = "/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-final.json"
    
    print("Loading questions-expanded.json...")
    data = load_json(input_file)
    
    print(f"Current total questions: {data['metadata']['total_questions']}")
    print(f"Current version: {data['metadata']['version']}")
    
    print("\nExpanding questions to 10 per test...")
    expanded = expand_questions(data)
    
    # 검증
    total = 0
    for combo_key, combo_data in expanded["combinations"].items():
        for test_type in ["sum", "self", "other"]:
            count = len(combo_data.get(test_type, []))
            if count != 10:
                print(f"Warning: {combo_key}.{test_type} has {count} questions (expected 10)")
            total += count
    
    print(f"\nNew total questions: {total}")
    
    print(f"\nSaving to {output_file}...")
    save_json(output_file, expanded)
    
    # 파일 크기 확인
    size = os.path.getsize(output_file)
    print(f"File size: {size:,} bytes ({size/1024:.1f} KB)")
    
    print("\n✅ Done!")

if __name__ == "__main__":
    main()


def main():
    input_file = "/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-expanded.json"
    output_file = "/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-final.json"
    
    print("Loading questions-expanded.json...")
    data = load_json(input_file)
    
    print(f"Current total questions: {data['metadata']['total_questions']}")
    print(f"Current version: {data['metadata']['version']}")
    
    print("\nExpanding questions to 10 per test...")
    expanded = expand_questions(data)
    
    # 검증
    total = 0
    for combo_key, combo_data in expanded["combinations"].items():
        for test_type in ["sum", "self", "other"]:
            count = len(combo_data.get(test_type, []))
            if count != 10:
                print(f"Warning: {combo_key}.{test_type} has {count} questions (expected 10)")
            total += count
    
    print(f"\nNew total questions: {total}")
    
    print(f"\nSaving to {output_file}...")
    save_json(output_file, expanded)
    
    # 파일 크기 확인
    size = os.path.getsize(output_file)
    print(f"File size: {size:,} bytes ({size/1024:.1f} KB)")
    
    print("\n✅ Done!")

if __name__ == "__main__":
    main()
