##System Analysis and System Design - Group Assignment 2
This repository is for group assignment 2 in the System Analysis and System Design course at Reykjavik University.


To find out how much of the code is covered in the tests, we use the Python library "Coverage.py". 
To be able to run our code you need to install all the libraries we used. Use the [pip](https://pip.pypa.io/en/stable/)  package manager to install coverage:

also run this command in your terminal:
```
$ pip install -r requirements.txt
```

## Requirements for the following instructions
python 3.11 

coverage 7.4.3

# Installation
1. Clone or fork the repository
2. Navigate to the project's directory
3. Install all necessary downloads by running the following command:
     ``` $ pip install -r requirements.txt ```
4. To run the unit test, use these commands:
     ```
     $ python -m unittest src/post_problem_test.py
     $ coverage run -m unittest src/post_problem_test.py
     ```
     ```
     $ python -m unittest src/questionnaire_test.py
     $ coverage run -m unittest src/questionnaire_test.py
     ```
     ```
     $ python -m unittest src/study_group_test.py
     $ coverage run -m unittest src/study_group_test.py
     ```
     ```
     $ python -m unittest src/study_session_test.py
     $ coverage run -m unittest src/study_session_test.py
     ```
5. To see how much of the code is covered run the following after each coverage run:
    ``` $ coverage report ```
6. After running `coverage report` you may want to run `coverage html` which generates a html report showing the coverage in a more visual way

# links
[here](https://coverage.readthedocs.io/en/7.4.4/index.html) you can see documentation for the `coverage.py` tool.

