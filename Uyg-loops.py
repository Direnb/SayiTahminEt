'''
	1-100 arasında rastgele üretilecek bir sayıya aşağı yukarı ifadeleri 
	ile buldurmaya çalışın.
	** "random modülü" için "python random" şeklinde arama yapın.
	** 100 üzerinden puanlama yapın. Her soru 20 puan.
	** Hak bilgini kullanıcıdan alın ve her soru belirtilen can sayısı 
	üzerinden hesaplansın.
'''


import random
sayi = random.randint(1,5)
can = int(input('kaç hak kullanmak istersiniz:'))
hak = can
sayac = 0
while hak > 0:
	hak -= 1
	sayac += 1	
		
	tahmin = int(input('1 ile 100 arasında bir sayı tahmin edin:'))

	if tahmin == sayi:
		print(f'{sayac}. defada bildiniz. Toplam puanınız : {100-(100/can) * (sayac-1)}')
		break

	elif sayi >tahmin:
		print('yukarı')
	else:
		print('aşağı')

	if hak == 0 :
		print(f'Kaybettiniz. Sayı {sayi}')







