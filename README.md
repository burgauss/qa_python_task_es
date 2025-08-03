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

---
### open_and_close_page.py
It includes the basics functionality to start running automated test. It opens the website and validate that the URL is the correct one.

---
### find_element_exercise_1.py
It demostrates how to select elements in an automated tests using the find_element method which returns a webElement object. For this example a css_selector is used. Finally a the text of the selector is used by used the .text property7

---
### find_element_exercise_2.py
It demostrates how to select elements in an automated tests using the find_elements method which returns a list of webElement objects. For this example xpath is used. Finally a the text of the selector is used by used the .text property

---
### find_element_exercise_3
It demostrates how to select elements in an automated tests using the find_element method which returns a webElement object. For this example also the css_selector is used. Finally the method .get_attribute('placeholder') is used to retrieve the placeholder

---
### click_on_an_element.py
It demostrates how to click on an element after being selected using a selector, basically the .click() method is used

---
### filling_in_the_input_field.py 
It demostrates the uses of explicit awaits in Selenium web driver, mostly by using the method ```WebDriverWait()```. Furthermore, the ```.sendKeys()``` method is used in order to send text to the fields in the website as part of the tests.

---
### get_text.py
It demostrates the basic use of the .text property in order to get the text to a webElement object.

---
### go_to_element.py
It demostrates the use of a javascript runed by using the ```.execute_script("arguments[0].scrollIntoView();", element)``` method. Another methods are also used like the .send_keys() and the .find_element()

---
### practice_exercise_1.py
This practice demostrates the use of automation testing using selenium, the full overview is as follows: automating the process of changing a profile picture on a website using Selenium. The session begins with logging into the platform. Then, the profile picture is clicked, which opens a new window or section for editing. The input field for the image URL is located using the ```find_element_by_id``` method, and a link with the image is inserted. Next, the "Save" button is located using XPath. Starting from the root element, the form is identified by its name attribute, and the button is found using both the element type and the text it contains. An explicit wait of three seconds is added using the ```expected_conditions.text_to_be_present_in_element_attribute``` method to ensure that the new profile picture has loaded correctly. Finally, an assert statement is used to verify that the style attribute of the profile picture element contains the correct image URL. This exercise reinforces the use of essential Selenium tools such as element selection, data input, XPath navigation, explicit waits, and automated validation.

### practice_exercise_2.py
This practice focuses on automating the process of creating and deleting a post on a web application using Selenium. The session begins by logging into the platform. The title of the most recent post is saved (by extracting the text of the corresponding element) and stored in a variable named title_before, which will be used later for comparison. Then, the script clicks the button to add a new post, locating it using a class-based search. The random module is imported to generate a unique title by appending three random digits to the word "Tokio", resulting in a string like "Tokio312", which is stored in the variable new_title. In the new window, this generated title is entered into the "Name" field, and the image URL is inserted into the "Link" field. These fields are located using attribute-based element searches (specifically the name attribute).

Once the form is filled, the data is saved by locating the submit button via XPath. Starting from the root element, the script finds the form using its name attribute and then identifies the button based on its element type and visible text. The test then waits for the delete button to appear, using a relative XPath query that targets the element by its class attribute. An assert statement is used to verify that the post card displays the correct name stored in new_title.

After the test, the script cleans up by reverting the environment to its original state. It records the number of cards before deletion, clicks the delete button for the newly created post, and waits for the post to be removed using the expected_conditions.text_to_be_present_in_element method. A final assert ensures that the number of cards has decreased by one, confirming that the post was successfully deleted.

### practice_exercise_3.py

