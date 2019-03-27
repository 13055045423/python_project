print("定制自己的手机套餐:")
#lsj_duratlon = []
#def call_list()
call_list1 = ["A.请设置通话时长:","1.0分钟","2.50分钟","3.100分钟","4.300分钟","5.不限量"]
for call in call_list1:
    print(call)
lsj_user = int(input("请选择通话时间编号:"))
#lsj_duratlon.append(call_list1[lsj_user])
duration = call_list1[lsj_user].split('.')[1]
print("")
flow_list =["B.请设置流量:","1.0M","2.500M","3.1G","4.5G","5.不限量"]
for flow in flow_list:
    print(flow)
lsj_user1 = int(input("请设置流量:"))
flow1 = flow_list[lsj_user1].split(".")[1]
print("")
note_list = ["C.请设置短信条数:","1.0条","2.50条","3.100条"]
for note in note_list:
    print(note)
lsj_user3 = int(input("请设置短信条数:"))
note1 = note_list[lsj_user3].split(".")[1]
print("")
print("您的手机套餐定制成功:免费通话时长为%s/月,流量为%s/月,短信条数%s/月"%(duration,flow1,note1))

    
