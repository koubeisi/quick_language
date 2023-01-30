bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[-1])

print(bicycles[0].title())

message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

bicycles.append('fenghuang')

print(bicycles[-1])

del bicycles[1]

print(bicycles)


for bicycle in bicycles:
 print(bicycle)

for i in range(1,11,3):
    print(i)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11,3)]
print(squares) 