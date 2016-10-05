def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with functions"

age = add(20, 5)
height = subtract(70, 4)
weight = multiply(25, 5)
iq = divide(300, 3)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# a puzzle for extra credit

print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "Answer:", what