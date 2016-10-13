#when you import a function python will automatically run the whole file
#need to guard this with a wrapper method
from ex39 import make_section
#execfile("/Users/hmiller/Desktop/Python_practice/ex39.py")

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

make_section()
happy_bday.sing_me_a_song()
make_section()
bulls_on_parade.sing_me_a_song()
