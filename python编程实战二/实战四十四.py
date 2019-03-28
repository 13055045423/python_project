#1题
def love_word():
    a = "l,love,python"
    b =a[2:6]
    print(b)
love_word()

#2题
def change_the_word():
    c = "aabbccddee"
    i = c.replace("dd","ff",1)
    print(i)
change_the_word()

#3题
e = "ab2b3n5nn2n67mm4n2"
print(e.count("n"))
for i in e:
    f = 1
    while True:
        
        if i == "n":
            print("字母%s"%i)
            break
        else:
            break
        f += 1
#4题
h = "ab2bn5nn2n67mm4n2"
dict_count = {}
for i in e:
    dict_count.setdefaullt(i,h.count(i))
print(dict_count)
