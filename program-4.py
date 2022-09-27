input=[1,2,3,4,5,6,7,8,9]
m=[1,2,8,9,12,46,76,82,15,20,30]
d={}
for i in input:
  count=0
  for j in m:
    if j%i==0:
      count=count+1
    d.update({i:count})
print("output:",d)
