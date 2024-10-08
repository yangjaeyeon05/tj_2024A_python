import numpy as np
import tensorflow as tf

# 케라스의 내장된 데이터셋에서 mnist(손글씨이미지) 데이터셋 로드
mnist = tf.keras.datasets.mnist
print(mnist)

# 데이터셋을 다운로드 (훈련용 , 테스트용)
(x_train , y_train) , (x_test , y_test)= mnist.load_data()
print(x_train.shape , y_train.shape)    # (60000, 28, 28) (60000,)
print(x_test.shape , y_test.shape)  # (10000, 28, 28) (10000,)
                                    # (데이터크기 , 세로픽셀 , 가로픽셀)
                                    # 28 * 28 픽셀 크기의 정사각형 이미지 6만개 저장된 상태

# 시각화
import matplotlib.pyplot as plt

fig, axes = plt.subplots(3 , 5) # 3행 5열 여러개 차트 표현
fig.set_size_inches(8 , 5)  # 전체 차트의 크기를 가로 8인치 세로 5인치
for i in range(15): # 0부터 14까지 반복문 실행
    ax = axes[i//5 , i%5]    # i//5 : 몫(행 인덱스)    # i%5 : 나머지(열 인덱스)
    # i = 0 , 0//5 -> 0 , 0%5 -> 0 [0 , 0]
    # i = 1 , 1//5 -> 0 , 1%5 -> 1 [0 , 1]
    ax.imshow(x_train[i] , cmap='gray')  # ax.imshow() : 이미지 출력하는 메소드
    ax.axis('off')  # 축 표시 끄기
    ax.set_title(str(y_train[i]))   # 각 이미지(차트)/정답을 제목으로 출력

plt.show()

# 데이터 전처리   # [0 : 첫번째이미지 , 10:15 : 특정한 픽셀 , 10:15 : 특정한 픽셀]
print(x_train[0 , 10:15 , 10:15])
'''
[[  1 154 253  90   0]
 [  0 139 253 190   2]
 [  0  11 190 253  70]
 [  0   0  35 241 225]
 [  0   0   0  81 240]]
'''
# 0~255사이가 아닌 0~1 사이를 가질 수 있도록 범위를 정규화
print(x_train.min() , x_train.max())    # min() : 최솟값 찾기 함수 # max() : 최대값 찾기 함수 # 0 255
# 데이터 정규화
x_train = x_train / x_train.max()   # 값 / 최대값   # 각 값들에 나누기 255
print(x_train.min() , x_train.max())    # 0.0 1.0
x_test = x_test / x_test.max()  # 테스트용 정규화

print(x_train[0 , : , :])   # 5손글씨 정규화 후 출력

# Dense 레이어에는 1차원 배열만 들어갈 수 있으므로 2차원 배열을 1차원으로 변경
print(x_train.shape)    # (60000, 28, 28) # 2차원 (데이터수 , 가로 , 세로)
# 방법1) 텐서플로 방법
print(x_train.reshape(60000 , -1).shape)    # (60000, 784) # 1차원 (데이터수 , 가로)
# 방법2) 플레튼 레이어 방법
print(tf.keras.layers.Flatten()(x_train).shape) # (60000, 784)

# 방법1) 레이어에 활성화 함수 적용할때 # relu 함수
tf.keras.layers.Dense(128 , activation='relu')
                    # 128개의 노드 , relu 활성화 함수를 적용하는 레이어
# 방법2)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128) , # 128개 노드의 레이어 1개
    tf.keras.layers.Activation('relu')  # 별도로 활성화 함수 레이어 추가
])  # 입력층 명시된 상태 아니고, 1개의 레이어만 정의될 때는 출력층이다.
# 출력층이 128개의 노드로 구성된 모델

# 모델 생성
model = tf.keras.Sequential([
    # 입력층 # 독립변수 784개
    # 2차원 (이미지)를 1차원 변환 : Flatten 패턴  # 28 * 28 -> 784를 가지는 1차원 배열
    tf.keras.layers.Flatten(input_shape=(28,28)) ,
    # 은닉층 # 각 레이어들 간의 연결된 완전 연결층이다. # 각 256 , 64 , 32개의 노드를 가지는 은닉층 3개 # 각 relu라는 비선형성 활성화 함수 적용
    tf.keras.layers.Dense(256 , activation='relu') ,
    # 은닉층
    tf.keras.layers.Dense(64 , activation='relu') ,
    # 은닉층
    tf.keras.layers.Dense(32 , activation='relu') ,
    # 출력층 # 종속변수 10개 # 분류 모델
    tf.keras.layers.Dense(10 , activation='softmax')
    # 정답은 0 ~ 9 사이의 손글씨 정답 # 정답은 0 또는 1 또는 2 또는 ~~~ 9 # 개수 10개
])
# 각 레이어(은닉층)개수 , 각 노드의 개수는 중요한 하이퍼 파라미터가 된다.

