from sys import exit

#This happens if you want a cat nap
def sleepy_cat():
	print "You stretch out for a luxurious nap. Good job!"
	exit(0)

#This happens if you want to destroy the house plants
def destructive_cat():
	print "You human has a plant perched on a window sill.\nDo you destroy it?"

	choice = raw_imput("> ")
	if ("yes" in choice) or ("destroy" in choice):
		print "You knock over the plant and hear it crash onto the floor. You're satisfied with your destruction."
		print "What do you do now? Are you tired or do you escape out the open window?"
		choice = raw_imput("> ")

		#This is how you decide what to do after you destory the plants
		if "tired" in choice:
			sleepy_cat()
		else:
			adventurous_cat()
	#This is what happens if you don't want to destroy the plant
	else:
		print "You decide a nap sounds better, after all."
		sleepy_cat()

#This ends the program - might not need it eventually 
def ending(why):
	print why, "Good job." 
	exit(0)