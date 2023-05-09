#Function to *approximate* fraction from decimal expansion
#Outputs closest fraction a/b where a,b are 0,1,2...10.

n = float(input('Enter decimal expansion: '))

a = [0, 0.1, 0.111, 0.125, 0.143, 0.166, 0.2, 0.222, 0.25, 0.286, 0.3, 0.333, 0.375, 0.4, 0.429, 0.444, 0.5, 0.555, 
     0.571, 0.6, 0.625, 0.666, 0.7, 0.714, 0.75, 0.777, 0.8, 0.833, 0.857, 0.875, 0.888, 0.9, 1]

e = 1
temp = 0

for i in range(len(a)):
    temp = abs(n - a[i])
    if temp < e:
        e = temp
        d = a[i]

d = 1/d
for i in range(8):
    temp = d*(i+1)
    if temp % 1 < 0.01:
        break
print(i+1, "/", temp)