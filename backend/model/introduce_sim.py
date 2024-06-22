import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

path = "./model/"
# train = pd.read_csv(path+'updated_train.csv')

def tokenize_ko(x):
    print("tokenize_ko 시작")
    tokenizer = Okt()
    print("tokenizer", end='')
    print(tokenizer)
    print(x)
    x = tokenizer.normalize(x) # 텍스트 Normalization
    print(x)
    x = tokenizer.morphs(x) # 형태소 분리
    print(x)
    return x


#모국어 외국어 매칭해서 데이터프레임 반환
def match_lang(user_id, train):
    print("match_lang 시작")
    user = train[train['User_ID'] == user_id]
    print(user)
    # 모국어와 희망하는 외국어가 모두 동일한 사용자 필터링
    filtered_users = train[(user['외국어'].iloc[0] == train['모국어']) & (user['모국어'].iloc[0] == train['외국어']) | (train['User_ID'] == user_id)]
    print(filtered_users)
    return filtered_users

def match_gender(user_id, train, gender):
    print("match_gender 시작")
    if not gender:
        return train
    print(1)
    filtered_df = train[(train['성별'] == gender) | (train['User_ID'] == user_id)]
    print(2)
    return filtered_df

def match_age(user_id, train, age):
    print("match_age 시작")
    if not age:
        return train
    print(1)
    filtered_df = train[(train['연령대'] == age) | (train['User_ID'] == user_id)]
    print(2)
    return filtered_df

def match_level(user_id, train, level):
    print("match_level 시작")
    if not level:
        return train
    print(1)
    filtered_df = train[(train['외국어 수준'] == level) | (train['User_ID'] == user_id)]
    print(2)
    return filtered_df

def content_base(user_id, train, gender, age, level):
    print("content_base 시작")
    temp1 = match_lang(user_id, train)
    print(1)
    temp2 = match_gender(user_id, temp1, gender)
    print(2)
    temp3 = match_age(user_id, temp2, age)
    print(3)
    result = match_level(user_id,temp3, level)
    print(4)
    return result

def stopwords(path):
    print("stopwords 시작")
    tokenizer = Okt()
    print("tokenizer: ", end='')
    print(tokenizer)

    # 불용어 파일에서 불용어 읽어오기
    with open(path+'stopwords-ko.txt', 'r', encoding='utf-8') as f:
        stopwords = f.readlines()
    print("before")
    print(stopwords)
<<<<<<< HEAD
    #stopwords = [word.strip() for word in stopwords]
    stopwords = [tokenizer.morphs(word)[0] for word in stopwords if word]
=======
    stopwords = [tokenizer.morphs(word)[0] for word in stopwords]
>>>>>>> 756504c9e95f1c82e0dae31b5b69ac40a539e408
    print("after")
    print(stopwords)
    return stopwords

#stopwords(path)
def cosine_sim(train, n, gender, age, level):
    print("cosine_sim 시작")
    #유저 아이디 n과 언어 매칭되는 유저들 추출
    print(1)
    sample = content_base(n, train, gender, age, level)
    print(2)
    introduce = list(sample['자기 소개'])
    #자기 소개 임베딩
    print(3)
    tf = TfidfVectorizer(tokenizer=tokenize_ko)
    print(4)
    tfidf_matrix =tf.fit_transform(introduce)
    # print(tfidf_matrix.shape) user수 * 임베딩수
    #코사인 유사도 게산
    print(5)
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    print(6)
    return cosine_sim

#자기소개 기반 추천
def intro_recommend(user_id, train, gender, age, level):
    print("intro_recommend 시작")
    sample = content_base(user_id, train, gender, age, level)
    print(1)
    rec_df = sample.set_index('User_ID')
    print(2)
    idx = rec_df.index.get_loc(user_id)
    print(3)
    sim_scores = list(enumerate(cosine_sim(train, user_id, gender, age, level)[idx]))
    print(4)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    print(5)
    sim_scores = sim_scores[1:21]
    print(6)
    user_indices = [i[0] for i in sim_scores]
    print(7)
    return sample.iloc[user_indices]['User_ID'].tolist()

# print(type(30), type(pd.read_csv('./updated_train.csv')), type(None), type(None), type(None))
#print(30, pd.read_csv('./updated_train.csv'), None, None, None)
# print(train[train['User_ID'] == 30000])
#print(intro_recommend(30, pd.read_csv('./updated_train.csv'), None, None, None))
