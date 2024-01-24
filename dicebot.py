def dice(args):
	import random
	import sys

	def printusage():
		return """The ants are confused! 
		Example use '/roll 3 6'
		Please use whole, positive numbers"""
	

	sum = 0

	try: 
		dice_size = int(args[1])
		dice_count = int(args[2])
	except:
		return printusage()
		#exit(1)

	if dice_size < 1:
		return printusage()
		#exit(1)
	

	if dice_count < 1:
		return printusage()
		#exit(1)


	for i in range(dice_count):
		roll = random.randint(1, dice_size)
		sum = sum + roll

	return "sum: "+str(sum)