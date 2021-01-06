import os#載入作業系統os

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='Big5') as f:
		for line in f:
			if '商品,價格,購買日期,購買地點' in line:
				continue #繼續(continue和break不同之處在於continue只是跳過該階段而非離開迴圈loop)
			name, price, date, location = line.strip().split(',')
			products.append([name, price, date, location])
	print(products)
	return products

#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品明稱')
		if name == 'q':
			break
		price = input('請輸入價格')
		price = int(price)
		date = input('請輸入購買日期')
		location = input('請輸入購買地點')
		products.append([name, price, date, location])
	print(products)
	return products


#印出紀錄
def print_products(products):
	for p in products:
		print(p[2]) #p[2]就是指date，當我們想要提取清單中特定的欄位時可以使用的方式

#寫入檔案
def write_file(filename,products):
	with open(filename, 'w', encoding='Big5') as f: 
		f.write('商品,價格,購買日期,購買地點\n')
		for p in products:
			f.write(p[0]+ ',' + str(p[1])+ ',' + p[2]+ ',' + p[3]+ '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('access permission')
		products = read_file(filename)
	else:
		print('access fail due to no file existence')

	products = user_input(products)
	print_products(products)
	write_file('products.csv',products)

main()