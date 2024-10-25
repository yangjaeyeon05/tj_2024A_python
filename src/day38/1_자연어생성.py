import numpy as np
import tensorflow as tf
import pandas as pd

# 1. 데이터 수집 # .get_file()
file = tf.keras.utils.get_file(
    'ratings_train.txt' , # 파일명
    origin='https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt' , # 다운로드 받을 링크
    extract=True # 압축 설정
)
df = pd.read_csv(file , sep='\t')
print(df[1000:1007]) # 데이터 중 임의의 행 확인

# 2. 데이터 전처리
from konlpy.tag import Okt # 한글 형태소 분석기 클래스 # Open Korean Text
okt = Okt() # 파이썬 객체 생성 방법 : 클래스명() # vs Okt okt = new Okt();

def word_tokenization(text):
    # 방법1
    # list = []
    # result = okt.morphs(text) # okt.morphs() : vs okt.pos() :
    # for word in result:
    #     list.append(word)
    # return list
    # 방법2
    return [word for word in okt.morphs(text)] # 리스트 컴프리헨션

def preprocessing(df):
    df = df.dropna() # 데이터프레임(df) # 결측값 제거 null값
    df = df[1000:2000] # 샘플 데이터 1000개 사용
    df['document'] = df['document'].str.replace("[^A-Za-z0-9가-힣ㄱ-ㅎㅏ-ㅣ ]" , "" , regex=True) # 데이터프레임(df)['열/속성 이름'] # 데이터프레임(df) 안에서의
    # "안녕하세요".replace()     : 문자열을 치환하는 함수
    # df['document'].replace()  : 특정 열/속성의 여러개 문자열 치환 함수 # str : 문자열 반환
    # * 서로 다른 객체들이 동일한 이름의 함수/기능 제공하는 경우 # 매개변수와 반환이 다를 수 있다.
    data = df['document'].apply( (lambda x:word_tokenization(x)) )
    return data

# # 일반함수
# def func1(param):
#     return param + 1
# func1(2)
# # 람다식함수
# func2 = lambda param : param + 1
# func2(2)

review = preprocessing(df)
print(review)
print(review[:10])

# 3. 토큰화 및 패딩
from tensorflow.keras.preprocessing.text import Tokenizer # 토큰 관련 클래스
from tensorflow.keras.preprocessing.sequence import pad_sequences # 패딩 관련 클래스
tokenizer = Tokenizer() # 객체 생성

# 1. 정말 최고의
def get_tokens(review):
    # 토큰객체.fit_on_texts() : 각 단어의 인덱스(숫자)를 대응하는 *단어사전* 생성 # 빈도수에 따라 인덱스(숫자) 위치가 결정된다.
    tokenizer.fit_on_texts(review)
    print(tokenizer.word_index)
    total_words = len(tokenizer.word_index)+1
    print(total_words)
    # 각 문장을 숫자(벡터)로 변환 # .texts_to_sequences()
    tokenized_sentences = tokenizer.texts_to_sequences(review) # 위에 정의된 단어 사전 기준으로 단어를 인덱스(숫자)
    print(tokenized_sentences) # [14, 31, 3, 139, 538, 1, 410, 63, 1380, 3, 790, 10, 127, 179, 46, 61, 238, 89, 57

    #
    input_seauences = []
    for token in tokenized_sentences: # 문장(여러 벡터)을 하나씩 반복
        for t in range(1,len(token)): #
            n_gram_sequence = token[:t+1] # 토큰 리스트에서 처음부터 t+1번째 단어까지를 슬라이싱한다 (시퀀스)
            print(f'n_gram_sequence : {n_gram_sequence}')
            input_seauences.append(n_gram_sequence) # 각 시퀀스 저장

    return input_seauences , total_words # 리스트 반환 # 모든 시퀀스가 저장된 리스트 반환 # 2개 값이 저장된 튜플 1개 반환
    # 모든 수학 및 프로그래밍의 연산식 또는 함수는 항상 반환/결과 값이 1개이다.

input_seauences , total_words = get_tokens(review)
print(input_seauences[31:40]) # 샘플 홛인

# 단어사전
print("감동 : " , tokenizer.word_index['감동'])
print("영화 : " , tokenizer.word_index['영화'])
print("코믹 : " , tokenizer.word_index['코믹'])

# # 4. 패딩 : 모델이 시퀀스(문장)들을 학습할 때 길이를 맞춤으로써 동일한 차원을 처리할 수 있게 하기 위해서 해야한다.
max_len = max([len(word) for word in input_seauences]) # 모든 시퀀스 중에 가장 길이가 큰 수 찾기
print(f'max_len : {max_len}') # 가장 긴 문장은 59개 단어를 가졌다.
# 패딩 함수를 이용한 패딩화 하기 # pad_sequences(데이터리스트 , maxlen=최대길이 , padding='pre앞 post뒤')
result = pad_sequences(input_seauences , maxlen=max_len , padding='pre')
print(f'result : {result}')
input_seauences = np.array(result) # 패딩 결과를 다시 배열로 변환
print(f'input_seauences : {input_seauences}')

# 5. 독립변수와 종속변수(정답) 구분하기 : 모델의 학습을 위해서
from tensorflow.keras.utils import to_categorical
# x는 독립변수 데이터로 , 각 시퀀스의 마지막 단어를 제외함(왜? 마지막 단어는 예측하기 위해서
# 즉) 모델은 시퀀스의 처음부터 마지막 단어 직전까지를 학습 시킨다.
x = input_seauences[:,:-1] # 마지막 값은 제외함
# y는 종속변수 데이터로 , 각 시퀀스의 마지막 단어를 원핫인코딩으로 변환한다.(왜? 위치 찾기 위해서)
y = to_categorical(input_seauences[:,-1] , num_classes=total_words) # 마지막 값만 이진 클래스 벡터 변환
# * to_categorical() : 레이블 값을 원핫 인코딩을 하며 반환 함수
a = to_categorical([0,1,2,3],num_classes=4)
# [0,1,2,3] 원핫 인코딩 했을 때
print(a) # [[1. 0. 0. 0.] [0. 1. 0. 0.] [0. 0. 1. 0.] [0. 0. 0. 1.]]

