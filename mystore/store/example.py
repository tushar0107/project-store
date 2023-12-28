x= [5,7,5,3,5,6,7,5,3,5,7,5,2,3,4,7,6,8]

y={}

for i in x:
    if i not in y.keys():
        y[i]=x.count(i)

print(y)
print(y.values())

# class Obj:
#     a=4
#     b=5

#     def __init__(self):
#         return (self.a,self.b)

# Obj.c = 7
# print(Obj.c)