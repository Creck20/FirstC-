# Overview

Intro to C++

This is my first delve into the world of C++. I created a Shunting Yard Algorithm Calculator. 

I have been looking into work in embedded systems. I consitently see C and C++ as desired work qualifications. I am experienced in C, but have never programmed in C++. I decided to start learnign it with a project inspired from my data structures class. 

In my data structures class, we evaluted the code for a Reverse Polish Notation arithmetic execution software using stacks. RPN is a different form of writing mathematical expresions. 

- Infix is the common example we are used to: 4 + 7 / ( 9 − 3 )
- Postfix puts operators after operands and doesn't use parenthesis: 4 7 9 3 − / + 


There are many reasons to compute in postfix rather than in infix. 
- No need for parenthesis 
- More efficient
- Parse code from left to right in O(n) time

Many calcultors follow this style. 

There is an algorithm commonly used to convert infix to postfix called the Shunting Yard Algorithm. This uses stacks to variably push operators, operands, and parenthesis. 

Here is a link to my explanation of the code. 

[Software Demo Video](https://drive.google.com/file/d/1MwkYQyVphh2-3q3BshwKe0t6JkctzdV8/view?usp=sharing)

# Development Environment

Most of my time spent on this project was spent trying to get a HelloWorld.cpp program to run on an IDE. I spent alot of time trouble shooting VS Code and decided that it was not going to work. I spoke to a professor who suggested using Microsoft Visual Studio. I learned a lot throughout this process. 

I discovered that you can integrate Microsoft's Copilot LLM directly into softwares like VS Code and Visual Studio. This proved to be very helpful as it predicted what I wanted in a software as common as the one I created. This tool proved useful in fleshing out what I was looking for. All LLM's have limitations, and I needed to go through to alter the code it filled in according to my desired specifications. 

I used Bill Weinman's C++ Essential Training Course on LinkedIn learning to futher my education and provide a baseline. 

I used the following C++ libraries:

#include iostream
#include cstring
#include cstdlib
#include cctype

- iostream covers basic user in and out as well file writing and reading
- cstring enables cstrings or Char[] arrays
- cstdlib gives common c functions such as malloc() and free()
- cctype gives character classification such as isdigit()
# Useful Websites

Websites I found helpful

- [Brilliant SYA](https://brilliant.org/wiki/shunting-yard-algorithm/)
- [Shunting Yard Algorithm Youtube](https://www.youtube.com/watch?v=1VjJe1PeExQ)

# Future Work

In the future I could:

- Implement the software to handle multi digit numbers 
- Add a Gui
- Add more operators (such as exponentiation)
