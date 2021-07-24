#Sum of digit
'''s = 0
a = int(input("Enter Value")) #121
while(a!=0):
	rem = a % 10
	s = s + rem
	a = a // 10
print("Sum of digit",a)'''
'''
a = int(input("Enter a value"))#10 jkszdhfkjah
b = int(input("Enter b value"))#20
c = int(input("Enter c value"))#30

if a>b and a>c:
	print("A is Greatest number ",a)
elif b>c:
	print("B is greatest number ",b)
else:
	print("C is greatest number ",c)




printf("value %d,%d",a,b) '''
'''
a=10
b=20
c=30
print("value  {1}  of   {0}  of  {2} ".format(a,b,c))
'''
'''
a= [2,43,32,3435,546]
a.sort()
print(a)

'''
'''

a = []

for i in range(5):
	element = int(input("Enter input"))
	a.append(element)
a.sort()
print(a)

'''
'''
a = [1,2]
a.insert(1,3)'''
'''
a = [1,2,3,4,54,454,5]
a.sort(reverse=True)
print(a)'''


#Polindriome
''' 
a= input("Enter string")  #jack
b= a[::-1]
if a==b:
	print("Polindrome")
else:
	print("This word is not polindrome")
'''
'''
l = int(input("Enter length	"))
a=[]
for i in range(l):
	ele = int(input())
	a.append(ele)

b=sum(a)
b=b/l
print("Mean"b)

'''

'''
l = int(input("Enter length	"))
a=[]
for i in range(l):
	ele = int(input())
	a.append(ele)
b = a.sort()
mid = l%2
c=l/2
#print(c)
if mid!=0:
	print("Median",a[c])
else:
	print("Median",(a[c]+(a[c]-1))/2)

'''
'''

txt = 'The best friends'
if 'best' not in txt:
	print("Yes")
else:
	print('no')
	'''
'''
a= '    suresh     '
b=a.strip()
print(len(b))

'''
'''
a='suresh'
b=a.replace('s','q',2)
print(b)'''

'''
print("sasi\'s creation")

'''
'''
a=['makesh','madhavan']
b=' '.join(a)
print(b)'''



#Ways to remove i’th character from 
#string in Python
'''
s1 = input("Enter string") #madhavan
n = int(input("Enter Character place")) #3
count = 0
for i in s1:
	count = count+1
	if count == n:
		s2=s1.replace(i,'')
		break
print(s2)
'''
'''
l = int(input("Enter length"))
a=[]
for i in range(l):
	element = input("Enter value")
	a.append(element)
b=''.join(a)
print(b)
c=[]
for i in b:
	c.append(i)
print(c)'''


#Class 24/07
'''
s1 = input("Enter String\t")
l = len(s1)
count = 0
for i in s1: # k
	if i!=' ':
		count = count+1 #6
print("Normal len",l)
print("Avoid space",count)
'''
#Python program to print even
# length words in a string
'''
l = int(input("length of list\t"))
a=[]
b=[]
for i in range(l):
	ele = input("Enter string\t")
	a.append(ele)
for i in a:
	length = len(i)
	if length%2==0:
		b.append(i)
print(b)
'''

