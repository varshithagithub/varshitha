rows=7
first_num=1
odd_num=first_num
for i in range(1,rows+1):
  odd_num=first_num
  for j in range(1,i+1):
    print("input a=",i,"output:",odd_num,end='')
    odd_num+=2
  print('')
