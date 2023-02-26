# input 函数的基本使用
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# 处理输入默认为字符串的问题
age = input("How old are you?")
age = int(age)
print(age > 18)