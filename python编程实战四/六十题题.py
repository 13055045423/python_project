print("车次\t出发站-到达站\t出发时间\t到达时间\t历时")
print("T40\t长春-北京\t00:12\t\t12:20\t\t12:08")
print("T298\t长春-北京\t00:06\t\t10:50\t\t10:44")
print("Z158\t长春-北京\t12:48\t\t21:06\t\t08:18")
print("Z62\t长春-北京\t21:58\t\t06:08\t\t8:20")
the_input_number = input("请输入要购买的车次:")
enter_the_passenger = input("请输入乘车人 (用逗号分隔) :")
traln_number_list = ["T40","您已购T40次列车 长春-北京 12:48开","T298","您已购T298次列车 长春-北京 11:18开","Z158","您已购Z158次列车 长春-北京 21:34开","Z62","您已购Z62次列车 长春-北京 06:36开"]
for subscript,traln_number in enumerate(traln_number_list):
#    print(traln_number)
#    print(traln_number)
    if the_input_number == traln_number:
        print(traln_number_list[subscript+1],end="")
        print("请%s尽快换取纸质车票.铁路客服"%enter_the_passenger)
        break
   # elif the_input_number != traln_number:
    #    the_input_number = input("没有该车次,请重新输入车次:")
