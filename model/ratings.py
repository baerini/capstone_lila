import numpy as np
import pandas as pd
from tqdm import tqdm
from introduce_sim import intro_recommend

def generate_rating(user1, user2):
    # 성별이 같으면 3점, 다르면 1점
    if user1['성별'] == user2['성별']:
        criterion1 = 3
    else:
        criterion1 = 1

    # 성별이 같으면 1점, 다르면 3점
    if user1['성별'] == user2['성별']:
        criterion2 = 1
    else:
        criterion2 = 3

    # 나이대가 같으면 3점, 다르면 1점
    if user1['연령대'] == user2['연령대']:
        criterion3 = 3
    else:
        criterion3 = 1

    # 수준이 상이면 3점, 하면 1점
    if user2['외국어 수준'] == '상':
        criterion4 = 3
    elif user2['외국어 수준'] == '중':
        criterion4 = 2
    else:
        criterion4 = 1

    # 기준5: 2점
    criterion5 = 2

     # user1의 id에 따라 기준 선택
    user_id_mod = user1['User_ID'] % 5
    if user_id_mod == 0:
        criterion = criterion1
    elif user_id_mod == 1:
        criterion = criterion2
    elif user_id_mod == 2:
        criterion = criterion3
    elif user_id_mod == 3:
        criterion = criterion4
    else:
        criterion = criterion5

    # 평점 부여
    if criterion == 1:
        rating = 1
    elif criterion == 2:
        rating = 2
    else:
        rating = 3

    return rating

def generate_rating_matrix(user_id, df):
    user = df[df['User_ID'] == user_id]
    # content base로 추천받은 애들만 평점 매김
    filtered_users = intro_recommend(user_id,None,None)
    # 모국어와 희망하는 외국어가 모두 동일한 사용자 필터링
    #filtered_users = df[(user['외국어'].iloc[0] == df['모국어']) & (user['모국어'].iloc[0] == df['외국어']) | (df['User_ID'] == user_id)]
   # rating 행렬 초기화
    rating_matrix = []

    # 각 유저에 대해 평점 부여
    for _, user in filtered_users.iterrows():
        if user['User_ID'] != user_id:
            rating = generate_rating(df[df['User_ID'] == user_id].iloc[0], user)
            rating_matrix.append([user_id, user['User_ID'], rating])

    # rating 행렬을 DataFrame으로 변환
    rating_df = pd.DataFrame(rating_matrix, columns=['User_ID', 'Target_User_ID', 'Rating'])
    return rating_df
    
path = "./data/train/"
train = pd.read_csv(path+'updated_train.csv')
all_ratings = []
for user_id in tqdm(range(1, 2001)):
    # 해당 유저 아이디에 대한 rating 행렬 생성
    rating_df = generate_rating_matrix(user_id, train)
    # 생성된 rating 행렬을 all_ratings 리스트에 추가
    all_ratings.append(rating_df)

all_ratings_df = pd.concat(all_ratings, ignore_index=True)
all_ratings_df.to_csv(path+'rating.csv', index=False)

