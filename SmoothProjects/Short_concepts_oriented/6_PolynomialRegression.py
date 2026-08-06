from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Real world - ice cream sales vs temperature!
temp = [[5], [10], [15], [20], [25], [30], [35], [40]]
sales = [10, 20, 35, 55, 80, 85, 75, 60]

poly = PolynomialFeatures(degree=2)
temp_poly = poly.fit_transform(temp)

model_lin = LinearRegression()
model_lin.fit(temp_poly, sales)

model_score = model_lin.score(temp_poly, sales)
print(f"Linear Model Score: {model_score:.2f}")