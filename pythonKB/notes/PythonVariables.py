#---------------------------------Global variables and local variables------------------------
s = "I love Paris"
def f(): 
    print(s) 

f()

"""The variable s is defined as the string "I love Paris in the summer!", before calling the function f(). The body of f() consists solely of the "print(s)" statement. As there is no local variable s, i.e. no assignment to s, the value from the global variable s will be used. So the output will be the string I love Paris in the summer!""".
#---------------------------------------------------------------------------------
Now,if we change the value of s inside of the function f()? Will it affect the global variable as well? We test this in the following piece ofcode:

s = "I love Paris!" 
def f(): 
    s = "I love London!"
    print(s) 

f()
print(s)


#here, inside the function the s ios assigned the new value inside the function scope, so s will use this value and its scope would remain upto that function only.
'''The output looks like this:
I love London!
I love Paris!'''


#-----------------------------------------------------------------------------------------------
def f(): 
	print(s)
	s = "I love London!"
	print(s)

s = "I love Paris!"
f()

#this will give the error because inside the function it will look for variable s which it dont consider the global value but search inside the function as s is declared after the print statement.
"""A variable can't be both local and global inside of a function. So Python decides that we want a local variable due to the assignment to s inside of f(), so the first print statement before the definition of s throws the error message above. Any variable which is changed or created inside of a function is local, if it hasn't been declared as a global variable."""
"""To tell Python, that we want to use the global variable, we have to explicitly state this by using the keyword "global", as can be seen in the following example:"""

def f():
    global s
    print(s)
    s = "Only in spring, but London is great as well!"
    print(s)


s = "I am looking for a course in Paris!" 
f()
print(s)

#Local variables of functions can't be accessed from outside, when the function call has finished:
def f():
    s = "I am globally not known"
    print(s) 

f()
print(s)

#this will give error
#-------------------------------------------------------------------------
#The following example shows a wild combination of local and global variables and function parameters:
def foo(x, y):
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print(a,b,x,y)

a, b, x, y = 1, 15, 3,4 
foo(17, 4)
print(a, b, x, y)

#Global Variables in Nested Functions
def f():
    x = 42
    def g():
        global x
        x = 43
    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))
    
f()
print("x in main: " + str(x))


"""We can see that the global statement inside of the nested function g does not affect the variable x of the function f, i.e. it keeps its value 42. We can also deduce from this example that after calling f() a variable x exists in the module namespace and has the value 43. This means that the global keyword in nested functions does not affect the namespace of their enclosing namespace! This is consistent to what we have found out in the previous subchapter: A variable defined inside of a function is local unless it is explicitly marked as global. In other words, we can refer a variable name in any enclosing scope, but we can only rebind variable names in the local scope by assigning to it or in the module-global scope by using a global declaration."""

#------------------non local variables---------------------------
"""Python3 introduced nonlocal variables as a new kind of variables. nonlocal variables have a lot in common with global variables. One difference to global variables lies in the fact that it is not possible to change variables from the module scope, i.e. variables which are not defined inside of a function, by using the nonlocal statement. We show this in the two following examples:"""

def f():
    global x
    print(x)
    
x = 3
f()
This program is correct and returns the number 3 as the output. We will change "global" to "nonlocal" in the following program:
def f():
    nonlocal x
    print(x)
    
x = 3
f()
"""The program, which we have saved as example1.py, cannot be executed anymore now. We get the following error:
 File "example1.py", line 2
    nonlocal x
SyntaxError: no binding for nonlocal 'x' found
This means that nonlocal bindings can only be used inside of nested functions. A nonlocal variable has to be defined in the enclosing function scope. If the variable is not defined in the enclosing function scope, the variable cannot be defined in the nested scope. This is another difference to the "global" semantics."""
def f():
    x = 42
    def g():
        nonlocal x
        x = 43
    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))
    
x = 3
f()
print("x in main: " + str(x))
"""Calling the previous program results in the following output:
Before calling g: 42
Calling g now:
After calling g: 43
x in main: 3
In the previous example the variable x was defined prior to the call of g. We get an error if it isn't defined:"""
def f():
    #x = 42
    def g():
        nonlocal x
        x = 43
    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))
    
x = 3
f()	
print("x in main: " + str(x))
"""We get the following error message:
  File "example3.py", line 4
    nonlocal x
SyntaxError: no binding for nonlocal 'x' found
The program works find - with or without the line "x = 42" inside of f - , when we change "nonlocal" to "global":"""
def f():
    #x = 42
    def g():
        global x
        x = 43
    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))
    
x = 3
f()
print("x in main: " + str(x))
"""This leads to the following output:
Calling g now:
The value of x after the call to g: 43
Before calling g: 3
Calling g now:
After calling g: 43
x in main: 43"""