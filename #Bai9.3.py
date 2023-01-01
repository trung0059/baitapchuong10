#Bai9.3
chieucao = float(input("nhap chieu cao cua ban"))
cannang = float(input("nhao can nang cua ban"))
BMI = cannang/(chieucao*chieucao)
if BMI<18.5:
    print("bạn quá gầy")
elif 18.5<BMI<24.99:
    print("bạn bình thường")
elif BMI>=25:
    print("bạn bị thừa cân")