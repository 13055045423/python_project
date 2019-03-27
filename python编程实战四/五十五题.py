lsj_user = input("")
lsj_user.lower()
empty_list = []
for str_list in lsj_user:
    empty_list.append(str_list)
#empty_list = []
#small_write_list.count()
new_list = {}
for character in empty_list:
#    small_write_list.count(character)
    empty_list.count(character)
    new_list.setdefault(character,empty_list.count(character))
print(new_list)
    

