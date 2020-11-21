print("Klub A: ",end="")
klubA = input()
print("Klub B: ",end="")
klubB = input()

print("Pertandingan 1 : ",end="")
skor = input().split()
i = 1
array = []
while int(skor[0]) != -1 and int(skor[1]) != -1:
    if int(skor[0]) > int(skor[1]):
        array.append(klubA)
    elif int(skor[1]) > int(skor[0]):
        array.append(klubB)
    elif int(skor[0]) == int(skor[1]):
        array.append("Draw")
    i = i + 1
    print(f"Pertandingan {i} : ",end="")
    skor = input().split()

for i in range(len(array)):
    print(f"Hasil {i+1} : {array[i]}")
print("Pertandingan selesai")