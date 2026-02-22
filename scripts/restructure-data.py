#!/usr/bin/env python3
"""
SomeThing 데이터 재구성 스크립트
- 정확히 40개 조합 (5×2×4)
- 각 테스트 10문항 (sum/self/other 각각 10개)
- 총 문항: 40×3×10 = 1,200개
"""

import json
import os

# 파일 경로
INPUT_FILE = "/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-v3.json"
OUTPUT_FILE = "/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-v4.json"

# 40개 조합 정의
AGE_GROUPS = ["10", "20e", "20m", "20l", "30"]
GENDERS = ["F", "M"]
TYPES = ["D", "C", "R", "P"]

# 조합별 이름 매핑
COMBINATION_NAMES = {
    "10F_D": "10대_여성_직진파",
    "10F_C": "10대_여성_신중파",
    "10F_R": "10대_여성_합리파",
    "10F_P": "10대_여성_감성파",
    "10M_D": "10대_남성_직진파",
    "10M_C": "10대_남성_신중파",
    "10M_R": "10대_남성_합리파",
    "10M_P": "10대_남성_감성파",
    "20eF_D": "20대초반_여성_직진파",
    "20eF_C": "20대초반_여성_신중파",
    "20eF_R": "20대초반_여성_합리파",
    "20eF_P": "20대초반_여성_감성파",
    "20eM_D": "20대초반_남성_직진파",
    "20eM_C": "20대초반_남성_신중파",
    "20eM_R": "20대초반_남성_합리파",
    "20eM_P": "20대초반_남성_감성파",
    "20mF_D": "20대중반_여성_직진파",
    "20mF_C": "20대중반_여성_신중파",
    "20mF_R": "20대중반_여성_합리파",
    "20mF_P": "20대중반_여성_감성파",
    "20mM_D": "20대중반_남성_직진파",
    "20mM_C": "20대중반_남성_신중파",
    "20mM_R": "20대중반_남성_합리파",
    "20mM_P": "20대중반_남성_감성파",
    "20lF_D": "20대후반_여성_직진파",
    "20lF_C": "20대후반_여성_신중파",
    "20lF_R": "20대후반_여성_합리파",
    "20lF_P": "20대후반_여성_감성파",
    "20lM_D": "20대후반_남성_직진파",
    "20lM_C": "20대후반_남성_신중파",
    "20lM_R": "20대후반_남성_합리파",
    "20lM_P": "20대후반_남성_감성파",
    "30F_D": "30대_여성_직진파",
    "30F_C": "30대_여성_신중파",
    "30F_R": "30대_여성_합리파",
    "30F_P": "30대_여성_감성파",
    "30M_D": "30대_남성_직진파",
    "30M_C": "30대_남성_신중파",
    "30M_R": "30대_남성_합리파",
    "30M_P": "30대_남성_감성파",
}

