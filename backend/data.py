import pandas as pd
import numpy as np
from translation import *

# CSV 파일을 읽습니다.
df = pd.read_csv('./k.csv')

# '외국어 수준' 매핑을 설정합니다.
level_mapping = {'상': 3, '중': 2, '하': 1}
language_mapping = {
    '영어': 'english',
    '중국어': 'chinese',
    '아랍어': 'arabic',
    '스페인어': 'spanish',
    '불어': 'french',
    '한국어': 'korean',
    '일어': 'japanese'
}
gender_mapping = {
    '남': 'Male',
    '여': 'Female'
}

# '외국어 수준' 열의 값을 매핑하여 숫자로 바꿉니다.
df['외국어 수준'] = df['외국어 수준'].map(level_mapping)
df['성별'] = df['성별'].map(gender_mapping)
df['모국어'] = df['모국어'].map(language_mapping)
df['외국어'] = df['외국어'].map(language_mapping)

df = df.drop(columns=['User_ID'])

def generate_age(age_group):
    if age_group == '10대 이하':
        return int(np.random.randint(5, 10))
    elif age_group == '10대':
        return int(np.random.randint(10, 20))
    elif age_group == '20대':
        return int(np.random.randint(20, 30))
    elif age_group == '30대':
        return int(np.random.randint(30, 40))
    elif age_group == '40대':
        return int(np.random.randint(40, 50))
    elif age_group == '50대':
        return int(np.random.randint(50, 60))
    elif age_group == '60대 이상':
        return int(np.random.randint(60, 80))

df['연령대'] = df['연령대'].apply(generate_age)

for index, row in df.iterrows():
    print(index)
    print(f"이름: {row['이름']}, 성별: {row['성별']}, 연령대: {row['연령대']}")
    print(f"자기 소개: {row['자기 소개']}")
    print(f"모국어: {row['모국어']}, 외국어: {row['외국어']}, 외국어 수준: {row['외국어 수준']}")
    print("-" * 50)
    
df2 = pd.read_csv('./p.csv')
for index, row in df2.iterrows():
    print(index)
    
# 변경된 내용을 새로운 CSV 파일로 저장합니다.
df.to_csv('updated_k.csv', index=False)