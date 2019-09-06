
K = input("국어 점수는?")
M = input("수학 점수는?")
E = input("영어 점수는?")
J = input("자바 점수는?")
P = input("파이썬 점수는?")
JS = input("JSP 점수는?")
sum = int(K) + int(M) + int(E) + int(J) + int(P) + int(JS)
print("총점은", sum)
avg = sum/6
print("평균은", round(avg,2))
if avg >=90:
    print("용돈 : 100000원")

elif avg >= 80:
    print("용돈 :80000원")

elif avg >= 70:
    print("용돈 :70000원")

elif avg >= 60:
    print("용돈 :60000원")

else:
    print("용돈 :50000원")