# 조합별 프로필 매핑
COMBINATION_PROFILES = {
    "10F_D": "설렘과 적극성으로 가득찬 10대 여학생. 첫사랑의 두근거림을 적극적으로 표현하고 팔로우하며, 친구들의 응원과 조언을 매우 중요하게 여깁니다. SNS에서 자연스럽게 댓글과 좋아요를 주고받으며, 학교나 학원에서의 만남을 기대하고 계획합니다. 친구들의 반응에 따라 관계의 행방이 좌우되기도 합니다.",
    "10F_C": "관찰과 신중함으로 상대의 마음을 살피는 10대 여학생. 집단 속에서의 위치와 친구들의 시선을 의식하며, 무모한 행동보다는 분위기와 간접적인 신호를 해석하려 합니다. 학교와 학원 등 일상 속에서의 소소한 상호작용을 중요하게 여기며, 상대의 반응을 꼼꼼히 분석합니다.",
    "10F_R": "현실적 조건과 상황을 우선으로 고려하는 10대 여학생. 성적, 진로, 학부모의 시선 등 실제적인 제약을 따지며 감정을 분석합니다. 드문 만남 속에서도 가능성을 계산하고, 친구들의 조언과 객관적 사실을 중시합니다. SNS보다는 현실의 상호작용을 더 신뢰하며, 미래 가능성을 함께 고려합니다.",
    "10F_P": "감정과 분위기, 순수한 마음을 중시하는 10대 여학생. 첫사랑의 설렘과 순수함을 소중하게 여기며, 작은 순간의 감정과 분위기에 깊게 몰입합니다. SNS를 통해 서로의 감정을 읽으려 하고, 학교에서의 우연한 만남이나 학원에서의 대화 하나에도 큰 의미를 부여합니다. 친구들과의 교감을 통해 감정을 확인하려 합니다.",
    "10M_D": "적극적이고 경쟁심 강한 10대 남학생. 외모와 첫인상을 중시하며, 친구들 사이에서 인정받는 관계를 원합니다. 학교나 학원에서의 직접적인 상호작용을 선호하고, 상대의 반응을 명확히 알고 싶어 합니다. SNS에서도 적극적으로 표현하며, 친구들의 호응과 응원을 동력으로 삼습니다.",
    "10M_C": "관찰과 신중함으로 상대를 지켜보는 10대 남학생. 학교나 학원에서의 분위기와 상대의 미묘한 반응을 꼼꼼히 살피며, 무모한 행동보다는 적절한 타이밍을 기다립니다. 친구들의 시선을 의식하면서도 자신의 감정을 숨기려 노력하며, 신중하게 관계의 가능성을 탐색합니다.",
    "10M_R": "조건과 현실을 따지며 감정을 분석하는 10대 남학생. 성적, 진로, 학부모의 시선 등 실제적인 제약을 고려하며 관계를 생각합니다. 학교나 학원에서의 만남 가능성과 미래의 방향성을 함께 따지며, 친구들의 조언과 객관적 사실을 중시합니다. 드문 만남 속에서도 가능성을 계산합니다.",
    "10M_P": "감정과 순수한 마음을 중시하는 10대 남학생. 첫사랑의 설렘을 소중하게 여기며, 작은 순간의 감정에 깊게 몰입합니다. 학교에서의 우연한 만남이나 학원에서의 대화 하나에도 큰 의미를 부여하고, 친구들과의 교감을 통해 감정을 확인하려 합니다. 서정적인 분위기를 좋아합니다.",
    "20eF_D": "대학생, 적극적, 설렘 추구, 바로 행동",
    "20eF_C": "대학생, 신중함, 관찰 중시, 확실한 신호 필요",
    "20eF_R": "대학생, 현실적, 조건 따지지만 설렘도 중요",
    "20eF_P": "대학생, 감성적, 분위기 중시, 설렘 추구",
    "20eM_D": "대학생, 적극적, 경쟁적, 성과 중시",
    "20eM_C": "대학생, 신중고박, 진심 파악 중",
    "20eM_R": "대학생, 현실적, 효율 중시, 조건 따짐",
    "20eM_P": "대학생, 감성 충만, 설렘 우선",
    "20mF_D": "사회초년생, 직진, 일은 일 연애는 연애",
    "20mF_C": "사회초년생, 신중, 안정 추구, 깊은 관계 선호",
    "20mF_R": "사회초년생, 현실적, 조건 따짐, 안정 추구",
    "20mF_P": "사회초년생, 감성적, 깊은 관계, 분위기 중시",
    "20mM_D": "사회초년생, 적극적, 성과 중시, 빠른 진행",
    "20mM_C": "사회초년생, 진지사귐, 미래까지 생각중",
    "20mM_R": "사회초년생, 현실적, 효율 중시, 조건 따짐",
    "20mM_P": "사회초년생, 감성적, 안정 속 설렘",
    "20lF_D": "결혼고려, 적극, 안정",
    "20lF_C": "결혼고려, 신중, 확신",
    "20lF_R": "결혼고려, 현실, 조건",
    "20lF_P": "결혼고려, 감정, 진정",
    "20lM_D": "결혼고려, 적극, 성과",
    "20lM_C": "결혼고려, 신중, 검증",
    "20lM_R": "결혼고려, 현실, 효율",
    "20lM_P": "결혼고려, 감정, 안정",
    "30F_D": "현실, 적극, 빠른결정",
    "30F_C": "현실, 신중, 확실",
    "30F_R": "현실, 조건, 효율",
    "30F_P": "현실, 감정, 안정",
    "30M_D": "현실, 적극, 성과",
    "30M_C": "현실, 신중, 검증",
    "30M_R": "현실, 효율, 조건",
    "30M_P": "현실, 감정, 가족",
}

def load_json(filepath):
    """JSON 파일 로드"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    """JSON 파일 저장"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def create_question_structure(text, options_data):
    """질문 구조 생성"""
    options = []
    for opt_text, score in options_data:
        options.append({"text": opt_text, "score": score})
    return {"text": text, "options": options}

def get_default_questions(combo_key, test_type):
    """기본 질문 생성"""
    # 테스트 유형별 기본 질문 템플릿
    if test_type == "sum":
        return [
            "함께하는 미래를 상상해본 적이 있나요? 이건 썸인가요?",
            "친구들이 우리 사이를 특별하다고 하는데 이건 썸인가요?",
            "다른 이성 언급했을 때 서로의 반응이 특별했나요? 이건 썸인가요?",
            "사소한 일도 서로 먼저 공유하나요? 이건 썸이겠죠?",
            "다투거나 어려울 때 서로를 배려하나요? 이건 썸인가요?",
            "상대가 나를 특별하게 대하나요? 이건 썸인가요?",
            "함께 있을 때 시간이 빨리 가나요? 이건 썸인가요?",
            "상대의 작은 행동에도 설레나요? 이건 썸인가요?",
            "서로의 눈빛이 특별한가요? 이건 썸인가요?"
        ]
    elif test_type == "self":
        return [
            "얼마나 진심인지 스스로 확인해본 적 있나요?",
            "얼마나 기다릴 수 있을 것 같나요?",
            "얼마까지 양보할 수 있을 것 같나요? 이건 좋아하는 거죠?",
            "실패해도 후회 없을 것 같나요? 진짜 좋아하는 건가요?",
            "다른 사람과 비교해도 이 사람이 최고인가요?",
            "이 사람 생각나는 빈도는?",
            "연락 왔을 때 내 기분은?",
            "이 사람과 미래를 상상해본 적?",
            "다른 이성 언급 시 내 심정은?",
            "고백하고 싶은 충동이?"
        ]
    else:  # other
        return [
            "상대가 진심인 것 같나요?",
            "상대가 얼마나 노력하는 것 같나요?",
            "내가 더 노력하는 느낌인가요? 아니면 상대도 그런가요?",
            "상대의 미래 계획에 내가 포함되어 있나요?",
            "나 말고 다른 사람도 가능할 것 같나요?",
            "상대가 나를 특별하게 대하나요?",
            "상대가 나를 얼마나 이해하나요?",
            "상대가 나에게 시간을 투자하나요?",
            "상대가 나를 위해 배려하나요?",
            "상대가 나에 대해 진심인 것 같나요?"
        ]

