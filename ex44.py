class Parent(object):

	def implicit(self):
		print "PARENT implicit()"

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

#if you put functions in base class then all subclasses will automatically get those features
#they inherit these functions IMPLICITLY

class Parent2(object):

	def override(self):
		print "PARENT2 override()"

class Child2(Parent2):

	def override(self):
		print "CHILD2 override()"

pop = Parent2()
pip = Child2()

pop.override()
pip.override()

#if you want a subclass to behave differently than its parent, you can EXPLICITLY override it
#by defining it in the subclass' methods