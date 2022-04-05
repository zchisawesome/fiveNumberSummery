thislist=[]
val = 0
yorn='y'
while yorn == 'y':
  val = float(input("add number"))
  thislist.append(val)
  yorn=input("continue? y/n")

thislist.sort()
print(thislist)
print("median:")
y = 0.0
x=0.0
if int(len(thislist))%2==1:
  print(thislist[int(len(thislist)/2)])
else:
  y=thislist[int(len(thislist)/2)]
  x=thislist[int(len(thislist)/2)-1]
  print((y+x)/2)
print("min:")
print(thislist[0])
print("max")
print(thislist[len(thislist)-1])

print("Q1")
if (int(len(thislist))-1)%4==0:
  print(thislist[int(len(thislist)/4)])
elif int(len(thislist))%2==0:
  x=thislist[int(len(thislist)/4)]
  y=thislist[int(len(thislist)/4)-1]
  print((x+y)/2)
else:
  x=thislist[int(len(thislist)/4)+1]
  y=thislist[int(len(thislist)/4)]
  print((x+y)/2)

print("Q3")
if (int(len(thislist))-1)%4==0:
  print(thislist[int(len(thislist)*3/4)])
elif int(len(thislist))%2==0:
  x=thislist[int(len(thislist)*3/4)]
  y=thislist[int(len(thislist)*3/4)-1]
  print((x+y)/2)
else:
  x=thislist[int(len(thislist)*3/4)+1]
  y=thislist[int(len(thislist)*3/4)]
  print((x+y)/2)