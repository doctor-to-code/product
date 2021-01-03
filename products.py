products =[]
while True:
	name = input('請輸入商品明稱')
	if name == 'q':
		break
	price = input('請輸入價格')
	date = input('請輸入購買日期')
	location = input('請輸入購買地點')
	p = []
	p.append(name)
	p.append(price)
	p.append(date)
	p.append(location)
	products.append(p)
print(products)