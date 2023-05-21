print("20202727_김상현")
aa = []
for i in range(0, 10) :
    aa.append(0)
hap = 0


for i in range(0, 10) :
    aa[i] = int(input(str(i + 1) + "번째 숫자 : "))


i = 0
while i < 10:
    hap = hap + aa[i]
    i += 1

print("합계 ==> %d" %hap)
    
