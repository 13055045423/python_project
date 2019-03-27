lsj_user = input("")
number_list = []
for character in lsj_user:
    number_list.append(character)
centre_str = number_list[int((len(number_list)-1)/2)]
print(centre_str)

