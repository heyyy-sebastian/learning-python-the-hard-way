# game skeleton
#expansion of ex36

#import a few files for methods here
from sys import exit


class Scene(object):
	pass

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map =  scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
		    next_scene_name = current_scene.enter()
		    current_scene = self.scene_map.next_scene(next_scene_name)

		current_scene.enter()

class Nap(Scene):
	pass

class Destroy(Scene):
	pass

class Adventure(Scene):
	pass

def start():
	pass

