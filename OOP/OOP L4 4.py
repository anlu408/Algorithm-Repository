# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen = True)  #The frozen argument makes the data class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def somefunc(self,newval):
        self.value2 = newval

obj = ImmutableClass()
#print(obj.value1)

#obj.value1 = 2 #Attempting to change the value. Should return a frozen instance error.

#obj.somefunc(20) In functions you will get the same frozen instance error

'''
When you wnat to create data classes whose data can't be changed we can use immutable data classes. You can specify an argument to the dataclass decorator to create an immutable class.

'''