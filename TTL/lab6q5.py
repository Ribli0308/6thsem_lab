'''wap to define a func with an argument which can take n number of keyword arguments.'''
def myFun(**a):
	for key, value in a.items():
		print("%s = %s" % (key, value))

myFun(name='Devashree', address='Mumbai', roll=20051066)