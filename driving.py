country = input('請問你是哪個人: ')
age = input('輸入年齡: ')
age = int(age)
if country == '臺灣':
	if age >= 18:
		print('可以考駕照')
	else:
		print('還不能考駕照')
elif country == '美國':
	if age >=16:
		print('可以考駕照')
	else:
		print('還不能考駕照')
else:
	print('只能輸入臺灣 & 美國')
