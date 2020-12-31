products = []
while True:
	name = input('product name:')
	if name == 'q':
		break
	price = input('product price:')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)