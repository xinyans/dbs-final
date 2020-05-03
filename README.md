# Database Systems: Final Project
This is the final project for Database Systems in the spring of 2020. It involves finding two publicly available datasets that share common attributes (e.g., Zipcode), creating a normalized schema describing the structure of the data, and producing an application that can populate the schema with the data, and run queries on the data producing useful output.

### Group Members
Abdulai Jalloh (jalloa) - jalloa@rpi.edu

Frank Liang (liangt2) - liangt2@rpi.edu

Brian Gembarski (gembab) - gembab@rpi.edu

Xinyan Sun (sunx15) - sunx15@rpi.edu

Yutao Yang (yangy27) - yangy27@rpi.edu

## Goals
Agree on what the schemas should be then split the work into three parts: loading the data, designing the queries, and user interface.

**Data Loading** group would write the load_data.py to download the dataset and parse them into the corresponding schemas.

**Query** group would write methods that takes arguments from user and queries the database, which is done in database.py.

**UI** group would complete the application.py to ask user for input and sends the information to database.py.

## GitHub Instructions
This is a general guideline to follow to ensure effeciency and avoid conflicts.

1. When you plan to add a feature or change something, put a message in the team Discord specifying what you will be working on

2. Write good code, see ***Coding Standards*** below

3. Test on your own machine, ensure everything compiles and runs on your machine. (Ideally, write a couple test cases for each function or part you worked on and add it to our testing suite... but that's ehh) *testing suite to be completed*

4. Now that your part is done and works on your machine, **PULL** the file from the repository. IF there are any conflicts, solve them on your machine. Once you have **PULL**ed, now you can **COMMIT** and then **PUSH**

5. You have now pushed your edits and additions. Post another message to the Discord, letting your teammates know what you completed.

## Coding Standards

A class name should be **UpperCamelCase**

Variables should be **lower_case_and_seperated**

Functions should be **UPPER_CASE_AND_SEPERATED**

As always, be sure to comment when appropriate. Every class should have a line that specifies what it does. Every function should have at least one line specifying what it does. If you come across a part of code where the logic is complex and hard to explain, **refactor** it.

When possible, make TODO comments
