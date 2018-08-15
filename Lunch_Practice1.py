from operator import itemgetter

body_parts=['head', 'shoulders', 'knees', 'toes']
partial=(itemgetter(0,3)(body_parts))
command="you should touch your %s"

print(command % body_parts[0])

print(partial)

#body_parts.append('weenus')
#print (body_parts)

def skills():
    person = input()
    print(person)