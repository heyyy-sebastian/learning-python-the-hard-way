from sys import exit

#This happens if you want a cat nap
def sleepy_cat():
	print "You stretch out for a luxurious nap. Good job!"
	exit(0)

#This happens if you want to destroy the house plants
def destructive_cat():
	print "You human has a plant perched on a window sill.\nDo you destroy it?"

	choice = raw_input("> ")
	if ("yes" in choice) or ("destroy" in choice):
		print "You knock over the plant and hear it crash onto the floor. You're satisfied with your destruction."
		print "What do you do now? Are you tired or do you escape out the open window?"
		choice = raw_input("> ")

		#This is how you decide what to do after you destory the plants
		if "tired" in choice:
			sleepy_cat()
		else:
			adventurous_cat()
	#This is what happens if you don't want to destroy the plant
	else:
		print "You decide a nap sounds better, after all."
		sleepy_cat()

#This happens when the cat goes out the window
def adventurous_cat():
	print "You jump out the window and make your way to the park down the street.\nYou see a bird perched above you in a tree."
	print "Do you kill the bird or befriend it?"

	choice = raw_input("> ")

	if "kill" in choice:
		print "You climb the tree and pounce on the bird."
		print "You bring it home as a present for your owner. Good job!"
		exit(0)
	else:
		print "You make friends with the bird and climb trees with it until you are tired, then return home."
		sleepy_cat()

def start():
	print "Pretend you are a cat living with your humans in an apartment."
	print "In morning you decide what to do with your day."
	print "Do you want to take a nap or do you want to play?"

	choice = raw_input("> ")

	if "nap" in choice:
		sleepy_cat()
	elif "play" in choice:
		destructive_cat()
	else:
		print "That's not something a cat would do. Try again."
		start()

start()
