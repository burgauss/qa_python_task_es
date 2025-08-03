# qa_python_tasks
This repository serves as a reference for creating automated tests using Chrome WebDriver, Pytest, and Selenium. It demonstrates how to set up and structure test cases to efficiently validate web applications through browser automation. The project is developed using the PyCharm ID.
It aims to provide a clear and practical foundation for anyone looking to implement reliable automated testing in Python-based environments.

## How to run this code?
1. Install PyCharm, check https://www.jetbrains.com/pycharm/
2. Make sure you create a virtual environment, follow this steps:
    - Open PyCharm and click New Project.
    - On the left, select Pure Python.
    - On the right, under Python Interpreter, choose New environment using and select Virtualenv.
    - Choose a location for the virtual environment.
    - Make sure the Base interpreter is set (e.g., Python 3.11).
3. Install pytest using ```pip install pytest``` in your console
4. Install the requests packages using ```pip install requests``` in your console

## open_and_close_page.py
It includes the basics functionality to start running automated test. It opens the website and validate that the URL is the correct one.

## find_element_exercise_1.py
It demostrates how to select elements in an automated tests using the find_element method which returns a webElement object. For this example a css_selector is used. Finally a the text of the selector is used by used the .text property
## find_element_exercise_1.py
