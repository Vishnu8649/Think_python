prefx='JKLMNOPQ'
sufx='ack'
sufx1='uack'
for letter in prefx:
	if letter=='O' or letter=='Q':
		print letter+sufx1
	else:
		print letter+sufx
