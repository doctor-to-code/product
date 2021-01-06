def is_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

y = is_leap(2016)
if y == False:
	print('平年')
else:
	print('閏年')