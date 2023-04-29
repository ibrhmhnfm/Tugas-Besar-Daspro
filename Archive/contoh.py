f = open("/home/em/Documents/Daspro/Tubes/tes.csv")

arr = f.readlines()
arr = [j.strip() for j in arr]
for i in range (len(arr)):
    arr[i] = arr[i].split(";")
print(arr)

f.close()

