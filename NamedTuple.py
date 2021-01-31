from collections import namedtuple

n = int(input())
fields = input().split()

total = 0
for i in range(n):
    sheet = namedtuple('student', fields)
    field1, field2, field3, field4 = input().split()
    obj = sheet(field1, field2, field3, field4)
    total = total + int(obj.MARKS)

print("%.2f"%(total / n))
