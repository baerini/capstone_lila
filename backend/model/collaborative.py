import pandas as pd
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate
from backend.model.introduce_sim import match_lang
from tqdm import tqdm

path = "./data/train/"
ratings = pd.read_csv(path+'ratings.csv')
train = pd.read_csv(path+'updated_train.csv')
reader = Reader(rating_scale=(1,3))
data = Dataset.load_from_df(ratings, reader=reader)
svd = SVD()
#cross_validate(svd, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

trainset = data.build_full_trainset()
svd.fit(trainset)


predictions = []
def collaborative_recommend(user_id, train):
    train = match_lang(user_id,train)
    print(train[train['User_ID']==user_id])
    print('='*30)
    for target_user in tqdm(train['User_ID'].values):
        #본인 제외
        if target_user != user_id:
            #이미 평가한 user제외해서 뽑음
            compare = ratings[ratings['User_ID'] == user_id]
            if not target_user in compare['Target_User_ID'].values:
                pred = svd.predict(user_id, target_user)  # 사용자 id 1에 대한 각 사용자의 평점 예측
                predictions.append((target_user, pred.est))  # 사용자 id와 예측 평점을 튜플로 저장
    # 예측된 평점을 기준으로 사용자 정렬하여 상위 10개 선택
    top_users = sorted(predictions, key=lambda x: x[1], reverse=True)[:10]
    return top_users

top_users = collaborative_recommend(30000,train)


# 상위 10개 사용자의 user_id와 name 출력
for user_id, rate in top_users:
    user_info = train[train['User_ID'] == user_id]
    name = user_info.iloc[0]['이름']
    print(f"User ID: {user_id}, Name: {name}, Rate: {rate}")