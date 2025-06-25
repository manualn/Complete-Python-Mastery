# Introduction
Time range: 0:00 - 0:56  
Python is used for AI, Machine learning, Web development and Automation. This is a comprehensive, easy to follow, well organized and practical course. No prior knowledge is required. Step by step explanation of simple terms is included in this course. Mosh hamedani, a software engineer with over 20 years of experience is teaching this through his youtube channel.

# What is python 
Time range: 0:56 - 4:11  
It is the most popular programming language among software developers, mathematicians, data analysts, scientists, accountants, network engineers and even kids. Python solves complex problems in less time with fewer lines of code. Many huge companies like google, spotify, dropbox and facebook use this language. Average salary of python developer in US was over $115000 in 2018. Python has been around over 20 years.  
There are two versions of python:
1. Python 2 - legacy version of python
2. Python 3 - python for future

Python 3 is taught in this video

# Installing Python
Time range: 04:11 - 05:36  
Head over to python.org in your browser and under downloads you can download latest versions. Latest version is python 3.13 during this video. Before click install make sure to check the bow saying "Add python.exe to PATH".

Step 1
![syntax demo](/images/03_installing_screenshot1.png)  

Step 2
![syntax demo](/images/03_installing_screenshot2.png)  

Step 3
![syntax demo](/images/03_installing_screenshot3.png)  

Step 4
![syntax demo](/images/03_installing_screenshot4.png)

# Python Intepreter
Time range: 05:36 - 07:30

![syntax demo](/images/04_python_intepreter_terminal.png)

We can write python code in a file and give it to this intepreter and it executes the code. Also this is an interactive shell were we can type the code directly.  
![syntax demo](/images/04_python_intepreter_example.png)

Syntax means grammar.In the last example the expression is not complete and grammar is not right. 

# Code Editor
Time stamp: 07:30 - 08:49  
For writing python code there are two options: 
1. Code editor
2. IDE - Integrated Development Environment

IDE have many features like autocompletion, debugging (fixing bugs) and testing  
Popular code editors: 
1. VS code
2. Atom
3. Sublime

Popular IDE:
1. Pycharm

![syntax demo](/images/05_code_editor_screenshot.png)

# Your First python program
1. Open vs code and create a folder 
2. You can see the folders in explorer panel. Add new file there

Python files should have py extension.  
Some examples of using built-in-function : 
``` python
# 06_your_first_pythonprogram.py
print("Hello world")
print("*" * 10)
```

# Python extension
In this section we study how to convert vs code to a powerful IDE.  
IDE has many features
1. linting - analyzing codes for errors 
2. debugging - finding and fixing errors 
3. Autocompletion - write code faster 
4. Code formatting - making our code clean and readable
5. Unit testing - bunch of testing for code
6. Code snippets - reusable code blocks

Click on the left side icon to open extension panel install additional extensions.

![syntax demo](/images/07_python-extension_screenshot.png)

# Linting Python code
Python linting is used for analyzing and detecting errors. Pylint is the software used for this.

![syntax demo](/images/08_linting_code_screenshot1.png)

If there is error, it will be shown in the problem section. We can change the default pylint by going to command pallette and choose python: select linter. There will be various linters available.  

![syntax demo](/images/08_linting_code_screenshot2.png)


# Formatting python code
You can see the formatting rules and styles in this link. Visit this [site](https://peps.python.org/)  
Formatting can be done by a format document option in command palette. Since you are a beginner you have to first install format autopep8.  
Steps to be followed:  
1. Go to extension panel(left side fifth icon)
2. Search autopep8
3. Click install 

![syntax demo](/images/09_formatting_python_code_installing.png)

Formatting Example
![syntax demo](/images/09_formatting_python_code_example1.png)


![syntax demo](/images/09_formatting_python_code_example2.png)
Select format document from the options

![syntax demo](/images/09_formatting_python_code_example3.png)

Your file can be automatically formatted while saving it.  
Steps: Go to code menu ---> Preferences ---> Settings  
Search for formatOnSave in the search bar. There tick the options saying format a file on save. 

![syntax demo](/images/09_formatting_python_code_settings.png)


# Running python code
Different ways to run python code is studied here. Simpler way to run is to use the play button on right top corner. But clicking this button everytime is little bit tedious.  
Another way is  
1. Go to command palette and search preferences: open keyboard shortcuts.  
2. All commands in vs code and shortcuts will be displayed there.  

![syntax demo](/images/10_running_python_code_step2.png)

3. In search bar, search for run python file.  
4. You will get the command Python: Run python file.  
5. You can see keybinding column blank. Double click there.  

![syntax demo](/images/10_running_python_code_step5.png)

6. Set any key combination for creating shortcut.  

# Python Implementations
There are two topics covered in this chapter.
1. Language  
Defines a set of rules and grammar in writing code
2. Implementations  
Program that understand the code and can execute it.

When you run python in terminal , you get CPython. This is default implementation of python.  
Few other implementations are 
1. Jython - written in Java
2. Ironpython - Written in C#
3. PyPy - subset of python

![syntax demo](/images/11_python_implementations_types.png)

Purpose of having different implementations is like you have different operating systems and browsers.  
Jython can be used if you want to import some java code into python program. Similarly other implementations also can be used. 

# How Python code is executed
1. Computers only understand machine level instructions, so high level languages like C, Java and python need to be translated before execution.  
2. In C, this translation is done by a compiler that produces machine code tailored to a specific operating system and hardware.  
3. This means a C program built for windows wont work on a Mac due to differences in system architecture.  
4. Java handles this by converting its source code into a universal format called bytecode.  
5. This buytecode is executed by the Java Virtual Machine (JVM), which adapts it to the host system's machine code on the fly.  
6. Python works in a similar way - its default implementation (CPython) converts code into bytecode, which the Python runtime executes.  
7. Jython, a variant of Python, translates Python code into Java bytecode instead of Python bytecode.  
8. Because of this, Jython programs can run on the JVM and even use Java libraries within Python scripts.  
9. This allows smooth integration between python and Java code under the same runtime.  
10. Using virtual machines and bytecode makes language like Java, Python and C# more flexible and portable across platforms. 

# Quiz 1
## Question 1  
### What is an expression?
- Expression is a piece of code that produces a value.  
Example: 
```python
#13_quiz.py
"*" * 3
```
## Question 2 
### What is a syntax error?
- Its a kind of error due to bad syntax or bad grammar in the code. 

## Question 3 
### What does linter do?
- Linter is a tool that checks code for potential errors mainly syntatical errors. 

