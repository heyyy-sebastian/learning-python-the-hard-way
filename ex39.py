#map of state abbrev
states = {
	'Oregon':'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

#states w associated cities
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#divider method
def make_section():
	print '-' * 10

#print some cities
make_section()
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#do it by using the state then cities dict
make_section()
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation
make_section()
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

#print every cite in from the states dict
make_section()
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

#now print both at the same time
make_section()
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

make_section()
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city
