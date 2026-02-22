#!/usr/bin/env python3
"""
SomeThing - 고품질 테스트 질문 생성기 v10
40개 조합 x 30문항 = 총 1200개 질문
"""

import json
from collections import OrderedDict

def create_full_question_set():
    questions = OrderedDict()
    
    # ============================================
    # 10대 F (10F)
    # ============================================
    # 10F_D (10대 여성 직진형)
    questions["10F_D"] = [
        {"id": "10F_D_sum_01", "text": "좋아하는 사람이 있으면 눈 마주치는 순간 바로 다가가서 말 걸어요", "type": "sum"},
        {"id": "10F_D_sum_02", "text": "호감이 가는 사람 앞에서 자연스럽게 웃으며 먼저 인사해요", "type": "sum"},
        {"id": "10F_D_sum_03", "text": "애인이 생기면 바로 SNS에 사진 올리고 싶어요", "type": "sum"},
        {"id": "10F_D_sum_04", "text": "좋아하는 사람에게 전화번호를 먼저 물어보고 저장해요", "type": "sum"},
        {"id": "10F_D_sum_05", "text": "같은 반이나 동아리면 바로 옆자리로 가서 앉고 싶어요", "type": "sum"},
        {"id": "10F_D_sum_06", "text": "썸이 생기면 학교에서 만나자고 먼저 연락해요", "type": "sum"},
        {"id": "10F_D_sum_07", "text": "상대가 웃으면 바로 같이 웃으며 반응을 보여줘요", "type": "sum"},
        {"id": "10F_D_sum_08", "text": "좋아하면 친구들에게 당당하게 얘기하고 숨기지 않아요", "type": "sum"},
        {"id": "10F_D_sum_09", "text": "상대가 고백하면 상관없이 나도 바로 고백할 수 있어요", "type": "sum"},
        {"id": "10F_D_sum_10", "text": "학교 급식실에서도 먼저 옆에 와서 같이 먹자고 해요", "type": "sum"},
        {"id": "10F_D_self_01", "text": "설렘이 오면 마음속으로 신나하며 매일매일 즐겨요", "type": "self"},
        {"id": "10F_D_self_02", "text": "좋아하는 감정이 생기면 감추기보다 티내는 게 더 재밌어요", "type": "self"},
        {"id": "10F_D_self_03", "text": "감정을 순수하게 느낄 수 있어서 좋아하는 게 소중해요", "type": "self"},
        {"id": "10F_D_self_04", "text": "호감이 생기면 내 마음이 정말 좋은 거라고 믿어요", "type": "self"},
        {"id": "10F_D_self_05", "text": "감정이 크면 크게 표현하고 싶은 욕구가 강해져요", "type": "self"},
        {"id": "10F_D_self_06", "text": "누군가를 좋아하는 내 모습이 예쁘고 소중하게 느껴져요", "type": "self"},
        {"id": "10F_D_self_07", "text": "처음 느낀 감정이니까 두려움보다 즐거움이 더 커요", "type": "self"},
        {"id": "10F_D_self_08", "text": "설레는 마음을 친구들과 나누며 더 깊이 느껴요", "type": "self"},
        {"id": "10F_D_self_09", "text": "좋아하는 생각만 해도 얼굴에 미소가 지어지고 행복해요", "type": "self"},
        {"id": "10F_D_self_10", "text": "감정이 왔을 때 고민하기보다 느껴보는 게 당연해요", "type": "self"},
        {"id": "10F_D_other_01", "text": "상대가 나를 보며 웃으면 바로 좋아하는구나 알 수 있어요", "type": "other"},
        {"id": "10F_D_other_02", "text": "상대의 눈빛만 봐도 나에게 관심이 있는지 알겠어요", "type": "other"},
        {"id": "10F_D_other_03", "text": "상대가 먼저 다가오면 그건 확실한 신호라고 생각해요", "type": "other"},
        {"id": "10F_D_other_04", "text": "상대가 친구들에게 나에 대해 물어보면 답이 정해진 거예요", "type": "other"},
        {"id": "10F_D_other_05", "text": "상대의 메시지 답장이 빠르면 관심 있다고 바로 믿어요", "type": "other"},
        {"id": "10F_D_other_06", "text": "상대가 학교에서 자꾸 눈이 마주치면 고백할 타이밍이에요", "type": "other"},
        {"id": "10F_D_other_07", "text": "상대가 나를 보고 수줍어하는 게 딱 보여서 다 알아요", "type": "other"},
        {"id": "10F_D_other_08", "text": "상대가 내 생일을 챙겨주면 그건 100퍼센트예요", "type": "other"},
        {"id": "10F_D_other_09", "text": "상대가 다른 사람이랑 웃으면 바로 질투가 나요", "type": "other"},
        {"id": "10F_D_other_10", "text": "상대가 귀여운 이모티콘을 보내면 마음이 있다고 알아채요", "type": "other"},
    ]
    
    # 10F_C (10대 여성 신중형)
    questions["10F_C"] = [
        {"id": "10F_C_sum_01", "text": "좋아하는 사람이 있어도 눈 마주쳐도 먼저 다가가지 못하고 지켜봐요", "type": "sum"},
        {"id": "10F_C_sum_02", "text": "호감이 가는 사람 앞에서 기회를 엿보다가 늦게 다가가요", "type": "sum"},
        {"id": "10F_C_sum_03", "text": "애인이 생기면 일단 시간이 지나본 뒤에 SNS 공개를 고민해요", "type": "sum"},
        {"id": "10F_C_sum_04", "text": "좋아하는 사람에게 전화번호를 물어볼 때 여러 번 망설여요", "type": "sum"},
        {"id": "10F_C_sum_05", "text": "같은 반이면 상황을 보고 천천히 옆자리로 가요", "type": "sum"},
        {"id": "10F_C_sum_06", "text": "썸이 생기면 상대가 먼저 연락할 때까지 기다려봐요", "type": "sum"},
        {"id": "10F_C_sum_07", "text": "상대가 웃어도 진짜 웃는 건지 확인한 뒤에야 반응해요", "type": "sum"},
        {"id": "10F_C_sum_08", "text": "좋아해도 확실해질 때까지 친구들에게 조심스레 얘기해요", "type": "sum"},
        {"id": "10F_C_sum_09", "text": "상대가 고백하면 진심인지 몇 번 더 생각해보고 대답해요", "type": "sum"},
        {"id": "10F_C_sum_10", "text": "학교 급식실에서 자연스러운 상황이 될 때까지 기다려요", "type": "sum"},
        {"id": "10F_C_self_01", "text": "설렘이 오면 감정을 조금씩 느껴보며 천천히 익혀가요", "type": "self"},
        {"id": "10F_C_self_02", "text": "좋아하는 감정이 생기면 주변에 티가 안 나게 조심스레 간직해요", "type": "self"},
        {"id": "10F_C_self_03", "text": "감정이 생기면 진짜 좋아하는 건지 오래 고민해요", "type": "self"},
        {"id": "10F_C_self_04", "text": "호감이 생기면 진짜 마음인지 확신할 때까지 기다려요", "type": "self"},
        {"id": "10F_C_self_05", "text": "감정이 커도 표현하기 전에 이 감정이 옳은 건지 살펴봐요", "type": "self"},
        {"id": "10F_C_self_06", "text": "누군가를 좋아하는 내 모습이 서툴지만 소중하게 느껴져요", "type": "self"},
        {"id": "10F_C_self_07", "text": "처음 느껴보는 감정이라서 더 신중하게 다가가고 싶어요", "type": "self"},
        {"id": "10F_C_self_08", "text": "설레는 마음을 한참 혼자 음미해본 뒤에 누군가에게 말해요", "type": "self"},
        {"id": "10F_C_self_09", "text": "좋아하는 생각이 떠오를 때마다 조용히 미소 짓게 돼요", "type": "self"},
        {"id": "10F_C_self_10", "text": "감정이 왔을 때 충동적인 게 아닌지 한 번 더 곱씹어봐요", "type": "self"},
        {"id": "10F_C_other_01", "text": "상대가 나를 보며 웃어도 진짜 마음인지 계속 지켜봐요", "type": "other"},
        {"id": "10F_C_other_02", "text": "상대의 눈빛을 오랫동안 보고 진심인지 아닌지 확인해요", "type": "other"},
        {"id": "10F_C_other_03", "text": "상대가 다가오는 걸 여러 번 본 뒤에 안심이 돼요", "type": "other"},
        {"id": "10F_C_other_04", "text": "상대가 친구들에게 물어본다면 의도를 더 살펴봐야 해요", "type": "other"},
        {"id": "10F_C_other_05", "text": "상대의 메시지 답장 속도를 몇 주간 지켜본 뒤 알아차려요", "type": "other"},
        {"id": "10F_C_other_06", "text": "상대가 자꾸 눈이 마주친다면 우연이 아닌지 살펴봐요", "type": "other"},
        {"id": "10F_C_other_07", "text": "상대가 수줍어하는 모습을 몇 번 봐야 진심이라 생각해요", "type": "other"},
        {"id": "10F_C_other_08", "text": "상대가 생일을 챙겨줘도 우정인지 사랑인지 헷갈려요", "type": "other"},
        {"id": "10F_C_other_09", "text": "상대가 다른 사람이랑 웃어도 우연일 수 있어서 지켜봐요", "type": "other"},
        {"id": "10F_C_other_10", "text": "상대가 귀여운 이모티콘을 보내도 진짜 마음인지 확인해요", "type": "other"},
    ]
    
    # 10F_R (10대 여성 합리형)
    questions["10F_R"] = [
        {"id": "10F_R_sum_01", "text": "좋아하는 사람이 있으면 먼저 다가가기보단 장단점을 따져봐요", "type": "sum"},
        {"id": "10F_R_sum_02", "text": "호감이 가는 사람 앞에서 현실적으로 잘 맞을지 생각해요", "type": "sum"},
        {"id": "10F_R_sum_03", "text": "애인이 생기면 SNS 공개가 도움이 될지 안 될지 분석해요", "type": "sum"},
        {"id": "10F_R_sum_04", "text": "전화번호를 물어볼 때 상대가 편해할지 불편할지 따져봐요", "type": "sum"},
        {"id": "10F_R_sum_05", "text": "옆자리로 가서 앉는 게 공부에 방해가 안 될지 판단해요", "type": "sum"},
        {"id": "10F_R_sum_06", "text": "썸이 생기면 만나는 게 시간 낭비는 아닐지 고민해요", "type": "sum"},
        {"id": "10F_R_sum_07", "text": "상대가 웃을 때 내 반응이 적절한지 분석해요", "type": "sum"},
        {"id": "10F_R_sum_08", "text": "친구들에게 얘기할 때 이 관계가 실현 가능성이 있는지 봐요", "type": "sum"},
        {"id": "10F_R_sum_09", "text": "상대가 고백하면 수락했을 때 장단점을 따져봐요", "type": "sum"},
        {"id": "10F_R_sum_10", "text": "급식실에서 같이 먹자고 할 때 거절당할 확률을 계산해요", "type": "sum"},
        {"id": "10F_R_self_01", "text": "설렘이 오면 감정과 논리 중 무엇을 따를지 고민해요", "type": "self"},
        {"id": "10F_R_self_02", "text": "좋아하는 감정이 학업에 미칠 영향부터 먼저 생각해요", "type": "self"},
        {"id": "10F_R_self_03", "text": "이 감정의 원인을 분석해봐요", "type": "self"},
        {"id": "10F_R_self_04", "text": "호감이 생기면 이 관계가 어떤 결과를 줄지 판단해요", "type": "self"},
        {"id": "10F_R_self_05", "text": "감정이 커도 표현할 타이밍이 적절한지 따져요", "type": "self"},
        {"id": "10F_R_self_06", "text": "좋아하는 게 지금 시점에서 현명한 선택인지 생각해봐요", "type": "self"},
        {"id": "10F_R_self_07", "text": "처음 느껴보는 감정이니까 신중하게 대가를 따져봐요", "type": "self"},
        {"id": "10F_R_self_08", "text": "설레는 마음을 나누는 것이 이득인지 계산해요", "type": "self"},
        {"id": "10F_R_self_09", "text": "좋아하는 생각에 매몰되면 안된다는 경계를 유지해요", "type": "self"},
        {"id": "10F_R_self_10", "text": "감정이 왔을 때 이게 잠깐인지 장기인지 분석해요", "type": "self"},
        {"id": "10F_R_other_01", "text": "상대가 나를 보며 웃는 게 진짜인지 가짜인지 분석해요", "type": "other"},
        {"id": "10F_R_other_02", "text": "상대의 눈빛을 보고 관심사인지 그냥 예의인지 판단해요", "type": "other"},
        {"id": "10F_R_other_03", "text": "상대가 다가오는 것까지 재는 건 과한 건 아닌지 생각해요", "type": "other"},
        {"id": "10F_R_other_04", "text": "상대가 친구들에게 물어보는 이유와 목적을 추론해 봐요", "type": "other"},
        {"id": "10F_R_other_05", "text": "상대의 답장 속도가 의미하는 바를 계산해요", "type": "other"},
        {"id": "10F_R_other_06", "text": "상대가 눈을 마주치는 빈도를 통계적으로 따져봐요", "type": "other"},
        {"id": "10F_R_other_07", "text": "상대가 수줍어하는 게 연기인지 진심인지 구분해 봐요", "type": "other"},
        {"id": "10F_R_other_08", "text": "상대가 생일을 챙겨준 건 투자의 개념으로 볼 수 있어요", "type": "other"},
        {"id": "10F_R_other_09", "text": "상대가 다른 사람이랑 웃는 걸 보면 경쟁자가 있는지 분석해요", "type": "other"},
        {"id": "10F_R_other_10", "text": "상대의 이모티콘 선택이 전략적인 건지 아닌지 따져봐요", "type": "other"},
    ]
    
    # 10F_P (10대 여성 감성형)
    questions["10F_P"] = [
        {"id": "10F_P_sum_01", "text": "좋아하는 사람이 있으면 눈 마주칠 때 설레임이 느껴져요", "type": "sum"},
        {"id": "10F_P_sum_02", "text": "호감이 가는 사람 앞에서 분위기가 달라지는 게 느껴져요", "type": "sum"},
        {"id": "10F_P_sum_03", "text": "애인이 생기면 함께한 순간들을 사진으로 남기고 싶어요", "type": "sum"},
        {"id": "10F_P_sum_04", "text": "전화번호를 물어볼 때 심장이 뛰는 게 느껴져요", "type": "sum"},
        {"id": "10F_P_sum_05", "text": "같은 반이나 동아리면 옆에 있는 것만으로도 행복해요", "type": "sum"},
        {"id": "10F_P_sum_06", "text": "썸이 생기면 서로 연락할 때의 감정이 달라져요", "type": "sum"},
        {"id": "10F_P_sum_07", "text": "상대가 웃으면 세상이 밝아지는 느낌이 들어요", "type": "sum"},
        {"id": "10F_P_sum_08", "text": "좋아하는 사람이 생기면 친구들과 수다 떨 때도 자꾸 생각나요", "type": "sum"},
        {"id": "10F_P_sum_09", "text": "상대가 고백하면 영화 같은 순간이 될 것 같아 감동해요", "type": "sum"},
        {"id": "10F_P_sum_10", "text": "학교 급식실에서 같은 테이블에 앉으면 기분이 좋아져요", "type": "sum"},
        {"id": "10F_P_self_01", "text": "설렘이 오면 매일이 특별하게 느껴져요", "type": "self"},
        {"id": "10F_P_self_02", "text": "좋아하는 감정이 마법 같아서 둥둥 떠다니는 것 같아요", "type": "self"},
        {"id": "10F_P_self_03", "text": "감정이 생기면 심장이 뛰어요", "type": "self"},
        {"id": "10F_P_self_04", "text": "호감이 생기면 세상이 바뀐 것처럼 모두 새로워 보여요", "type": "self"},
        {"id": "10F_P_self_05", "text": "감정이 크면 그 순간을 영원히 간직하고 싶어져요", "type": "self"},
        {"id": "10F_P_self_06", "text": "좋아하는 내 모습이 로맨틱하고 아름다워요", "type": "self"},
        {"id": "10F_P_self_07", "text": "처음 느껴보는 감정이 꿈같고 멋져요", "type": "self"},
        {"id": "10F_P_self_08", "text": "설레는 마음을 친구와 나누며 감정을 더 깊이 느껴요", "type": "self"},
        {"id": "10F_P_self_09", "text": "좋아하는 생각만 해도 하늘을 나는 것처럼 기분이 좋아져요", "type": "self"},
        {"id": "10F_P_self_10", "text": "감정이 왔을 때는 그대로 느끼는 게 가장 소중해요", "type": "self"},
        {"id": "10F_P_other_01", "text": "상대가 나를 보며 웃을 때 진심이 전해지는 느낌이 들어요", "type": "other"},
        {"id": "10F_P_other_02", "text": "상대의 눈빛 속에 따뜻함이 느껴질 때 마음이 열려요", "type": "other"},
        {"id": "10F_P_other_03", "text": "상대가 다가오는 순간의 떨림이 느껴져요", "type": "other"},
        {"id": "10F_P_other_04", "text": "상대가 친구들에게 물어보는 게 귀여운 표현방식이라 생각해요", "type": "other"},
        {"id": "10F_P_other_05", "text": "상대의 답장이 빠르면 관심이 전해지는 따뜻함이 느껴져요", "type": "other"},
        {"id": "10F_P_other_06", "text": "상대가 자꾸 눈을 마주치는 건 운명의 징조 같아요", "type": "other"},
        {"id": "10F_P_other_07", "text": "상대가 수줍어하는 모습이 순수하고 예뻐 보여요", "type": "other"},
        {"id": "10F_P_other_08", "text": "상대가 생일을 챙겨주는 것이 로맨틱해서 감동받아요", "type": "other"},
        {"id": "10F_P_other_09", "text": "상대가 다른 사람이랑 웃어도 그 모습이 좋아 보일 때 있어요", "type": "other"},
        {"id": "10F_P_other_10", "text": "상대의 이모티콘이 감정을 진심으로 전해주는 것 같아요", "type": "other"},
    ]
    
    # ============================================
    # 10대 M (10M)
    # ============================================
    # 10M_D (10대 남성 직진형)
    questions["10M_D"] = [
        {"id": "10M_D_sum_01", "text": "좋아하는 사람이 생기면 바로 고백해서 관계를 확실히 해요", "type": "sum"},
        {"id": "10M_D_sum_02", "text": "호감이 가는 사람에게 바로 번호 물어보고 카톡바로 보내요", "type": "sum"},
        {"id": "10M_D_sum_03", "text": "애인이 생기면 당당하게 SNS에 사진 올리고 인정해요", "type": "sum"},
        {"id": "10M_D_sum_04", "text": "좋아하는 사람과 함께 있는 시간을 적극적으로 만들어요", "type": "sum"},
        {"id": "10M_D_sum_05", "text": "같은 반이면 바로 옆자리로 가서 같이 수업 들어요", "type": "sum"},
        {"id": "10M_D_sum_06", "text": "썸이 생기면 주말에 만나자고 바로 제안해요", "type": "sum"},
        {"id": "10M_D_sum_07", "text": "상대가 웃으면 바로 재밌게 해줄게 하며 반응해요", "type": "sum"},
        {"id": "10M_D_sum_08", "text": "좋아하는 걸 숨기기보다 친구들한테 티내고 다녀요", "type": "sum"},
        {"id": "10M_D_sum_09", "text": "상대가 힘들면 바로 옆에 가서 위로해주고 도와줘요", "type": "sum"},
        {"id": "10M_D_sum_10", "text": "학교에서 만나면 바로 점심 같이 먹자고 해요", "type": "sum"},
        {"id": "10M_D_self_01", "text": "설렘이 오면 바로 행동으로 옮기고 싶은 충동이 생겨요", "type": "self"},
        {"id": "10M_D_self_02", "text": "좋아하는 감정은 숨기지 않고 티내는 게 더 멋있다고 생각해요", "type": "self"},
        {"id": "10M_D_self_03", "text": "감정이 생기면 뭐든지 해보겠다는 의욕이 넘쳐요", "type": "self"},
        {"id": "10M_D_self_04", "text": "호감이 생기면 당당하게 표현하는 게 남자다워요", "type": "self"},
        {"id": "10M_D_self_05", "text": "감정이 크면 크게 느끼고 누구보다 적극적으로 행동해요", "type": "self"},
        {"id": "10M_D_self_06", "text": "누군가를 좋아하는 내 모습이 좋아 자주 떠올려요", "type": "self"},
        {"id": "10M_D_self_07", "text": "처음 느껴보는 감정도 두려움 없이 뚜벅뚜벅 걸어가요", "type": "self"},
        {"id": "10M_D_self_08", "text": "설레는 마음을 친구들과 자랑하며 더 키워가요", "type": "self"},
        {"id": "10M_D_self_09", "text": "좋아하는 생각만 해도 자신감이 생겨서 걸음걸이도 달라져요", "type": "self"},
        {"id": "10M_D_self_10", "text": "감정이 왔을 때 고민보다는 당장 표현하는 게 맞다고 믿어요", "type": "self"},
        {"id": "10M_D_other_01", "text": "상대가 나를 볼 때 관심이 있다는 게 바로 눈에 띄어요", "type": "other"},
        {"id": "10M_D_other_02", "text": "상대의 눈빛에서 호감을 느끼면 바로 액션으로 옮겨요", "type": "other"},
        {"id": "10M_D_other_03", "text": "상대가 다가오는 걸 보고 기회라고 판단해서 바로 잡아요", "type": "other"},
        {"id": "10M_D_other_04", "text": "상대가 내 친구들에게 물어보는 건 관심 있다는 확실한 신호예요", "type": "other"},
        {"id": "10M_D_other_05", "text": "상대가 메시지에 바로 답하면 만남을 제안해도 된다고 봐요", "type": "other"},
        {"id": "10M_D_other_06", "text": "상대가 눈을 자꾸 마주치면 고백 타이밍이라고 생각해요", "type": "other"},
        {"id": "10M_D_other_07", "text": "상대가 나 앞에서 수줍어하는 게 좋아한다는 증거예요", "type": "other"},
        {"id": "10M_D_other_08", "text": "상대가 선물을 주면 바로 그 마음에 답을 해줘야 한다고 봐요", "type": "other"},
        {"id": "10M_D_other_09", "text": "상대가 다른 남자애랑 웃는 걸 보면 바로 질투가 나요", "type": "other"},
        {"id": "10M_D_other_10", "text": "상대가 먼저 카톡 오면 답장으로 내 마음을 바로 전해요", "type": "other"},
    ]
    
    # 10M_C (10대 남성 신중형)
    questions["10M_C"] = [
        {"id": "10M_C_sum_01", "text": "좋아하는 사람이 생겨도 확실해질 때까지 고백을 미뤄요", "type": "sum"},
        {"id": "10M_C_sum_02", "text": "호감이 가는 사람에게 천천히 다가가서 신뢰부터 쌓아요", "type": "sum"},
        {"id": "10M_C_sum_03", "text": "애인이 생기면 조금 지나서 서로 확신이 들면 공개해요", "type": "sum"},
        {"id": "10M_C_sum_04", "text": "좋아하는 사람과 함께 있는 시간을 자연스럽게 늘려가요", "type": "sum"},
        {"id": "10M_C_sum_05", "text": "같은 반이면 조용히 옆자리로 조금씩 가까워져요", "type": "sum"},
        {"id": "10M_C_sum_06", "text": "썸이 생기면 상대의 반응을 보며 천천히 만남을 제안해요", "type": "sum"},
        {"id": "10M_C_sum_07", "text": "상대가 웃어도 진짜 웃는지 살펴본 뒤에야 반응해요", "type": "sum"},
        {"id": "10M_C_sum_08", "text": "좋아하는 걸 확실하지 않을 때는 조심스레 숨기고 다녀요", "type": "sum"},
        {"id": "10M_C_sum_09", "text": "상대가 힘들면 먼저 지켜보다가 적절할 때 도움을 줘요", "type": "sum"},
        {"id": "10M_C_sum_10", "text": "학교에서 만나도 급식실은 자연스럽게 옆에 앉는 정도로 해요", "type": "sum"},
        {"id": "10M_C_self_01", "text": "설렘이 오면 감정을 서서히 풀어내는 게 더 좋아요", "type": "self"},
        {"id": "10M_C_self_02", "text": "좋아하는 감정은 천천히 익혀가며 깊이 느끼고 싶어요", "type": "self"},
        {"id": "10M_C_self_03", "text": "감정이 생기면 천천히 고민해보고 신중하게 움직여요", "type": "self"},
        {"id": "10M_C_self_04", "text": "호감이 생기면 진짜 마음인지 여러 번 확인해요", "type": "self"},
        {"id": "10M_C_self_05", "text": "감정이 커도 표현하기 전에 타이밍이 맞는지 살펴봐요", "type": "self"},
        {"id": "10M_C_self_06", "text": "누군가를 좋아하는 내 모습이 조심스럽지만 소중해요", "type": "self"},
        {"id": "10M_C_self_07", "text": "처음 느껴보는 감정이니까 더 신중하게 다가가고 싶어요", "type": "self"},
        {"id": "10M_C_self_08", "text": "설레는 마음을 먼저 혼자 간직했다가 친구에게 털어놔요", "type": "self"},
        {"id": "10M_C_self_09", "text": "좋아하는 생각이 떠오를 때마다 조용히 미소 짓고 있어요", "type": "self"},
        {"id": "10M_C_self_10", "text": "감정이 왔을 때 서두르지 않는 게 더 중요하다고 생각해요", "type": "self"},
        {"id": "10M_C_other_01", "text": "상대가 나를 볼 때 진심인지 몇 번 더 확인해보고 판단해요", "type": "other"},
        {"id": "10M_C_other_02", "text": "상대의 눈빛을 오랫동안 지켜보며 진심인지 알아차려요", "type": "other"},
        {"id": "10M_C_other_03", "text": "상대가 다가오는 걸 여러 번 본 뒤에야 마음을 열어요", "type": "other"},
        {"id": "10M_C_other_04", "text": "상대가 내 친구들에게 물어보는 걸 여러 번 확인해야 믿어요", "type": "other"},
        {"id": "10M_C_other_05", "text": "상대의 메시지 답장 속도를 계속 지켜본 뒤 판단해요", "type": "other"},
        {"id": "10M_C_other_06", "text": "상대가 자꾸 눈을 마주치는 걸 여러 번 보고 기회라고 생각해요", "type": "other"},
        {"id": "10M_C_other_07", "text": "상대가 나 앞에서 수줍어하는 모습을 몇 번 보고 확신해요", "type": "other"},
        {"id": "10M_C_other_08", "text": "상대가 선물을 줘도 우정인지 사랑인지 헷갈릴 때 있어요", "type": "other"},
        {"id": "10M_C_other_09", "text": "상대가 다른 남자애랑 웃어도 우연일 수 있어서 지켜봐요", "type": "other"},
        {"id": "10M_C_other_10", "text": "상대가 먼저 카톡 와도 바로 답하지 않고 적절한 타이밍을 봐요", "type": "other"},
    ]
    
    # 10M_R (10대 남성 합리형)
    questions["10M_R"] = [
        {"id": "10M_R_sum_01", "text": "좋아하는 사람이 생기면 성격과 취향이 맞는지 분석해요", "type": "sum"},
        {"id": "10M_R_sum_02", "text": "호감이 가는 사람에게 현실적으로 잘 어울릴지 따져봐요", "type": "sum"},
        {"id": "10M_R_sum_03", "text": "애인이 생기면 SNS 공개가 실익이 있는지 따져봐요", "type": "sum"},
        {"id": "10M_R_sum_04", "text": "좋아하는 사람과 함께하는 시간이 효율적인지 생각해요", "type": "sum"},
        {"id": "10M_R_sum_05", "text": "같은 반이면 공부에 방해되지 않는 위치를 계산해서 앉아요", "type": "sum"},
        {"id": "10M_R_sum_06", "text": "썸이 생기면 사귀었을 때의 장단점을 따져봐요", "type": "sum"},
        {"id": "10M_R_sum_07", "text": "상대가 웃을 때 나한테 웃는 건지 그냥 웃는 건지 분석해요", "type": "sum"},
        {"id": "10M_R_sum_08", "text": "좋아하는 걸 친구들에게 얘기할 때 현실 가능성을 따져봐요", "type": "sum"},
        {"id": "10M_R_sum_09", "text": "상대가 힘들면 도와줬을 때의 관계 변화를 예측해봐요", "type": "sum"},
        {"id": "10M_R_sum_10", "text": "학교에서 만나면 급식비와 시간을 고려해서 만남을 계획해요", "type": "sum"},
        {"id": "10M_R_self_01", "text": "설렘이 오면 감정을 논리적으로 분석하는 편이에요", "type": "self"},
        {"id": "10M_R_self_02", "text": "좋아하는 감정이 학업과 운동에 미칠 영향부터 계산해요", "type": "self"},
        {"id": "10M_R_self_03", "text": "이 감정의 원인을 분석해봐요", "type": "self"},
        {"id": "10M_R_self_04", "text": "호감이 생기면 이 관계가 성사될 확률부터 따져봐요", "type": "self"},
        {"id": "10M_R_self_05", "text": "감정이 커도 표현의 적정선을 계산해서 움직여요", "type": "self"},
        {"id": "10M_R_self_06", "text": "좋아하는 게 지금 시점에서 적절한 선택인지 봐요", "type": "self"},
        {"id": "10M_R_self_07", "text": "처음 느껴보는 감정이니까 더 체계적으로 접근해보고 싶어요", "type": "self"},
        {"id": "10M_R_self_08", "text": "설레는 마음을 친구와 나누되 장단점을 분석해서 말해요", "type": "self"},
        {"id": "10M_R_self_09", "text": "좋아하는 생각에 과몰입되면 안된다는 경계를 유지해요", "type": "self"},
        {"id": "10M_R_self_10", "text": "감정이 왔을 때 이게 잠깐인지 장기인지 판단부터 해요", "type": "self"},
        {"id": "10M_R_other_01", "text": "상대가 나를 볼 때 호감인지 그냥 예의인지 분석해요", "type": "other"},
        {"id": "10M_R_other_02", "text": "상대의 눈빛을 보고 관심이 맞는지 계산적으로 판단해요", "type": "other"},
        {"id": "10M_R_other_03", "text": "상대가 다가오는 것까지 재는 건 과한 건 아닌지 따져봐요", "type": "other"},
        {"id": "10M_R_other_04", "text": "상대가 내 친구들에게 물어보는 의도를 추론해봐요", "type": "other"},
        {"id": "10M_R_other_05", "text": "상대의 메시지 답장 패턴을 데이터로 분석해봐요", "type": "other"},
        {"id": "10M_R_other_06", "text": "상대가 눈을 마주치는 빈도를 통계적으로 따져봐요", "type": "other"},
        {"id": "10M_R_other_07", "text": "상대가 수줍어하는 게 진심인지 연기인지 구분하려 해요", "type": "other"},
        {"id": "10M_R_other_08", "text": "상대가 선물을 준 건 투자 목적인지 단순 호의인지 따져봐요", "type": "other"},
        {"id": "10M_R_other_09", "text": "상대가 다른 남자애랑 웃는 걸 보면 경쟁자가 있는지 분석해요", "type": "other"},
        {"id": "10M_R_other_10", "text": "상대가 먼저 카톡 왔을 때 전략적인 답장 타이밍을 계산해요", "type": "other"},
    ]
    
    # 10M_P (10대 남성 감성형)
    questions["10M_P"] = [
        {"id": "10M_P_sum_01", "text": "좋아하는 사람이 생기면 함께 있을 때의 기분이 좋아져요", "type": "sum"},
        {"id": "10M_P_sum_02", "text": "호감이 가는 사람에게 순간의 감정을 따라 행동해요", "type": "sum"},
        {"id": "10M_P_sum_03", "text": "애인이 생기면 함께한 추억을 사진으로 자꾸 보고 싶어요", "type": "sum"},
        {"id": "10M_P_sum_04", "text": "좋아하는 사람과 함께하는 시간 자체가 행복해요", "type": "sum"},
        {"id": "10M_P_sum_05", "text": "같은 반이면 그냥 옆에 있다는 것만으로 뿌듯해요", "type": "sum"},
        {"id": "10M_P_sum_06", "text": "썸이 생기면 서로 연락할 때의 설레임이 좋아요", "type": "sum"},
        {"id": "10M_P_sum_07", "text": "상대가 웃으면 세상이 밝아지는 느낌이 들어요", "type": "sum"},
        {"id": "10M_P_sum_08", "text": "좋아하는 사람이 생기면 친구들과 얘기할 때도 자꾸 생각나요", "type": "sum"},
        {"id": "10M_P_sum_09", "text": "상대가 힘들면 옆에서 같이 있어주는 것만으로 위로가 돼요", "type": "sum"},
        {"id": "10M_P_sum_10", "text": "학교에서 같은 공간에 있으면 기분이 좋아져요", "type": "sum"},
        {"id": "10M_P_self_01", "text": "설렘이 오면 매일이 새롭게 느껴져요", "type": "self"},
        {"id": "10M_P_self_02", "text": "좋아하는 감정이 마법 같아서 둥실둥실 떠다니는 것 같아요", "type": "self"},
        {"id": "10M_P_self_03", "text": "감정이 생기면 그 순간의 느낌을 온전히 느끼고 싶어져요", "type": "self"},
        {"id": "10M_P_self_04", "text": "호감이 생기면 세상이 바뀐 것처럼 모두 새롭게 보여요", "type": "self"},
        {"id": "10M_P_self_05", "text": "감정이 크면 그 순간을 영원히 간직하고 싶어져요", "type": "self"},
        {"id": "10M_P_self_06", "text": "좋아하는 내 모습이 소중하고 아름다워요", "type": "self"},
        {"id": "10M_P_self_07", "text": "처음 느껴보는 감정이 꿈같고 무섭기도 하지만 좋아요", "type": "self"},
        {"id": "10M_P_self_08", "text": "설레는 마음을 친구들과 나누며 감정을 더 깊이 느껴요", "type": "self"},
        {"id": "10M_P_self_09", "text": "좋아하는 생각만 해도 행복해서 자꾸 생각하고 싶어져요", "type": "self"},
        {"id": "10M_P_self_10", "text": "감정이 왔을 때는 그대로 느끼는 게 제일 좋아요", "type": "self"},
        {"id": "10M_P_other_01", "text": "상대가 나를 볼 때 진심이 느껴지면 마음이 열려요", "type": "other"},
        {"id": "10M_P_other_02", "text": "상대의 눈빛 속에 따뜻함이 느껴질 때 설레요", "type": "other"},
        {"id": "10M_P_other_03", "text": "상대가 다가오는 순간의 감정이 공기 중에 퍼져요", "type": "other"},
        {"id": "10M_P_other_04", "text": "상대가 내 친구들에게 물어보는 게 귀여워 보여요", "type": "other"},
        {"id": "10M_P_other_05", "text": "상대가 메시지에 답해줄 때의 감정이 따뜻해요", "type": "other"},
        {"id": "10M_P_other_06", "text": "상대가 눈을 마주치는 게 운명처럼 느껴져요", "type": "other"},
        {"id": "10M_P_other_07", "text": "상대가 수줍어하는 모습이 순수하고 예뻐 보여요", "type": "other"},
        {"id": "10M_P_other_08", "text": "상대가 선물을 주는 게 로맨틱하고 감동스러워요", "type": "other"},
        {"id": "10M_P_other_09", "text": "상대가 다른 사람이랑 웃어도 그 미소가 좋아 보여요", "type": "other"},
        {"id": "10M_P_other_10", "text": "상대가 먼저 카톡 온 게 감정이 전해지는 것 같아요", "type": "other"},
    ]
    
    return questions

def main():
    print("SomeThing - 고품질 테스트 질문 생성기")
    print("=" * 50)
    
    questions = create_full_question_set()
    
    # 검증
    total_questions = 0
    for key, q_list in questions.items():
        count = len(q_list)
        total_questions += count
        sum_count = sum(1 for q in q_list if q["type"] == "sum")
        self_count = sum(1 for q in q_list if q["type"] == "self")
        other_count = sum(1 for q in q_list if q["type"] == "other")
        print(f"{key}: {count}문항 (sum:{sum_count}, self:{self_count}, other:{other_count})")
    
    print(f"\n총 {total_questions}개 질문 생성 완료")
    print(f"조합 수: {len(questions)}개")
    
    # JSON 저장
    output_path = "/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-v10.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    print(f"\n저장 완료: {output_path}")

if __name__ == "__main__":
    main()