print(model.summary())

# [3-6] 손실함수
# (1) 이진분류 : 출력노드가 1개 , sigmoid일 경우
model.compile(loss='binary_crossentropy')

# (2) y가 원핫 벡터 인경우
    # y = 5 일때 원핫 = [0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ,0]
model.compile(loss='categorical_crossentropy')
# (3) y가 원핫 벡터가 아닐 때
    # y = 5
model.compile(loss='sparse_categorical_crossentropy')

# [3-7] 옵티마이저
# (1) 클래스로 지정하는 방법
adam = tf.keras.optimizers.Adam(learning_rate=0.001) # 텐서플로2 부터는 lr 대신 -> learning_rate
model.compile(optimizer=adam)
# (2) 문자열로 지정하는 방법
model.compile(optimizer='adam')

# [3-8] 평가지표
# (1) 클래스를 지정하는 방법
acc = tf.keras.metrics.SparseCategoricalAccuracy()
model.compile(optimizer='adam' ,
              loss='sparse_categorical_crossentropy' ,
              metrics=[acc])
# (2) 문자열로 지정하는 방법
model.compile(optimizer='adam' ,
              loss='sparse_categorical_crossentropy' ,
              metrics=['accuracy'])

# [3-9] 훈련  # fit(독립변수 , 종속변수 , epochs=학습반복수 , validation_data=)
model.fit(x_train , y_train , epochs=10 , validation_data=(x_test , y_test))
'''
Epoch 1/10
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 5s 2ms/step - accuracy: 0.8740 - loss: 0.4179 - val_accuracy: 0.9614 - val_loss: 0.1218
    - 1. Epoch 1/10 - 현재 훈련중인 반복(에포크)수
    - 2. 35/1875    - 현재 진행중인 배치의 번호
        총 = 1875 , 총 데이터수가 60000개 . 총 배치수 : 32개 => 총데이터수/총배치수
    - 배치란? : 모델 훈련에서 전체를 구분한 집합 수 # 주로 32개 64개 128개 사용 # 기본값은 32개 사용한다.
'''
'''
# loss랑 val_loss가 차이나는 이유
과적합: 모델이 훈련 데이터에 너무 잘 맞춰져서 검증 데이터에서는 성능이 떨어질 수 있습니다. 
이 경우 loss는 낮지만 val_loss는 상대적으로 높게 나타날 수 있습니다.

데이터 분포 차이: 훈련 데이터와 검증 데이터의 분포가 다를 수 있습니다. 
이 경우 모델이 훈련 데이터에서는 좋은 성능을 보이지만, 검증 데이터에서는 잘 일반화되지 않을 수 있습니다.

모델의 성능을 평가할 때는 val_loss를 더 중요하게 고려하는 것이 좋습니다.
'''

# [3-10] 평가
test_loss , test_acc = model.evaluate(x_test , y_test)
print(test_acc) # 1에 가까울 수록 좋은 성능   # 백분율   # 0.9797999858856201
print(test_loss)

# [3-11] 예측
predictions = model.predict(x_test)
print(predictions[0])
'''
[3.50064758e-13 1.02153626e-10 2.52314055e-12 3.84136334e-11
 6.10178019e-11 1.56672411e-10 1.98643162e-16 1.00000000e+00
 5.55875451e-15 1.20178742e-10]
'''
# 가장 높은 확률만 추출  # np.argmax() : 배열내 가장 큰 값을 가진 인덱스 반환 함수
print(np.argmax(predictions[0]))    # 인덱스 7
# 가장 앞에 있는 10개 예측 값 확인 # np.argmax( , axis=차원수)
print(np.argmax(predictions[ : 10] , axis=1)) # 예측 10개 확인 : [7 2 1 0 4 1 4 9 6 9]

print(y_test[ : 10])    # 예측값 정답 10개 확인 : [7 2 1 0 4 1 4 9 5 9]

# [3-12] 시각화
def get_one_result(idx):
    img , y_true , y_pred , confidence = x_test[idx], y_test[idx] , np.argmax(predictions[idx]) , 100*np.max(predictions[idx])
                                         # 테스트 독립변수 , 테스트 종속변수/정답 , 예측값 , 예축값 확률
    return img , y_true , y_pred , confidence

fig , axes = plt.subplots(3 , 5)    # 3행 5열로 차트 구성
fig.set_size_inches(12 , 10)    # 차트 전체 크기를 가로 12인치 세로 10인치로 구성
for i in range(15): # 0 ~ 14까지 반복
    ax = axes[i//5 , i%5]
    img , y_true , y_pred , confidence = get_one_result(i)
    # imshow로 이미지 시각화
    ax.imshow(img , cmap='gray')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f'True : {y_true}')    # 정답을 차트 제목
    ax.set_xlabel(f'Prediction : {y_pred}\nConfidence : ({confidence:.2f} %)')
plt.tight_layout()
plt.show()










