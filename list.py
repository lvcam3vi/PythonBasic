'''
name_list = ["zhangsan","lisi","wangwu"]
print(name_list[0])

i = 0
while i < len(name_list):
    print("while+",name_list[i])
    i += 1

for i in range(0,len(name_list)):
    print("for+",name_list[i])

#简便方法
for item in name_list:
    print("item+",item)


infos_list = [["zhangsan",20,180],["lisi",21,170]]

print(infos_list[0][1])


for list in infos_list:
    for item in list:
        print("q++",item)

'''

#append 向列表末尾添加元素

info_list = ["zhangsan",20,180]
info_list.append(["xiaobai",30,175])
print(info_list)

#insert 向列表指定位置添加元素
info_list.insert(1,"50kg")
print(info_list)

#+拼接两个列表
name_list = ["zhangsan"]
name_list2 = ["lisi","wangba"]
name_list3 = name_list + name_list2
print("namelist3",name_list3)

#extend 向一个列表中添加另外一个列表的元素

name_list.extend(name_list2)
print("extend",name_list)

#删除列表元素
group = ["唐僧","悟空","八届"]

# del group[1]

# print("del group",group)

group.pop(0)
print(group)

if "唐僧" in group:
    print("师傅还在")
else:
    print("师傅没了")


#sort()排序

num_list = [5,6,2,1,1]
num_list.sort() #默认生序
print(num_list)
num_list.sort(reverse=True) #倒叙
print(num_list)
num_list.reverse()
print(num_list)
num_list.reverse()
print(num_list)

#count(元素) 统计这个元素在列表中有多少个

i = num_list.count(1)
print(i)
