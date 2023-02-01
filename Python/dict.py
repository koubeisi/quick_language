# 定义字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_1 = {}  # 定义一个空字典

# 访问字典的中的值
print(alien_0['color'])

# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 修改字典中的值
alien_0['color'] = 'yellow'
print(alien_0)

# 删除键值对
del alien_0['points']
print(alien_0)

# 遍历字典
for key, value in alien_0.items():
    print("{}: {}".format(key, value))

# 遍历字典中的所有键
for key in alien_0.keys():
    print("key: {}".format(key))

for key in alien_0:
    print("key: {}".format(key))

if 'color' in alien_0:
    print("yes")

# 遍历字典中所有的值
alien_1 = {'Marry': "c", 'Jeryy': 'java', 'Tom': 'go', "Jim": "java"}
for value in sorted(alien_1.values()):  # 排序后遍历
    print("value: {}".format(value.title()))

for value in set(alien_1.values()):     # 放入集合中中遍历
    print("value: {}".format(value.title()))

