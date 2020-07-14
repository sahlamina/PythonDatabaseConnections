# Python Database Connections

- We are trying to establish a connection and read data from the database in the Python console
- In real time the results of our code will be presented in the UI, not the terminal
- UI is user interface, ux is user experience. We can use UI and front end interchangeably
---
PYODBC: is a python library which helps connect to a database
- helps us showcase data in the console which in real time, we would display on the front end
- we installed PYODBC simply by importing it and then hovering over the error then asking it to install

## ODBC
- open database ___ which is for opening microsoft applications

cursor is a control structure that allows us to control and manage rows data from a response. in the pyodbc instance it is used to manage our

## SOLID principle
- Single responsibility - so having one task per file
- Open-Closed Principle
Software entities(Classes, modules, functions) should be open for extension, not modification.

---

# Project notes
My project has been through a couple of iterations but has a lot of room for improvement

Currently, it is comprised of three files
- My Databasecnxn file imports pyodbc and creates a class to establish a connection with the database 
- I can improve on this by storing the sensitive information in a secret file in my gitignore to prevent the details from being shared publicly 

Next I have a file called queries
- I used instantiation to link the methods in my Open connection class with the method in my queries class
- I hard coded the SQL command, but in the future, I will try to implement user inputs to drive the SQL queries

Finally i have a 'main' or run file
- I used the pillar of abstraction here to hide some of the details from plain sight. I like the simplicity of this file and I will continue using this framework for future iterations of my project 








