from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# 데이터 준비
X = [[0.44], [0.68], [0.89], [0.93]]
y = [0.55, 0.8, 0.92, 0.99]

# 2차 다항 회귀 모델 생성
model = make_pipeline(PolynomialFeatures(2), LinearRegression())

# 모델 훈련
model.fit(X, y)

# 예측
print(model.predict([[0.5], [0.75]]))
