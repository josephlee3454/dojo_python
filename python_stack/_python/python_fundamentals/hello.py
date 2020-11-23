# It's time to start creating Python files! As a rite of passage, our first program needs to be
# Hello World :). Let’s practice string concatenation. Copy the code below, replacing each of the 
# your code here placeholders with the appropriate values. Hopefully it's not too patronizing that 
# every other task below is running 
# the file--this is just a friendly reminder to get into the habit of testing your code regularly!


# 1. TASK: print "Hello World"
print( "Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print( name + ",") # with a comma
print( name + " a +" ) # with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print( "Hello " + f"{name}" + "," ) # with a comma
print( "Hello " + f"{name}" + "a + --") # with a + -- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( fave_food1.format()) # with .format()
print( f"{fave_food2} " ) # with an f string
