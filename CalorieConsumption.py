print("=====================")
bm = float(input("your BM[kcal] : "))
print("=====================\n")
print("====================================================================")
print("[A : I don't exercise] [B : I do exercise] [C : I do exercise a lot]")
ty = input("your type     : ")
print("====================================================================")

if ty=='A' :
    cc = bm * 1.2
elif ty=='B' :
    cc = bm * 1.55
elif ty=='C':
    cc = bm * 1.725
else :
    print("UNKO!!!!!")
    quit()


print(f"\n>> your CC[kcal] is {cc}")
