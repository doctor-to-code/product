data = []
while True:
	digital = input('數字')
	if digital == 'q':
		break
	data.append(digital)
print(data)
with open('data.csv', 'w') as f: 
	for d in data:
		f.write(d+ ',' + '\n')