# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 22:54:56 2017

@author: A0688377
"""

#my first python code
#print("hello world")

#myName = input("Enter your name :")
#print("Your name is " + myName)

s = "Hello Python"
print(s)      # prints whole string
print(s[0])   # prints "H"
print(s[1]) # prints "e"


l = [ "Drake", "Derp", "Derek", "Dominique" ]
 
print(l)                # prints all elements
l.append("Victoria")   # add element.
print(l)                # print all elements
l.remove("Derp")       # remove element.
l.remove("Drake")      # remove element.
print(l)               # print all elements.


def f(x):
    return(x*x)
 
print(f(3))