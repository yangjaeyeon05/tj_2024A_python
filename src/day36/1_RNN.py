import tensorflow as tf
# 1. 임베딩 레이어 구현 # Embedding(단어수 , 차원수) : 임베딩 클래스
embedding_layer = tf.keras.layers.Embedding(100 , 3) # 100개 단어 , 3차원 사용
result = embedding_layer(tf.constant([12 , 8 , 15 , 20])) # 임의(더미)의 숫자 4개를 입력데이터에 넣어준다.
print(result) # 각 임의 데이터 4개를 임베딩 레이어를 걸쳐 3개의 숫자로 변환하여 표현된다.
# tf.Tensor(
# [[ 0.04025617 -0.02730993  0.0382051 ] # 12데이터
#  [-0.04267859  0.04141765  0.0150621 ] # 8데이터
#  [ 0.02547157 -0.03365153  0.02231524] # 15데이터
#  [-0.04135699 -0.03323986  0.02032632] # 20데이터
#  ], shape=(4, 3), dtype=float32)
# 결론 : 각 숫자(단어)를 의미하는 벡터로 바꾸어 주는 임베딩 레이어 역할

# 임베딩 레이어 활용
model = tf.keras.Sequential() # Sequential([ 레이어객체1 , 레이어객체2 , 레이어객체3 ])
    # 100개의 단어를 3차원 벡터로 변환하겠다는 속성값 대입 , 최대 32개의 단어로 이루어져 있다는 속성값 대입
model.add(tf.keras.layers.Embedding(100 , 3 , input_length=32)) # .add(레이어객체)
    # 32개의 결과를 예측한다.
model.add(tf.keras.layers.LSTM(units=32)) # Long short Term Memory 긴 문장에서 중요한 정보는 기억하는 RNN 클래스
    # 출력(결과)레이어 , 결과를 1개로 출력한다.
model.add(tf.keras.layers.Dense(units=1))
print(model.summary())

# 라이브러리 불러오기
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding , LSTM , Dense

# 임베딩 레이어 활용
model = Sequential()
model.add(Embedding(100 , 3 , input_length=32))
model.add(LSTM(32))
model.add(Dense(1))
print(model.summary())

# 3. 양방향 순환 신경망 # Bindirectional() 클래스
from tensorflow.keras.layers import Bidirectional

model = Sequential()
model.add(Embedding(100,3)) # 임베딩 (총 단어수 : 100 , 차원수 : 3)
model.add(Bidirectional(LSTM(32))) # LSTM 구조를 양방향으로 설정 # 유닛의 개수가 32의 2배인 64개 나왔다.
model.add(Dense(1))
print(model.summary())

# 4. 스태킹 RNN
model = Sequential() #
model.add(Embedding(100 , 32)) # 총 100개의 단어 , 32차원
model.add(LSTM(32 , return_sequences=True)) # 32개의 유닛(뉴런) # 모든 timeStep에 대해 출력을 한다.
model.add(LSTM(32)) # 최상단 RNN에서는 return_sequences=True 할 필요가 없다.
model.add(Dense(1)) # 출력 레이어
print(model.summary())

# 5. 순환 드롭아웃
model = Sequential()
model.add(Embedding(100 , 32))
    # recurrent_dropout=0.2 # LSTM의 순환 드롭아웃의 비율
        # 타입스텝의 출력을 다음 타임스텝의 입력으로 사용할 때 20%를 무작위로 제거하여 과대적합을 방지한다.
    # dropout=0.2
        # 입력으로 들어오는 데이터로 사용할 때 20%를 무작위로 제거하여 과대적합을 방지한다.
model.add(LSTM(32 , recurrent_dropout=0.2 , dropout=0.2))
model.add(Dense(1 , activation='sigmoid'))
print(model.summary())