products =[]
while True:
	name = input('請輸入商品明稱')
	if name == 'q':
		break
	price = input('請輸入價格')
	date = input('請輸入購買日期')
	location = input('請輸入購買地點')
	products.append([name, price, date, location])
print(products)

for p in products:
	print(p[2]) #p[2]就是指date，當我們想要提取清單中特定的欄位時可以使用的方式

with open('products.csv', 'w') as f: 
	for p in products:
		f.write(p[0]+ ',' + p[1]+ ',' + p[2]+ ',' + p[3]+ '\n')