# 6. 모델 생성
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding , LSTM , Dense , Bidirectional , Dropout

embedding_dim = 256
model = Sequential() # 딥러닝 모델
    # 1. 임베딩 레이어(원핫인코딩(벡터) vs 밀집인코딩(벡터)) : 밀집벡터로 변환 하는 역할
        # input_dim : 입력받을 단어의 총수
        # output_dim : 밀집 벡터로 변환된 벡터 차원 수 # 256차원의 벡터로 표현
        # input_length : 입력 데이터의 최대길이(마지막 단어 제외한 -1) 지정 # 59
model.add(Embedding(input_dim=total_words , output_dim=embedding_dim , input_length=max_len-1))
    # 2. 양방향(Bidirectional) , RNN알고리즘(LSTM) # Bidirectional(LSTM()) : 양방향 RNN 알고리즘
model.add(Bidirectional(LSTM(units=256))) # 유닛/노드/뉴런 : 학습하면서 특징/파라미터/값을 저장하는 개수 # 양방향 *2
    # 3. 출력레이어 : 출력개수는 2진 분류가 아닌 다중 분류이므로 활성화함수는 'softmax' ,
model.add(Dense(units=total_words , activation='softmax')) # 마지막 출력 레이어의 유닛/노드/뉴런의 종속변수 개수
print(model.summary())
# model = Sequential([
#     Embedding(input_dim=total_words ,
#               output_dim=embedding_dim ,
#               input_length=max_len-1) ,
#     Bidirectional(LSTM(units=256)) ,
#     Dense(units=total_words , activation='softmax')
# ])
    # 5. 컴파일(머신러닝과 다르게 학습 도중에 손실함수(loss)와 평가지표(accuracy 정확도) 확인/모니터링 할 수 있는 함수/기능
    # 최적의 파라미터 찾기 = 튜닝 작업
model.compile(loss='categorical_crossentropy' ,
              optimizer='adam' ,
              metrics=['accuracy'])
history = model.fit(x , y , epochs=20 , verbose=1) # x : 독립변수 , y : 종속변수 , # 학습 수
# 딥러닝 : 머신러닝보다 조금 더 복잡하고 많은 학습을 함으로 패턴 찾기

# 문장 생성 추론
# 7. 문장생성 함수 / 예측
def text_generation(sos , count): # sos : "안녕하세요" , count = 3 #
    for _ in range(1 , count): # 1 부터 생성할 단어수 까지
        token_list = tokenizer.texts_to_sequences([sos])[0] # sos(새로운문장)을 벡터로 변환
        token_list = pad_sequences([token_list] , # 새로운문장을 패딩화해서 학습된 문장들과 동일하게 일치
                                   maxlen=max_len-1 ,
                                   padding='pre')
        # 예측하기 # 모델객체명.predict(예측할데이터)
        result = model.predict(token_list)
        print(result) # 예측된 단어들의 확률 (0~1)
        # 여러 확률 중 가장 확률이 높은 단어 확인
        predicted = np.argmax(result , axis=1) # numpy(np) 넘파이 객체 # np.argmax(배열 , axis=1) 배열 내 최대값 인덱스
        # 반복문을 이용한 단어 사전에서 비율이 높은 예측 단어 찾기
        for word , idx in tokenizer.word_index.items(): # 토크나이저객체.word_index.items() : 단어사전들의 단어
            if idx == predicted:
                # 만약에 단어 사전내 인덱스가 예측 인덱스와 같으면
                output = word # 찾은 인덱스의 단어 저장
                break

        sos += " "+ output # 새로운 문장 뒤에 예측한 단어 연결하기
    return sos

# # argmax 설명 : 최대값의 인덱스 반환
# data = [[0.1 , 0.2 , 0.7] , [0.3 , 0.5 , 0.2] , [0.4 , 0.3 , 0.3]]
# print(np.argmax([data] , axis=-1))

print(text_generation("연애 하면서" , 12)) # 연애 하면서 뒤로 11개의 예측단어 붙여준다.
# 연애 하면서 연기 가 너무 잘 몰라서 그러는데 이런 영화 임 ㅠㅠㅠ 대 -> epochs=20
# 연애 하면서 나 만 당할수 없다가있었는데 꼭 맞는 영화 이다 차라리 월트디즈니 애니메이션 -> epochs=30

print(text_generation("꿀잼" , 12))
# 꿀잼 영화 추억 이다 ㅜㅜ ㅜㅜ 재밌게 봤어요 ㅋㅋㅋ 그래도 10 점 -> epochs=20
# 꿀잼 영화 추억 이다 ㅜㅜ ㅜㅜ 또 않은 영화 옥주현 나오는줄 알았다 -> epochs=30

print(text_generation("최고의 영화" , 12))
# 최고의 영화 를 숨 참고 만들었나 봐요 ㅋㅋ 그냥 열심히 하는 배우 들 -> epochs=20
# 최고의 영화 정말 감동 적임 내용 이 뻔하다는 것 때문 에 1 점 -> epochs=30

print(text_generation("손발 이" , 12))
# 손발 이 오 그라드 네 요 재밌었는데 친구 는 개 좋음 좋음 아니었으면 -> epochs=20
# 손발 이 오 그라드 네 요 네 요 ㅋㅋ 도 더 그래서 더 -> epochs=30





