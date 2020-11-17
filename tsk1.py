from math import sin

fin=[]
def main():
	"""Пошук коренів функції"""
	i=-3.0
	x=round(i, 3)
	while x <= 3.0:
		if round(sin(x),2) - round(x**3,2) == 0:
			fin.append(x)
		x=round(x+0.01,2)

main()

print('Корені даної функції:',fin)
