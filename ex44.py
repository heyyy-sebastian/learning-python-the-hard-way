def section_break():
	print "------------------------------------"

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

section_break()

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

section_break()

class Parent3(object):

	def altered(self):
		print "PARENT3 altered()"

class Child3(Parent3):

	def altered(self):
		print "CHILD3, BEFORE PARENT3 altered()"
		super(Child3, self).altered()
		print "CHILD3, AFTER PARENT3 altered()"

padre = Parent3()
hijo = Child3()

padre.altered()
hijo.altered()
