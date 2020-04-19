print("======================")
weight = float(input("your weight[kg] : "))
height = float(input("your height[cm] : "))
age    = float(input("your age        : "))
print("======================")

bm = 10 * weight + 6.25 * height - 5 * age + 5
print(f"\n>> your bm[kcal] is {bm}");
