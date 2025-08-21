peppa_characters = {"001":{"name":"Peppa","hobby":"jumping in the muddy puddles"},\
            "002":{"name":"George","hobby":"playing with dinosaur"}}
while True:
    input1=input("请输入编号：").strip()
    if input1 not in peppa_characters:
        print("编号不存在！")
        continue
    break
while True:
    input2=input("请输入要查询的是name还是hobby：").strip()
    if input2 not in ['name','hobby']:
        print("非法输入！")
        continue
    break
print(peppa_characters.get(input1).get(input2))
