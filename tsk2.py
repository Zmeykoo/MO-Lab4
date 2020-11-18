#точність
eps = 0.0001
#межі відрізка в якому знаходяться корені 
a, b = -2, 2


def f(x3):
    return (x3**5) - (5*x3) + 2

def df_dx(x2):
    return 5*(x2**4 - 1)

def df_dx2(x4):
    return 20*(x4**3)

def h1(i):
    return round(a + i*(b-a)/3, 4)

def h2(i):
    return round(a + (i+1)*(b-a)/3, 4)

def NewM():
	"""Метод Ньютона"""
	lst = []
	for i in range(3):
		a0 = h1(i)
		b0 = h2(i)
		#перевірка до якої сторони відрізка рухатись
		if f(a0)*df_dx2(a0) > 0:
			x0 = a0
		else:
			x0 = b0

		xp = x0
		check = True
		while check:
			xn = round(xp - (f(xp)/df_dx(xp)), 3)
			res = xn - xp
			xp = xn
			if abs(res) <= eps:
				lst.append(xp)
				print(f"x{i+1} = {xp}")
				check = False

NewM()
