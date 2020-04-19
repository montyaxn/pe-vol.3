print("=======================")
bm = float(input("your weight[kg] : "))
ci = float(input("your CI[kcal]   : "))
print("=======================\n")

p = bm*2
f = ci / 36.0
c = ci - f - p*4

print("\n>> Macronutorient you should take in")
print(f'>> P : {p}')
print(f'>> F : {f}')
print(f'>> C : {c}')
