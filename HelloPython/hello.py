a=123
b=1.231
value = None
s='str'
print(a)
print(b)
print(value)
print(s)

print('{} - {} - {}'.format(a,b,s))

a=int(input())
b=int(input())
print(f'{a} + {b} = {a+b}')

r=range(10)
for i in r:
    print(i)


for i in 'qwerty':
    print(i)

r1 = list(range(1,6))
print(type(r1))