# Assignment 2
# Yedidia Bakuradze - 332461854
# Meir Crombie - 214736688
from functools import reduce

def getIntPosNeg(msg:str) -> int:
	try:
		return int(input(msg))
	except ValueError:
		print("ERROR: Input number is incorrect!")
		exit()
	
def getIntPos(msg:str) -> int:
	try:
		a = int(input(msg))
		if(a<0):
			print("ERROR: Input number is incorrect!")
			exit()
		return a
	except ValueError:
		print("ERROR: Input number is incorrect!")
		exit()
	
def read_dict_from_input():
	try:

		raw = input("Enter a dictionary: ")
		try:
			d = eval(raw, {}, {})
		except Exception:
			raise ValueError
		if not isinstance(d, dict):
			raise ValueError
		return d
	except ValueError:
		print("ERROR: Input is incorrect!")
		exit()
			
def q1(): 
	# Given two numbers n1,n2 it would return the number of verteies that are between these values and can make a polygon
	def pentaNumRange(n1:int,n2:int):
		f = lambda x: 0.5*x*(3*x-1)
		return list(map(f,range(n1,n2)))
	# def getUserInputNonFunctionalWay():
	# 	n1 = int(input("enter the value of n1: "))
	# 	n2 = int(input("enter the value of n2: "))

	# 	if n2<n1 :
	# 		print("ERROR: the values must be positive integers and n2 > n1")
	# 		exit()

	# 	for i in pentaNumRange(n1,n2):
	# 		print(i,end=" ")

	# Functional way to get user input and print the numbers
	def printAllPentalNumbers():
		n1 = int(input("enter the value of n1: "))
		n2 = int(input("enter the value of n2: "))

		if n2<n1 :
			print("ERROR: the values must be positive integers and n2 > n1")
			exit()
		list(map(lambda x: print(x,end=" ") ,pentaNumRange(n1,n2)))
		print("")
	
	printAllPentalNumbers()


def q2():
	def sumDigits(n:int)->int:
		return sum(list(map(lambda x: int(x),str(abs(n)))))
	print(sumDigits(getIntPosNeg("Enter an integer number n (positive or negative): ")))


def q3():
	reverseNumber = lambda s: reduce(lambda acc, c: c + acc, s, "")

	def isPalindrome(n:int)->bool:
		return all(list(map(lambda x,y: x==y,str(n),reverseNumber(str(n)))))

	print(isPalindrome(getIntPosNeg("Enter an integer number n (positive or negative): ")))


def q4():
	def getList(n:int) -> list:
		return range(1,n+1)

	def m(n:int):
		f = lambda x: float(x/(x+1))
		return sum(list(map(lambda x: f(x),getList(n))))
	
	def init():
		n = getIntPos("Enter a Natural number n: ")
		list(map(lambda y,x: print(f"{x} {y}"), map(m, getList(n)), getList(n)))

	init()


def q5():
	
	def add3dicts(d1:dict,d2:dict,d3:dict) -> dict:
		allKeys = lambda *ds: reduce(lambda x,y : x | y ,map(lambda x: set(x.keys()),ds))
		commonKeys = lambda d1, d2, d3: ( (set(d1) & set(d2)) | (set(d1) & set(d3)) | (set(d2) & set(d3)) )
		uniqueKeys = lambda d1,d2,d3: allKeys(d1,d2,d3) - commonKeys(d1,d2,d3)

		uniquePart = dict(map(lambda k: (k,
				next(d[k] for d in (d1, d2, d3) if k in d) ),
			uniqueKeys(d1,d2,d3)
		))

		aggregate  = lambda k, dicts: tuple(
			reduce(
				lambda acc, d: acc + [d[k]]
					if (k in d)
					else acc,
				dicts,
				[]
			)
		)

		commonPart = dict(map(
			lambda k: (k, aggregate(k, (d1, d2, d3))),
			commonKeys(d1,d2,d3)
		))

		return {**commonPart,**uniquePart}

	d1 = read_dict_from_input()
	d2 = read_dict_from_input()
	d3 = read_dict_from_input()
	# d1 = {2:'bc', 3:(34,2)}
	# d2 = {4:'gg', 2:(7,'f'), 5:'d'}
	# d3 = dict([(5,(2,6,'def')),(7,'abc'),(8,(2,)),(2,(5,7,8))])

	print(add3dicts(d1,d2,d3))
def main():
	lfuncs = [q1,q2,q3,q4,q5]
	lstrs = [
        "Calculate pentagonal numbers in range",
        "Sum digits of an integer number",
        "Check if a number is a palindrome",
        "Calculate sum of x/(x+1) series for n elements",
        "Merge three dictionaries with special rules"
    ]
	while True:
		print("your choices:")
		for (i,s) in enumerate(lstrs):
			print(i+1, " : ", s)
		print("Press 0 to exit")
		c = int(input("please enter your choice >>> "))
		if c==0:
			break
		elif c>=1 and c<=len(lstrs):
			lfuncs[c-1]()
		else:
			print ("error")
if __name__ =="__main__":
	print(main())