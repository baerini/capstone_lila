import pandas as pd
import random

# 새로운 자기 소개 문장 생성 함수
def generate_introduction(jobs, personalities, likes, num_sentences):
    introductions = []
    for _ in range(num_sentences):
        job = random.choice(jobs)
        personality = random.choice(personalities)
        like = random.choice(likes)
        introductions.append(f"나는 {job}이다. 나의 MBTI는 {personality}이다. 나는 {like}을(를) 좋아한다.")
    return introductions


def generate_introduction_with_age(data, jobs, personalities, likes):
    introductions = []
    for index, row in data.iterrows():
        age = row['연령대']  # 연령대 컬럼
        if age == "10대 이하":
            job = "학생"
        else:
            job = random.choice(jobs)
        personality = random.choice(personalities)
        like = random.choice(likes)
        introductions.append(f"나는 {job}이다. 나의 MBTI는 {personality}이다. 나는 {like}을(를) 좋아한다.")
    return introductions

# 직업, MBTI, 좋아하는 것 리스트
jobs = [
    "학생", "주부", "애널리스트", "보험계리사", "마케터", "의사", "수중 용접공",
    "소프트웨어 개발자", "웹 개발자", "그래픽 디자이너", "UI/UX 디자이너", "데이터 과학자",
    "데이터 분석가", "기계 엔지니어", "전기 엔지니어", "토목 엔지니어", "건축가", 
    "인테리어 디자이너", "교사", "교수", "변호사", "회계사", "세무사", "경영 컨설턴트", 
    "투자 분석가", "은행원", "간호사", "약사", "물리치료사", "치과의사", 
    "심리 치료사", "사회복지사", "운동선수", "헬스 트레이너", "요리사", "제과점 사장",
    "농부", "조경사", "화가", "조각가", "사진가", "작가", "시인", 
    "저널리스트", "번역가", "통역가", "비행기 조종사", "선장", "경찰관", 
    "소방관", "군인", "해양 탐험가", "천문학자", "물리학자", "화학자", 
    "생물학자", "지질학자", "고고학자", "역사학자", "철학자", "심리학자",
    "도서관 사서", "공예가", "영화 제작자", "영화 감독", "배우", "무용가", 
    "음악가", "작곡가", "가수", "DJ", "음향 엔지니어", "게임 개발자",
    "게임 디자이너", "드론 조종사", "로봇공학자", "인공지능 개발자", "네트워크 엔지니어",
    "시스템 관리자", "보안 전문가", "블록체인 개발자", "재활용 코디네이터", "환경 과학자",
    "동물 보호관", "수의사", "해양생물학자", "기상학자", "유아교육가", "초등학교 교사",
    "중학교 교사", "고등학교 교사", "특수교육 교사", "언어치료사", "미술 치료사"
]

personalities = ["ESTP", "ESFP", "ENTP", "ENFP", "ESTJ", "ESFJ", "ENTJ", "ENFJ", "ISTP", "ISFP", "INTP", "INFP", "ISTJ", "ISFJ", "INTJ", "INFJ"]
likes = [
    "낚시", "공부", "자격증 따기", "코딩", "축구", "축구 응원", "농구", "배드민턴", "농구 응원",
    "오토바이 타기", "여행", "등산", "캠핑", "사진 찍기", "블로깅", "요리", "베이킹", "그림 그리기",
    "노래하기", "기타 연주", "피아노 연주", "드럼 치기", "춤추기", "영화 감상", "도서 읽기", "만화 보기",
    "게임", "보드게임", "퍼즐 풀기", "마술", "요가", "명상", "필라테스", "크로스핏", "마라톤", "트라이애슬론",
    "스노우보드", "스키", "서핑", "스케이트보드", "BMX", "산악 자전거", "모터스포츠", "스카이다이빙",
    "번지점프", "패러글라이딩", "수영", "다이빙", "스쿠버 다이빙", "카약", "카누", "패들보드", "로프 클라이밍",
    "암벽 등반", "바둑", "체스", "쇼핑", "패션 디자인", "인테리어 디자인", "DIY 프로젝트", "정원 가꾸기",
    "화초 돌보기", "동물 돌보기", "새 관찰", "별보기", "천문학", "지리학", "역사 탐구", "문화 탐구",
    "언어 학습", "글쓰기", "시 쓰기", "연극 보기", "뮤지컬 보기", "오페라 감상", "클래식 음악 감상",
    "재즈 음악 감상", "팝 음악 감상", "록 음악 감상", "메탈 음악 감상", "R&B 음악 감상", "힙합 음악 감상",
    "전자 음악 감상", "빈티지 수집", "스탬프 수집", "코인 수집", "아트 수집", "와인 시음", "맥주 제조",
    "커피 추출", "차 시음", "요리 클래스 참가", "댄스 클래스 참가", "미술 클래스 참가", "작문 클래스 참가",
    "언어 교환", "자원 봉사", "커뮤니티 서비스", "환경 보호 활동", "동물 보호 활동", "건강 및 웰니스",
    "개인 금융 관리", "투자 및 주식", "암호화폐", "블록체인", "가상 현실", "증강 현실", "드론 조종",
    "로봇 제작", "3D 프린팅", "메이커 운동", "해킹", "보안 연구", "우주 탐사", "신재생 에너지",
    "지속 가능한 생활", "제로 웨이스트 라이프스타일", "미니멀리즘", "비건 생활"
]


# 원본 데이터 로드
file_path = '/Users/donggun/Desktop/SKKU/캡스톤/train.csv'
data = pd.read_csv(file_path)

# 연령대를 고려하여 새로운 자기 소개 데이터 생성
new_introductions = generate_introduction_with_age(data, jobs, personalities, likes)

# 자기 소개 컬럼 교체
data['자기 소개'] = new_introductions

# 수정된 데이터 저장
new_file_path = '/Users/donggun/Desktop/SKKU/캡스톤/updated_train.csv'
data.to_csv(new_file_path, index=False)

import pandas as pd

# 수정된 train.csv 파일 로드
updated_data_path = '/Users/donggun/Desktop/SKKU/캡스톤/train.csv'
updated_data = pd.read_csv(updated_data_path)

# 자기 소개 중복 확인
total_intros = len(updated_data)  # 전체 행의 수
unique_intros = updated_data['자기 소개'].nunique()  # 유니크한 자기 소개의 수
duplicate_intros = total_intros - unique_intros  # 중복된 자기 소개의 수
duplicate_rate = (duplicate_intros / total_intros) * 100  # 중복률 계산

print(f"Total Introductions: {total_intros}")
print(f"Unique Introductions: {unique_intros}")
print(f"Duplicate Introductions: {duplicate_intros}")
print(f"Duplicate Rate: {duplicate_rate:.2f}%")
