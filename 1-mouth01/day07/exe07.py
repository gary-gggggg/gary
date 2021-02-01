"""骰子"""
list2=[1,2,3,4,5,6]
list1=[1,2,3,4,5,6]
result=[(l1,l2)for l1 in list1 for l2 in list2]
print(result)
list3=[1,2,3,4,5,6]
result2=[(l1,l2,l3)for l1 in list1 for l2 in list2 for l3 in list3]
print(result2)
