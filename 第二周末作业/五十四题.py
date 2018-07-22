lsj_user = input("")
l = ""
l2 = ""
for subscript,value in enumerate(lsj_user):
    if subscript%2==0:
        l+=value
    else:
        l2+=value
l3 = l+l2
print(l3)
