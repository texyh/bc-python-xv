def even_numbers(low,high):
	for i in range (low:high):
		if i%3 ==0:
			print i
		else:
			print 'bad idea'
even_numbers(1,10)