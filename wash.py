#function函式/功能
#function是用來收納程式碼
#他是個功能

def wash(x = 8):
	print('add water',x*10 ,'%')
	print('add detergent')
	print('rotation')

wash() #使用功能
       #
def say_hi():
	print('hi')
say_hi()

def add(x = 0, y = 1):
	print(x + y)
add(2)

def average(numbers):
	 return sum(numbers) / len(numbers)
a = average([1, 2, 30])
print(a)
