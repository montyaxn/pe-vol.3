print("=====================")
cc = float(input("your CC[kcal] : "))
print("=====================\n")

print("============================================================================")
print("[A : I wanna be smaller] [B : I don't care about it] [C : I wanna be bigger]")
ty = input("your type     : ")
print("============================================================================")

if ty=='A' :
    ci = cc * 0.8
elif ty=='B' :
    ci = cc * 1
elif ty=='C' :
    ci = cc * 1.2
else:
    print("UNKO!")

print(f"\n>> your CI[kcal] is {ci}")
