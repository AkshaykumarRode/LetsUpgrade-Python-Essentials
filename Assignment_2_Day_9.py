lst = list(range(1,1000))
def armst(lst):
    for num in lst:
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** order
            temp  = temp//10
        if num == sum:
            yield num
print(list(armst(lst)))
