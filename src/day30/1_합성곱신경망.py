import tensorflow as tf

# 1. 데이터셋 로드 : , 10가지 종류의 의류 이미지 데이터셋
fashion_mnist = tf.keras.datasets.fashion_mnist
(x_train , y_train),(x_valid , y_valid) = fashion_mnist.load_data()


# 생각해보기 : 위 데이터셋을 이용한 합성곱 모델 구축하고 학습하여 정확도(accuracy) 95% 이상 되도록 최적의 하이퍼 파라미터 설정하여 모델 만들기
print(x_train.min() , x_train.max())
print(x_valid.min() , x_valid.max())

# 2. 데이터 전처리
x_train = x_train/255.0 # 정규화 # 0~255 범위를 0~1 범위로 변경
x_valid = x_valid/255.0

print(x_train.min() , x_train.max())
print(x_valid.min() , x_valid.max())

print(x_train.shape , x_valid.shape) # (60000, 28, 28) (10000, 28, 28)

x_train_in = x_train[..., tf.newaxis] # 3차원 ---> 4차원
x_valid_in = x_valid[..., tf.newaxis]

print(x_train_in.shape , x_valid_in.shape) # (60000, 28, 28, 1) (10000, 28, 28, 1)
model = tf.keras.Sequential([ # Conv(특성맵수 , (커널영역단위) , activation='활성화함수' , input_shape=(입력텐서차원)
    tf.keras.layers.Conv2D(32,(3,3), activation='relu', # 1. 합성곱 레이어 # input_shape=
                           input_shape=(28,28,1), name='conv'),
    tf.keras.layers.MaxPooling2D((2,2), name='pool'), # 최대값 풀링 (2*2)
    tf.keras.layers.Dense(32 , activation='relu'),
    tf.keras.layers.Flatten(),  # 학습된 결과의 다차원을 1차원으로 변환
    tf.keras.layers.Dense(10, activation='softmax'), # 종속변수의 결과 종류가 10개라서 10 , 다중분류 : softmax 활성화 함수 사용한다.
])
# 4. 모델 컴파일 # 학습하면서 학습된 데이터를 가지고 테스트용 데이터를 실행할 수 있다.
model.compile(optimizer='adam' , loss='sparse_categorical_crossentropy' , metrics=['accuracy'])
# 5. 모델 훈련
history = model.fit(x_train_in , y_train, # 학습에 사용되는 데이터
                    validation_data=(x_valid_in , y_valid), # 학습하면서 컴파일이 테스트를 할 테스트 데이터
                    epochs=20)  # 훈련 반복 횟수

# 최적의 파라미터 찾기 위해서는 1. epochs 조정 2. 레이어 조정
# 1. epochs=n개
# 2.     tf.keras.layers.Dense(32 , activation='relu')
# 등등
# 적절한 정확도 떨어지지 않고 손실값이 증가하지 않는 지점
import matplotlib.pyplot as plt
def plot_loss_acc(history , epoch):
    loss , val_loss = history.history['loss'], history.history['val_loss'] # 훈련 손실(오차) 값 # 테스트 손실(오차) 값
    acc , val_acc = history.history['accuracy'], history.history['val_accuracy']    # 훈련 정확도 # 테스트 정확도
    # 서브플롯 차트 구성
    fig , axes = plt.subplots(1 , 2 , figsize=(12 , 4)) # 1행의 2열로 구선된 서브플롯
        # x축 훈련수 # y축 훈련 오차값
    axes[0].plot(range(1 , epoch+1) , loss , label='Training')
        # x축 훈련수 # y축 테스트 오차값
    axes[0].plot(range(1, epoch+1), val_loss, label='Validation')
    axes[0].legend(loc='best')
    axes[0].set_title('Loss')

    axes[1].plot(range(1, epoch+1), acc, label='Training') # x축 훈련수 # y축 훈련 정확도
    axes[1].plot(range(1, epoch+1), val_acc, label='Validation') # x축 훈련수 # y축 테스트 정확도
    axes[1].legend(loc='best')
    axes[1].set_title('Accuracy')

    plt.show()

plot_loss_acc(history , 20)



