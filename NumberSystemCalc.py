class Convertor():

	'''
	convert numbers between Decimal, Binary, Octal and Hex
	'''
			
	@staticmethod	
	def toDecimal(n, base):
		return int(n, base)
	
	@staticmethod
	def toHex(n, base):
		h = Convertor.toDecimal(n, base)
		return hex(h)[2:]

	@staticmethod
	def toBinary(n, base):
		b = Convertor.toDecimal(n, base)
		return bin(b)[2:]
	
	@staticmethod
	def toOct(n, base):
		o = Convertor.toDecimal(n, base)
		return oct(o)[2:]
	
	@staticmethod
	def validateNum(n:str) -> bool:
		nums = '0123456789abcdefABCDEF'
		res = list(map(lambda x: True if x in nums else False, n))
		if all(res):
			return True
		return False

	@staticmethod
	def validateBase(b:str) -> bool:
		bases = ('b','bin','binary','o','oct','octal','d','dec','decimal','h','hex')
		bn = (2, 2, 2, 8, 8, 8, 10, 10, 10, 16, 16)
		if b.lower() in bases:
			return bn[bases.index(b.lower())]
		return False

	@staticmethod
	def showResult(n, b):

		isValidNum = Convertor.validateNum(n)
		isValidBase = Convertor.validateBase(b)
		
		if isValidNum:
			if isValidBase != False:
				
				try:
					B = Convertor.toBinary(n, isValidBase)
					D = Convertor.toDecimal(n, isValidBase)
					H = Convertor.toHex(n, isValidBase)
					O = Convertor.toOct(n, isValidBase)
					print('\nDecimal:',D)
					print('Octal:', O)
					print('Binary:',B)
					print('Hex:',H)
					
				except ValueError as e:
					print('Number and Base are not mathcing.')
						
			else:
				print('\nInvalid Base')
		
		else:
			print('\ninvalid Number')


class Calculator():

	'''
	calculate mixed number system problems
	'''

	# Class constructor
	def __init__(self, calc, bases):
		
		'''
		param calc: Calculation, entered by user
		param type: str
		param bases: Bases of numbers in calculation, enterd by user
		param type: str
		'''
		
		self.__calc = calc.strip().split()
		self.__bases = bases.strip().split()		
		self.__result = 0
		self.__toCalc = ''
		self.__baseN = []
		self.__nums = []
		self.__ops = []
		
		'''
		self.__calc : list to store numbers in calculation enterd by user
		self.__bases : list to store bases of each number in calculation 
		self.__result : integer to store final result's integer value'
		self.__toCalc : string to store finalized calculation to proceed
		self.__baseN : list to store numbers related to each base
		self.__nums : list to store decimal value of each number in calculation
		self.__ops : list to store opearotrs in calculation 
		'''


	@staticmethod
	def getCalc(calc, beses):
		if calc and bases:
			return Calculator(calc, bases)
			
		elif not calc:
			raise Exception('Calculation cannot be empty')
			
		elif not bases:
			raise Exception('Bases cannot be empty')
	
	def __repr__(self):
		return f'Multi Number Systems Object.\nCoded by Hirusha Fernando.'


	# extract numbers and operators from self.__calc and store them in two lists
	def __extract_items(self):
		for item in self.__calc:
			if not item in '+-*/':
				self.__nums.append(item)
			
			else:
				self.__ops.append(item)


	# validate each number in calculation that stored in self.__nums
	# if all numbers are validated correctly return True else False 			
	def __validate_numbers(self) -> bool:
		for num in self.__nums:
			status = Convertor.validateNum(num)
			if not status:
				return False
		else:
			return True
			

        # validate each base of number in calculation that stored in self.__bases
	# store related value to base in list called self.__baseN
	# return true if all bases are validated correctly else return false 
	def __validate_bases(self) -> bool:
                for base in self.__bases:
			status = Convertor.validateBase(base)
			if status != False:
				self.__baseN.append(status)
			else:
				return False
		return True


	# check, did user entere enough details to calculate the problem.
	def __validate_calc(self) -> bool:
		self.__extract_items()
		
		if len(self.__nums) != len(self.__bases):
			return False
		
		if len(self.__ops) != len(self.__nums) -1:
			return False
			
		return True


	# store the finalized calculation to calculate in self.__toCalc
	# if all numbers are mathced with their bases return true else return false
	def __set_calc(self) -> bool:
		try:
			for i in range(len(self.__nums)-1):
				N = Convertor.toDecimal(self.__nums[i], self.__baseN[i]) 
				self.__toCalc += str(N) + self.__ops[i]

			N = Convertor.toDecimal(self.__nums[-1], self.__baseN[-1]) 
			self.__toCalc += str(N)
			return True
		
		except ValueError as e:
			return False


	# calculate the finalized calculation	
	def __calculate(self) -> tuple:
		self.__result = eval(self.__toCalc)
		self.ansD = str(self.__result)
		self.ansB = str(Convertor.toBinary(self.ansD, 10))
		self.ansO = str(Convertor.toOct(self.ansD, 10))
		self.ansH = str(Convertor.toHex(self.ansD, 10))
		
		return (self.ansB, self.ansO, self.ansD, self.ansH)


	# if all validations are passed this method return the answer		
	def get_result(self):
		VCALC = self.__validate_calc()
		
		if VCALC:
		 	VNUMS = self.__validate_numbers()
		 		
		 	if VNUMS:
		 		VBASES = self.__validate_bases()
		 			
		 		if VBASES:
		 			FINAL = self.__set_calc()
		 				
		 			if FINAL:
		 				ANSWER = self.__calculate()
		 				return ANSWER
		 				
		 			else:
		 				print('\nBases are not matching to numbers')
		 				return None
		 		else:
		 			print('\nSome number bases are invalid')
		 			return None
		 	else:
		 		print('\nSome numbers are invalid')
		 		return None
		else:
			print('\nDetails are not enough to calculate')
			return None


	def show_result(self):
		ans = self.get_result()
		if ans:
			print('\n==========[ Solution ]==========\n')
			print(f'  [+] Binary answer   : {ans[1]}')
			print(f'  [+] Octal answer    : {ans[2]}')
			print(f'  [+] Decimal answer  : {ans[0]}')
			print(f'  [+] Hex answer      : {ans[3]}')
			

									
# Implementation of Convertor class
								
#n = input('Number:').strip()
#b = input('Format:').strip()
#Convertor.showResult(n, b)



# Implementation of Calculator class

# Input Format Example
# Your problem: 1101 + 234 + 679a - abcd
# Bases of above numbers: b d h h

#calc = input('Your problem:').strip()
#bases = input('Bases of above numbers:').strip()
#nsys = Calculator(calc, bases)

# Method 1
#k = nsys.get_result()
#print(k)

# Method 2
#nsys.show_result()
