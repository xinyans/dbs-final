# Database Systems: Final Project
This is the final project for Database Systems in the spring of 2020. 

### Group Members
Abdulai Jalloh (jalloa) - jalloa@rpi.edu

Frank Liang (liangt2) - liangt2@rpi.edu

Brian Gembarski (gembab) - gembab@rpi.edu

Xinyan Sun (sunx15) - sunx15@rpi.edu

Yutao Yang (yangy27) - yangy27@rpi.edu

## Datasets
The datasets that we use are Annual Average Daily Traffic in different municipalities across New York since 1977, and the Motor Vehicle Crashes dataset from 2014 to 2016. By combining these two datasets (via common municipality and year), we can provide some interesting insights such as relationship between traffic and crash rate.

## Instructions
* Run `load_data.py`. This file populates the database with the datasets stated above.
* Run `application.py` to start the main application.

## Other files
The main querying component is in `database.py` and is used by `application.py` to get the result with user inputs.
`datasets.txt` contains the link to download the datasets, `schema.sql` contains the schemas used in this application, and `requirements.py` contains the prerequisites for this application.