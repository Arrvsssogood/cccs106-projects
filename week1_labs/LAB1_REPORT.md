# Lab 1 Report: Environment Setup and Python Basics

**Student Name:** Harvey Lloyd V. Palacios\
**Student ID:** 231002286\
**Section:** A\
**Date:** 08-27-2025

## Environment Setup

### Python Installation
- **Python Version:** Python 3.11.5
- **Installation Issues:** None
- **Virtual Environment Created:** ✅ cccs106_env_palacios

### VS Code Configuration
- **VS Code Version:** 1.103.2
- **Python Extension:** ✅ Installed and configured
- **Interpreter:** ✅ Set to cccs106_env_lastname/Scripts/python.exe

### Package Installation
- **Flet Version:** 0.28.3
- **Other Packages:**
    - anyio==4.10.0
    - certifi==2025.8.3
    - flet==0.28.3
    - h11==0.16.0
    - httpcore==1.0.9
    - httpx==0.28.1
    - idna==3.10
    - oauthlib==3.3.1
    - repath==0.9.0
    - six==1.17.0
    - sniffio==1.3.1
    - typing_extensions==4.15.0

## Programs Created

### 1. hello_world.py
- **Status:** ✅ Completed
- **Features:** Student info display, age calculation, system info
- **Notes:** Generally, I did not experience any serious problems using the program. I found the code simple and working as I expected, which gave the whole process a satisfying feel. I loved how clear and well-structured it was because the basic concepts became easy to learn. Not only did this assignment provide a boost in my confidence to implement Python basics, but it also demonstrated how simple programs can be useful as well as easy on the eyes.
### 2. basic_calculator.py
- **Status:** ✅ Completed
- **Features:** Basic arithmetic, error handling, min/max calculation
- **Notes:** Everything in the program was smooth and ran in a proper manner. I particularly enjoyed the way it dealt with division by zero without erroring out and rather informing the user instead. In general, the calculator was accurate in all basic operations and displayed clear and easily comprehended results.

## Challenges and Solutions

I encountered some problems whenever I'm going to activate my environment. I searched for a solution and found out that I need to set up some command to activate my env using this, "Set-ExecutionPolicy Bypass -Scope Process," as it say "running scripts is disabled on this system." And after that, I can now activate my environment. However, our professor said that we can just run it in command prompt and it is also working. 

In addition, the issue with formatting hasn't been resolved—specifically, when you intentionally use bad indentation, it automatically gets corrected upon saving due to settings in settings.json.



## Learning Outcomes

I came to realize that using virtual environments is a mandatory practice during software development, especially when one is working on different projects. Dependencies can be isolated in virtual environments so that every project is bound to its own dependent packages without conflicting with another. This is especially valuable in cases when various projects need different versions of the same package.

As an example, in case one project requires the globally installed package, which conflicts with the requirements of another project, compatibility issues and errors are possible to occur. By making them distinct environments, we are able to make a project self-contained and it will run reliably no matter what is installed globally on our computer system.

Through this setup, I also gained a better understanding of how Python development works in real-world scenarios. I learned how to:

- Create and activate a virtual environment

- Use the terminal to manage packages with pip

- Generate a requirements.txt file for sharing or deployment

- Configure a development environment in VS Code

- Select the correct interpreter to match the environment

## Screenshots

Environement Setup:\
![alt text](/week1_labs/lab1_screenshots/environment_setup.png)

VS Code Setup:\
![alt text](/week1_labs/lab1_screenshots/vscode_setup.png)


Hello World:
![alt text](/week1_labs/lab1_screenshots/hello_world_output.png)

Basic Calculator:\
![alt text](/week1_labs/lab1_screenshots/basic_calculator_output.png)

