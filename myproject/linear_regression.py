import numpy as np
import matplotlib.pyplot as plt

# 데이터 정의
x = np.array([0, 2, 4, 6, 9, 11, 12, 15, 17, 19])
y = np.array([5, 6, 7, 6, 9, 8, 7, 10, 12, 12])

# 필요한 계산 수행
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x*y)
sum_x2 = np.sum(x**2)
sum_y2 = np.sum(y**2)

# 기울기(m_yx) 및 절편(c_yx) 계산 (x 대 y)
m_yx = (n*sum_xy - sum_y*sum_x) / (n*sum_y2 - sum_y**2)
c_yx = (sum_x - m_yx*sum_y) / n

# x에 대한 예측
x_pred = m_yx*y + c_yx

# 상관 계수(r) 계산
r = (n*sum_xy - sum_x*sum_y) / np.sqrt((n*sum_x2 - sum_x**2)*(n*sum_y2 - sum_y**2))

# 표준 오차(SE) 계산
SE = np.sqrt(np.sum((x - x_pred)**2) / (n-2))

# 결과 출력
print(f"기울기: {m_yx:.2f}")
print(f"절편: {c_yx:.2f}")
print(f"상관 계수: {r:.2f}")
print(f"표준 오차: {SE:.2f}")

# 그래프 그리기
plt.figure(figsize=(8, 4))
plt.scatter(y, x, color='blue', label='Actual Data')
plt.plot(y, x_pred, color='red', label=f'Regression Line: $x = {m_yx:.2f}y + {c_yx:.2f}$')
plt.title('Linear Regression Analysis (Regressing x on y)')
plt.xlabel('y')
plt.ylabel('x')
plt.legend()
plt.grid(True)
plt.show()
