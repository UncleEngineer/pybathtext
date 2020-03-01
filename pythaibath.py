def pythaibath(number=123134234234,bath=False):

	thainumber = {1:'หนึ่ง',
				 2:'สอง',
				 3:'สาม',
				 4:'สี่',
				 5:'ห้า',
				 6:'หก',
				 7:'เจ็ด',
				 8:'แปด',
				 9:'เก้า',
				 0:''}

	word = ''
	unit_check = 0
	original = number
	check = str(number).split('.')
	
	decimalpoint = ''
	if len(check) == 2:
		number = int(check[0])
		decimalpoint = int(check[1])

	else:
		number = int(check[0])
	
	


	

	for n in str(number):

		if len(str(number)) - unit_check == 2:
			unit = 'สิบ'
		elif len(str(number))  - unit_check == 3:
			unit = 'ร้อย'
		elif len(str(number))  - unit_check == 4:
			unit = 'พัน'
		elif len(str(number))  - unit_check == 5:
			unit = 'หมื่น'
		elif len(str(number))  - unit_check == 6:
			unit = 'แสน'
		elif len(str(number))  - unit_check == 7:
			unit = 'ล้าน'
		elif len(str(number))  - unit_check == 8:
			unit = 'สิบ'
		elif len(str(number))  - unit_check == 9:
			unit = 'ร้อย'
		elif len(str(number))  - unit_check == 10:
			unit = 'พัน'
		elif len(str(number))  - unit_check == 11:
			unit = 'หมื่น'
		elif len(str(number))  - unit_check == 12:
			unit = 'แสน'
		elif len(str(number))  - unit_check == 13:
			unit = 'ล้าน'
		else:
			unit = ''

		if  len(str(number)) - unit_check == 8 and n == '2':
			word = word + 'ยี่' + unit
		elif len(str(number)) - unit_check == 2 and n == '2':
			word = word + 'ยี่' + unit
		elif len(str(number)) - unit_check == 2 and n == '1':
			word = word + unit
		elif len(str(number)) - unit_check == 1 and n == '1':
			word = word + 'เอ็ด' + unit
		# elif len(str(number)) - unit_check > 7:
		# 	word = word + 
		else:
			if n == '0' and  len(str(number))  - unit_check == 7:
				word = word + thainumber[int(n)]  + 'ล้าน'
			if n == '0':
				word = word + thainumber[int(n)]
			else:
				word = word + thainumber[int(n)] + unit
		unit_check = unit_check + 1
	if bath == True:
		word = word + 'บาท'


	word2 = ''

	unit_check2 = 0
	state = False
	if len(str(decimalpoint)) == 1:
			state = True
	
	if len(check) == 2:
		
		for n in str(decimalpoint):
			if len(str(decimalpoint)) - unit_check2 == 2:
				unit2 = 'สิบ'
			else:
				unit2 = ''



			if len(str(decimalpoint))  - unit_check2 == 2 and n == '2':
				word2 = word2 + 'ยี่' + unit2
			elif len(str(decimalpoint))  - unit_check2 == 2 and n == '1':
				word2 = word2 + unit2
			elif len(str(decimalpoint))  - unit_check2 == 1 and n == '1' and state == True:
				word2 = word2 + 'หนึ่ง' + unit2
			elif len(str(decimalpoint))  - unit_check2 == 1 and n == '1' and state == False:
				word2 = word2 + 'เอ็ด' + unit2
			else:
				if n == '0':
					word2 = word2 + thainumber[int(n)]
				else:
					word2 = word2 + thainumber[int(n)] + unit2

			unit_check2 += 1

	if len(check) == 1:
		print('ตัวเลข: {:,d}'.format(original))
		print('คำอ่าน: {}ถ้วน'.format(word))
		return '{}ถ้วน'.format(word)
	else:
		print('ตัวเลข: {:,.2f}'.format(original))
		print('คำอ่าน: {}'.format(word + word2 + 'สตางค์'))
		return word + word2 + 'สตางค์'

pythaibath(101004455,bath=True)