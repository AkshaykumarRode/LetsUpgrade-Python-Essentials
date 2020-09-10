lst1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst1.append(ele) # adding the element
print(lst1)
sub_list = [1,1,5]
flag = 0
if(all(x in lst1 for x in sub_list)):
    flag = 1
if (flag) :
    print ('Its a match')
else :
    print ('Its gone')
