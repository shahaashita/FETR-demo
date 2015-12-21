def hour():
	hr=input('enter hour:')
	return hr
def day():
	dy=input('enter day:')
	return dy

h=hour()
d=day()
def cost(h,r):
	cost=h*r*8
	print cost
cost(h,d)