def create_default_combination(combo_key, name, profile):
    """기본 조합 데이터 생성"""
    return {
        "name": name,
        "profile": profile,
        "sum": get_default_questions(combo_key, "sum"),
        "self": get_default_questions(combo_key, "self"),
        "other": get_default_questions(combo_key, "other")
    }

def restructure_data():
    """데이터 재구성 메인 함수"""
    # 기존 데이터 로드
    old_data = load_json(INPUT_FILE)
    old_combinations = old_data.get("combinations", {})
    
    # 새 데이터 구조 생성
    new_combinations = {}
    
    # 40개 조합 생성
    for age in AGE_GROUPS:
        for gender in GENDERS:
            for type_code in TYPES:
                combo_key = f"{age}{gender}_{type_code}"
                
                # 기존 데이터에서 찾기
                if combo_key in old_combinations:
                    # 기존 데이터 사용 (10문항으로 제한)
                    old_combo = old_combinations[combo_key]
                    new_combinations[combo_key] = {
                        "name": old_combo.get("name", COMBINATION_NAMES.get(combo_key, combo_key)),
                        "profile": old_combo.get("profile", ""),
                        "sum": old_combo.get("sum", [])[:10],
                        "self": old_combo.get("self", [])[:10],
                        "other": old_combo.get("other", [])[:10]
                    }
                else:
                    # 새로운 조합 생성
                    # 유사한 기존 조합에서 데이터 가져오기
                    source_key = None
                    if age == "20e":
                        if gender == "F":
                            source_key = "20F_D" if type_code == "D" else ("20F_C" if type_code == "C" else "20F_P")
                        else:
                            source_key = "20M_D" if type_code == "D" else ("20M_R" if type_code == "R" else "20M_P")
                    elif age == "20m":
                        if gender == "F":
                            source_key = "25F_C" if type_code == "C" else ("25F_R" if type_code == "R" else "25F_P")
                        else:
                            source_key = "25M_D" if type_code == "D" else ("25M_R" if type_code == "R" else "25M_P")
                    
                    if source_key and source_key in old_combinations:
                        source = old_combinations[source_key]
                        new_combinations[combo_key] = {
                            "name": COMBINATION_NAMES.get(combo_key, combo_key),
                            "profile": source.get("profile", ""),
                            "sum": source.get("sum", [])[:10],
                            "self": source.get("self", [])[:10],
                            "other": source.get("other", [])[:10]
                        }
                    else:
                        # 기본 데이터 생성
                        new_combinations[combo_key] = create_default_combination(
                            combo_key,
                            COMBINATION_NAMES.get(combo_key, combo_key),
                            COMBINATION_PROFILES.get(combo_key, "")
                        )
    
    # 메타데이터 업데이트
    new_metadata = {
        "version": "4.0",
        "created": "2026-02-21",
        "combinations": 40,
        "tests_per_combination": 3,
        "questions_per_test": 10,
        "total_question_sets": 120,
        "total_questions": 1200,
        "updated": "2026-02-21"
    }
    
    # 새 데이터 구조
    new_data = {
        "metadata": new_metadata,
        "combinations": new_combinations
    }
    
    # 저장
    save_json(OUTPUT_FILE, new_data)
    
    # 검증
    print(f"\n=== 검증 결과 ===")
    print(f"총 조합 수: {len(new_combinations)}")
    
    valid_count = 0
    for combo_key, combo_data in new_combinations.items():
        sum_count = len(combo_data.get("sum", []))
        self_count = len(combo_data.get("self", []))
        other_count = len(combo_data.get("other", []))
        
        if sum_count == 10 and self_count == 10 and other_count == 10:
            valid_count += 1
        else:
            print(f"  {combo_key}: sum={sum_count}, self={self_count}, other={other_count}")
    
    print(f"유효한 조합: {valid_count}/40")
    print(f"\n출력 파일: {OUTPUT_FILE}")

if __name__ == "__main__":
    restructure_data()
