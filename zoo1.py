#Then, use the interactive interpreter to import the zoo module and
#call its hours() function..
import zoo
zoo.hours()

#2. In the interactive interpreter, import the zoo module as menagerie
#and call its hours() function.

import zoo as menagerie
menagerie.hours()

#3. Using the interpreter, explicitly import and
#call the hours() function from zoo.
from zoo import hours
hours()


#4. Import the hours() function as info and call it.
from zoo import hours as info
info()

#5. Create a plain dictionary with the key-value pairs 'a':1,'b':2 and 'c':3
#and print it out.
x = {'a':1,'b':2,'c':3}
print(x)
for key, value in x.items():
    print(key, value)

#6.Make an OrderedDict called fancy from the same pairs listed in 5
# and print it. Did it print in the same order as plain?

from collections import OrderedDict
fancy=OrderedDict()
fancy['a']=1
fancy['b']=2
fancy['c']=3
print(fancy)
for key, value in fancy.items():
    print(key, value)
#yes it prints the same order as plain because we inserted the elements
#in the same order as the plain dictionary
#OrderedDict preserves the order in which the keys are inserted.
#A regular dict doesn’t track the insertion order, and
#iterating it gives the values in an arbitrary order


#7. Make a default dictionary called dict_of_lists and
#pass it the argument list.Make the list dict_of_lists['a] and append
# the value 'something for a' to it in one assignment.print dict_of_lists['a']
from collections import defaultdict

def def_value():
    return "Not Present"

dict_of_lists =defaultdict(def_value)
dict_of_lists['a'] = '1'
print(dict_of_lists['a'])
print(dict_of_lists['b'])