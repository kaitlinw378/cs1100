"""
This program experiments with the use of functions
and also learning error checking.


"""
import math #imported math function since uses sqrt

## Function returns the length of a line 
## starting at (x1,y1) and ending at (x2,y2)
def line_length(x1,y1,x2,y2):
    length = (x1-x2)**2 + (y1-y2)**2
    length = math.sqrt(length)
    return length


initial_x = 10
initial_y = 10
next_x = int(input("The next x value ==> ")) #changed to int values
print(next_x, end = "")
next_y = int(input("The next y value ==> ")) #changed to int values
print(next_y)
print("The point has moved from ({:d},{:d}) ".format(initial_x, initial_y),\
    "to", (next_x, next_y))
#removed unnecesary punctiation from print statement (+ and ,)

print("Total length traveled is", format(line_length(initial_x, initial_y, next_x, next_y), '.2f'))
#moved the line_length statement into the print line and changed it to format 