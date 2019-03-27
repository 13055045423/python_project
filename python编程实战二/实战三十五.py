print("2017~2018赛季NBA西部联盟前八名")
teamlist=["火箭","勇士","开拓者","爵士","鹈鹕","马刺","雷霆","森林狼"]
for i,t in enumerate(teamlist):
    print(t.split()[1],end = ""'\t')
    if i%2==1:
        print()
