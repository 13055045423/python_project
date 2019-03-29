import json

#将json字符窜转换为python数据类型
json.loads()

#将python数据类型转换为json字符串
#ensure_ascii=True:转换的时候默认使用ascii,
#将ensure_ascii=False:不使用ascii编码,使用unicode编码
json.dumps()

#将本地的json文件加载出来,转换为python数据类型
json.load()

#将python数据类型,转换为json字符串,并且存储到本地
#open('aaa.json','r')
#ensure_ascii=True:转换的时候默认使用ascii,
#将ensure_ascii=False:不使用ascii编码,使用unicode编码
json.dump()