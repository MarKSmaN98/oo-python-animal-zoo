from lib.animal import *
from lib.zoo import *

# code here

# e.g.  
#   z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
#   a1 = Animal( 'Lion', 75, 'Luke', z1 )
zoo = Zoo("Albany", "Albany, NY")
print(zoo)
a1 = Animal(zoo, "laex", 9, "Fox")
print(a1)
print(a1.zoo.name)
zoo2 = Zoo("someZoo", 'Austin, TX')

print(zoo2.all())
print(zoo.all())
print(Zoo.all(Zoo))



# do not remove 
# import ipdb; ipdb.set_trace()
