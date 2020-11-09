def sum_list(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum

print (sum_list([1,2,3,4]))

def max_list(list2):
    max = list2[0]
    for i in list2:
        if max < i:
            max = i
    return max

print (max_list([1,2,3,4]))

def multiplication_list(list3):
    res = 1
    for i in list3:
        res *= i
    return res

print (multiplication_list([1,2,3,4]))

def clean_list(list4):
    res=[]

    for i in list4:
        test = 0

        for j in res:
            if j == i:
                test = 1

        if test == 0 :
            res.append(i)

    return res

print (clean_list([1,2,4,3,4]))

def clean_list2(list5): # will ordinate list too
    res=list(set(list5))
    return res

print (clean_list2([1,2,4,3,4]))


def dot_product1(listA,listB):

    if len(listA) != len(listA):
        print("Please select two lists with the same length")
        exit()

    plist=list()
    res = 0

    for i in range(len(listA)):
        plist.append(listA[i]*listB[i])

    for j in plist:
        res += j
    return res

print (dot_product1([1,2,3,4],[1,2,2,3]))


def dot_product2(listA, listB):
    plist = list()

    for i in range(len(listA)):
        plist.append(listA[i] * listB[i])

    return sum_list(plist)

print (dot_product2([1,2,3,4],[1,2,2,3]))