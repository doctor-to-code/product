#讀取檔案
products = []
with open('products.csv', 'r', encoding='Big5') as f:
	for line in f:
		if '商品,價格,購買日期,購買地點' in line:
			continue #繼續(continue和break不同之處在於continue只是跳過該階段而非離開迴圈loop)
		name, price, date, location = line.strip().split(',')
		products.append([name, price, date, location])
print(products)